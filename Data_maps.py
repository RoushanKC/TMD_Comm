format_map={
    "Bool"         : "?",
    "SInt"         : ">b",
    "UInt"         : ">H",
    "BInt"         : ">H",
    "Real"         : ">f",
    "String"       : ">98s" ,
    "not_defined"  : "?",
}

type_dict={
    "Bool"   :1,
    "UInt"   :2,
    "BInt"   :2,
    "SInt"   :1,
    "Real"   :4,
    "String" :98,
}

receive_offset_map= [
    {"address":0,     "name":"xAlive",                       "type":"Bool"},      #case 1 byte bit manup
    #{"address":1,    "name":"xRemote",                      "type":"Bool"},
    #{"address":2,    "name":"xReserve1",                    "type":"Bool"},
    #{"address":3,    "name":"xReserve2",                    "type":"Bool"},
    #{"address":4,    "name":"xReserve3",                    "type":"Bool"},
    #{"address":5,    "name":"xReserve4",                    "type":"Bool"},
    #{"address":6,    "name":"xReserve5",                    "type":"Bool"},
    #{"address":7,    "name":"xReserve6",                    "type":"Bool"},
    {"address":8,     "name":"xReserve7",                    "type":"SInt"},
    {"address":16,    "name":"uiTelegramNo",                 "type":"UInt"},
    {"address":32,    "name":"uiReserve1",                   "type":"UInt"},
    {"address":48,    "name":"rReserve2",                    "type":"Real"},
    {"address":80,    "name":"rReserve3",                    "type":"Real"},
    {"address":112,   "name":"rReserve4",                    "type":"Real"},
    {"address":144,   "name":"rReserve5",                    "type":"Real"},
    {"address":176,   "name":"rReserve6",                    "type":"Real"},
    {"address":208,   "name":"rReserve7",                    "type":"Real"},
    {"address":240,   "name":"xMessungEin",                  "type":"Bool"},     #case 1 byte bit manup
    #{"address":241,  "name":"xRegelungEin",                 "type":"Bool"},
    #{"address":242,  "name":"xQuerRegEin",                  "type":"Bool"},
    #{"address":243,  "name":"xLaengsRegEin",                "type":"Bool"},
    #{"address":244,  "name":"xKalibrierungEin",             "type":"Bool"},
    #{"address":245,  "name":"xLinienmessungEin",            "type":"Bool"},
    #{"address":246,  "name":"xReserve1",                    "type":"Bool"},
    #{"address":247,  "name":"xReserve2",                    "type":"Bool"},
    {"address":248,   "name":"xReserve3",                    "type":"SInt"},
    {"address":256,   "name":"xAL_1",                        "type":"BInt"},
    {"address":272,   "name":"xAL_2",                        "type":"BInt"},
    {"address":288,   "name":"rAktPos_Sensor",               "type":"Real"},
    {"address":320,   "name":"rAktDicke",                    "type":"Real"},
    {"address":352,   "name":"rMittlereDicke",               "type":"Real"},
    {"address":384,   "name":"r2Sigma",                      "type":"Real"},
    {"address":416,   "name":"rMaxDicke",                    "type":"Real"},
    {"address":448,   "name":"rMinDicke",                    "type":"Real"},
    {"address":480,   "name":"rSollDicke",                   "type":"Real"},
    {"address":512,   "name":"rTolPos",                      "type":"Real"},
    {"address":544,   "name":"rTolNeg",                      "type":"Real"},
    {"address":576,   "name":"rMessung_StartPos",            "type":"Real"},
    {"address":608,   "name":"rMessung_EndPos",              "type":"Real"},
    {"address":640,   "name":"rNettoBreite",                 "type":"Real"},
    {"address":672,   "name":"rNettoBreite_Start",           "type":"Real"},
    {"address":704,   "name":"rNettoBreite_End",             "type":"Real"},
    {"address":736,   "name":"rBruttoBreite",                "type":"Real"},
    {"address":768,   "name":"rBruttoBreite_Start",          "type":"Real"},
    {"address":800,   "name":"rBruttoBreite_End",            "type":"Real"},
    {"address":832,   "name":"rKalibrierungswert",           "type":"Real"},
    {"address":864,   "name":"rDicke_Corrwert",              "type":"Real"},
    {"address":896,   "name":"rKalibrierungspos",            "type":"Real"},
    {"address":928,   "name":"rSollzeit_Linienmessung",      "type":"Real"},
    {"address":960,   "name":"rPos_Linienmessung",           "type":"Real"},
    {"address":992,   "name":"uiModusQuerProfilReg",         "type":"UInt"},
    {"address":1008,  "name":"uiBolzenAnzahl",               "type":"UInt"},
    {"address":1024,  "name":"rBolzenBreite",                "type":"Real"},
    {"address":1056,  "name":"rDuesenBreite",                "type":"Real"},
    {"address":1088,  "name":"rBolzenDeckling_links",        "type":"Real"},
    {"address":1120,  "name":"rBolzenDeckling_rechts",       "type":"Real"},
    {"address":1152,  "name":"rBolzenManuell_links",         "type":"Real"},
    {"address":1184,  "name":"rBolzenManuell_rechts",        "type":"Real"},
    {"address":1216,  "name":"rLiniengeschw",                "type":"Real"},
    {"address":1248,  "name":"rTraversieren_km",             "type":"Real"},
    {"address":1280,  "name":"rSchrumpf",                    "type":"Real"},
    {"address":1312,  "name":"stOrderNo_max_length",         "type":"SInt"},
    {"address":1320,  "name":"stOrderNo_actual_len_order_no","type":"SInt"},
    {"address":1328,  "name":"stOrderNo",                    "type":"String"},
    {"address":2112,  "name":"stCustomerName_max_len",       "type":"SInt"},
    {"address":2120,  "name":"stCustomerName_actual_len",    "type":"SInt"},
    {"address":2128,  "name":"stCustomerName",               "type":"String"},
    {"address":2912,  "name":"rArtikelNo",                   "type":"Real"},
    {"address":2944,  "name":"stPersonal_max_len",           "type":"SInt"},
    {"address":2952,  "name":"stPersonal_actual_len",        "type":"SInt"},
    {"address":2960,  "name":"stPersonal",                   "type":"String"},
    {"address":3744,  "name":"rAuftragsmenge",               "type":"Real"},
    {"address":3776,  "name":"rBenefits",                    "type":"Real"},
    {"address":3808,  "name":"stMaterialtyp_max_len",        "type":"SInt"},
    {"address":3816,  "name":"stMaterialtyp_actual_len",     "type":"SInt"},
    {"address":3824,  "name":"stMaterialtyp",                "type":"String"},
    {"address":4608,  "name":"rDicke_Produkt",               "type":"Real"},
    {"address":4640,  "name":"rBreite_Produkt",              "type":"Real"},
    {"address":4672,  "name":"rRemainingTime",               "type":"Real"},
    {"address":4704,  "name":"rReserve_1",                   "type":"Real"},
    {"address":4736,  "name":"rReserve_2",                   "type":"Real"},
    {"address":4768,  "name":"rReserve_3",                   "type":"Real"},
    {"address":4800,  "name":"rReserve_4",                   "type":"Real"},
    {"address":4832,  "name":"rReserve_5",                   "type":"Real"},
    {"address":4864,  "name":"rReserve_6",                   "type":"Real"},
    {"address":4896,  "name":"rReserve_7",                   "type":"Real"},
    {"address":4928,  "name":"rReserve_8",                   "type":"Real"},
    {"address":4960,  "name":"rReserve_9",                   "type":"Real"},
    {"address":4992,  "name":"rReserve_10",                  "type":"Real"},
    {"address":5024,  "name":"rReserve_11",                  "type":"Real"},
    {"address":5056,  "name":"rReserve_12",                  "type":"Real"},
    {"address":5088,  "name":"rReserve_13",                  "type":"Real"},
    {"address":5120,  "name":"rReserve_14",                  "type":"Real"},
    {"address":5152,  "name":"rReserve_15",                  "type":"Real"},
    {"address":5184,  "name":"rReserve_16",                  "type":"Real"},
    {"address":5216,  "name":"rReserve_17",                  "type":"Real"},
    {"address":5248,  "name":"rReserve_18",                  "type":"Real"},
    {"address":5280,  "name":"rReserve_19",                  "type":"Real"},
    {"address":5312,  "name":"rReserve_20",                  "type":"Real"},
    {"address":5344,  "name":"rReserve_21",                  "type":"Real"},
    {"address":5376,  "name":"rReserve_22",                  "type":"Real"},
    {"address":5408,  "name":"rReserve_23",                  "type":"Real"},
    {"address":5440,  "name":"rReserve_24",                  "type":"Real"},
    {"address":5472,  "name":"rReserve_25",                  "type":"Real"},
    {"address":5504,  "name":"rReserve_26",                  "type":"Real"},
    {"address":5536,  "name":"uiBolzenkurveNo",              "type":"UInt"},
    {"address":5552,  "name":"rAktDicke_Bolzen",             "type":"Real"},      #case array
    {"address":12144, "name":"rReserve_28",                  "type":"Real"},
    {"address":12176, "name":"rReserve_29",                  "type":"Real"},
    {"address":12208, "name":"rReserve_30",                  "type":"Real"},
    {"address":12240, "name":"rReserve_31",                  "type":"Real"},
    {"address":12272, "name":"rReserve_32",                  "type":"Real"},
    {"address":12304, "name":"uiMesskurveNo",                "type":"UInt"},
    {"address":12320, "name":"raktDicke_Pos",                "type":"Real"},      #case array

]
receive_offset_byte_0=[
    {"address":0,"name":"xAlive","type":"Bool"},
    {"address":1,"name":"xRemote","type":"Bool"},
    {"address":2,"name":"xReserve1","type":"Bool"},
    {"address":3,"name":"xReserve2","type":"Bool"},
    {"address":4,"name":"xReserve3","type":"Bool"},
    {"address":5,"name":"xReserve4","type":"Bool"},
    {"address":6,"name":"xReserve5","type":"Bool"},
    {"address":7,"name":"xReserve6","type":"Bool"},
    ]

