import glob
import numpy as np
import matplotlib.pyplot as plt 

import analysis_tools

filenames = sorted(glob.glob('inflammation*.csv'))

for f in filenames[:3]:
    print(f)
    analyse(f)
    detect_problems(f)
