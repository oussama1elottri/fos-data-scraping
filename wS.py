# import requests
# # from bs4 import BeautifulSoup
# # import csv

# page = requests.get('https://fr.wikipedia.org/wiki/Alger')

# # def main (page):
# #     src = page.content
# #     soup = BeautifulSoup(src, 'lxml')

# #     # population = soup.find_all('th', {'scope':'class="infobox_v2 noarchive"'})
# #     population = soup.find('table').find_all('tr')[14].td.text.split(' ')[0][0:9]

    
# #     # population_title = population.content
# #     print (population)


# # main(page)

# import requests
# from selenium import webdriver
# from selenium.webdriver.common.by import By


# page_url = 'https://www.woolworths.com.au/shop/browse/drinks/cordials-juices-iced-teas/iced-teas'
# driver = webdriver.Chrome()
# # driver.implicitly_wait(10) # seconds
# # def main(page_url):

# driver.get(page_url)




# videos = driver.find_elements('css selector', 'wx-header__container')
# print (videos)
# # videos = driver.find_elements_by_class_name('style-scope ytd-compact-video-renderer')
# title = driver.find_element('xpath', './html/body/wow-root/wow-app-layout/div/div/main/wow-browse-container/shared-layout-wrapper-tile/div/shared-grid/div/div[1]/shared-product-tile/shared-product-tile-v2/section/div[3]/div/shared-product-tile-price/div/div[1]')
#     # title = video.find_element_by_xpath('.//*[@id="video-title"]').text
    
#     # views = video.find_element_by_xpath('./html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/div[9]/ytd-watch-next-secondary-results-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-compact-video-renderer[1]/div[1]/div/div[1]/a/div/ytd-video-meta-block/div[1]/div[2]/span[1]').text
#     # when = video.find_element_by_xpath('./html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/div[9]/ytd-watch-next-secondary-results-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-compact-video-renderer[1]/div[1]/div/div[1]/a/div/ytd-video-meta-block/div[1]/div[2]/span[2]').text
# print(title)




# main(page_url)

# # browseContainer-title ng-star-inserted
###########
# from selenium import webdriver
# from selenium.webdriver.firefox.options import Options

# def main(page):
#     options = Options()
#     options.binary_location = '/Applications/Firefox Developer Edition.app/Contents/MacOS/firefox'
#     # print (options=options)
#     driver = webdriver.Firefox(options=options)


# main(page)




import requests
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.implicitly_wait(10) # seconds

url = "https://www.woolworths.com.au/shop/browse/drinks/cordials-juices-iced-teas/iced-teas"

driver.get(url)

elements = driver.find_elements(By.XPATH, "./html/body/wow-root/wow-app-layout/div/div/main/wow-browse-container/shared-layout-wrapper-tile/div/shared-grid/div/div[3]/shared-product-tile/shared-product-tile-v2/section/div[3]/div[1]/shared-product-tile-price/div/div[1]")
print (elements)
for elt in elements:
    print(elt.text)

driver.quit()