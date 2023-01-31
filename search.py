import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER

phc = PARALLEL_HILL_CLIMBER()

phc.Evolve()

# for a in range(0,5):
# 	os.system("python3 generate.py")
# 	os.system("python3 simulate.py")