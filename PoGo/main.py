import stats

# 34.895	1789.4

# Excadrill:
HP = STA = 242
DEF = 129
ATK = 255
# Groudon:
HP = STA = 205
DEF = 228
ATK = 270

# Mud-Slap
FPower = 18
FE = 12
FDur = 1.4
FDWS = 1.15
# Mud Shot:
FPower = 5
FE = 7
FDur = 0.6
FDWS = 0.35
# Drill Run:
CPower = 80
CE = 50
CDur = 2.8
CDWS = 1.7
# Earthquake:
CPower = 140
CE = 100
CDur = 3.6
CDWS = 2.7

STAB = 1.2
WAB = 1  # weather
FAB = 1  # friendship
Effectiveness = 1.6

# ivs:
AttackIV = 15
DefenseIV = 15

level2CPM = {
    1: 0.094,
    1.5: 0.1351374318,
    2: 0.16639787,
    2.5: 0.192650919,
    3: 0.21573247,
    3.5: 0.2365726613,
    4: 0.25572005,
    4.5: 0.2735303812,
    5: 0.29024988,
    5.5: 0.3060573775,
    6: 0.3210876,
    6.5: 0.3354450362,
    7: 0.34921268,
    7.5: 0.3624577511,
    8: 0.3752356,
    8.5: 0.387592416,
    9: 0.39956728,
    9.5: 0.4111935514,
    10: 0.4225,
    10.5: 0.4329264091,
    11: 0.44310755,
    11.5: 0.4530599591,
    12: 0.4627984,
    12.5: 0.472336093,
    13: 0.48168495,
    13.5: 0.4908558003,
    14: 0.49985844,
    14.5: 0.508701765,
    15: 0.51739395,
    15.5: 0.5259425113,
    16: 0.5343543,
    16.5: 0.5426357375,
    17: 0.5507927,
    17.5: 0.5588305862,
    18: 0.5667545,
    18.5: 0.5745691333,
    19: 0.5822789,
    19.5: 0.5898879072,
    20: 0.5974,
    20.5: 0.6048236651,
    21: 0.6121573,
    21.5: 0.6194041216,
    22: 0.6265671,
    22.5: 0.6336491432,
    23: 0.64065295,
    23.5: 0.6475809666,
    24: 0.65443563,
    24.5: 0.6612192524,
    25: 0.667934,
    25.5: 0.6745818959,
    26: 0.6811649,
    26.5: 0.6876849038,
    27: 0.69414365,
    27.5: 0.70054287,
    28: 0.7068842,
    28.5: 0.7131691091,
    29: 0.7193991,
    29.5: 0.7255756136,
    30: 0.7317,
    30.5: 0.7347410093,
    31: 0.7377695,
    31.5: 0.7407855938,
    32: 0.74378943,
    32.5: 0.7467812109,
    33: 0.74976104,
    33.5: 0.7527290867,
    34: 0.7556855,
    34.5: 0.7586303683,
    35: 0.76156384,
    35.5: 0.7644860647,
    36: 0.76739717,
    36.5: 0.7702972656,
    37: 0.7731865,
    37.5: 0.7760649616,
    38: 0.77893275,
    38.5: 0.7817900548,
    39: 0.784637,
    39.5: 0.7874736075,
    40: 0.7903,
    40.5: 0.792803968,
    41: 0.79530001,
    41.5: 0.797800015,
    42: 0.8003,
    42.5: 0.802799995,
    43: 0.8053,
    43.5: 0.8078,
    44: 0.81029999,
    44.5: 0.812799985,
    45: 0.81529999,
    45.5: 0.81779999,
    46: 0.82029999,
    46.5: 0.82279999,
    47: 0.82529999,
    47.5: 0.82779999,
    48: 0.83029999,
    48.5: 0.83279999,
    49: 0.83529999,
    49.5: 0.83779999,
    50: 0.84029999,
    50.5: 0.84279999,
    51: 0.84529999
}

# Formulas:
CPM = level2CPM[40]
Atk = (ATK + AttackIV) * CPM
Def = (DEF + DefenseIV) * CPM
print("Atk: %s, Def: %s" % (Atk, Def))

Multipliers = STAB * WAB * FAB * Effectiveness
FDmg = int(0.5 * FPower * Atk/Def * Multipliers) + 1
CDmg = int(0.5 * CPower * Atk/Def * Multipliers) + 1
print("FDmg: %s, CDmg: %s" % (FDmg, CDmg))

FDPS = FDmg / FDur

EnemyDPS = 1930 / DEF
EPSdmg = EnemyDPS /2
print("EPSdmg: %s" % EPSdmg)
EPSFmoves = FE / FDur
print("EPSFmoves: %s" % EPSFmoves)

PercentEnergyFromFmoves = EPSFmoves / (EPSFmoves + EPSdmg)
print("PercentEnergyFromFmoves: %s" % PercentEnergyFromFmoves)

TotalFmoveEnergyGainsPerCycle = (CE - CDur * EPSdmg) * PercentEnergyFromFmoves
print("TotalFmoveEnergyGainsPerCycle: %s" % TotalFmoveEnergyGainsPerCycle)

nFPC = TotalFmoveEnergyGainsPerCycle / FE
print("nFPC: %s" % nFPC)

# CT is cycle time: how many seconds the cycle lasts.
CT = CDur + nFPC * FDur
print("CT: %s" % CT)

wDPSsimple = (CDmg + nFPC * FDmg) / CT
print("wDPSsimple: %s" % wDPSsimple)

# nC is the number of Cmoves you do throughout the battle
# nC = SurvivalTime / CT - 0.5
nC = (0.0005 * STA * DEF - 1/2 * FDur * nFPC - 1/2 * CDWS) / (CDur + nFPC * FDur)
print("nC: %s" % nC)

wDPSactual = (nC * wDPSsimple + 0.5 * FDPS) / (nC + 0.5)
print("wDPSactual: %s" % wDPSactual)

# TDOprop = DPS1 * HP * DEF

# DPS= (nC * DPSsimple + 1/2 * FDmg/FDur) / (nC + 1/2)

# TDO = DPS * (HP + 14) * (DEF + 14)