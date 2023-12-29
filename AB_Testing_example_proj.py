import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')

ad_platform = ad_clicks.groupby('utm_source').user_id.count().reset_index()

ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()

clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()

clicks_pivot = clicks_by_source.pivot(
  index = 'utm_source',
  columns = 'is_click',
  values = 'user_id',
).reset_index()

clicks_pivot['percent_clicked'] = clicks_pivot[True] / (clicks_pivot[True] + clicks_pivot[False])

exp_users = ad_clicks.groupby('experimental_group').user_id.count().reset_index()

clicks_by_exp_group = ad_clicks.groupby(['experimental_group', 'is_click']).user_id.count().reset_index()

exp_group_clicks_pivot = clicks_by_exp_group.pivot(
  columns = 'is_click',
  index = 'experimental_group',
  values = 'user_id'
).reset_index()

a_clicks = ad_clicks[
   ad_clicks.experimental_group
   == 'A']
b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']

a_clicks_per_day = a_clicks.groupby(['day', 'is_click']).user_id.count().reset_index()

a_perday_pivot = a_clicks_per_day.pivot(
  columns = 'is_click',
  values = 'user_id',
  index = 'day'
).reset_index

b_clicks_per_day = b_clicks.groupby(['day', 'is_click']).user_id.count().reset_index()

b_perday_pivot = b_clicks_per_day.pivot(
  columns = 'is_click',
  values = 'user_id',
  index = 'day'
).reset_index

print(a_perday_pivot)
print(b_perday_pivot)