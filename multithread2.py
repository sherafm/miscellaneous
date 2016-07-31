import random
import sys
from threading import Thread, RLock
import time

verrou = RLock()

class Afficheur(Thread):
    """Thread in charge of showing one letter in the Terminal"""

    def __init__(self, mot):
        Thread.__init__(self)
        self.mot = mot

    def run(self):
        """Code to exeute during the thread execution"""
        # Repeats 20 times
        i = 0
        while i < 10:
            # The thread is locked so words can be entirely written
            with verrou:
                for lettre in self.mot:
                    # Write "1" on the terminal
                    sys.stdout.write(lettre)
                    # Make it appear immediately, otherwise it will at the end of the loop
                    sys.stdout.flush()

                    attente = 0.2
                    attente += random.randint(1, 40) / 100
                    # attente is now between 0.2 and 0.8

                    time.sleep(attente)
            i += 1

# Theead creation
thread_1 = Afficheur("canard")
thread_2 = Afficheur("TORTUE")

# Thread launch
thread_1.start()
thread_2.start()

# Waiting the Threads end
thread_1.join()
thread_2.join()
