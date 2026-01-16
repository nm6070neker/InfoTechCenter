# Welcome Branch

# Libraries Imported Here
import sys
import time

# ANSI color codes
CYAN = "\033[96m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
RESET = "\033[0m"

print(f"\n{CYAN}Welcome Branch - Developer: Natalie Maher{RESET}\n")
print(f"{CYAN}Welcome to InfoTech Center v.1.0{RESET}\n")

x = 0
ellipsis = 0

while x != 20:
    x += 1
    ellipsisMessage = f"{YELLOW}InfoTechCenter OS Booting{'.' * ellipsis}{RESET}"
    ellipsis += 1
    sys.stdout.write("\r\033[K" + ellipsisMessage)
    sys.stdout.flush()
    time.sleep(0.5)

    if ellipsis == 4:
        ellipsis = 0

    if x == 20:
        print(f"\n{GREEN}Operating System Booted Up - Retina Scanned - Access Granted{RESET}")