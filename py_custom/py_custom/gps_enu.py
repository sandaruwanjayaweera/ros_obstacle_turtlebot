from time import sleep
import math

def gps_to_enu(lat2, long2, alt2, lat1, long1, alt1):
    print("Beginning data processing...")
    r = 6378388                                         # earth radius in m (http://www.cs.jyu.fi/el/summerschool/materials/lbs/lbs_integration/tsld026.htm)
    x = 2*math.pi*r*(long2 - long1)/360/10**7           # x in cm (10**7 to convert 0.1 udeg to deg, (removed - unit is m)100 to convert m to cm)
    y = 2*math.pi*r*(lat2 - lat1)/360/10**7             # y in cm (10**7 to convert 0.1 udeg to deg, (removed - unit is m)100 to convert m to cm)
    z = alt2 - alt1                                     # z in cm
    print("Data processing finished.")
    return x,y,z

def enu_to_gps(x, y, z, lat1, long1, alt1):
    print("Beginning data processing2...")
    r = 6378388                                         # earth radius in m (http://www.cs.jyu.fi/el/summerschool/materials/lbs/lbs_integration/tsld026.htm)
    long2   = x*360*10**7/(2*math.pi*r) + long1
    lat2    = y*360*10**7/(2*math.pi*r) + lat1
    alt2    = z + alt1
    print("Data processing finished2.")
    return lat2,long2,alt2
