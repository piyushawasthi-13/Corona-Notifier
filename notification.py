import requests
from bs4 import BeautifulSoup
from plyer import notification
import time
#created by Piyush Awasthi
def notify_me(title, message):
        notification.notify(
            title= title,
            message=message,
            app_icon="D:\picture.ico",
            timeout=15, 
        )
# while True: 
url="https://economictimes.indiatimes.com/news/politics-and-nation/number-of-coronavirus-cases-649-in-india-death-toll-13-health-ministry/articleshow/74823820.cms"
r= requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
paras=soup.find('h1')
notify_me("Notification!", paras.get_text())
time.sleep(60)