import pandas as pd

df = pd.read_csv("avg_price.csv")
df['day'] = 1
df['date'] = pd.to_datetime(df[['year', 'month', 'day']])
df = df.sort_values(["city","year", "month"],ascending=[True, True, True]).reset_index(drop=True)

df.to_csv("monthly_avg_price.csv", index=False)

dubai2br = df[ (df["city"] == 'Dubai') & (df["bedrooms"] == 4) ]
print(dubai2br.head(100))

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
#
# ts = ts.cumsum()
# ts.plot()
# pd.scatter_matrix(dubai2br, diagonal='kde', figsize=(10, 10))
dubai2br.plot(x = 'date', y ='price')

plt.show()

