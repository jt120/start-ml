# encoding: utf-8


import json
import pandas as pd
import matplotlib.pyplot as plt

with open('d:/tmp/bs.txt', 'r') as f:
    s = json.loads(json.loads('"' + f.read() + '"'))

bsentrust = s['bsentrust']
day = s['day']
code = s['code']

df = pd.DataFrame(bsentrust)
cols = ['time', 'u1', 'u2', 'buy', 'sell']
df.columns = cols
df['std_sell'] = df['sell'].rolling(5).std()
df['std_buy'] = df['buy'].rolling(5).std()

fig = plt.figure()
# df.iloc[:-5, [-2, -1]].plot()
# df[['sell', 'buy']].plot()
# plt.title(code)
# plt.show()

# fig, axes = plt.subplots(2, 1)
# plt.title(code)
# axes[0].plot(df.iloc[:-5, -2], label='sell')
# axes[0].plot(df.iloc[:-5, -1], label='buy')
# axes[1].plot(df['sell'], label='sell')
# axes[1].plot(df['buy'], label='buy')
plt.subplot(2, 1, 1)
plt.plot(df.iloc[:-5, -2], label='sell_std')
plt.plot(df.iloc[:-5, -1], label='buy_std')
plt.legend(loc='best')
plt.title(code)
plt.subplot(2, 1, 2)
plt.plot(df['sell'], label='sell')
plt.plot(df['buy'], label='buy')
plt.legend(loc='best')
plt.show()