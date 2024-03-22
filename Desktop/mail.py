from ast import Continue
import csv
from ctypes import sizeof
import time as t
import RPi.GPIO as GPIO
import serial 
import os
import smtplib
import imghdr
from email.message import EmailMessage

ser = serial.Serial('/dev/ttyACM0',9600)
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(7,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(35,GPIO.IN)
GPIO.setup(7,GPIO.OUT)

def email():
    EMAIL_ADDRESS = "sghiourisimohammed@gmail.com"#os.environ.get('EMAIL_USER')
    EMAIL_PASSWORD = "tmlziwxavmxtjmis" #os.environ.get('EMAIL_PASS')

    contacts = ['sghiouri.mohammed@ensam-casa.ma',"moha.hamlich@gmail.com"]

    msg = EmailMessage()
    msg['Subject'] = 'Reminder - PillPal'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = contacts

    msg.set_content('Pilules non prises !')

    msg.add_alternative("""\
    <!DOCTYPE html>
    <html>
        <body>
            <h1 style="color:SlateGray;">This is an HTML Email!</h1>
        </body>
    </html>
    """, subtype='html')


    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)


#La fonction Moteur qui va tourner le 

def motor(l):
    d=0
    #d est le nombre de doses dans le jours l
    while d < 4:
        for i  in l :
            #i indique la dose numéro i, si le temps est venu pour prendre la dose i
            i=i.strip('"') 
            if i=='00:00:00': # la condition sur les inputs vides du formulaire
                d=d+1
                ser.write(b"1")
            if i==t.ctime().split()[3]: # l'horaire exacte actuelle en hh:mm:ss
                ser.write(b"1")
                print("blabla")
                print(i)
                GPIO.output(7,1)
                for j in range(60):
                    if (GPIO.input(35)==GPIO.HIGH):
                        GPIO.output(7,0)
                        break
                    elif j==20 :
                        GPIO.output(7,0)
                        email()
                        break
                    t.sleep(1)       
                # print("Il est temps de prendre vos médicaments")    
                # sur une raspberry pi qui va faire tourner la roue une fois le temps est venu
                t.sleep(1)
                d=d+1
    return 0

l=[]
with open('Meds.csv', 'r') as f:
    data = csv.reader(f) #lire le fichier csv qui contient le planning de prise des médicaments sous forme d'un tableau
    while True:
        for row in data: # row = on parcourt les lignes du tableau
            for elem in row: # row = on parcourt les éléments de la ligne 
                elem=elem.split(';')
                if elem[0].strip('"') and t.ctime().split()[0]=='Mon':
                    motor(elem)
                if elem[0].strip('"')=='Mardi' and t.ctime().split()[0]=='Tue':
                    motor(elem)
                elif elem[0].strip('"')=='Mercredi' and t.ctime().split()[0]=='Wed':
                    motor(elem)
                elif elem[0].strip('"')=='Jeudi' and t.ctime().split()[0]=='Thu':
                    motor(elem)    
                elif elem[0].strip('"')=='Vendredi' and t.ctime().split()[0]=='Fri':
                    motor(elem)           
                elif elem[0].strip('"')=='Samedi' and t.ctime().split()[0]=='Sat':
                    motor(elem)           
                elif elem[0].strip('"')=='Dimanche' and t.ctime().split()[0]=='Sun':
                    motor(elem)
