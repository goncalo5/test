cpe.log(7, "/live/AXCustomerSupportPortal/Scenarios/AVM_ParseDeviceLog")
"""
Allowed response codes:
    200 Success: Method was successfully executed
    201 Success: Method was successfully executed, but the changes will be applied after reboot

    301  Retry again in next CWMP Session
    302  Retry again in next CWMP session after reboot
    303  Retry again in next CWMP, see details

    500 Scenario error
    501 Invalid input arguments
    502 CPE does not support this service
"""

get_param = [
    'I.DI.DL'
]

log_regexs=[
    '(?:'+# not-capturing submask
    '([0-9]{4}-[0-9]{2}-[0-9]{2})'+ #date
    '\s([0-9]{2}:[0-9]{2}:[0-9]{2})'+ #one space and time
    '\s(.+?)'+# string
    '(?=(?:[0-9]{4}-[0-9]{2}-[0-9]{2}|$))'+#end if next is date or end of str
    ')'
]
log_levels = {
        'emerg': 0,
        'alert':1,
        'crit': 2,
        'error': 3,
        'warning': 4,
        'notice': 5,
        'info': 6,
        'debug': 7,
        }

def get_log_level(msg):
    level = msg.split(']')[0][1:].lower()
    return log_levels.get(level, '')

def get_comments(msg):
    if 'Battery cannot be detected' in msg:
        return '?? ??????? ???????'
    elif 'Terminal:ACS' in msg and 'Result:Success,Type:Login,Username' in msg:
        return 'ACS ??????? ??????????? ??????????'
    elif 'Battery cannot be detected' in msg:
        return '?? ??????? ???????'
    elif 'Configuration file backup successful' in msg:
        return '?????????????? ???????????????? ????? ?????????'
    elif 'Backing up configuration file.' in msg:
        return '????????? ??????? ?????????????? ???????????????? ????? ?????????'
    elif 'Set,IPPingDiagnostics:,DiagnosticsState:Requested' in msg:
        return '????????? ??????????????? ???? IPPingDiagnostics: %s' % (msg.split('DiagnosticsState:Requested')[-1],)
    elif 'Device reset. Cause: ONU reset after being powered on, Terminal:OTHER' in msg:
        return '?????????? ?????????????. ???????: ONU ????????????? ????? ?????????? ???????'
    elif 'Device reset. Cause: ONU reset by the software, Terminal:ACS' in msg:
        return '?????????? ?????????????. ???????: ????? ???????????? ? ACS'
    elif 'State:Requested' in msg.split('.')[-1]:
        test = msg.split('Type:Set,')[1].split(':')
        return '????????? ??????????????? ???? %s' % test
    elif 'Execute Result:' in msg:
        test = msg.split('Execute Result:')[0].split(",")[-1]
        res = msg.split('Execute Result:')[-1]
        return '?????????? ??????????????? ???? %s: %s' % (test, res)
    else:
        return ''


if str(step) == '0':
    cpe.log(7, "AVM_ParseDeviceLog - enter step %s" % step)
    step = 'get_log'

if str(step) == 'get_log':
    cpe.log(7, "AVM_ParseDeviceLog - enter step %s" % step)
    return 'parse_log', {'method': 'GetParameterValues', 'args': get_param}

if str(step) == 'parse_log':
    cpe.log(7, "AVM_ParseDeviceLog - enter step %s" % step)
    props = cpe.props
    vendor = props.get('I.DI.MO', props.get('D.DI.MO'))
    cpe.log(7, "AVM_ParseDeviceLog - vendor: %s" % vendor)
    if not vendor:
        raise Exception, "Device must have the '.DeviceInfo.ManufacturerOUI' parameter"

    manufacturer = props.get('I.DI.M', props.get('D.DI.M'))
    cpe.log(7, "AVM_ParseDeviceLog - manufacturer: %s" % manufacturer)
    if not manufacturer:
        raise Exception, "Device must have the '.DeviceInfo.Manufacturer' parameter"

    model = props.get('I.DI.MN', props.get('I.DI.MN'))
    cpe.log(7, "AVM_ParseDeviceLog - model: %s" % model)
    if not model:
        raise Exception, "Device must have the '.DeviceInfo.ModelName' parameter"

    if vendor == '00040E':
        # 29.11.16 23:45:18 Der Dienstanbieter konnte keine Einstellungen an dieses Ger�t �bertragen: Ung�ltiger Datensatz empfangen
        # 29.11.16 23:45:18 Automatische Einrichtung und Updates f�r dieses Ger�t durch den Dienstanbieter nicht m�glich: Server melder Fehler.
        import re
        regex = re.compile('\d\d\.\d\d\.\d\d\s+\d\d:\d\d:\d\d\s+')
        
        cpe_log = lastResult[0].items()[0][1] 
        dates = regex.findall(cpe_log)
        if not dates:
            raise Exception, "Warning: custom separator regex failed.</br>Returning raw device log."

        log = regex.split(cpe_log)
        log.pop(0)
        result = []
        for i in range(len(log)):
            d=dates[i].split(' ')[0]
            t=dates[i].split(' ')[1]
            msg=log[i]
            result.append({
                'date':d,
                'time':t, 
                'entry':msg, 
                'loglevel':log_levels.get('info'),
                'translation':'',
                })           
        
        return {'code' : 200, 'msg' : "Test finished", "details": result}

    import re
    result = []
    cpe_log = lastResult[0].items()[0][1]
    cpe.log(7, "AVM_ParseDeviceLog - cpe_log: %s" % cpe_log)
    parsed_cpe_log = re.findall(log_regexs[0],cpe_log)
    for date, time, entry in parsed_cpe_log:
        result.append({
            'date':date,
            'time':time,
            'entry':entry,
            'loglevel': get_log_level(entry),
            'translation': get_comments(entry)
        })

    #stats for device overview
    stats = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0
    }

    for entry in result:
        # don't know how, but it happens
        if entry['loglevel'] in stats:
            stats[entry['loglevel']] = stats[entry['loglevel']] + 1

    cpe.scProps['device_log_stats'] = stats

    return {'code' : 200, 'msg' : "Test finished", "details": result}

return {'code' : 500, 'msg' : "Unexpected step %s"%(step,), "details": {}}
