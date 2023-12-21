# add your code here


import pandas as pd
reviews = pd.read_csv("/content/sample_data/winemag-data-130k-v2.csv")


reviews.points.describe()

#median_points = reviews.points.unique()

average_points = reviews.groupby("country").points.mean().round(1)


print(average_points)

average_count = reviews.groupby("country").points.count()

print(average_count)

result = pd.DataFrame()
result["count"] = average_count
result["point"] = average_points

print(result)

result.to_csv('reviews-per-country.csv', index=True)


