import pandas as pd
# a = ["A","B","C"]
# a= pd.DataFrame(a)
# print(a)
# print(a)
# import requests
# from BeautifulSoup import BeautifulSoup
# # import shutil
# res = requests.get('http://www.gamebase.com.tw/forum/64172/topic/96278769/1')
# soup = BeautifulSoup(res.text)
# for img in soup.select('.img'):
#     print(img)
dfs = pd.read_html('https://rate.bot.com.tw/xrt?Lang=zh-TW')
currency = dfs[0]
currency = currency.ix[:,0:5]
currency.to_excel('currency.xlsx')
