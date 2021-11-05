import sys
import pandas as pd
from os import listdir
from os.path import isfile, join
files = [f for f in listdir('Marriage') if isfile(join('Marriage', f))]
#get total data
def read_all_data(file_name):
    data = pd.read_csv('Marriage/'+file_name,encoding='utf-8')
    data = data.melt(id_vars= ["月份區域別"], value_name="count").rename(columns={'variable':'month'})
    data['year'] = file_name.replace('.csv','')
    return data
total_data = pd.DataFrame()
for file_name in files:
    one_data = read_all_data(file_name)
    total_data = total_data.append(one_data)
total_data.to_csv('Marriage/wrangle_data.csv')

#prepare testing data
old_data = total_data[(total_data.year=='102') | (total_data.year=='103')]
new_data = total_data[(total_data.year=='108') | (total_data.year=='109')]


#normal distribution test
from scipy.stats import shapiro
data = total_data['count'].values
stat, p = shapiro(data)
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
	print('Probably Gaussian')
else:
	print('Probably not Gaussian')


#wilcoxon test
from scipy.stats import wilcoxon
old_102_103 = old_data['count'].values
new_108_109 = new_data['count'].values
stat, p = wilcoxon(data1, data2)
if p > 0.05:
	print('Same')
else:
	print('Different')