receive_offset_byte_30 = [
    
    {"address":240,"name":"xMessungEin","type":"Bool"},
    {"address":241,"name":"xRegelungEin","type":"Bool"},
    {"address":242,"name":"xQuerRegEin","type":"Bool"},
    {"address":243,"name":"xLaengsRegEin","type":"Bool"},
    {"address":244,"name":"xKalibrierungEin","type":"Bool"},
    {"address":245,"name":"xLinienmessungEin","type":"Bool"},
    {"address":246,"name":"xReserve1","type":"Bool"},
    {"address":247,"name":"xReserve2","type":"Bool"},
    
]

send_offset_map=[
    
{"address":0,         "name":"xAlive",                       "type":"Bool"},
{"address":1,         "name":"xRemote",                      "type":"Bool"},
{"address":2,         "name":"xReserve1",                    "type":"Bool"},
{"address":3,         "name":"xReserve2",                    "type":"Bool"},
{"address":4,         "name":"xReserve3",                    "type":"Bool"},
{"address":5,         "name":"xReserve4",                    "type":"Bool"},
{"address":6,         "name":"xReserve5",                    "type":"Bool"},
{"address":7,         "name":"xReserve6",                    "type":"Bool"},
{"address":8,         "name":"xReserve7",                    "type":"SInt"},
{"address":16,        "name":"uiTelegramNo",                 "type":"UInt"},
{"address":32,        "name":"uiReserve1",                   "type":"UInt"},
{"address":48,        "name":"rReserve2",                    "type":"Real"},
{"address":80,        "name":"rReserve3",                    "type":"Real"},
{"address":112,       "name":"rReserve4",                    "type":"Real"},
{"address":144,       "name":"rReserve5",                    "type":"Real"},
{"address":176,       "name":"rReserve6",                    "type":"Real"},
{"address":208,       "name":"rReserve7",                    "type":"Real"},
{"address":240,       "name":"xMessungEin",                  "type":"Bool"},
{"address":241,       "name":"xRegelungEin",                 "type":"Bool"},
{"address":242,       "name":"xQuerRegEin",                  "type":"Bool"},
{"address":243,       "name":"xLaengsRegEin",                "type":"Bool"},
{"address":244,       "name":"xResetAlarm",                  "type":"Bool"},
{"address":245,       "name":"xRolleWechseln",               "type":"Bool"},
{"address":246,       "name":"xKalibrierungEin",             "type":"Bool"},
{"address":247,       "name":"xLinienmessungEin",            "type":"Bool"},
{"address":248,       "name":"xReserve1",                    "type":"SInt"},
{"address":256,       "name":"rSollDicke",                   "type":"Real"},
{"address":288,       "name":"rTolPos",                      "type":"Real"},
{"address":320,       "name":"rTolNeg",                      "type":"Real"},
{"address":352,       "name":"rMessung_StartPos",            "type":"Real"},
{"address":384,       "name":"rMessung_EndPos",              "type":"Real"},
{"address":416,       "name":"rNettoBreite",                 "type":"Real"},
{"address":448,       "name":"rKalibrierungswert",           "type":"Real"},
{"address":480,       "name":"rDicke_Corrwert",              "type":"Real"},
{"address":512,       "name":"rKalibrierungspos",            "type":"Real"},
{"address":544,       "name":"rSollzeit_Linienmessung",      "type":"Real"},
{"address":576,       "name":"rPos_Linienmessung",           "type":"Real"},
{"address":608,       "name":"uiModusQuerProfilReg",         "type":"UInt"},
{"address":624,       "name":"uiBolzenAnzahl",               "type":"UInt"},
{"address":640,       "name":"rBolzenBreite",                "type":"Real"},
{"address":672,       "name":"rDuesenBreite",                "type":"Real"},
{"address":704,       "name":"rBolzenDeckling_links",        "type":"Real"},
{"address":736,       "name":"rBolzenDeckling_rechts",       "type":"Real"},
{"address":768,       "name":"rBolzenManuell_links",         "type":"Real"},
{"address":800,       "name":"rBolzenManuell_rechts",        "type":"Real"},
{"address":832,       "name":"rLiniengeschw",                "type":"Real"},
{"address":864,       "name":"rSchrumpf",                    "type":"Real"},
{"address":896,       "name":"stOrderNo_max_len",            "type":"SInt"},
{"address":904,       "name":"stOrderNo_actual_len",         "type":"SInt"},
{"address":912,       "name":"stOrderNo",                    "type":"String"},
{"address":1696,      "name":"stCustomerName_max_len",       "type":"SInt"},
{"address":1704,      "name":"stCustomerName_actual_len",    "type":"SInt"},
{"address":1712,      "name":"stCustomerName",               "type":"String"},
{"address":2496,      "name":"rArtikelNo",                   "type":"Real"},
{"address":2528,      "name":"stPersonal_max_len",           "type":"SInt"},
{"address":2536,      "name":"stPersonal_actual_len",        "type":"SInt"},
{"address":2544,      "name":"stPersonal",                   "type":"String"},
{"address":3328,      "name":"rAuftragsmenge",               "type":"Real"},
{"address":3360,      "name":"rBenefits",                    "type":"Real"},
{"address":3392,      "name":"stMaterialtyp_max_len",        "type":"SInt"},
{"address":3400,      "name":"stMaterialtyp_actual_len",     "type":"SInt"},
{"address":3408,      "name":"stMaterialtyp",                "type":"String"},
{"address":4192,      "name":"rDicke_Produkt",               "type":"Real"},
{"address":4224,      "name":"rBreite_Produkt",              "type":"Real"},
{"address":4256,      "name":"uiBolzenkurveNo",              "type":"UInt"},
{"address":4272,      "name":"uiMesskurveNo",                "type":"UInt"},
{"address":4288,      "name":"rReserve_1",                   "type":"Real"},
{"address":4320,      "name":"rReserve_2",                   "type":"Real"},
{"address":4352,      "name":"rReserve_3",                   "type":"Real"},
{"address":4384,      "name":"rReserve_4",                   "type":"Real"},
{"address":4416,      "name":"rReserve_5",                   "type":"Real"},
{"address":4448,      "name":"rReserve_6",                   "type":"Real"},
{"address":4480,      "name":"rReserve_7",                   "type":"Real"},
{"address":4512,      "name":"rReserve_8",                   "type":"Real"},
{"address":4544,      "name":"rReserve_9",                   "type":"Real"},
{"address":4576,      "name":"rReserve_10",                  "type":"Real"},
{"address":4608,      "name":"rReserve_11",                  "type":"Real"},
{"address":4640,      "name":"rReserve_12",                  "type":"Real"},
{"address":4672,      "name":"rReserve_13",                  "type":"Real"},
{"address":4704,      "name":"rReserve_14",                  "type":"Real"},
{"address":4736,      "name":"rReserve_15",                  "type":"Real"},

]
    

