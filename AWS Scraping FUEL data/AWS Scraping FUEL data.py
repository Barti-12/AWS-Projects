#import nessesary library
import os
import smtplib
from email.message import EmailMessage
from bs4 import BeautifulSoup
import requests
import pymysql
import re
from datetime import datetime, date

today = date.today()
d1 = today.strftime("%d.%m.%Y")

#connection setup
endpoint= '********************.rds.amazonaws.com'
username=username
password=password
database_name=database_name

#creating connection to RDS MySql  
connection=pymysql.connect(host=endpoint, user=username, password=password, db=database_name)


def lambda_handler(event, context):
  
  #scraping data
  page=requests.get('https://www.autocentrum.pl/paliwa/ceny-paliw/')
  soup=BeautifulSoup(page.content, "html.parser")

  def transform(x):
    return float(x.get_text().strip().replace(',','.').replace('-','0'))

  for data in soup.find_all('tr')[1:]:

    areas=data.find(class_='row-link').get_text().strip()
    pb_normal = transform(data.find('a', href=re.compile("/pb/")))
    pb_premium = transform(data.find('a', href=re.compile('pb-premium')))
    n_normal = transform(data.find('a', href=re.compile("/on/")))
    on_premium = transform(data.find('a', href=re.compile("on-premium")))
    lpg = transform(data.find('a', href=re.compile('lpg')))
    date = datetime.now()
    
    cursor=connection.cursor()
    
    #upload data to datebase
    cursor.execute(
        'INSERT INTO fuel_data (area,pb_normal,pb_premium,n_normal,on_premium,lpg,data) VALUES (%s,%s,%s,%s,%s,%s,%s)',
        (areas, pb_normal, pb_premium, n_normal, on_premium, lpg, date))
  connection.commit()
  
  # function to selecting area , fuel type and dealing with NaN values
  #if data==null print no date/Brak Danych 
  def catch_sql(P):
    cursor.execute(f"select {P}  from fuel_data where area = 'podlaskie' and data = CURDATE() limit 1")
    d=cursor.fetchone()
    if d[0] ==0.0:
        return  ('Brak Danych')
    return d[0]
  
  #prepare configuration to send mail
  EMAIL_ADDRESS = "simple1@gmail.com"
  EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
    
  msg = EmailMessage()
  msg['Subject'] = f"Ceny paliw! - {d1}"
  msg['From'] = EMAIL_ADDRESS
  msg['To'] = ['simple2@gmail.com']
    
  #mail message  
  msg.set_content('Dane pobrane i zapisane w bazie danych!!! \n'
  'Dzisiejsze średnie ceny paliw na Podlasiu \n'
  f'Cena benzyny zwykłej (95): {catch_sql("pb_normal")} \n'
  f'Cena benzyny premium (98): {catch_sql("pb_premium")} \n'
  f'Cena diesla : {catch_sql("n_normal")} \n'
  f'Cena diesla plus : {catch_sql("on_premium")} \n'
  f'Cena LPG : {catch_sql("lpg")} \n')
  
  #send mail  
  with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
      smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
      smtp.send_message(msg)
  
  print('Success')
