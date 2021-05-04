from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import re

def get_contents(links):
    
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("headless")
    
    driver = webdriver.Chrome(ChromeDriverManager().install(),  options=options)
    crawled_data = []
    
    for link in links:
        driver.get(link)

        try:
            title = driver.find_elements_by_class_name('page-header-title')[0]
            title = title.text
        except:
            title = "N/A"
        
        try:
            date = driver.find_elements_by_class_name('page-header-meta')[0]
            publish_date = date.text[date.text.find("LE")+3 : date.text.find("LE")+13]
        except:
            date = "N/A"


        try:
            content = driver.find_elements_by_class_name('wysiwyg-content')[0]
            if 'ANSM sous le n°' in content.text:
                identifire = content.text[content.text.find("n°")+3 : content.text.find("n°")+11]
            else:
                identifire = "N/A"
        except:
            pass

        crawled_data.append([identifire, title, publish_date])

    
    return crawled_data



# get_contents()