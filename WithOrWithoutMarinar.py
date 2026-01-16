#BetaTestDev

# Welcome Branch
# This program simulates a basic operating system boot sequence
# Developer: Natalie Maher

# Libraries Imported Here
import sys      # Used to control terminal output (overwrite the same line)
import time     # Used to add delays for the boot animation

# ANSI color codes for terminal text formatting
CYAN = "\033[96m"     # Cyan color for headings
YELLOW = "\033[93m"   # Yellow color for the booting animation
GREEN = "\033[92m"    # Green color for successful access message
RESET = "\033[0m"     # Resets text color back to default

# Display welcome and version information
print(f"\n{CYAN}Welcome Branch - Developer: Natalie Maher{RESET}\n")
print(f"{CYAN}Welcome to InfoTech Center v.1.0{RESET}\n")

# Initialize counters for the boot sequence
x = 0                 # Controls how many times the loop runs
ellipsis = 0          # Controls the number of dots shown in the loading animation

# Loop runs until the boot sequence completes 20 cycles
while x != 20:
    x += 1            # Increment the loop counter

    # Create the boot message with animated dots
    ellipsisMessage = f"{YELLOW}InfoTechCenter OS Booting{'.' * ellipsis}{RESET}"
    ellipsis += 1     # Increase the number of dots each loop

    # Write the message to the same terminal line
    sys.stdout.write("\r\033[K" + ellipsisMessage)
    sys.stdout.flush()    # Forces the output to appear immediately

    time.sleep(0.5)       # Pause to simulate loading time

    # Reset dots after three dots are displayed
    if ellipsis == 4:
        ellipsis = 0

    # Display final message when boot sequence is complete
    if x == 20:
        print(f"\n{GREEN}Operating System Booted Up - Retina Scanned - Access Granted{RESET}")