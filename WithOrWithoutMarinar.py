#Welcome Branch

#Libraries Imported Here
import sys
import time

print("\nWelcome Branch - Developer: Natalie Maher\n")
print("Welcome to InfoTech Center v.1.0\n")


x = 0
ellipsis = 0

while x != 20:
    x += 1
    ellipsisMessage = ("InfoTechCenter OS Booting" + "." * ellipsis)
    ellipsis += 1
    sys.stdout.write("\r" + ellipsisMessage + "   ")
    sys.stdout.flush()
    time.sleep(.5)
    if ellipsis == 4:
        ellipsis = 0
    if x == 20:
        print("\nOperating System Booted Up - Retina Scanned - Access Granted")