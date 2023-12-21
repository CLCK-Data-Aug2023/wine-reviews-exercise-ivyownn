# add your code here


import pandas as pd
reviews = pd.read_csv("winemag-data-130k-v2.csv")


reviews.points.describe()

#median_points = reviews.points.unique()

average_points = reviews.groupby("country")['points'].mean().round(1)



average_count = reviews.groupby("country")['points'].count()


result = pd.DataFrame()
result["count"] = average_count
result["points"] = average_points


result.to_csv('reviews-per-country.csv', index=True)


