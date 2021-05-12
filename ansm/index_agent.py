from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

import content_agent

url = "https://ansm.sante.fr/S-informer/Informations-de-securite-Lettres-aux-professionnels-de-sante"


# variables contains xpath

# xpath including search_indices function
search_filed_xpath = "//input[@id='global_search_text']"
search_icon_xpath = '//*[@id="btn-header-icon"]'
search_button_xpath = '//*[@id="btn-header-search"]'
pagination_xpath = "//a[normalize-space()='>']"
each_article = '//*[@id="wrapper"]/div/div/article['

# xpath including select_date function
date_btn_xpath = "//a[normalize-space()='Date']"
startDate_xpath = '//*[@id="filter_startDate"]'
endDate_xpath = '//*[@id="filter_endDate"]'
valider_xpath = "//i[contains(@class,'fa fa-check')]"


# calling api to retrieve elements selector from database
def get_selectors():
    pass



def search_indices():

    # read input_output xlsx file to get search and date period for ANSM database
    getIndices = get_indices()
    # search_string = getIndices[0]
    search_string = ['covid', 'VAXZEVRIA']
    date_from = getIndices[1]
    date_to   = getIndices[2]
    


    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("headless")

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    driver.get(url)
    driver.refresh()

    links = []
    for key in search_string:
        
        # driver.get(url)
        search_field = driver.find_element_by_xpath(search_filed_xpath)
        driver.execute_script('''
            var elem = arguments[0];
            var value = arguments[1];
            elem.value = value;
        ''', search_field, key)

        try: 
            search_icon = driver.find_element_by_xpath(search_icon_xpath)
            driver.execute_script('arguments[0].click();', search_icon)
        except:
            return links

        driver.implicitly_wait(2)

        try:    
            search_button = driver.find_element_by_xpath(search_button_xpath)
            driver.execute_script('arguments[0].click();', search_button)
        except:
            return links
        
        select_date(driver, date_from, date_to)
        time.sleep(2)
        
    
        while True:

            try:  
                # get href links
                articles = driver.find_elements_by_tag_name('article')
                for i in range(1, len(articles)+1):
                    data = driver.find_element_by_xpath(each_article + str(i) +']')

                    href = data.find_element_by_tag_name('a').get_attribute('href')
                    links.append(href)

                driver.refresh()
            except:
                break


            try:
                pagination = driver.find_element_by_xpath(pagination_xpath)
                driver.execute_script('arguments[0].click();', pagination)
            except:
                break
        


    time.sleep(5)
    # driver.quit()

    # return content_agent.get_contents(links)
    return links


    

def select_date(driver, date_from, date_to):
    try:
        # select date button
        date_btn = driver.find_element_by_xpath(date_btn_xpath)
        driver.execute_script("arguments[0].click();", date_btn)
        time.sleep(2)
    except:
        return

    try:
        # set start date
        startDate = driver.find_element_by_xpath(startDate_xpath)
        value = driver.execute_script('return arguments[0].value;', startDate)
        driver.execute_script('''
            var elem = arguments[0];
            var value = arguments[1];
            elem.value = value;
        ''', startDate, date_from)
    except:
        pass

    try:
        # set end date
        endDate = driver.find_element_by_xpath(endDate_xpath)
        value = driver.execute_script('return arguments[0].value;', endDate)
        driver.execute_script('''
            var elem = arguments[0];
            var value = arguments[1];
            elem.value = value;
        ''', endDate, date_to)
    except:
        pass

    try:
        # select valider button and hit enter
        valider = driver.find_element_by_xpath(valider_xpath)
        driver.execute_script("arguments[0].click();", valider)
    except:
        return


def get_indices():
    data = pd.read_excel(r'../read_data/Template_Input_Output.xlsx', header=None, sheet_name='SearchStrategy')

    search_strings = data.loc[7:9][19].values
    date_from = str(data.loc[2:3][1].values[0]).split(" ")[0]
    date_to = str(data.loc[2:3][1].values[1]).split(" ")[0]

    return (search_strings, date_from, date_to)



if __name__ == "__main__":
    datas = search_indices()

    for data in datas:
        print(data)

