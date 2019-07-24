import requests
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO
import re

#爬取網頁：http://5850web.moneydj.com/Z/ZG/ZGB/ZGB.djhtm
hq = '6380'
hqs = '6386'
st='2019-7-22'
ed='2019-7-24'
res = requests.get("http://5850web.moneydj.com/z/zg/zgb/zgb0.djhtm?a="+hq+"&b="+hqs+"&c=E&e="+st+"&f="+ed)
soup = BeautifulSoup(res.text,'html.parser')

soup.find_all("td",attrs={'class':'t4t1'})
dfs = pd.read_html(StringIO(res.text))
#去除不需要的文字
dfs[3][0] = dfs[3][0].map(lambda x: x.lstrip('<!-- \tGenLink2stk').rstrip('; //-->'))
dfs[4][0] = dfs[4][0].map(lambda x: x.lstrip('<!-- \tGenLink2stk').rstrip('; //-->'))

#買超
print('*'*21,'買超','*'*21)
print(dfs[3][1:])
print('\n')
#賣超
print('*'*21,'賣超','*'*21)
print(dfs[4][1:])
