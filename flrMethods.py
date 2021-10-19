def getFloorExp(flr, size):
    if size == "large":
        return (0.00042784 * (flr ** 5)) - (0.06745351 * (flr ** 4)) + (4.50808617 * (flr ** 3)) - (92.717664905 * (flr **2)) + (1200 * flr) + 1545.7
    elif size == "med":
        return 0.355 * (flr ** 3) - 1.25 * (flr ** 2) + 203 * flr + 1409
    elif size == "small":
        return -0.00544 * (flr ** 4) + .681 * (flr ** 3) - 16 * (flr ** 2) + 261 * flr + 314

def getPrestigeExp(flr, size):
    if size == "large":
        # return 578 * (flr - prestige) + getFloorExp(60, "large") # variable prestige is a project for a different day
        return 578 * flr + 137284
    elif size == "med":
        # return 284 * (flr - 60) + getFloorExp(60, "med")
        return 284 * flr + 68954
    elif size == "small":
        return 132 * flr + 33619

def getTotExp(flr, size):
    if (size == "c1"):
        return 500 + 100 * flr # not accurate at all but I cba finding exp for c1 rushes, negligible exp anyways

    tot = (getFloorExp(flr, size) + getPrestigeExp(flr, size))/2

    if (size == "large"): # assumes that level mod and bonus balance out, which, on average, they just about will
        return tot * 1.15
    elif (size == "med"):
        return tot * 1.075
    return tot



def skipCost(flr):
    return 507 * flr



