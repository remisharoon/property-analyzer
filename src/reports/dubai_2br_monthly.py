import pandas as pd
df_avg = pd.read_csv('avg_price.csv')
dubai_2br_monthly_avg = df_avg.loc[(df_avg['city'] == 'Dubai') & (df_avg['num_bedrooms'] == 2.0)]

dubai_2br_monthly_avg['day'] = 1
dubai_2br_monthly_avg['date'] = pd.to_datetime(dubai_2br_monthly_avg[['year', 'month', 'day']])
dubai_2br_monthly_avg = dubai_2br_monthly_avg.sort_values(["city", "year", "month"], ascending=[True, True, True]).reset_index(drop=True)
print(dubai_2br_monthly_avg.head())

dubai_2br_monthly_avg.to_csv("dubai_2br_monthly_avg.csv", index=False)
dubai_2br_monthly_avg.to_json("dubai_2br_monthly_avg.json", orient="records")

with open("dubai_2br_monthly_avg.json","r") as json_file:
    json_data = json_file.read()
    with open("../../gatsby/property-analyzer-site/src/data/dubai_2br_monthly_avg.js","w") as file_js:
        js_data = "export default " + json_data + ";"
        file_js.write(js_data)

import matplotlib.pyplot as plt
dubai_2br_monthly_avg.plot(x='date', y='price')

plt.show()