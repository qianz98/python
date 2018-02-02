# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 14:12:22 2018

@author: eric
"""

#import urllib2  
#import urllib
import requests
import json
#import sys
import time 
import locale
from ftplib import FTP



def ftpconnect(host, username, password):
    ftp = FTP()
    # ftp.set_debuglevel(2)
    ftp.connect(host, 21)
    ftp.login(username, password)
    return ftp

def uploadfile(ftp, remotepath, localpath):
    bufsize = 1024
    fp = open(localpath, 'rb')
    ftp.storbinary('STOR ' + remotepath, fp, bufsize)
    ftp.set_debuglevel(0)
    fp.close()

    
def getData(uuid):
    #显示
    
    locale.setlocale(locale.LC_CTYPE, 'chinese')

    ftext=""  
    format2='%Y年%m月%d日 %H时%M分%S秒'
    format='%Y年%m月%d日'
    url= "http://61.175.135.197:8888/NbApi/outForecast7Day.do"
    value58467={'code':'A100023','uuid':uuid,'stationNo':'58467',}
    value58562={'code':'A100023','uuid':uuid,'stationNo':'58562',}  
    value58565={'code':'A100023','uuid':uuid,'stationNo':'58565',}
    value58468={'code':'A100023','uuid':uuid,'stationNo':'58468',}
    value58563={'code':'A100023','uuid':uuid,'stationNo':'58563',} 
    value58567={'code':'A100023','uuid':uuid,'stationNo':'58567',} 
    value58561={'code':'A100023','uuid':uuid,'stationNo':'58561',} 
    value58566={'code':'A100023','uuid':uuid,'stationNo':'58566',} 

    #获取鄞州和宁波预报，其中鄞州代表宁波-----------------------------------------
    s58562=requests.get(url,params=value58562)
    data58562 = json.loads(s58562.text) 
    if   data58562['resultStatus']=="1":
        #python里时间戳是10位。而java里默认是13位（精确到毫秒）
        rel_time=time.localtime(data58562['releaseTime']/1000)
        T24=time.localtime(data58562['releaseTime']/1000+24*60*60)
        T48=time.localtime(data58562['releaseTime']/1000+2*24*60*60)
        T72=time.localtime(data58562['releaseTime']/1000+3*24*60*60)
        ST=time.strftime(format2,rel_time)  
        ST24=time.strftime(format,T24)  
        ST48=time.strftime(format,T48)   
        ST72=time.strftime(format,T72)   
        #print (ST)    
        #print (ST24)
        #print (ST48)
        #print (ST72)
        for d58562 in data58562["resultData"]: 
            if d58562["fcstHour"] == '12': 
                yz12=d58562["tqzk"]
               #print (yz12)  
        for d58562 in data58562["resultData"]: 
            if d58562["fcstHour"] == '24': 
                yz24="鄞州 " + yz12  + " " + d58562["tqzk"] + " " + d58562["minTemp"] + " " + d58562["maxTemp"]
                nb24="宁波 " + yz12  + " " + d58562["tqzk"] + " " + d58562["minTemp"] + " " + d58562["maxTemp"]
                #print (yz24)  
        for d58562 in data58562["resultData"]: 
            if d58562["fcstHour"] == '36': 
                yz36=d58562["tqzk"]
                #print (yz36)  
        for d58562 in data58562["resultData"]:        
            if d58562["fcstHour"] == '48': 
                yz48="鄞州 " + yz36  + " " + d58562["tqzk"] + " " + d58562["minTemp"] + " " + d58562["maxTemp"]
                nb48="宁波 " + yz36  + " " + d58562["tqzk"] + " " + d58562["minTemp"] + " " + d58562["maxTemp"]
                #print (yz48) 
        for d58562 in data58562["resultData"]: 
            if d58562["fcstHour"] == '60': 
                yz60=d58562["tqzk"]
                #print (yz60)  
        for d58562 in data58562["resultData"]:        
            if d58562["fcstHour"] == '72': 
                yz72="鄞州 " + yz60  + " " + d58562["tqzk"] + " " + d58562["minTemp"] + " " + d58562["maxTemp"]
                nb72="宁波 " + yz60  + " " + d58562["tqzk"] + " " + d58562["minTemp"] + " " + d58562["maxTemp"]
                #print (yz72)  
   
    #获取北仑预报
        s58563=requests.get(url,params=value58563)
        data58563 = json.loads(s58563.text) 
        for d58563 in data58563["resultData"]: 
            if d58563["fcstHour"] == '12': 
                bl12=d58563["tqzk"]
                #print (bl12)  
        for d58563 in data58563["resultData"]: 
            if d58563["fcstHour"] == '24': 
                bl24="北仑 " + bl12  + " " + d58563["tqzk"] + " " + d58563["minTemp"] + " " + d58563["maxTemp"]
                #print (bl24)  
        for d58563 in data58563["resultData"]: 
            if d58563["fcstHour"] == '36': 
                bl36=d58563["tqzk"]
                #print (bl36)  
        for d58563 in data58563["resultData"]:        
            if d58563["fcstHour"] == '48': 
                bl48="北仑 " + bl36  + " " + d58563["tqzk"] + " " + d58563["minTemp"] + " " + d58563["maxTemp"]
                #print (bl48) 
        for d58563 in data58563["resultData"]: 
            if d58563["fcstHour"] == '60': 
                bl60=d58563["tqzk"]
                #print (bl60)  
        for d58563 in data58563["resultData"]:        
            if d58563["fcstHour"] == '72': 
                bl72="北仑 " + bl60  + " " + d58563["tqzk"] + " " + d58563["minTemp"] + " " + d58563["maxTemp"]
                #print (bl72)         
           
    #获取镇海预报
        s58561=requests.get(url,params=value58561)
        data58561 = json.loads(s58561.text) 
        for d58561 in data58561["resultData"]: 
            if d58561["fcstHour"] == '12': 
                zh12=d58561["tqzk"]
                #print (zh12)  
        for d58561 in data58561["resultData"]: 
            if d58561["fcstHour"] == '24': 
                zh24="镇海 " + zh12  + " " + d58561["tqzk"] + " " + d58561["minTemp"] + " " + d58561["maxTemp"]
                #print (zh24)  
        for d58561 in data58561["resultData"]: 
            if d58561["fcstHour"] == '36': 
                zh36=d58561["tqzk"]
                #print (zh36)  
        for d58561 in data58561["resultData"]:        
            if d58561["fcstHour"] == '48': 
                zh48="镇海 " + zh36  + " " + d58561["tqzk"] + " " + d58561["minTemp"] + " " + d58561["maxTemp"]
                #print (zh48) 
        for d58561 in data58561["resultData"]: 
            if d58561["fcstHour"] == '60': 
                zh60=d58561["tqzk"]
                #print (zh60)  
        for d58561 in data58561["resultData"]:        
            if d58561["fcstHour"] == '72': 
                zh72="镇海 " + zh60  + " " + d58561["tqzk"] + " " + d58561["minTemp"] + " " + d58561["maxTemp"]
                #print (zh72)           
       
    #获取慈溪预报       
        s58467=requests.get(url,params=value58467)
        data58467 = json.loads(s58467.text) 
        for d58467 in data58467["resultData"]: 
            if d58467["fcstHour"] == '12': 
                cx12=d58467["tqzk"]
               #print (cx12)  
        for d58467 in data58467["resultData"]: 
            if d58467["fcstHour"] == '24': 
                cx24="慈溪 " + cx12  + " " + d58467["tqzk"] + " " + d58467["minTemp"] + " " + d58467["maxTemp"]
                #print (cx24)  
        for d58467 in data58467["resultData"]: 
            if d58467["fcstHour"] == '36': 
                cx36=d58467["tqzk"]
                #print (cx36)  
        for d58467 in data58467["resultData"]:        
            if d58467["fcstHour"] == '48': 
                cx48="慈溪 " + cx36  + " " + d58467["tqzk"] + " " + d58467["minTemp"] + " " + d58467["maxTemp"]
                #print (cx48) 
        for d58467 in data58467["resultData"]: 
            if d58467["fcstHour"] == '60': 
                cx60=d58467["tqzk"]
                #print (cx60)  
        for d58467 in data58467["resultData"]:        
            if d58467["fcstHour"] == '72': 
                cx72="慈溪 " + cx60  + " " + d58467["tqzk"] + " " + d58467["minTemp"] + " " + d58467["maxTemp"]
                #print (cx72)         
      
    #获取余姚预报       
        s58468=requests.get(url,params=value58468)
        data58468 = json.loads(s58468.text) 
        for d58468 in data58468["resultData"]: 
            if d58468["fcstHour"] == '12': 
                yy12=d58468["tqzk"]
                #print (yy12)  
        for d58468 in data58468["resultData"]: 
            if d58468["fcstHour"] == '24': 
                yy24="余姚 " + yy12  + " " + d58468["tqzk"] + " " + d58468["minTemp"] + " " + d58468["maxTemp"]
               #print (yy24)  
        for d58468 in data58468["resultData"]: 
            if d58468["fcstHour"] == '36': 
                yy36=d58468["tqzk"]
               #print (yy36)  
        for d58468 in data58468["resultData"]:        
            if d58468["fcstHour"] == '48': 
                yy48="余姚 " + yy36  + " " + d58468["tqzk"] + " " + d58468["minTemp"] + " " + d58468["maxTemp"]
                #print (yy48) 
        for d58468 in data58468["resultData"]: 
            if d58468["fcstHour"] == '60': 
                yy60=d58468["tqzk"]
                #print (yy60)  
        for d58468 in data58468["resultData"]:        
            if d58468["fcstHour"] == '72': 
                yy72="余姚 " + yy60  + " " + d58468["tqzk"] + " " + d58468["minTemp"] + " " + d58468["maxTemp"]
                #print (yy72)           
           
       
    #获取奉化预报       
        s58565=requests.get(url,params=value58565)
        data58565 = json.loads(s58565.text) 
        for d58565 in data58565["resultData"]: 
            if d58565["fcstHour"] == '12': 
                fh12=d58565["tqzk"]
                #print (fh12)  
        for d58565 in data58565["resultData"]: 
            if d58565["fcstHour"] == '24': 
                fh24="奉化 " + fh12  + " " + d58565["tqzk"] + " " + d58565["minTemp"] + " " + d58565["maxTemp"]
                #print (fh24)  
        for d58565 in data58565["resultData"]: 
            if d58565["fcstHour"] == '36': 
                fh36=d58565["tqzk"]
                #print (fh36)  
        for d58565 in data58565["resultData"]:        
            if d58565["fcstHour"] == '48': 
                fh48="奉化 " + fh36  + " " + d58565["tqzk"] + " " + d58565["minTemp"] + " " + d58565["maxTemp"]
                #print (fh48) 
        for d58565 in data58565["resultData"]: 
            if d58565["fcstHour"] == '60': 
                fh60=d58565["tqzk"]
                #print (fh60)  
        for d58565 in data58565["resultData"]:        
            if d58565["fcstHour"] == '72': 
                fh72="奉化 " + fh60  + " " + d58565["tqzk"] + " " + d58565["minTemp"] + " " + d58565["maxTemp"]
                #print (fh72)  
           
       
    #获取宁海预报       
        s58567=requests.get(url,params=value58567)
        data58567 = json.loads(s58567.text) 
        for d58567 in data58567["resultData"]: 
            if d58567["fcstHour"] == '12': 
                nh12=d58567["tqzk"]
                #print (nh12)  
        for d58567 in data58567["resultData"]: 
            if d58567["fcstHour"] == '24': 
                nh24="宁海 " + nh12  + " " + d58567["tqzk"] + " " + d58567["minTemp"] + " " + d58567["maxTemp"]
                #print (nh24)  
        for d58567 in data58567["resultData"]: 
            if d58567["fcstHour"] == '36': 
                nh36=d58567["tqzk"]
                #print (nh36)  
        for d58567 in data58567["resultData"]:        
            if d58567["fcstHour"] == '48': 
                nh48="宁海 " + nh36  + " " + d58567["tqzk"] + " " + d58567["minTemp"] + " " + d58567["maxTemp"]
                #print (nh48) 
        for d58567 in data58567["resultData"]: 
            if d58567["fcstHour"] == '60': 
                nh60=d58567["tqzk"]
                #print (nh60)  
        for d58567 in data58567["resultData"]:        
            if d58567["fcstHour"] == '72': 
                nh72="宁海 " + nh60  + " " + d58567["tqzk"] + " " + d58567["minTemp"] + " " + d58567["maxTemp"]
                #print (nh72)            
           
        
    #获取象山预报       
        s58566=requests.get(url,params=value58566)
        data58566 = json.loads(s58566.text) 
        for d58566 in data58566["resultData"]: 
            if d58566["fcstHour"] == '12': 
                xs12=d58566["tqzk"]
                #print (xs12)  
        for d58566 in data58566["resultData"]: 
            if d58566["fcstHour"] == '24': 
                xs24="象山 " + xs12  + " " + d58566["tqzk"] + " " + d58566["minTemp"] + " " + d58566["maxTemp"]
                #print (xs24)  
        for d58566 in data58566["resultData"]: 
            if d58566["fcstHour"] == '36': 
                xs36=d58566["tqzk"]
                #print (xs36)  
        for d58566 in data58566["resultData"]:        
            if d58566["fcstHour"] == '48': 
                xs48="象山 " + xs36  + " " + d58566["tqzk"] + " " + d58566["minTemp"] + " " + d58566["maxTemp"]
                #print (xs48) 
        for d58566 in data58566["resultData"]: 
            if d58566["fcstHour"] == '60': 
                xs60=d58566["tqzk"]
                #print (xs60)  
        for d58566 in data58566["resultData"]:        
            if d58566["fcstHour"] == '72': 
                xs72="象山 " + xs60  + " " + d58566["tqzk"] + " " + d58566["minTemp"] + " " + d58566["maxTemp"]
                #print (xs72)            
                ftext= ST24+ "\n" + nb24 + "\n" + bl24 + "\n" + zh24 + "\n" + cx24 + "\n" + yz24 + "\n" + yy24 + "\n" + fh24 + "\n" + nh24 + "\n" + xs24 + "\n" + ST48 + "\n" + nb48 + "\n" + bl48 + "\n" + zh48 + "\n" + cx48 + "\n" + yz48 + "\n" + yy48 + "\n" + fh48 + "\n" + nh48 + "\n" + xs48 + "\n" + ST72 + "\n" + nb72 + "\n" + bl72 + "\n" + zh72 + "\n" + cx72 + "\n" + yz72 + "\n" + yy72 + "\n" + fh72 + "\n" + nh72 + "\n" + xs72 + "\n" + "预报发布时间：" + ST  
                #print (ftext)            
                return ftext

    else: 
        ftext=data58562['resultInfo']
        return ftext

         
    
    #预报天气状况

def getYZM(js01):
#获取验证码
    YZM=js01['resultData']
    print(YZM)
#返回验证码
    return YZM
  
def getUUID(js02):
#获取UUID
    UUID=js02['resultData']['uuid']
    print(UUID)
#返回UUID
    return UUID


if __name__ == '__main__':
    
    
    url01="http://61.175.135.197:8888/NbApi/out.do"
    value01={
    'code':'A100000',
    'cellphone':'18657431030',
    }
    s01=requests.get(url01,params=value01)
    js01=s01.json()
    yzm=getYZM(js01)

    url02="http://61.175.135.197:8888/NbApi/outyzm.do"
    value02={
    'code':'A100001',
    'cellphone':'18657431030',
    'yzm':yzm,
    }
    s02=requests.get(url02,params=value02)
    js02=s02.json()
    uuid=getUUID(js02)

    txt=getData(uuid)
    #print (txt) 
    f = open("tqyb.txt","w")
    f.write(txt)
    f.close()
    #ftp = ftpconnect("172.21.146.40", "share", "share")
    #uploadfile(ftp, "tqyb.txt", "tqyb.txt")
    #ftp.quit()


    

