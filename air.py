import serial
import requests
import json
import time
import re

def arr_s(a,b):
    return ((b-a)*(b-a))

def variance (arr):
    print(arr)
    s=sum(arr)/10
    var=(arr_s(s,arr[0])+arr_s(s,arr[1])+arr_s(s,arr[2])+arr_s(s,arr[3])+arr_s(s,arr[4])+arr_s(s,arr[5])+arr_s(s,arr[6])+arr_s(s,arr[7])+arr_s(s,arr[8])+arr_s(s,arr[9]))/10
    return (s,var)

ser = serial.Serial('/dev/ttyACM0',9600,timeout=1)
key='a'
key = key.encode("ascii")

data_arr=[]

var_key=0
while var_key==0:
    data_arr=[]
    while len(data_arr)<10 :
        ser.write(key)
        da=ser.readline()
        time.sleep(0.5)
        data=re.split(r'\|' , str(da))
        if len(data)==8:
            for i in range(9):
                if i>1 and i<6:
                    data[i]=int(data[i])
            c= data[2]+data[3]+data[4]
            if data[1] == 'aaa' and data[6] == 'bbb' and c == data[5]:
                data_arr.append(data[2:5])
    print(data_arr)
    PM1=[data_arr[0][0],data_arr[1][0],data_arr[2][0],data_arr[3][0],data_arr[4][0],data_arr[5][0],data_arr[6][0],data_arr[7][0],data_arr[8][0],data_arr[9][0]]
    PM2=[data_arr[0][1],data_arr[1][1],data_arr[2][1],data_arr[3][1],data_arr[4][1],data_arr[5][1],data_arr[6][1],data_arr[7][1],data_arr[8][1],data_arr[9][1]]
    PM10=[data_arr[0][2],data_arr[1][2],data_arr[2][2],data_arr[3][2],data_arr[4][2],data_arr[5][2],data_arr[6][2],data_arr[7][2],data_arr[8][2],data_arr[9][2]]
    s1,var1=variance(PM1)
    s2,var2=variance(PM2)
    s3,var3=variance(PM10)
    print(var1,var2,var3)
    print(s1,s2,s3)
    if var1<2 and var2<2 and var3<2:
        var_key=1


url='http://api.heclouds.com/devices/9106291/datapoints?type=3'
headers = {'api-key': 'EazpwgBmpqo=S4Uhl=BOgGyWQqY='}
payload = {'PM1_0': s1,'PM2_5':s2,'PM10':s3}
print(payload)
r = requests.post(url, headers=headers, data=json.dumps(payload))
print(r)