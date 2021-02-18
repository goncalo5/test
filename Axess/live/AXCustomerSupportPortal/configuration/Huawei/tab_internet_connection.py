internet_interface =  {
    "__type": "section-widget",
    "name": "WANInterfaceInternet",
    "flow": "InternetConnectionFlow",
    "pr": "Internet Interface",
    "lockScreen": False,
    "width": 6,
    "errorTimeout": 120,
    "errorMessage": "Error retrieving WAN interface info!",
     "elements": [
    {
        "name": "I.WD.smartIndex1.WCD.smartIndex2._WAN_TYPE_.smartIndex3.E",
        "smartindex":"Huawei_internet_interface",
        "pr": "Enable",
        "tFunction": "eval_enabled",
        "mFunction": "eval_enabled"
    },
    {
        "name": "I.WD.smartIndex1.WCD.smartIndex2._WAN_TYPE_.smartIndex3.CS",
        "smartindex":"Huawei_internet_interface",
        "pr": "Status",
        "mFunction": "eval_connection_status",
        "tFunction": "eval_connection_status"
    },
    # {
    #     "name": "I.WD.smartIndex1.WCD.smartIndex2._WAN_TYPE_.smartIndex3.U",
    #     "smartindex":"Huawei_internet_interface",
    #     "pr": "Uptime",
    #     "mFunction": "convert_uptime",
    #     "tFunction": "eval_uptime",
    # },
    {
        "name": "I.WD.smartIndex1.WCD.smartIndex2._WAN_TYPE_.smartIndex3.N",
        "smartindex":"Huawei_internet_interface",
        "pr": "Name",
    },
    {
        "name": "I.WD.smartIndex1.WCD.smartIndex2._WAN_TYPE_.smartIndex3.EIA",
        "smartindex":"Huawei_internet_interface",
        "pr": "IP Address",
    },
    {
        "name": "I.WD.smartIndex1.WCD.smartIndex2._WAN_TYPE_.smartIndex3.DG",
        "smartindex":"Huawei_internet_interface",
        "pr": "Gateway",
    },
    {
        "name": "I.WD.smartIndex1.WCD.smartIndex2._WAN_TYPE_.smartIndex3.DS",
        "smartindex":"Huawei_internet_interface",
        "pr": "DNS Servers",
    },
    # {
    #     "name": "I.WD.smartIndex1.WCD.smartIndex2._WAN_TYPE_.smartIndex3.S.EBR",
    #     "smartindex":"Huawei_internet_interface",
    #     "pr": "Bytes Received",
    #     "mFunction": "convert_traffic",
    # },
    # {
    #     "name": "I.WD.smartIndex1.WCD.smartIndex2._WAN_TYPE_.smartIndex3.S.EBS",
    #     "smartindex":"Huawei_internet_interface",
    #     "pr": "Bytes Sent",
    #     "mFunction": "convert_traffic",
    # },
    # {
    #     "name": "I.WD.smartIndex1.WCD.smartIndex2._WAN_TYPE_.smartIndex3.S.EPR",
    #     "smartindex":"Huawei_internet_interface",
    #     "pr": "Total Packets Received",
    # },
    # {
    #     "name": "I.WD.smartIndex1.WCD.smartIndex2._WAN_TYPE_.smartIndex3.S.EPS",
    #     "smartindex":"Huawei_internet_interface",
    #     "pr": "Total Packets Sent",
    # },
    # {
    #     "name": "I.WD.smartIndex1.WCD.smartIndex2._WAN_TYPE_.smartIndex3.S.EUPR",
    #     "smartindex":"Huawei_internet_interface",
    #     "pr": "Unicast Packets Received",
    # },
    # {
    #     "name": "I.WD.smartIndex1.WCD.smartIndex2._WAN_TYPE_.smartIndex3.S.EUPS",
    #     "smartindex":"Huawei_internet_interface",
    #     "pr": "Unicast Packets Sent",
    # },
    # {
    #     "name": "I.WD.smartIndex1.WCD.smartIndex2._WAN_TYPE_.smartIndex3.S.EMPR",
    #     "smartindex":"Huawei_internet_interface",
    #     "pr": "Multicast Packets Received",
    # },
    # {
    #     "name": "I.WD.smartIndex1.WCD.smartIndex2._WAN_TYPE_.smartIndex3.S.EMPS",
    #     "smartindex":"Huawei_internet_interface",
    #     "pr": "Multicast Packets Sent",
    # },
    # {
    #     "name": "I.WD.smartIndex1.WCD.smartIndex2._WAN_TYPE_.smartIndex3.S.EDPR",
    #     "smartindex":"Huawei_internet_interface",
    #     "pr": "Discarded Packets Received",
    # },
    # {
    #     "name": "I.WD.smartIndex1.WCD.smartIndex2._WAN_TYPE_.smartIndex3.S.EDPS",
    #     "smartindex":"Huawei_internet_interface",
    #     "pr": "Discarded Packets Received",
    # },
    # {
    #     "name": "I.WD.smartIndex1.WCD.smartIndex2._WAN_TYPE_.smartIndex3.S.EER",
    #     "smartindex":"Huawei_internet_interface",
    #     "pr": "Errors Received",
    # },
    # {
    #     "name": "I.WD.smartIndex1.WCD.smartIndex2._WAN_TYPE_.smartIndex3.S.EES",
    #     "smartindex":"Huawei_internet_interface",
    #     "pr": "Errors Sent",
    # },
    ]
}

