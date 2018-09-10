import multiprocessing

import os

def myfunction():
    print multiprocessing.cpu_count()
    #print os.cpu_count
#kernel name
    print os.uname()[0]
# load average
    print os.getloadavg
#uptime
    print os.system("uptime")
 #disk usage
    print os.system("df -h")

print myfunction()