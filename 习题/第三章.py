import numpy as np
import pandas as pd

data_age=[13,15,16,19,20,20,21,22,25,25,25,25,30,30,33,35,35,35,35,36,40,45,46,52,70]
#等深分箱，用箱均值光滑数据
pd.qcut(data_age,3)
