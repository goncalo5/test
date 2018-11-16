import logging
import datetime
import sys
import json


class Props:
    def __init__(self, props):
        self.props = props

    def convert_tree_from_props(self, tree, fail=None):
        new_dict = self.props
        for value in tree.split('.'):
            # print value
            if value is None:
                # print 'fail', fail
                return fail if fail is not None else None
            try:
                new_dict = new_dict.get(value)
                if new_dict is None:
                    return fail
            except AttributeError:
                # print 'ex fail', fail
                return fail if fail is not None else None
            # print new_dict
            # print
        # print type(new_dict)
        # return json.dumps(new_dict, sort_keys=True, indent=4)
        return new_dict


event = {'status': 'SUCCESS', 'event_source': 'lb_7547', 'store_name': u'cpe_store', 'cpeid': '000E8F-E1806BXKA05113', 'creation_time': datetime.datetime(2018, 10, 31, 1, 22, 40, 915618), 'raw': {'L3F': {'FNOE': 12}, 'LD': {'1': {'LEIC': {'1': {'S': 'Up', 'St': {'PR': 1532833069, 'PS': 1520870351, 'BR': 275616881, 'BS': 3001387330}}, '3': {'S': 'NoLink', 'St': {'PR': 0, 'PS': 0, 'BR': 0, 'BS': 0}}, '2': {'S': 'NoLink', 'St': {'PR': 0, 'PS': 0, 'BR': 0, 'BS': 0}}}, 'LHCM': {'X_DNSProxyEnable': '1', 'DSE': '1', 'DS': '192.168.0.1'}, 'WC': {'1': {'C': 5, 'B': 'D4:60:E3:D1:80:91', 'AD': {'1': {'MACAddress': '', 'SignalStrength': '', 'X_PhysicalDownlinkRate': '', 'Standard': '', 'X_LastDataDownlinkRate': '', 'X_LastDataUplinkRate': '', 'X_TimeConnected': '', 'Active': '', 'IPAddress': '', 'Retransmissions': '', 'X_HostName': '', 'X_PhysicalUplinkRate': ''}}, 'ACE': '1', 'Sta': {'ES': 2223, 'ER': 4}, 'ToPS': 7146837, 'TBS': 2639966710, 'TBR': 1453320832, 'X_WatchDog': {'SuccessCount': 0}, 'MACE': '0', 'TP': 100, 'St': 'b,g,n', 'RE': '1', 'S': 'Up', 'TPR': 4204837, 'W': {'E': '1'}, 'MBR': 'Auto', 'X_WlanAdapter': {'BandWidth': '0'}}, '5': {'C': 36, 'B': 'D4:60:E3:D1:80:95', 'Sta': {'ES': 0, 'ER': 15}, 'ACE': '1', 'ToPS': 1513219, 'TBS': 2008748266, 'TBR': 38459520, 'X_WatchDog': {'SuccessCount': 0}, 'MACE': '0', 'TP': 100, 'St': 'n,ac', 'RE': '1', 'S': 'Up', 'X_WlanAdapter': {'BandWidth': '0'}, 'MBR': 'Auto', 'TPR': 325507}}, 'H': {'H': {'1': {'A': '1', 'LTR': 86353, 'MA': 'B0:4E:26:EF:EB:1A', 'L2I': 'InternetGatewayDevice.LANDevice.1.LANEthernetInterfaceConfig.1.', 'IT': 'Ethernet', 'AS': 'DHCP', 'HN': 'TL-WPA4220', 'IA': '192.168.0.154'}, '3': {'A': '0', 'LTR': 50383, 'MA': 'BC:3D:85:84:DC:B7', 'L2I': 'InternetGatewayDevice.LANDevice.1.WLANConfiguration.0', 'IT': '802.11', 'AS': 'DHCP', 'HN': 'MYA-L41', 'IA': '192.168.0.160'}, '2': {'A': '1', 'LTR': 56912, 'MA': 'B8:D9:4D:99:7E:C8', 'L2I': 'InternetGatewayDevice.LANDevice.1.LANEthernetInterfaceConfig.1.', 'IT': 'Ethernet', 'AS': 'DHCP', 'HN': 'Unknown', 'IA': '192.168.0.156'}, '4': {'A': '0', 'LTR': 41624, 'MA': 'D0:C5:F3:49:76:B0', 'L2I': 'InternetGatewayDevice.LANDevice.1.WLANConfiguration.0', 'IT': '802.11', 'AS': 'DHCP', 'HN': 'EDUARDO', 'IA': '192.168.0.157'}}, 'HNOE': 4}}}, 'WD': {'1': {'WEIC': {'SR': 52500000, 'DM': 'Full', 'MBR': '1000'}, 'WCD': {'1': {'WC': {'1': {'CS': 'Disconnected', 'PMNOE': 0, 'S': {'EPR': 0, 'EPS': 0, 'EBR': 0, 'EBS': 0}, 'E': '0', 'DS': ''}, '2': {'CS': 'Connected', 'E': '1', 'S': {'EPR': 6285831, 'EPS': 3988161, 'EBR': 1905489871, 'EBS': 826757357}, 'PMNOE': 0, 'DS': '212.166.132.110,212.166.132.104'}}, 'WIC': {'3': {'CS': 'Connected', 'PMNOE': 0, 'S': {'EPR': 2775198661, 'EPS': 7831874, 'EBR': 1944986176, 'EBS': 2254798694}, 'E': '1'}, '2': {'CS': 'Disconnected', 'PMNOE': 0, 'S': {'EPR': 0, 'EPS': 0, 'EBR': 0, 'EBS': 0}, 'E': '0'}}}}}, '2': {'WIC': {'UCR': 0, 'UMR': 0, 'DNM': 0, 'DCR': 0, 'X_NumberOfCuts': 0, 'S': 'NoSignal', 'St': {'T': {'LOF': 0, 'IT': 0, 'CE': 0, 'FE': 0, 'SES': 0, 'IE': 0, 'ES': 0, 'HE': 0}}, 'MT': '', 'DMR': 0, 'DA': 0, 'UA': 0, 'UNM': 0}, 'WCD': {'1': {'WC': {'1': {'CS': 'Disconnected', 'PMNOE': 0, 'S': {'EPR': 0, 'EPS': 0, 'EBR': 0, 'EBS': 0}, 'E': '0', 'DS': ''}}}, '3': {'WIC': {'1': {'CS': 'Disconnected', 'E': '0', 'S': {'EPR': 0, 'EPS': 0, 'EBR': 0, 'EBS': 0}, 'PMNOE': 0, 'DS': ''}}}, '2': {'WIC': {'1': {'CS': 'Disconnected', 'S': {'EBR': 0}, 'E': '0', 'DS': ''}}}, '5': {'WC': {'1': {'CS': 'Disconnected', 'E': '0', 'S': {'EPR': 0, 'EPS': 0, 'EBR': 0, 'EBS': 0}, 'PMNOE': 0, 'DS': ''}}}, '4': {'WC': {'1': {'CS': 'Disconnected', 'PMNOE': 0, 'S': {'EPR': 0, 'EPS': 0, 'EBR': 0, 'EBS': 0}, 'E': '0', 'DS': ''}}, 'WIC': {'1': {'CS': 'Disconnected', 'E': '0', 'S': {'EPR': 0, 'EPS': 0, 'EBR': 0, 'EBS': 0}, 'PMNOE': 0, 'DS': ''}, '2': {'CS': 'Disconnected', 'E': '0', 'S': {'EPR': 0, 'EPS': 0, 'EBR': 0, 'EBS': 0}, 'PMNOE': 0, 'DS': ''}}}}}}, 'DI': {'PS': {'CU': 6}, 'HV': 'Vodafone-H-500-sv1', 'PrC': 'TR11.8110.0000', 'UT': 3017825, 'MO': '000E8F', 'MN': 'Vodafone-H-500-s', 'M': 'SERCOMM', 'SV': 'Vodafone-H-500-s-v3.4.17', 'PC': 'Vodafone-H-500-s', 'SN': 'E1806BXKA05113', 'MS': {'T': 122852, 'F': 40992}}, 'S': {'VS': {'1': {'VP': {'1': {'L': {'1': {'DN': '+34956660794', 'SI': {'AP': '82TeQFKVDfe2xe9DCO9tVw==', 'AUN': '34956660794@ims.vodafone.es'}, 'E': 'Enabled', 'S': 'Up', 'St': {'SDT': 0, 'RTD': 0, 'OuCA': 173, 'OCC': 193, 'ARIJ': 15, 'OCA': 194, 'PS': 1366373, 'TCT': 26383, 'PR': 1352072, 'RPLR': 0, 'ICF': 0, 'FEPLR': 0, 'OCF': 0, 'ICA': 169, 'ICC': 228, 'ARTD': 0, 'ICR': 228, 'CD': 0, 'AFEIJ': 159, 'PL': 29}}}}}, 'PI': {'1': {'PP': '1', 'X_PortStatus': 'On Hook'}}}}, 'StS': {'1': {'E': '0 '}}}, 'T': {'CLT': '2018-10-31 02:22:38', 'S': 'Synchronized'}, 'MS': {'PII': 3600, 'CRUs': 'E1806BXKA05113-Vodafone-H-500-s-000E8F', 'U': 'http://qt-acs.fnet.vodafone.es:8080/cwmpWeb/CPEMgt'}, 'QM': {'QNOE': 25}, 'X_Management': {'Upnp': {'Enable': '0'}}}, 'mode': u'Vodafone-H-500-s.2', 'props': {'alarmed3_NEBASVLAN': False, 'alarmed4_NEBAPAI': False, 'BS_3': 0, 'TS': 'Synchronized', 'EBR_112_1': 0, 'EBS_241_1': 0, 'EBR_221': 0, 'PMNOE_10': 0, 'PII': 3600, 'wlan24': {'WLANTBS_delta': 0.2200002670288086, 'WLANTPS_delta': 1085.0, 'WLANSER_delta': 0.0, 'abnormal_noise': 0, 'max_rate': 'Auto', 'issue_noise': 0, 'channel_change_count': 865, 'WLANSES_delta': 0.0, 'WLANTBR_delta': 0.07545757293701172, 'WLANTPR_delta': 567.0, 'channel_change': 1}, 'cpe_wlan_filter_w50': '0', 'alarmed3_Zone': False, 'alarmed6_NEBAPAI': False, 'DMR_1': 0, 'Host': {'LD': {'1': {'H': {'H': {'1': {'A': '1', 'LTR': 86353, 'MA': 'B0:4E:26:EF:EB:1A', 'L2I': 'InternetGatewayDevice.LANDevice.1.LANEthernetInterfaceConfig.1.', 'IT': 'Ethernet', 'AS': 'DHCP', 'HN': 'TL-WPA4220', 'IA': '192.168.0.154'}, '3': {'A': '0', 'LTR': 50383, 'MA': 'BC:3D:85:84:DC:B7', 'L2I': 'InternetGatewayDevice.LANDevice.1.WLANConfiguration.0', 'IT': '802.11', 'AS': 'DHCP', 'HN': 'MYA-L41', 'IA': '192.168.0.160'}, '2': {'A': '1', 'LTR': 56912, 'MA': 'B8:D9:4D:99:7E:C8', 'L2I': 'InternetGatewayDevice.LANDevice.1.LANEthernetInterfaceConfig.1.', 'IT': 'Ethernet', 'AS': 'DHCP', 'HN': 'Unknown', 'IA': '192.168.0.156'}, '4': {'A': '0', 'LTR': 41624, 'MA': 'D0:C5:F3:49:76:B0', 'L2I': 'InternetGatewayDevice.LANDevice.1.WLANConfiguration.0', 'IT': '802.11', 'AS': 'DHCP', 'HN': 'EDUARDO', 'IA': '192.168.0.157'}}}}}}, 'EBS_211': 0, 'EPS_112': 3988161, 'EPS_113': 7831874, 'PrC': 'TR11.8110.0000', 'EPS_111': 0, 'URI': '+34956660794', 'alarmed6_SBCPrimary': False, 'EPR_113': 2775198661, 'FEC_1': 0, 'EPS_211': 0, 'PS_3': 0, 'PS_1': 1520870351, 'EBR_231': 0, 'WAN_DS_251': '', 'restart': {'quick_restart_total': 0, 'quick_restart_count': 0, 'restart_count': 0, 'restart_total': 0}, 'alarmed6_Zone': False, 'watchdog_50': 0, 'alarmed4_Prov': False, 'alarmed5_NEBAPAI': False, 'MBR': '1000', 'cpe_upnp': '0', 'wono': {'enabled_remap': None, 'enabled_remap_gui': None, 'status_remap': None, 'status_remap_gui': None}, 'EBS_111': 0, 'EBS_112': 826757357, 'EBS_113': 2254798694, 'WLANS_1': 'Up', 'NUMC_1': 0, 'SErr_1': 0, 'alarmed2_CDC': False, 'HV': 'Vodafone-H-500-sv1', 'alarmed5_SBCPrimary': False, 'PMNOE_3': 0, 'WAN_DS_241': '', 'cpe_storage_service': '0 ', 'PMNOE_2': 0, 'PMNOE_1': 0, 'Enable': 'Enabled', 'EPR_241_1': 0, 'EPS_112_1': 0, 'LOF_1': 0, 'cpe_wlan_filter': 0, 'PMNOE_6': 0, 'EBS_231': 0, 'PC': 'Vodafone-H-500-s', 'alarmed5_NEBASVLAN': False, 'cpe_dns_proxy': '1', 'WAN_DS_241_1': '', 'EPR_112': 6285831, 'EPR_111': 0, 'ITO_1': 0, 'EBR_211': 0, 'Err_1': 0, 'USNR_1': 0, 'EBR_111': 0, 'EBR_113': 1944986176, 'EBR_112': 1905489871, 'EPR_112_1': 0, 'PR_3': 0, 'PR_2': 0, 'PR_1': 1532833069, 'BR_2': 0, 'EPR_211': 0, 'alarmed6_CDC': False, 'EBS_112_1': 0, 'wlan50': {'abnormal_noise': 0, 'user_pkts_tx': 1513219, 'radio_channel': '36', 'auto_channel_enabled': 1, 'WLANTBR_delta': 0.0, 'WLANTPR_delta': 0.0, 'channel_change': 1, 'status_remap': 0, 'WLANSER_delta': 0.0, 'status_remap_gui': 'Up', 'status': 'Up', 'WLANTBS_delta': 0.0, 'max_rate': 'Auto', 'user_bytes_tx': 2008748266, 'radio_enabled_remap': True, 'radio_enabled': 1, 'WLANTPS_delta': 0.0, 'user_errs_rx': 15, 'user_bytes_rx': 38459520, 'issue_noise': 0, 'channel_change_count': 1514, 'WLANSES_delta': 0.0, 'user_pkts_rx': 325507, 'user_errs_tx': 0}, 'MO': '000E8F', 'MN': 'Vodafone-H-500-s', 'alarmed5_CDC': False, 'DCR_1': 0, 'alarmed3_Prov': False, 'MU': 'http://qt-acs.fnet.vodafone.es:8080/cwmpWeb/CPEMgt', 'alarmed1_NEBAPAI': False, 'alarmed1_NEBASVLAN': False, 'alarmed5_Zone': False, 'wlan': {'wlan50': {'transmit_power': 100, 'op_channel_bandwidth': '0', 'op_standard': 'n,ac', 'bssid': 'D4:60:E3:D1:80:95'}, 'wlan24': {
    'transmit_power': 100, 'associated_devices': {'LD': {'1': {'WC': {'1': {'AD': {'1': {'MACAddress': '', 'SignalStrength': '', 'X_PhysicalDownlinkRate': '', 'Standard': '', 'X_LastDataDownlinkRate': '', 'X_LastDataUplinkRate': '', 'X_TimeConnected': '', 'Active': '', 'IPAddress': '', 'Retransmissions': '', 'X_HostName': '', 'X_PhysicalUplinkRate': ''}}}}}}}, 'op_channel_bandwidth': '0', 'op_standard': 'b,g,n', 'bssid': 'D4:60:E3:D1:80:91'}}, 'roll4_win': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'WAN_DS_231': '', 'alarmed1_Prov': False, 'PMNOE_9': 0, 'PMNOE_8': 0, 'WAN_DS_221': '', 'LANS_3': 'NoLink', 'LANS_2': 'NoLink', 'LANS_1': 'Up', 'PMNOE_7': 0, 'DA_1': 0, 'PMNOE_5': 0, 'PMNOE_4': 0, 'wan': {'report1_issue_changets': None, 'enabled_ip_231': '0', 'status_ppp_211': 'Disconnected', 'BEST_UCR': None, 'report4_issue': 0, 'enabled_ip_112': '0', 'enabled_ip_113': '1', 'status_ppp_251': 'Disconnected', 'enabled_ppp_112': '1', 'status_ip_241': 'Disconnected', 'status_ip_242': 'Disconnected', 'enabled_ppp_111': '0', 'enabled_ppp_251': '0', 'report2_issue': None, 'UA_rollw': [None, None, None], 'enabled_ppp_241': '0', 'EPR_sum': 1167370.0, 'enabled_ppp_211': '0', 'PMNOE_sum': 0, 'DCR_rollw': [None, None, None], 'status_ip_221': 'Disconnected', 'report3_issue': None, 'DM_remap': 1, 'enabled_ip_241': '0', 'enabled_ip_242': '0', 'EPS_sum': 2757.0, 'EBS_sum': 0.7573966979980469, 'DA_rollw': [None, None, None], 'report3_issue_changets': None, 'if_up_count': 2, 'UCR_rollw': [None, None, None], 'enabled_ip_221': '0', 'WANMT_remap': None, 'status_ppp_112': 'Connected', 'status_ppp_111': 'Disconnected', 'status_ppp_241': 'Disconnected', 'status_ip_112': 'Disconnected', 'status_ip_113': 'Connected', 'report1_issue': None, 'WAN_DS_value': '212.166.132.110,212.166.132.104', 'report2_issue_changets': None, 'MBR_remap': 2, 'SR': 52500000, 'status_ip_231': 'Disconnected', 'EBR_sum': 1497.765944480896, 'BEST_DCR': None, 'if_enabled_count': 2, 'WAN_DS_value_rang': '212_166_132_110,212_166_132_104', 'report4_issue_changets': None}, 'alarmed5_Prov': False, 'EPS_241_1': 0, 'BR_1': 275616881, 'BR_3': 0, 'EBR_241_1': 0, 'alarmed1_CDC': False, 'drop2': {'BEST_DA': None, 'MST': 122852, 'VLE': 1, 'BEST_UA': None, 'PSCU_remap': 6.0, 'MSF': 40992, 'VLS': 1}, 'alarmed1_Zone': False, 'alarmed4_CDC': False, 'WANMT_1': '', 'alarmed4_Zone': False, 'WAN_DS_211': '', 'alarmed7_CPEModel': False, 'CRC_1': 0, 'AUP': '82TeQFKVDfe2xe9DCO9tVw==', 'eth_status_change': 0, 'BS_1': 3001387330, 'BS_2': 0, 'WANS_1': 'NoSignal', 'CLT': '2018-10-31 02:22:38', 'last_boot_time': datetime.datetime(2018, 9, 26, 3, 18, 1, 75000), 'alarmed3_NEBAPAI': False, 'EBS_251': 0, 'EPS_251': 0, 'LANDS': '192.168.0.1', 'WAN_DS_242': '', 'EPR_231': 0, 'SV': 'Vodafone-H-500-s-v3.4.17', 'PSCU': 6, 'alarmed2_NEBAPAI': False, 'IErr_1': 0, 'SN': 'E1806BXKA05113', 'EBS_241': 0, 'EBS_242': 0, 'voice': {'OCA': 194, 'OCC': 193, 'report6_issue_changets': None, 'OCF': 0, 'report6_issue': 0, 'PPP_1': '1', 'report5_issue_changets': datetime.datetime(2018, 10, 16, 16, 18, 4, 614000), 'Enable_remap': 0, 'TimeStatus_NewRemap': 'Up', 'PR': 1352072, 'PS': 1366373, 'PPS_1': 'On Hook', 'report7_issue': 0, 'TCT': 26383, 'OCAN': 173, 'OCFR': -1, 'DPE_1': '1', 'ARTD': 0, 'report8_issue': 0, 'ICFR': -1, 'AFEIJ': 159, 'PL': 29, 'report7_issue_changets': None, 'ARIJ': 15, 'RTD': 0, 'ICC': 228, 'ICA': 169, 'ICF': 0, 'FEPLR': 0, 'CD': 0, 'ICR': 228, 'VoiceLine_NewRemap': 'Up', 'SDT': 0, 'VoiceLineStatus_NewRemap': 'Up', 'ConfStat_NewRemap_1': 'Up', 'RPLR': 0, 'VoiceS_remap': 0, 'report5_issue': 0}, 'cpe_wlan_filter_w24': '0', 'DM': 'Full', 'alarmed2_NEBASVLAN': False, 'vf': {'diff': {'NUMC_1': 0.0, 'SErr_1': 0.0, 'EPR_112_1': 0.0, 'EPS_241_1': 0.0, 'EBR_241': 0.0, 'EBR_112_1': 0.0, 'EBR_242': 0.0, 'PS_3': 0.0, 'EBS_241_1': 0.0, 'EPS_112': 1005.0, 'EBR_221': 0.0, 'EPS_241': 0.0, 'HEC_1': 0.0, 'ITO_1': 0.0, 'EPS_211': 0.0, 'EPR_241_1': 0.0, 'BR_1': 180452.0, 'LOF_1': 0.0, 'EPS_242': 0.0, 'PR_2': 0.0, 'EBS_231': 0.0, 'FEC_1': 0.0, 'PR_1': 1530900720.0, 'EBS_211': 0.0, 'EPR_113': 1166332.0, 'EPR_112': 1038.0, 'EPR_111': 0.0, 'EBR_251': 0.0, 'EPR_242': 0.0, 'EPR_241': 0.0, 'lan': {'WLANSES': 0.0, 'WLANSER': 0.0, 'TBS': 0.2200002670288086, 'TBR': 0.07545757293701172, 'TPS': 1085.0, 'TPR': 567.0}, 'EBR_211': 0.0, 'Err_1': 0.0, 'EPS_113': 1752.0, 'EPS_111': 0.0, 'CRC_1': 0.0, 'EBR_111': 0.0, 'EBR_113': 1570187921.0, 'EBR_112': 333502.0, 'PS_2': 0.0, 'BS_1': 1586311520.0, 'BS_2': 0.0, 'PS_1': 1165352.0, 'EBR_231': 0.0, 'PR_3': 0.0, 'EPS_112_1': 0.0, 'BR_3': 0.0, 'BR_2': 0.0, 'EPS_251': 0.0, 'EPR_211': 0.0, 'EBS_112_1': 0.0, 'wlan50': {'user_errs_rx': 0.0, 'user_bytes_rx': 0.0, 'user_pkts_tx': 0.0, 'user_bytes_tx': 0.0, 'user_pkts_rx': 0.0, 'user_errs_tx': 0.0}, 'EPS_231': 0.0, 'EPR_231': 0.0, 'EPR_251': 0.0, 'BS_3': 0.0, 'EBS_251': 0.0, 'EBR_241_1': 0.0, 'IErr_1': 0.0, 'EBS_241': 0.0, 'EBS_242': 0.0, 'voice': {'PR': 0.0, 'PS': 0.0, 'OCA': 0.0, 'ICA': 0.0, 'OCAN': 0.0, 'ICF': 0.0, 'OCF': 0.0, 'ICC': 0.0, 'ICR': 0.0, 'OCC': 0.0, 'PL': 0.0}, 'EBS_111': 0.0, 'EBS_112': 368424.0, 'EBS_113': 425764.0}, 'rate': {'NUMC_1': 0.0, 'SErr_1': 0.0, 'EPR_112_1': 0.0, 'EPS_241_1': 0.0, 'EBR_241': 0.0, 'EBR_112_1': 0.0, 'EBR_242': 0.0, 'PS_3': 0.0, 'EBS_241_1': 0.0, 'EPS_112': 0.27893422148209823, 'EBR_221': 0.0, 'EPS_241': 0.0, 'HEC_1': 0.0, 'ITO_1': 0.0, 'EPS_211': 0.0, 'EPR_241_1': 0.0, 'BR_1': 50.083819039689146, 'LOF_1': 0.0, 'EPS_242': 0.0, 'PR_2': 0.0, 'EBS_231': 0.0, 'FEC_1': 0.0, 'PR_1': 424896.1199000832, 'EBS_211': 0.0, 'EPR_113': 323.7113516514016, 'EPR_112': 0.2880932556203164, 'EPR_111': 0.0, 'EBR_251': 0.0, 'EPR_242': 0.0, 'EPR_241': 0.0, 'lan': {'WLANSES': 0.0, 'WLANSER': 0.0, 'TBS': 64.02636691645851, 'TBR': 21.96031085206772, 'TPS': 0.30113794060505134, 'TPR': 0.15736885928393005}, 'EBR_211': 0.0, 'Err_1': 0.0, 'EPS_113': 0.48626144879267275, 'EPS_111': 0.0, 'CRC_1': 0.0, 'EBR_111': 0.0, 'EBR_113': 435800.1446017208, 'EBR_112': 92.5623091867888, 'PS_2': 0.0, 'BS_1': 440275.1928948099, 'BS_2': 0.0, 'PS_1': 323.43935609214543, 'EBR_231': 0.0, 'PR_3': 0.0, 'EPS_112_1': 0.0, 'BR_3': 0.0, 'BR_2': 0.0, 'EPS_251': 0.0, 'EPR_211': 0.0, 'EBS_112_1': 0.0, 'wlan50': {'user_errs_rx': 0.0, 'user_bytes_rx': 0.0, 'user_pkts_tx': 0.0, 'user_bytes_tx': 0.0, 'user_pkts_rx': 0.0, 'user_errs_tx': 0.0}, 'EPS_231': 0.0, 'EPR_231': 0.0, 'EPR_251': 0.0, 'BS_3': 0.0, 'EBS_251': 0.0, 'EBR_241_1': 0.0, 'IErr_1': 0.0, 'EBS_241': 0.0, 'EBS_242': 0.0, 'voice': {'PR': 0.0, 'PS': 0.0, 'OCA': 0.0, 'ICA': 0.0, 'OCAN': 0.0, 'ICF': 0.0, 'OCF': 0.0, 'ICC': 0.0, 'ICR': 0.0, 'OCC': 0.0, 'PL': 0.0}, 'EBS_111': 0.0, 'EBS_112': 102.25478767693588, 'EBS_113': 118.16930335831252}, 'since': datetime.datetime(2018, 10, 31, 1, 22, 40, 915618)}, 'alarmed6_Prov': False, 'UMR_1': 0, 'EBR_241': 0, 'EBR_242': 0, 'wono_priv': {'WLANTPR_delta': 0, 'client_count': 0, 'WLANTBS_delta': 0, 'WLANTPS_delta': 0, 'WLANTBR_delta': 0}, 'UA_1': 0, 'watchdog_24': 0, 'HEC_1': 0, 'alarmed2_Prov': False, 'EPS_242': 0, 'DSNR_1': 0, 'EPS_241': 0, 'alarmed6_NEBASVLAN': False, 'wono_pub': {'WLANTPR_delta': 0, 'client_count': 0, 'WLANTBS_delta': 0, 'WLANTPS_delta': 0, 'WLANTBR_delta': 0}, 'lan2': {'WLANTPR_delta': 567.0, 'WLANTBS_delta': 0.2200002670288086, 'WLANTPS_delta': 1085.0, 'WLANTBR_delta': 0.07545757293701172}, 'WAN_DS_112': '212.166.132.110,212.166.132.104', 'WAN_DS_111': '', 'EPR_242': 0, 'EPR_241': 0, 'lan': {'WIFI': 0, 'LANS_2_remap_gui': 'Down', 'LANS_1_remap_gui': 'Up', 'TS_remap': 0, 'HOMEPLUG': 0, 'HOMEPNA': 0, 'WLANS_1_remap': 0, 'BR_sum': 0.17209243774414062, 'PR_sum': 1530900720.0, 'ETH': 2, 'USB': 0, 'WLANSES': 2223, 'WLANSER': 4, 'LANS_2_remap': 3, 'HNOE': 2, 'LANS_4_remap_gui': None, 'WLANSER_delta': 0.0, 'QNOE': 25, 'WPS': '1', 'WLANC_1': '5', 'WLANRE': 1, 'LANS_count': 1, 'WLANSES_delta': 0.0, 'WACE_1': 1, 'LANS_3_remap_gui': 'Down', 'BS_sum': 1512.8245544433594, 'FNOE': 12, 'TPS': 7146837, 'TPR': 4204837, 'DSE': '1', 'LANS_4_remap': None, 'LANS_1_remap': 0, 'UT': 838.2847222222222, 'TBS': 2517.668447494507, 'TBR': 1385.9947509765625, 'LANS_3_remap': 3, 'MOCA': 0, 'OTHS': 0, 'WLANRE_remap': True, 'PS_sum': 1165352.0}, 'alarmed4_NEBASVLAN': False, 'M': 'SERCOMM', 'VoiceS': 'Up', 'alarmed3_CDC': False, 'AUN': '34956660794@ims.vodafone.es', 'alarmed2_Zone': False, 'EBR_251': 0, 'alarmed8_CPEModel': False, 'EPS_231': 0, 'nat444': {'port_fw_status_ever': 0, 'nat_with_port_fw': 0, 'nat_with_port_fw_changets': None, 'port_fw_changets': None, 'port_fw_status': 0, 'port_fw_down_changets': None, 'port_fw_status_last_90d': 0}, 'UCR_1': 0, 'uc4_status': '', 'PS_2': 0, 'MCU': 'E1806BXKA05113-Vodafone-H-500-s-000E8F', 'EPR_251': 0}}

