
def get_selectors():

    

    selectors = {
        # xpath including search_indices function
        'search_filed_xpath' : "//input[@id='global_search_text']",
        'search_icon_xpath' : '//*[@id="btn-header-icon"]',
        'search_button_xpath' : '//*[@id="btn-header-search"]',
        'pagination_xpath' : "//a[normalize-space()='>']",
        'each_article' : '//*[@id="wrapper"]/div/div/article[',

        # xpath including select_date function
        'date_btn_xpath' : "//a[normalize-space()='Date']",
        'startDate_xpath' : '//*[@id="filter_startDate"]',
        'endDate_xpath' : '//*[@id="filter_endDate"]',
        'valider_xpath' : "//i[contains(@class,'fa fa-check')]"
    }

    return selectors

