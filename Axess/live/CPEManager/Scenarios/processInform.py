cpe.log(7, "/live/CPEManager/Scenarios/processInform")
""" 
Entry Point Into Southbound Request Handling Logic 

    We are within one TR-069 request and have to respond
    finally with a TR-069 RPC or an empty reply.

    We may delegate the request handling to other scenarios
    from here.
"""

step = str(step)

if step == '0':
    cpe.log(7, "processInform - enter step %s" % step)
    cpe.log(7, "processInform - cpe.scProps %s" % cpe.scProps)
    # The cpe.state 3 indicates that this is the very first Inform of this device.
    if cpe.state == 3:
        # Writing a log statement using the AXESS internal log level 3 (cpe.logLevel)
        log(5, cpe, 'First sight of %s' % cpe.cpeid)
    # Policy Management (Polcies are defined in AXPolicyManager)
    # Call AXPolicyManager and apply existing policies to the CPE.
    return 'afterAXSCM', {'method': 'call_axscm', 'args': {}}

if step == 'afterAXSCM':
    cpe.log(7, "processInform - enter step %s" % step)
    axjobs = container.CPEManager.AXPassiveJobsConfig
    cpe.log(7, "processInform - type(cpe.cpeid) %s" % type(cpe.cpeid))
    cpe.log(7, "processInform - type(cpe) %s" % type(cpe))
    cpe.log(7, "processInform - cpe.scProps %s" % cpe.scProps)
    context = axjobs.create_context(cpe.cpeid, cpe_obj=cpe)
    axjobs.trigger_next_passive_job(cpe)
    # Additional logic could be added here.

    if cpe.pendingProps:
        return 'SPV_for_pendingProps', {'method' : 'SetParameterValues' , 'args' : {}}

# Set the default state (0) after the first Inform of the device. 
if cpe.state == 3:
    cpe.set('state', 0)
