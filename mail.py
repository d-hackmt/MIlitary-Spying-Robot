import smtplib
from email.message import EmailMessage
import imghdr

Sender_Email = "pragati.code@gmail.com"
Reciever_Email = "pragati.sct@gmail.com"
Password ='grqheqzoutabdfzd'
newMessage = EmailMessage()    #creating an object of EmailMessage class
newMessage['Subject'] = "Test Email from ATM safety" #Defining email subject
newMessage['From'] = Sender_Email  #Defining sender email
newMessage['To'] = Reciever_Email  #Defining reciever email


import requests 
api_address = "http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q="
        
import json
location_req_url='http://api.ipstack.com/2401:4900:5039:4b15:7e45:5534:75:3d5?access_key=f5ebf0974241e6218f17ad8737d77286'
r = requests.get(location_req_url)
location_obj = json.loads(r.text)
        
lat = location_obj['latitude']
lon = location_obj['longitude']
latitude = lat
longitude = lon
print(str(latitude))
print(str(longitude))


newMessage.set_content('Hi,I am in trouble.Please help me urgently... \n Here I attached my location: \n Latitude is:'+str(latitude)+'\n Langitude is:'+str(longitude)) #Defining email body
with open('abc.png', 'rb') as f:
    image_data = f.read()
    image_type = imghdr.what(f.name)
    image_name = f.name
newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    
    smtp.login(Sender_Email, Password)              
    smtp.send_message(newMessage)
