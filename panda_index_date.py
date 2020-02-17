import pandas as pd
import numpy as np
dt = pd.date_range(start='20130101',freq = '2H', end='20200101' )

df = pd.DataFrame(np.random.randn(len(dt), 5), index=dt, columns=list('ABCDF'))
print(type(df.index))

print(df[df.index.hour == 10])

