import numpy as np
import pandas as pd
from scipy.stats import pearsonr, chi2_contingency
import matplotlib.pyplot as plt
import seaborn as sns

np.set_printoptions(suppress=True, precision = 2)

nba = pd.read_csv('./nba_games.csv')

# Subset Data to 2010 Season, 2014 Season
nba_2010 = nba[nba.year_id == 2010]
nba_2014 = nba[nba.year_id == 2014]

print(nba_2010.head())
print(nba_2014.head())

knicks_pts = nba_2010.pts[nba.fran_id=='Knicks']
nets_pts = nba_2010.pts[nba.fran_id=='Nets']

knicks_mean_score = np.mean(knicks_pts)
nets_mean_score = np.mean(nets_pts)
diff_means_2010 = knicks_mean_score - nets_mean_score
print(diff_means_2010)
## mean diff is 9.73
## Fran id and pts are associated with this large difference
plt.hist(knicks_pts, alpha=0.8, normed = True, label='knicks')
plt.hist(nets_pts, alpha=0.8, normed = True, label='nets')
plt.legend()
plt.show()
## Knicks have higher points distribution than Nets

knicks_pts_2014 = nba_2014.pts[nba.fran_id=='Knicks']
nets_pts_2014 = nba_2014.pts[nba.fran_id=='Nets']

knicks_mean_score_2014 = np.mean(knicks_pts_2014)
nets_mean_score_2014 = np.mean(nets_pts_2014)
diff_means_2014 = knicks_mean_score_2014 - nets_mean_score_2014
print(diff_means_2014)

plt.clf()
plt.hist(knicks_pts_2014, alpha=0.8, normed = True, label='knicks')
plt.hist(nets_pts_2014, alpha=0.8, normed = True, label='nets')
plt.legend()
plt.show()
## Points mean is closer but 2014 nets have better mean, knicks have better distribution

plt.clf()
sns.boxplot(data = nba_2010, x = 'fran_id', y = 'pts')
plt.show()
## Nets have worst mean, thunder and knicks are very similar, spurs have better mean than celtics but similar distribution
location_result_freq = pd.crosstab(nba_2010.game_result, nba_2010.game_location)
print(location_result_freq)
location_result_proportions = location_result_freq/len(nba_2010.game_result)
print(location_result_proportions)

chi2, pval, dof, expected = chi2_contingency(location_result_proportions)
print(expected)
print(chi2)

nba_2010_forecast = np.cov(nba_2010.forecast, nba_2010.point_diff)
print(nba_2010_forecast)

## covariance is 1.37

point_diff_forecast_corr = pearsonr(nba.forecast, nba.point_diff)
print(point_diff_forecast_corr)
## A weak correlation
plt.clf() #to clear the previous plot
plt.scatter('forecast', 'point_diff', data=nba)
plt.xlabel('Forecasted Win Prob.')
plt.ylabel('Point Differential')
plt.show()
