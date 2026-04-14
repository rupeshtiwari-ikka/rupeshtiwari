import time
import sys

RED = '\033[91m'
YELLOW = '\033[93m'
BOLD = '\033[1m'
RESET = '\033[0m'

def print_lyrics():
    lyrics = [
         "Pachchi pindaan da sardar mera yaar ni",
         "Jitt ke main ohnu ajj dill gayi aan haar ni",
         "Ishq-e-majaazi da taaj sir te paa liya",
         "Jad vi bulaave sohna daudi main aavan",
         "Ni main vaari jaavan mera sohna ae yaar",
         "Ni main vaari jaavan ve main dill gayi aan haar",
         "Ni main vaari jaavan mera sohna hathyaar",
         "O ni main vaari jaavan ni main vaari vaari",


    ]

    delays = [0.5, 0.5, 0.6, 0.4, 0.5, 0.5, 1.0]

    print(f"\n{BOLD}{RED}Playing: Vaari Jaavan{RESET}\n")
    time.sleep(1.5)

    # Loop twice (repeat lyrics)
    for _ in range(2):
        for i, line in enumerate(lyrics):
            color = YELLOW if i % 2 == 0 else RED

            for char in line:
                sys.stdout.write(f"{BOLD}{color}{char}{RESET}")
                sys.stdout.flush()
                time.sleep(0.08)

            print()

            if i < len(delays):
                time.sleep(delays[i])
            else:
                time.sleep(1.0)

print_lyrics()