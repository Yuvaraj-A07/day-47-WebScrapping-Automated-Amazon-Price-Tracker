import requests
from bs4 import BeautifulSoup
import smtplib
import manager as mg

MY_PRICE = 100
MAIL = mg.MAIL
PASSWORD = mg.PASSWORD


amazon_url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 "
                  "Safari/537.36",
    "Accept-Language": "en-IN,en;q=0.9,ta-IN;q=0.8,ta;q=0.7,en-GB;q=0.6,en-US;q=0.5",
    "sec-ch-ua-platform": "Windows",
    "sec-ch-ua": f"'Not A(Brand';v='99', 'Google Chrome';v='121', 'Chromium';v='121'"
}

response = requests.get(url=amazon_url, headers=header)
amazon_web = response.text
# print(amazon_web)

soup = BeautifulSoup(amazon_web, "html.parser")

whole_price = soup.select_one(selector=".a-offscreen").getText().split("$")
# class="a-offscreen"
actual_price = float(whole_price[1])
print(actual_price)
if float(MY_PRICE) > actual_price:
    with smtplib.SMTP("smtp.gmail.com") as data:
        data.starttls()
        data.login(user=MAIL, password=PASSWORD)
        data.sendmail(from_addr=MAIL,
                      to_addrs="yuvaraj07at@gmail.com",
                      msg=f'Subject:Instant Pot Price Alert!\n\nThe product is now ${actual_price}, below your target '
                          f'price. Buy now!\n{amazon_url}')
