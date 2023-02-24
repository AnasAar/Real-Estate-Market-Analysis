from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome("C:/Users/hp/PycharmProjects/realestate_prjt/venv/Lib/site-packages/chromedriver_autoinstaller/105/chromedriver")
web_link= "https://fr.airbnb.com/s/Paris/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&price_filter_input_type=0&query=Paris%2C%20France&place_id=ChIJD7fiBh9u5kcRYJSMaMOCCwQ&date_picker_type=calendar&checkin=2022-09-26&checkout=2022-09-27&source=structured_search_input_header&search_type=autocomplete_click"
driver.get(web_link)
for scroll in range(5):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(2)
content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")
infos = soup.findAll("a", attrs={"class":"ln2bl2p dir dir-ltr"})
links = []
for inf in infos:
    links.append(inf.get_attribute_list("href")[0])
driver.get("https://fr.airbnb.com"+links[0])
for i in range(len(links)):
    driver.get("https://fr.airbnb.com"+links[i])
    for scroll in range(10):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(1)
    content = driver.page_source
    soup = BeautifulSoup(content, features="html.parser")

if __name__ == '__main__':
    print('-')