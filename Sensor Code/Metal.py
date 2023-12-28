import RPi.GPIO as GPIO
import time
import requests
import urlopen
import urllib

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)  # This command is to Disable Warning....!!!!

metal = 17
buzzer = 13
GPIO.setup(17, GPIO.IN)
GPIO.setup(buzzer, GPIO.OUT)
################Location#################################################
import json
location_req_url='http://api.ipstack.com/103.51.95.183?access_key=fcdaeccb61637a12fdf64626569efab0'
r = requests.get(location_req_url)
location_obj = json.loads(r.text)
        
lat = location_obj['latitude']
lon = location_obj['longitude']
latitude = lat
longitude = lon
print(str(latitude))
print(str(longitude))
msg ="Metal  detected...Here I attached object:Latitude is:"+str(latitude)+"Langitude is:"+str(longitude)

###################################SMS###################################################
def sms_send():
    url="https://www.fast2sms.com/dev/bulkV2"
    params={
  
        "authorization":"JNWc95zezpyn1Hah1cPF9ZKlV7d7ll9civgNwGrXQ1wb6sDk5jAnuOeCCQNl",
        "sender_id":"SMSINI",
        "message":"Metal  detected...Here I attached object:Latitude is:"+str(latitude)+"Langitude is:"+str(longitude),
        "language":"english",
        "route":"q",
        "numbers":"7887369235"
    }
    rs=requests.get(url,params=params)

########################Ultrasonic Sensor###############################


while True:
    j=GPIO.input(17)
    print(j)
    if j==1 :
        print('metal Detected!')
        time.sleep(1)
        GPIO.output(buzzer, True)
        time.sleep(1)
        GPIO.output(buzzer, False)
        sms_send() 
        import requests 
        #api_address = "http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q="
                      
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
       
       
    else :
        print ('metal Not Detected!')
        time.sleep(1)
        GPIO.output(buzzer, False)
