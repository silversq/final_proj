import os
from parallelhillclimber import PARALLEL_HILL_CLIMBER
import numpy
import matplotlib.pyplot as plt

phc = PARALLEL_HILL_CLIMBER()
phc.EVOLVE()
phc.Show_Best()

# for i in range(5):
#     os.system("py generate.py")
#     os.system("py simulate.py")*-     