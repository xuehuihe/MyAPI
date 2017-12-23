# -*- coding: utf-8 -*-  
""" 
Created on Dec 20 2017
 
Just do it!
"""  
####################################引用模块  
  
  
from OkcoinFutureAPI import *  
import pandas as pd
import numpy as np  
import datetime  
import time  
  
  
###################################初始数据  
okcoinRESTURL = 'www.okex.com'    
apikey=''
secretkey=''
okcoinFuture = OKCoinFuture(okcoinRESTURL,apikey,secretkey)  
##################################获取整理数据  
okcoinFuture.future_userinfo()  
###okcoinFuture.getKline('min','14','1'))#获取K线数据  
#ma8=pd.DataFrame(okcoinFuture.getKline('1min','8','0')).ix[::,4].mean()  
#ma34=pd.DataFrame(okcoinFuture.getKline('1min','34','0')).ix[::,4].mean()  
try:  
    ref_ma8=pd.DataFrame(okcoinFuture.getKline('1min','8','0')).ix[::,4].mean()  
    ref_ma34=pd.DataFrame(okcoinFuture.getKline('1min','34','0')).ix[::,4].mean()  
    print('ref_ma8:',ref_ma8,'　　ref_ma34',ref_ma34)  
except ValueError as e:  
    print('json错误')  
time.sleep(58)  
i=0  
while True:  
       try:  
           ma8=pd.DataFrame(okcoinFuture.getKline('1min','8','0')).ix[::,4].mean()  
           ma34=pd.DataFrame(okcoinFuture.getKline('1min','34','0')).ix[::,4].mean()  
           print('ma8:',ma8,'　　ma34',ma34)  
       except ValueError as e:  
           print('json错误')  
           continue  
       if ma8>ma34 and ref_ma8<=ref_ma34:  
           print('买入信号',okcoinFuture.trade('btc_usd', 'quarter', '', '1', '4','1','10'))  
           print('买入信号',okcoinFuture.trade('btc_usd', 'quarter', '', '1', '1','1','10')) 
       if ma8<ma34 and ref_ma8>=ref_ma34:  
           print('卖出信号',okcoinFuture.trade('btc_usd','quarter', '', '1', '3','1','10'))  
           print('卖出信号',okcoinFuture.trade('btc_usd','quarter', '', '1', '2','1','10')) 
       time.sleep(58)  
       try:  
           ref_ma8=pd.DataFrame(okcoinFuture.getKline('1min','8','0')).ix[::,4].mean()  
           ref_ma34=pd.DataFrame(okcoinFuture.getKline('1min','34','0')).ix[::,4].mean()  
           print('ref_ma8:',ref_ma8,'　　ref_ma34',ref_ma34)  
       except ValueError as e:  
           print('json错误')  
             
           continue  
       now=datetime.datetime.now()  
       now=now.strftime('%Y-%m-%d %H:%M:%S')   
       i=i+1  
       print(now,i)