voip_interface = {
    "__type": "section-widget",
    "name": "WANInterfaceVoIP",
    "flow": "InternetConnectionFlow",
    "pr": "VoIP Interface",
    "lockScreen": False,
    "width": 6,
    "errorTimeout": 120,
    "errorMessage": "Error retrieving WAN interface info!",
     "elements": [
    {
        "name": "I.WD.smartIndex1.WCD.smartIndex2._WAN_TYPE_.smartIndex3.E",
        "smartindex":"Huawei_voip_interface",
        "pr": "Enable",
        "tFunction": "eval_enabled",
        "mFunction": "eval_enabled"
    },
    # {
    #     "name": "I.WD.smartIndex1.WCD.smartIndex2._WAN_TYPE_.smartIndex3.CS",
    #     "smartindex":"AVM_voip_interface",
    #     "pr": "Status",
    #     "mFunction": "eval_connection_status",
    #     "tFunction": "eval_connection_status"
    # },
    # {
    #     "name": "I.WD.smartIndex1.WCD.smartIndex2._WAN_TYPE_.smartIndex3.U",
    #     "smartindex":"AVM_voip_interface",
    #     "pr": "Uptime",
    #     "mFunction": "convert_uptime",
    #     "tFunction": "eval_uptime",
    # },
    # {
    #     "name": "I.WD.smartIndex1.WCD.smartIndex2._WAN_TYPE_.smartIndex3.N",
    #     "smartindex":"AVM_voip_interface",
    #     "pr": "Name",
    # },
    # {
    #     "name": "I.WD.smartIndex1.WCD.smartIndex2._WAN_TYPE_.smartIndex3.EIA",
    #     "smartindex":"AVM_voip_interface",
    #     "pr": "IP Address",
    # },
    # {
    #     "name": "I.WD.smartIndex1.WCD.smartIndex2._WAN_TYPE_.smartIndex3.DG",
    #     "smartindex":"AVM_voip_interface",
    #     "pr": "Gateway",
    # },
    # {
    #     "name": "I.WD.smartIndex1.WCD.smartIndex2._WAN_TYPE_.smartIndex3.DS",
    #     "smartindex":"AVM_voip_interface",
    #     "pr": "DNS Servers",
    # },
    # {
    #     "name": "I.WD.smartIndex1.WCD.smartIndex2._WAN_TYPE_.smartIndex3.S.EBR",
    #     "smartindex":"AVM_voip_interface",
    #     "pr": "Bytes Received",
    #     "mFunction": "convert_traffic",
    # },
    # {
    #     "name": "I.WD.smartIndex1.WCD.smartIndex2._WAN_TYPE_.smartIndex3.S.EBS",
    #     "smartindex":"AVM_voip_interface",
    #     "pr": "Bytes Sent",
    #     "mFunction": "convert_traffic",
    # },
    # {
    #     "name": "I.WD.smartIndex1.WCD.smartIndex2._WAN_TYPE_.smartIndex3.S.EPR",
    #     "smartindex":"AVM_voip_interface",
    #     "pr": "Total Packets Received",
    # },
    # {
    #     "name": "I.WD.smartIndex1.WCD.smartIndex2._WAN_TYPE_.smartIndex3.S.EPS",
    #     "smartindex":"AVM_voip_interface",
    #     "pr": "Total Packets Sent",
    # },
    # {
    #     "name": "I.WD.smartIndex1.WCD.smartIndex2._WAN_TYPE_.smartIndex3.S.EUPR",
    #     "smartindex":"AVM_voip_interface",
    #     "pr": "Unicast Packets Received",
    # },
    # {
    #     "name": "I.WD.smartIndex1.WCD.smartIndex2._WAN_TYPE_.smartIndex3.S.EUPS",
    #     "smartindex":"AVM_voip_interface",
    #     "pr": "Unicast Packets Sent",
    # },
    # {
    #     "name": "I.WD.smartIndex1.WCD.smartIndex2._WAN_TYPE_.smartIndex3.S.EMPR",
    #     "smartindex":"AVM_voip_interface",
    #     "pr": "Multicast Packets Received",
    # },
    # {
    #     "name": "I.WD.smartIndex1.WCD.smartIndex2._WAN_TYPE_.smartIndex3.S.EMPS",
    #     "smartindex":"AVM_voip_interface",
    #     "pr": "Multicast Packets Sent",
    # },
    # {
    #     "name": "I.WD.smartIndex1.WCD.smartIndex2._WAN_TYPE_.smartIndex3.S.EDPR",
    #     "smartindex":"AVM_voip_interface",
    #     "pr": "Discarded Packets Received",
    # },
    # {
    #     "name": "I.WD.smartIndex1.WCD.smartIndex2._WAN_TYPE_.smartIndex3.S.EDPS",
    #     "smartindex":"AVM_voip_interface",
    #     "pr": "Discarded Packets Received",
    # },
    # {
    #     "name": "I.WD.smartIndex1.WCD.smartIndex2._WAN_TYPE_.smartIndex3.S.EER",
    #     "smartindex":"AVM_voip_interface",
    #     "pr": "Errors Received",
    # },
    # {
    #     "name": "I.WD.smartIndex1.WCD.smartIndex2._WAN_TYPE_.smartIndex3.S.EES",
    #     "smartindex":"AVM_voip_interface",
    #     "pr": "Errors Sent",
    # },
    ]
}

