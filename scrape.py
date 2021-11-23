from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy , ProxyType
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import json 
import time 
import requests
#Proxy Rotations
#Proxy >=90% uptime from US
'''def proxy_rotations():
    url  = "http://www.freeproxylists.net/"
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get(url)
    
    country = webdriver.support.ui.Select(driver.find_element_by_xpath("//*[@id='form1']/table/tbody/tr[2]/td[1]/select"))
    country.select_by_value('US')
    time.sleep(3)
    
    final = driver.find_element_by_xpath("//*[@id='form1']/table/tbody/tr[3]/td/input")
    final.click()
    time.sleep(2)
    
    #Selecting rows
    rows = driver.find_element_by_css_selector("table.DataGrid > tbody >tr.Odd, .Even")
    proxies=[]
    
    for i in range(0,len(rows)):
        
        if len(rows[i].find_elements_by_class_name("adsbygoogle"))>0:
            continue
        else:
            print(rows[i])
            info = rows[i].text.split()
            print(info)
            IP,PORT = info[0],info[1]
            proxies.append(IP + ":" + PORT)
    
    driver.close()
    return proxies

url = "http://httpbin.org/ip"
proxies = proxy_rotations()
for i in range(len(proxies)):
    proxy = proxies[1]
    try:
        response = requests.get(url,proxies={"http":proxy,"https":proxy})
    except:
        proxies.pop(i)
        print("Currently Occupied")

proxies = proxy_rotations()


#Using Proxies
def driver_proxy(IP):
    IP =IP
    chrome_opt = Options()
    chrome_opt.add_argument('--proxy-server=%s' % IP)
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    return driver    
'''

#Scraping Part
def scrapedata(driver):
    time.sleep(5)
    try:
        driver.find_element_by_css_selector("#close-button").click()
        time.sleep(2)
    except:
        pass    
    items = driver.find_elements_by_css_selector("#Div1.product")
    scraped_data = []
    for item in items:
        title = item.find_element_by_class_name("catalog-item-name")
        brand = item.find_element_by_class_name("catalog-item-brand")
        price = item.find_element_by_class_name("price")
        status = item.find_element_by_class_name("status")
        if status.text == "Out of Stock":
            in_stock = False
        else:
            in_stock = True
        scraped_data.append(
            {
                "price" : price.text,
                "title" : title.text,
                "stock" : in_stock,
                "brand" : brand.text

            }
        )

    return scraped_data


def main():
    url = "https://www.midsouthshooterssupply.com/dept/reloading/primers?currentpage=1"
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get(url)
    result = scrapedata(driver)
    driver.quit()
    with open('result.json','w') as output:
        json.dump(result,output,indent=4)
main()        




