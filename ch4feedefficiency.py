"""
Description: - This script will find the least cost feed ration as determined by linear programming.

Requirements:
- Python 3
- PuLP library

@author: Charles Grant
"""

from pulp import *

prob = LpProblem("ch2optefficiency", LpMinimize)
x1 = LpVariable("WHT", 0, None, LpInteger)
x2 = LpVariable("CRN", 0)
x3 = LpVariable("BAR", 0)
x4 = LpVariable("SBM", 0)
x5 = LpVariable("PRE", 0)
x6 = LpVariable("LYS", 0)

prob += 220 * x1 + 190 * x2 + 190 * x3 + 360 * x4 + 1800 * x5 + 1950 * x6, "RationCost"
prob += x1 + x2 + x3 + x4 + x5 + x6 == 1, "Proportions"
prob += 13 * x1 + 8.5 * x2 + 10.5 * x3 + 47 * x4 >= 16, "CPMin"
prob += 13 * x1 + 8.5 * x2 + 10.5 * x3 + 47 * x4 <= 18, "CPMax"
prob += .35 * x1 + .27 * x2 + .38 * x3 + 3.08 * x4 + 100 * x6 >= .95, "LysMin"
prob += .35 * x1 + .27 * x2 + .38 * x3 + 3.08 * x4 + 100 * x6 <= 1.05, "LysMax"
prob += .21 * x1 + .2 * x2 + .17 * x3 + .72 * x4 >= .28, "MethMin"
prob += .21 * x1 + .2 * x2 + .17 * x3 + .72 * x4 <= .31, "MethMax"
prob += .5 * x1 + .4 * x2 + .39 * x3 + 1.42 * x4 >= .56, "TSSAMin"
prob += .5 * x1 + .4 * x2 + .39 * x3 + 1.42 * x4 <= .62, "TSSAMax"
prob += .37 * x1 + .32 * x2 + .38 * x3 + 1.9 * x4 >= .62, "ThreMin"
prob += .37 * x1 + .32 * x2 + .38 * x3 + 1.9 * x4 <= .68, "ThreMax"
prob += .15 * x1 + .06 * x2 + .12 * x3 + .63 * x4 >= .18, "TrypMin"
prob += .15 * x1 + .06 * x2 + .12 * x3 + .63 * x4 <= .20, "TrypMax"
prob += 3425 * x1 + 3550 * x2 + 3100 * x3 + 3500 * x4 >= 3125, "DEMin"
prob += 3425 * x1 + 3550 * x2 + 3100 * x3 + 3500 * x4 <= 3455, "DEMax"
prob += .03 * x1 + .02 * x2 + .04 * x3 + .3 * x4 + 22 * x5 >= .65, "CaMin"
prob += .03 * x1 + .02 * x2 + .04 * x3 + .3 * x4 + 22 * x5 <= .90, "CaMax"
prob += .38 * x1 + .26 * x2 + .34 * x3 + .63 * x4 + 10 * x5 >= .60, "PMin"
prob += .21 * x1 + .2 * x2 + .17 * x3 + .72 * x4 + 10 * x5 <= .75, "PMax"

prob.solve()
print("Status:", LpStatus[prob.status])
for v in prob.variables():
    print(v.name, "=", v.varValue)
print("Cost of Ration = ", value(prob.objective))
