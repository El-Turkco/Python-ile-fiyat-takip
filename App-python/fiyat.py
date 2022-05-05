
import requests
from bs4 import BeautifulSoup
import smtplib
import time

url = "https://www.hepsiburada.com/apple-macbook-air-m1-cip-8gb-256gb-ssd-macos-13-qhd-tasinabilir-bilgisayar-uzay-grisi-mgn63tu-a-p-HBV0000130VND"

headers= {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}


def check_price():
    page = requests.get(url,headers=headers)
    soup = BeautifulSoup(page.content,"html.parser")
    title = soup.find(id='product-name').get_text().strip()
    title = title[0:17]
    print(title)
    span = soup.find(id="offering-price")
    content = span.attrs.get("content")
    price = float(content)
    print(price)

    if (price < 16000):
        send_mail(title)


def send_mail(title):
    sender = "To Enter= sender mail"
    receiver = "To Enter= receiver mail"
    try:
        server = smtplib.SMTP("smtp.gmail.com",587)
        server.ehlo()
        server.starttls()
        server.login(sender,"To Enter=Mail password")
        subject = title + "istedigin fiyata dustu!!"
        body = "Bu linkten gidebilirsin => "+ url
        mailContent =f"To:{receiver}\nFrom {sender}\nSubject {subject}\n\n{body}"
        server.sendmail(sender,receiver,mailContent)
        print("Mail Gönderildi")
    except smtplib.SMTPException as e:
        print(e)
    finally:
        server.quit()
    

while(1):
    check_price()
    time.sleep(60*60)


check_price()
send_mail()