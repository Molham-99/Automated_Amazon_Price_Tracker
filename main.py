from bs4 import BeautifulSoup
import requests
import smtplib
import os

MY_EMAIL = "tstrpython@gmail.com"
EMAIL_PASSWORD = os.environ.get("password")
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                  " Chrome/113.0.0.0 Safari/537.36",
    "Accept-Language": "cs-CZ,cs;q=0.9,en;q=0.8,ar;q=0.7"
}
URL = input("Enter the URL fo the product which you would like to track:")
price_input = float(input("Enter your price $:"))
response = requests.get(URL, headers=headers)
data = response.text
soup = BeautifulSoup(data, "html.parser")
price_whole = soup.find(name="span", class_="a-price-whole").getText()
price_fraction = soup.find(name="span", class_='a-price-fraction').getText()

price = float(price_whole + price_fraction)
if price < price_input:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=EMAIL_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"subject: Amazon Tracker Price\n\nThe product price is now less than {price_input}$\nURL: {URL}\n By now!\n\n Molham"
        )