pppoe = {
    "__type": "section-widget",
    "name": "PPPoE",
    "flow": "InternetConnectionFlow",
    "pr": "PPPoE Settings",
    "width": 6,
    "filter" : {
        "OP" : "custom_script",
        "condition": "AVM_has_pppoe",
        "argument": "internet",
    },
    "errorTimeout": 120,
    "errorMessage": "Error retrieving DSL interface info!",
    "elements": [
    {
        "name": "I.WD.smartIndex1.WCD.smartIndex2._WAN_TYPE_.smartIndex3.Us",
        "smartindex":"AVM_internet_interface",
        "pr": "Username",
    },
    {
        "name": "I.WD.smartIndex1.WCD.smartIndex2._WAN_TYPE_.smartIndex3.CoT",
        "smartindex":"AVM_internet_interface",
        "pr": "ConnectionTrigger",
    },
    {
        "name": "I.WD.smartIndex1.WCD.smartIndex2._WAN_TYPE_.smartIndex3.XAVMDPE",
        "smartindex":"AVM_internet_interface",
        "pr": "DisconnectPreventionEnable",
    },
    {
        "name": "I.WD.smartIndex1.WCD.smartIndex2._WAN_TYPE_.smartIndex3.XAVMDPH",
        "smartindex":"AVM_internet_interface",
        "pr": "DisconnectPreventionHour",
    },
    ],
}

dsl = {
    "__type": "section-widget",
    "name": "DSLConnection",
    "flow": "InternetConnectionFlow",
    "pr": "DSL",
    "width": 6,
    "filter" : {
        "OP" : "custom_script",
        "condition": "AVM_wantype",
        "argument" : "DSL"
    },
    "errorTimeout": 120,
    "errorMessage": "Error retrieving DSL interface info!",
    "elements": [
    {
        "name": "I.WD.1.WIC.ShS",
        "pr": "DSL Uptime",
        "mFunction": "convert_uptime",
        "tFunction": "eval_uptime",
    },
    {
        "name": "I.WD.1.WIC.MT",
        "pr": "DSL ModulationType",
    },
    {
        "name": "I.WD.1.WIC.DP",
        "pr": "DSL Datapath",
    },
    {
        "name": "I.XAVMAS.DP",
        "pr": "AVM DSL Performance",
    },
    {
        "name": "I.WD.1.WIC.DoP",
        "pr": "DSL Downstream-Power",
        "units": "dBmV",
        "mFunction": "AVM_div10",
    },
    {
        "name": "I.WD.1.WIC.DNM",
        "pr": "DSL Downstream-Noise-Margin",
        "units": "dB",
        "mFunction": "AVM_div10",
    },
    {
        "name": "I.WD.1.WIC.DA",
        "pr": "DSL Downstream-Daempfung",
        "units": "dB",
        "mFunction": "AVM_div10",
    },
    {
        "name": "I.WD.1.WIC.DMR",
        "pr": "DSL Downstream-Max-Rate",
        "units": "kb/s",
    },
    {
        "name": "I.WD.1.WIC.DCR",
        "pr": "DSL Downstream-Current-Rate",
        "units": "kb/s",
    },
    {
        "name": "I.WD.1.WIC.UP",
        "pr": "DSL Upstream-Power",
        "units": "dBmV",
        "mFunction": "AVM_div10",
     },
    {
        "name": "I.WD.1.WIC.UNM",
        "pr": "DSL Upstream-Noise-Margin",
        "mFunction": "AVM_div10",
        "units": "dB",
    },
    {
        "name": "I.WD.1.WIC.UA",
        "pr": "DSL Upstream-Daempfung",
        "units": "dB",
        "mFunction": "AVM_div10",
    },
    {
        "name": "I.WD.1.WIC.UMR",
        "pr": "DSL Upstream-Max-Rate",
        "units": "kb/s",
    },
    {
        "name": "I.WD.1.WIC.UCR",
        "pr": "DSL Upstream-Current-Rate",
        "units": "kb/s",
    },
    ]
}

