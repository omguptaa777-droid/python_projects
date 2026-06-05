import time
import os

print("Time starts...")

i=1
while i>0:
    command= command = "osascript -e 'say \"Hey Om drink water\"'; osascript -e 'display alert \"Hey Om, Drink water\"'"

    os.system(command)
    time.sleep(10)
    i=i+1


  


