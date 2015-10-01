
import re

pattern = re.compile(r'(.*) UTC.*winddir=.*,windspeedmph=.*,windgustmph=.*,windgustdir=.*,windspdmph_avg2m=(.*),winddir_avg2m=(.*),windgustmph_10m=.*,windgustdir_10m=.*,humidity=(.*),tempf=(.*),rainin=(.*),dailyrainin=.*,pressure=(.*),batt_lvl=.*,light_lvl=(.*),')

print "timeUTC",
print "HMS",
print "windspdmph_avg2m",
print "winddir_avg2m",
print "humidity",
print "tempf",
print "rainin",
print "pressure",
print "light_lvl"

for line in open('data.dat', 'r'):
  
  matchObj = pattern.search(line)

  if matchObj:
    print matchObj.group(1),
    print matchObj.group(2),
    print matchObj.group(3),
    print matchObj.group(4),
    print matchObj.group(5),
    print matchObj.group(6),
    print matchObj.group(7),
    print matchObj.group(8)