# props = Props(event.get('props'))
# print props.convert_tree_from_props('wlan.wlan24.associated_devices.LD.1.WC.1.AD.1.Standard')
# exit()


def convert_all_MACs_to_unique_MACs(all_MACs, hours):
    unique_MACs = set()
    for MACs in all_MACs[-hours:]:
        unique_MACs.update(MACs)
    try:
        unique_MACs.remove('')
    except KeyError:
        pass
    return ','.join(unique_MACs)


class CalcAssociatedDevicesKPIs(object):
    def __init__(self, name, config):
        self.logger = logging.getLogger("%s.%s" % (__name__, name))
        self.logger.info("Module %s reading config" % (name))
        self.config = config
        self.rssi_threshold_24 = config["rssi_threshold_24"]
        self.downlink_rate_threshold_24 = config["downlink_rate_threshold_24"]
        self.uplink_rate_threshold_24 = config["uplink_rate_threshold_24"]
        self.rssi_threshold_50 = config["rssi_threshold_50"]
        self.downlink_rate_threshold_50 = config["downlink_rate_threshold_50"]
        self.uplink_rate_threshold_50 = config["uplink_rate_threshold_50"]
        self.logger.info("Module %s initialized" % (name))

    def _props_have_params(self, props, *names):
        for name in names:
            if name not in props or props[name] is None:
                return False
        return True

    def process_event(self, event):
        LOW_RSSI_THRESHOLD_24 = self.rssi_threshold_24  # Needs to be confirmed
        LOW_PHY_DOWN_THRESHOLD_24 = self.downlink_rate_threshold_24
        LOW_PHY_UP_THRESHOLD_24 = self.uplink_rate_threshold_24
        LOW_RSSI_THRESHOLD_50 = self.rssi_threshold_50  # Needs to be confirmed
        LOW_PHY_DOWN_THRESHOLD_50 = self.downlink_rate_threshold_50
        LOW_PHY_UP_THRESHOLD_50 = self.uplink_rate_threshold_50

        debug = sys.stdout.write
        # debug("Got Event %s" % event)
        # raw = event.raw
        # props = event['props']
        props = Props(event.get('props'))
        # metadata = event.metadata

        wlan24_ass_low_rssi = 0
        wlan24_ass_phy_up = 0
        wlan24_ass_phy_down = 0
        wlan24_ass_low_rssi_list = []
        wlan24_ass_phy_up_list = []
        wlan24_ass_phy_down_list = []

        wlan50_ass_low_rssi = 0
        wlan50_ass_phy_up = 0
        wlan50_ass_phy_down = 0

        wlan50_device_number_ac = 0
        wlan50_device_number_n = 0

        wlan24_device_number_ab = 0
        wlan24_device_number_g = 0
        wlan24_device_number_n = 0
        wlan24_device_number_ac = 0

        wlan50_ass_low_rssi_list = []
        wlan50_ass_phy_up_list = []
        wlan50_ass_phy_down_list = []
        wlan24_last_data_uplink_rate_sum = 0
        wlan24_last_data_downlink_rate_sum = 0
        wlan24_rssi_sum = 0
        wlan50_last_data_uplink_rate_sum = 0
        wlan50_last_data_downlink_rate_sum = 0
        wlan50_rssi_sum = 0

        # check path to associated devices:
        ass_devices_24, ass_devices_50 = None, None
        if props.convert_tree_from_props('wlan.wlan24.associated_devices'):
            debug('TR-069')
            debug('\n')
            ass_devices_24 = 'wlan.wlan24.associated_devices'
            debug(ass_devices_24)
            debug('\n')
        elif props.convert_tree_from_props('wlan.associated_devices.wlan24'):
            debug('SNMP')
            debug('\n')
            ass_devices_24 = 'wlan.associated_devices.wlan24'
        debug('ass_devices_24: %s' % ass_devices_24)
        debug('\n')
        if props.convert_tree_from_props('wlan.wlan50.associated_devices'):
            debug('TR-069')
            debug('\n')
            ass_devices_50 = 'wlan.wlan50.associated_devices'
        elif props.convert_tree_from_props('wlan.associated_devices.wlan50'):
            debug('SNMP')
            debug('\n')
            ass_devices_50 = 'wlan.associated_devices.wlan50'
        debug('ass_devices_50: %s' % ass_devices_50)
        debug('\n')
        if not ass_devices_24 and not ass_devices_50:
            return event

        print 123
        # check associated devices paths:
        datamodel, datamodel_5GHz = None, None
        datamodel_MAC, datamodel_SS, datamodel_LDDR, datamodel_LDUR,\
            datamodel_operating_standard = None, None, None, None, None

        if props.convert_tree_from_props('%s.WF' % ass_devices_24) or\
                props.convert_tree_from_props('%s.WF' % ass_devices_50):
            # TR181 Parameter (associated_devices.WF.AP.32.AD)
            # Technicolor_TC7230
            debug("TR181 Parameter")
            debug('\n')
            datamodel_MAC = 'MA'
            datamodel_SS = 'SS'
            datamodel_LDDR = 'LDDR'
            datamodel_LDUR = 'LDUR'
            datamodel_operating_standard = 'OS'
            # 2.4 GHz
            print 123456, '%s.WF.AP.32.AD' % ass_devices_24
            if props.convert_tree_from_props('%s.WF.AP.32.AD' % ass_devices_24):
                print
                print
                print
                print
                print
                print 1245
                debug(ass_devices_24)
                debug('\n')
                datamodel = 'WF.AP.32.AD'
            print
            print
            print 124

            # 5GHz:
            debug("ass_devices_50 %s" % ass_devices_50)
            debug('\n')
            if props.convert_tree_from_props('%s.WF.AP.112.AD' % ass_devices_50):
                debug("Inside if WF.AP.112.AD ")
                debug('\n')
                datamodel_5GHz = 'WF.AP.112.AD'
            debug("TR181 Parameter over")
            debug('\n')
        # TR98 Parameter
        # Vodafone-H-500-s.2, AD1018.3, VOX25

        if props.convert_tree_from_props('%s.LD' % ass_devices_24):
            # 2.4 Ghz
            debug("TR98 Parameter 2.4Ghz")
            debug('\n')
            datamodel_MAC = 'MACAddress'
            if props.convert_tree_from_props('%s.LD.1.WC.1.AD.1.SignalStrength' % ass_devices_24):
                # Vodafone-H-500-s.2
                # VOX25.5
                datamodel_SS = 'SignalStrength'
            elif props.convert_tree_from_props('%s.LD.1.WC.1.AD.1.X_Stats.SignalStrength' %
                                               ass_devices_24):
                # AD1018.3
                datamodel_SS = 'X_Stats.SignalStrength'
            debug('datamodel_SS %s' % datamodel_SS)
            debug('\n')

            datamodel_LDDR = 'X_LastDataDownlinkRate'
            datamodel_LDUR = 'X_LastDataUplinkRate'
            datamodel_operating_standard = 'Standard'
            datamodel = 'LD.1.WC.1.AD'
            debug('datamodel_2.4Ghz %s' % datamodel)
            debug('\n')
            debug('TR98 Parameter over - 2.4Ghz')
            debug('\n')

        if props.convert_tree_from_props('%s.LD' % ass_devices_50):
            # 5GHz
            debug("TR98 Parameter - 5Ghz")
            debug('\n')
            datamodel_MAC = 'MACAddress'
            if props.convert_tree_from_props('%s.LD.1.WC.5.AD.1.SignalStrength' % ass_devices_50):
                # Vodafone-H-500-s.2
                # VOX25.5
                datamodel_SS = 'SignalStrength'
            elif props.convert_tree_from_props('%s.LD.1.WC.5.AD.1.X_Stats.SignalStrength' %
                                               ass_devices_50):
                # AD1018.3
                datamodel_SS = 'X_Stats.SignalStrength'
            print('datamodel_SS %s', datamodel_SS)

            datamodel_LDDR = 'X_LastDataDownlinkRate'
            datamodel_LDUR = 'X_LastDataUplinkRate'
            datamodel_operating_standard = 'Standard'

            datamodel_5GHz = 'LD.1.WC.5.AD'
            print('datamodel_5GHz %s', datamodel_5GHz)
            print('TR98 Parameter over -5Ghz')

        print
        print
        print
        print
        print
        associated_devices_dict = props.convert_tree_from_props(
            '%s.%s' % (ass_devices_24, datamodel), {})
        print 51, 'associated_devices_dict', associated_devices_dict
        print type(associated_devices_dict)
        print
        print
        print
        print
        print('associated_devices_dict %s' % associated_devices_dict)

        associated_devices_dict_5GHz = props.convert_tree_from_props(
            '%s.%s' % (ass_devices_50, datamodel_5GHz), {})

        print('associated_devices_dict_5GHz %s' % associated_devices_dict_5GHz)

        print
        print
        print
        print
        number_of_associated_devices_wlan24 = props.convert_tree_from_props(
            "wlan.wlan24.device_number", len(associated_devices_dict))
        print 52, number_of_associated_devices_wlan24
        print 53, len(associated_devices_dict)
        print
        print
        print
        number_of_associated_devices_wlan50 = props.convert_tree_from_props(
            "wlan.wlan50.device_number", len(associated_devices_dict_5GHz))

        # loop the all devices:
        # 2.4GHz:
        print 55, number_of_associated_devices_wlan24
        print 56, associated_devices_dict
        print 58, type(associated_devices_dict)
        print 57, len(associated_devices_dict)
        for host in range(1, number_of_associated_devices_wlan24 + 1):
            print("host: %s" % host)

            # get all usefull props:

            # MAC:
            MAC_model = '%s.%s.%s.%s' %\
                (ass_devices_24, datamodel, host, datamodel_MAC)
            MAC = props.convert_tree_from_props(MAC_model, "N/A")
            print("MAC: %s" % MAC)

            # SignalStrength
            signal_strength_model = '%s.%s.%s.%s'\
                % (ass_devices_24, datamodel, host, datamodel_SS)

            print("signal_strength_model: %s" %
                  signal_strength_model)
            SignalStrength = props.convert_tree_from_props(signal_strength_model)
            # SignalStrength = props.convert_tree_from_props(signal_strength_model,
            #                                                LOW_RSSI_THRESHOLD_24)
            print("SignalStrength: %s" % SignalStrength)

            if SignalStrength:
                print("Signal Strngth not empty string")
                wlan24_rssi_sum += int(SignalStrength)
            else:
                print("Signal Strength  empty string - continue looping")
                continue
            # LastDataDownlinkRate
            LastDataDownlinkRate = props.convert_tree_from_props(
                '%s.%s.%s.%s' %
                (ass_devices_24, datamodel, host, datamodel_LDDR),
                LOW_PHY_DOWN_THRESHOLD_24)
            print("LastDataDownlinkRate: %s" %
                  LastDataDownlinkRate)

            print
            print
            print
            print 312, type(LastDataDownlinkRate), LOW_PHY_DOWN_THRESHOLD_24
            print
            wlan24_last_data_downlink_rate_sum += int(LastDataDownlinkRate)

            # LastDataUplinkRate

            LastDataUplinkRate = props.convert_tree_from_props(
                '%s.%s.%s.%s' %
                (ass_devices_24, datamodel, host, datamodel_LDUR),
                LOW_PHY_UP_THRESHOLD_24)

            print("LastDataUplinkRate: %s" % LastDataUplinkRate)
            wlan24_last_data_uplink_rate_sum += int(LastDataUplinkRate)

            # wlan24_host_operating_standard
            wlan24_host_operating_standard = props.convert_tree_from_props(
                '%s.%s.%s.%s' %
                (ass_devices_24, datamodel, host,
                 datamodel_operating_standard),
                "N/A")

            print '%s.%s.%s.%s' %\
                (ass_devices_24, datamodel, host,
                 datamodel_operating_standard)

            print("wlan24_host_operating_standard: %s" %
                  wlan24_host_operating_standard)

            try:
                print("Low RSSI 2.4GHz threshold check")
                if int(SignalStrength) < LOW_RSSI_THRESHOLD_24:
                    print("Low RSSI 2.4GHz threshold met")
                    wlan24_ass_low_rssi += 1
                    wlan24_ass_low_rssi_list.append(MAC)
            except:
                print("Low RSSI 2.4GHz threshold check failed")

            try:
                print("Low Phy Down 2.4GHz threshold check")
                if int(LastDataDownlinkRate) < LOW_PHY_DOWN_THRESHOLD_24:
                    print(
                        "Low Phy Down 2.4GHz threshold met")
                    wlan24_ass_phy_down += 1
                    wlan24_ass_phy_down_list.append(MAC)
            except:
                print("Low Phy Down 2.4GHz threshold check failed")

            try:
                print("Low Phy Up 2.4GHz threshold check")
                if int(LastDataUplinkRate) < LOW_PHY_UP_THRESHOLD_24:
                    print("Low Phy Up 2.4GHz threshold met")
                    wlan24_ass_phy_up += 1
                    wlan24_ass_phy_up_list.append(MAC)
            except:
                print("Low Phy Up 2.4GHz threshold check failed")

            try:
                print("Operating Standard 2.4GHz  check")
                if wlan24_host_operating_standard == "ab":
                    wlan24_device_number_ab += 1
                if wlan24_host_operating_standard == "n":
                    wlan24_device_number_n += 1
                if wlan24_host_operating_standard == "g":
                    wlan24_device_number_g += 1
                if wlan24_host_operating_standard == "ac":
                    wlan24_device_number_ac += 1

            except:
                print("Operating Standard 2.4GHz check failed")

        # 5GHz:
        for host in range(1, number_of_associated_devices_wlan50 + 1):

            wlan50_host_mac_address = props.convert_tree_from_props(
                '%s.%s.%s.%s' %
                (ass_devices_50, datamodel_5GHz, host, datamodel_MAC),
                "N/A")

            try:
                print("Low RSSI 5GHz threshold check")

                wlan50_rssi_sum += props.convert_tree_from_props(
                    '%s.%s.%s.%s' %
                    (ass_devices_50, datamodel_5GHz, host, datamodel_SS),
                    0)

                rssi_val = props.convert_tree_from_props(
                    '%s.%s.%s.%s' %
                    (ass_devices_50, datamodel_5GHz, host, datamodel_SS), 0)

                if int(rssi_val) < LOW_RSSI_THRESHOLD_50:
                    print("Low RSSI 5GHz threshold met")
                    wlan50_ass_low_rssi += 1
                    wlan50_ass_low_rssi_list.append(wlan50_host_mac_address)
            except:
                print("Low RSSI 5GHz threshold check failed")

            try:
                print("Low Phy Down 5GHz threshold check")

                phy_down_val = props.convert_tree_from_props(
                    '%s.%s.%s.%s' %
                    (ass_devices_50, datamodel_5GHz, host, datamodel_LDDR),
                    0)
                phy_down_val_for_check = props.convert_tree_from_props(
                    '%s.%s.%s.%s' %
                    (ass_devices_50, datamodel_5GHz, host, datamodel_LDDR),
                    LOW_PHY_DOWN_THRESHOLD_50)

                wlan50_last_data_downlink_rate_sum += phy_down_val

                if int(phy_down_val_for_check) < LOW_PHY_DOWN_THRESHOLD_50:
                    print("Low Phy Down 5GHz threshold met")
                    wlan50_ass_phy_down = wlan50_ass_phy_down + 1
                    wlan50_ass_phy_down_list.append(wlan50_host_mac_address)

            except:
                print("Low Phy Down 5GHz threshold check failed")

            try:
                print("Low Phy Up 5GHz threshold check")

                phy_up_val = props.convert_tree_from_props(
                    '%s.%s.%s.%s' %
                    (ass_devices_50, datamodel_5GHz, host, datamodel_LDUR),
                    0)
                phy_up_val_for_check = props.convert_tree_from_props(
                    '%s.%s.%s.%s' %
                    (ass_devices_50, datamodel_5GHz, host, datamodel_LDUR),
                    LOW_PHY_UP_THRESHOLD_50)

                wlan50_last_data_uplink_rate_sum += phy_up_val
                if int(phy_up_val_for_check) < LOW_PHY_UP_THRESHOLD_50:
                    print("Low Phy Up 5GHz threshold met")
                    wlan50_ass_phy_up = wlan50_ass_phy_up + 1
                    wlan50_ass_phy_up_list.append(wlan50_host_mac_address)

            except:
                print("Low Phy Up 5GHz threshold check failed")

            wlan50_host_operating_standard = props.convert_tree_from_props(
                '%s.%s.%s.%s' %
                (ass_devices_50, datamodel_5GHz, host,
                 datamodel_operating_standard),
                "N/A")

            try:
                print("Operating Standard 5GHz  check")

                if wlan50_host_operating_standard == "n":
                    wlan50_device_number_n += 1

                if wlan50_host_operating_standard == "ac":
                    wlan50_device_number_ac += 1

            except:
                print("Operating Standard 5GHz check failed")

        # 2.4 GHz

        # props['wlan.wlan24.device_number'] =\
        #     number_of_associated_devices_wlan24
        #
        # props['wlan.wlan24.device_number_ab'] = wlan24_device_number_ab
        # props['wlan.wlan24.device_number_g'] = wlan24_device_number_g
        # props['wlan.wlan24.device_number_n'] = wlan24_device_number_n
        # props['wlan.wlan24.device_number_ac'] = wlan24_device_number_ac
        #
        # props['wlan.wlan24.ass_low_rssi.current'] = wlan24_ass_low_rssi
        # props['wlan.wlan24.ass_low_phy_down.current'] = wlan24_ass_phy_down
        # props['wlan.wlan24.ass_low_phy_up.current'] = wlan24_ass_phy_up
        #
        # props['wlan.wlan24.ass_low_rssi_list.current'] =\
        #     wlan24_ass_low_rssi_list
        # props['wlan.wlan24.ass_low_phy_down_list.current'] =\
        #     wlan24_ass_phy_down_list
        # props['wlan.wlan24.ass_low_phy_up_list.current'] =\
        #     wlan24_ass_phy_up_list
        #
        # props['wlan.wlan24.rssi_sum.current'] = wlan24_rssi_sum
        # props['wlan.wlan24.last_data_downlink_rate_sum.current'] =\
        #     wlan24_last_data_downlink_rate_sum
        # props['wlan.wlan24.last_data_uplink_rate_sum.current'] =\
        #     wlan24_last_data_uplink_rate_sum
        #
        #
        # # 5GHz
        # props['wlan.wlan50.device_number'] =\
        #     number_of_associated_devices_wlan50
        #
        # props['wlan.wlan50.device_number_n'] = wlan50_device_number_n
        # props['wlan.wlan50.device_number_ac'] = wlan50_device_number_ac
        #
        # props['wlan.wlan50.ass_low_rssi.current'] = wlan50_ass_low_rssi
        # props['wlan.wlan50.ass_low_phy_down.current'] = wlan50_ass_phy_down
        # props['wlan.wlan50.ass_low_phy_up.current'] = wlan50_ass_phy_up
        #
        # props['wlan.wlan50.ass_low_rssi_list.current'] =\
        #     wlan50_ass_low_rssi_list
        # props['wlan.wlan50.ass_low_phy_down_list.current'] =\
        #     wlan50_ass_phy_down_list
        # props['wlan.wlan50.ass_low_phy_up_list.current'] =\
        #     wlan50_ass_phy_up_list
        #
        # props['wlan.wlan50.rssi_sum.current'] = wlan50_rssi_sum
        # props['wlan.wlan50.last_data_downlink_rate_sum.current'] =\
        #     wlan50_last_data_downlink_rate_sum
        # props['wlan.wlan50.last_data_uplink_rate_sum.current'] =\
        #     wlan50_last_data_uplink_rate_sum

        debug("after change %s" % event)
        return event

    def close(self):
        pass


conf = {

    "rssi_threshold_24": -81,
    "downlink_rate_threshold_24": 1000,
    "uplink_rate_threshold_24": 1000,
    "rssi_threshold_50": -89,
    "downlink_rate_threshold_50": 1000,
    "uplink_rate_threshold_50": 1000,
    "issue_day_occurrences": 2
}

a = CalcAssociatedDevicesKPIs(name='test', config=conf)
a.process_event(event)
