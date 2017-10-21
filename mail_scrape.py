from bs4 import BeautifulSoup
import os # osモジュールのインポート
import re

# os.listdir('パス')
# 指定したパス内の全てのファイルとディレクトリを要素とするリストを返す
files = os.listdir('mails')

m = open('mails.txt', 'a')
for file in files:
    f = open('/home/iroha/gacha/mails/' +file, 'r')
    html = f.read()
    soup = BeautifulSoup(html, 'html.parser')
    mails = soup.find_all("span",id=re.compile("area_mailaddr"))
    for mail in mails:
        print(mail.text)
        m.write(mail.text.strip()+'\n')
    f.close()

m.close()

