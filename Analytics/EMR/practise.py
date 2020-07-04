import pandas as pd
import numpy as np


x = [1,3,2,5,4]
y = np.pad(x,(4,5),'edge')
print(y)
