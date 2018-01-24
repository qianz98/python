 #coding:UTF-8

import urllib2  
import urllib
import requests
import json
import sys
import time 


 


def Show58467F(js58467):
    #显示
                format='%Y-%m-%d %H:%M:%S'
                data1=time.localtime(js58467['serviceTime'])
                dt=time.strftime(format,data1)               
                data2=js58467['resultStatus']
                data3=js58467['resultInfo']
                data4=data1,data2,data3
                if   js58467['resultData']!="":
                        print  ('no data!')
                        return dt
    
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

    
    

    url03= "http://61.175.135.197:8888/NbApi/outForecast7Day.do"
   
   #uuid='9d8f677c-1a75-49c3-8ca4-bf77d6ebd1d7'
    value58467={
    'code':'A100023',
    'uuid':uuid,
    'stationNo':'58467',
    }
    #url='http://api.avatardata.cn/Weather/Query'
    s58467=requests.get(url03,params=value58467)
    js58467=s58467.json()


    f = open("out.txt","w")
    dd2= "eric edit"
    dd=Show58467F(js58467)
    f.write(dd2)
    f.close()



    

