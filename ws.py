
import serial
import re
import datetime

ser = serial.Serial('/dev/ttyACM0')

done = -5

while True:
  line = ser.readline()
  if len(line) == 2:  # ignore 0x0d 0x0a
    continue
  
  print(line)

  d = datetime.datetime.now()

  if d.minute % 5 == 0 and d.minute != done:
    
    f = open("data.dat", "a")

    f.write(d.strftime("%Y/%m/%d %H:%M:%S"))
    f.write(" UTC   ")
    f.write(line)
    f.close()
    
    done = d.minute

    print "written to file"
 

ser.close()