dsl_stats_current_day = {
    "__type": "section-widget",
    "name": "DSLstatsCD",
    "flow": "InternetConnectionFlow",
    "pr": "DSL stats current day",
    "width": 6,
    "filter" : {
        "OP" : "custom_script",
        "condition": "AVM_wantype",
        "argument" : "DSL"
    },
    "errorTimeout": 120,
    "errorMessage": "Error retrieving DSL interface info!",
    "elements": [
    {
        "name": "I.WD.1.WIC.St.CD.AE",
        "pr": "ATUCFECErrors",
    },
    {
        "name": "I.WD.1.WIC.St.CD.ATE",
        "pr": "ATUCHECErrors",
    },
    {
        "name": "I.WD.1.WIC.St.CD.ATUE",
        "pr": "ATUCCRCErrors",
    },
    {
        "name": "I.WD.1.WIC.St.CD.CD",
        "pr": "CellDelin",
    },
    {
        "name": "I.WD.1.WIC.St.CD.CE",
        "pr": "CRCErrors",
    },
    {
        "name": "I.WD.1.WIC.St.CD.FE",
        "pr": "FECErrors",
    },
    {
        "name": "I.WD.1.WIC.St.CD.HE",
        "pr": "HECErrors",
    },
    ]
}

dsl_stats_showtime = {
    "__type": "section-widget",
    "name": "DSLstatsS",
    "flow": "InternetConnectionFlow",
    "pr": "DSL stats showtime",
    "width": 6,
    "filter" : {
        "OP" : "custom_script",
        "condition": "AVM_wantype",
        "argument" : "DSL"
    },
    "errorTimeout": 120,
    "errorMessage": "Error retrieving DSL interface info!",
    "elements": [
    {
        "name": "I.WD.1.WIC.St.S.AE",
        "pr": "ATUCFECErrors",
    },
    {
        "name": "I.WD.1.WIC.St.S.ATE",
        "pr": "ATUCHECErrors",
    },
    {
        "name": "I.WD.1.WIC.St.S.ATUE",
        "pr": "ATUCCRCErrors",
    },
    {
        "name": "I.WD.1.WIC.St.S.CD",
        "pr": "CellDelin",
    },
    {
        "name": "I.WD.1.WIC.St.S.CE",
        "pr": "CRCErrors",
    },
    {
        "name": "I.WD.1.WIC.St.S.FE",
        "pr": "FECErrors",
    },
    {
        "name": "I.WD.1.WIC.St.S.HE",
        "pr": "HECErrors",
    },
    ]
}

dsl_stats_total = {
    "__type": "section-widget",
    "name": "DSLstatsT",
    "flow": "InternetConnectionFlow",
    "pr": "DSL stats total",
    "width": 6,
    "filter" : {
        "OP" : "custom_script",
        "condition": "AVM_wantype",
        "argument" : "DSL"
    },
    "errorTimeout": 120,
    "errorMessage": "Error retrieving DSL interface info!",
    "elements": [
    {
        "name": "I.WD.1.WIC.St.T.AE",
        "pr": "ATUCFECErrors",
    },
    {
        "name": "I.WD.1.WIC.St.T.ATE",
        "pr": "ATUCHECErrors",
    },
    {
        "name": "I.WD.1.WIC.St.T.ATUE",
        "pr": "ATUCCRCErrors",
    },
    {
        "name": "I.WD.1.WIC.St.T.CD",
        "pr": "CellDelin",
    },
    {
        "name": "I.WD.1.WIC.St.T.CE",
        "pr": "CRCErrors",
    },
    {
        "name": "I.WD.1.WIC.St.T.FE",
        "pr": "FECErrors",
    },
    {
        "name": "I.WD.1.WIC.St.T.HE",
        "pr": "HECErrors",
    },
    ]
}

return {
    "name": "InternetConnection",
    "__type": "support-portal-tab",
    "pr": "Internet Connection",
    "elements": [
        internet_interface,
        voip_interface,
#        pppoe,
#        dsl,
#        dsl_stats_current_day,
#        dsl_stats_showtime,
#        dsl_stats_total,
    ]
}
