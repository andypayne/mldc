def load(k):
    template = 'yellow_tripdata_2015-{:02d}.csv'
    return pd.read_csv(template.format(k))

def average(df):
    return df['total_amount'].mean()

def total(df):
    return df['total_amount'].sum()

data = db.from_sequence(range(1, 13)).map(load)
data
# dask.bag<map-loa..., npartitions=12>

totals = data.map(total)
averages = data.map(average)
totals.compute()
# [1175217.5200009614,
#  947282.0900005419,
#  956752.3400005258,
#  1304602.4800011297,
#  1354966.290001166,
#  1251511.6500010253,
#  1167936.1000008786,
#  915174.880000469,
#  994643.300000564,
#  1273267.4800010026,
#  1158279.990000822,
#  1166242.130000856]

averages.compute()
# [14.75051171665384,
#  15.463557844570461,
#  15.790076907851297,
#  15.971334410669527,
#  16.477159899324676,
#  16.250654434978838,
#  16.163639508987067,
#  16.164026987891997,
#  16.364647910506154,
#  16.544750841370114,
#  16.385807916489675,
#  16.28056690958003]

t_sum, t_min, t_max, = totals.sum(), totals.min(), totals.max()
t_mean, t_std, = totals.mean(), totals.std()
stats = [t_sum, t_min, t_max, t_mean, t_std]

# ipython %time
%time [s.compute() for s in stats]
# CPU times: user 142 ms, sys: 101 ms, total: 243 ms
# Wall time: 4.57 s
# [13665876.250009943,
#  915174.880000469,
#  1354966.290001166,
#  1138823.0208341617,
#  144025.81874405374]

import dask

%time dask.compute(t_sum, t_min, t_max, t_mean, t_std)
# CPU times: user 63.7 ms, sys: 29.1 ms, total: 92.7 ms
# Wall time: 852 ms
# (13665876.250009943,
#  915174.880000469,
#  1354966.290001166,
#  1138823.0208341617,
#  144025.81874405374)



by_word = speeches.str.split(' ')
n_words = by_word.map(len)
avg_words = n_words.mean()
print(type(avg_words))
print(avg_words.compute())

lower = speeches.str.lower()
health = lower.filter(lambda s:'health care' in s)
n_health = health.count()
print(n_health.compute())


