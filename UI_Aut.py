from selenium import webdriver
from csv import reader
import datetime
from datetime import date
import calendar
import time
from datetime import datetime
import os


with open('SourceCSV.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    dataList = []
    for row in csv_reader:
        dataList.append(row)

id_number =[]
expiry_date = []
new_expiry_date = []

for i in dataList:
    id_number.append(i[0])
    if i[2]:
        expiry_date.append(i[2])
    else:
        expiry_date.append('')
        datetime.today().strftime('%Y-%m-%d')

for i in expiry_date:
    if not '/' in i:
        date = datetime.today().strftime('%Y-%m-%d')
        date = date.split('-')        
        year = int(date[0])+3
        month = int(date[1])
        day = calendar.monthrange(year, month)[1]
    else:
        date = (i.split('/'))
        year = int(date[2]) + 3
        month = int(date[1])
        day = calendar.monthrange(year, month)[1]
    
    new_expiry_date.append( (str(day)+'/'+str(month)+'/'+str(year)))


try:
    driver = webdriver.Chrome(executable_path=r'.\chromedriver.exe');
    url = os.getcwd() + "\HTML_sample.html"
    driver.get(url)
    page_title = driver.title
    if page_title == "TAG index":
        time.sleep(10)
        driver.switch_to.frame('frm1')
        driver.switch_to.frame('frm2')
        userid = driver.find_element_by_xpath('//*[@id="usrid"]').text
        index = id_number.index(str(userid))
        expiry = new_expiry_date[int(index)]
        driver.find_element_by_xpath('//*[@id="expiryData"]').send_keys(expiry)
        time.sleep(5)
        print("The expiry date entered for userid :"+str(userid)+" is "+str(expiry))
        
except Exception as e:
    print (e)
    
finally:
    driver.close()
    driver.quit()
    
