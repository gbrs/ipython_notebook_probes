from memory_profiler import profile


@profile
def sm():
    # arr1 = pd.DataFrame(np.arange(0, 10**6).reshape(1000, 1000))
    # arr2 = pd.DataFrame(np.arange(0, 10**6).reshape(1000, 1000))
    
    arr1 = pd.DataFrame(np.random.rand(1000, 1000))
    arr2 = pd.DataFrame(np.random.rand(1000, 1000))
    arr3 = arr1 + arr2
    
    
import numpy as np
import pandas as pd

sm()
