from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
import location_pages as lp
import pandas as pd

driver = webdriver.Chrome("C:/Users/hp/PycharmProjects/realestate_prjt/venv/Lib/site-packages/chromedriver_autoinstaller/105/chromedriver")
web_link= "https://www.pap.fr/annonce/location-appartement-maison-paris-75-g439g441g442g455g456g457g458g459"
#web_link= "https://fr.airbnb.com/s/Paris/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&price_filter_input_type=0&query=Paris%2C%20France&place_id=ChIJD7fiBh9u5kcRYJSMaMOCCwQ&date_picker_type=calendar&checkin=2022-09-26&checkout=2022-09-27&source=structured_search_input_header&search_type=autocomplete_click"
driver.get(web_link)
sleep(3)  # Allow 2 seconds for the web page to open
scroll_pause_time = 2 # You can set your own pause time. My laptop is a bit slow so I use 1 sec
screen_height = driver.execute_script("return window.screen.height;")   # get the screen height of the web
i = 1

while True:
    # scroll one screen height each time
    driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))
    i += 1
    sleep(scroll_pause_time)
    # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
    scroll_height = driver.execute_script("return document.body.scrollHeight;")
    # Break the loop when the height we need to scroll to is larger than the total scroll height
    if (screen_height) * i > scroll_height:
        break
content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")
#print(driver.title)
infos = soup.findAll("a", attrs={"class": "item-thumb-link"})
links = []
for inf in infos:
        a = inf.get_attribute_list("href")[0]
        links.append("https://www.pap.fr"+a)
print(len(links))
#driver.get("https://www.pap.fr"+links[0])
frames = []
for i in range(len(links)):
        print(i)
        d = lp.page_scrapping(links[i])
        frames.append(d)
result = pd.concat(frames)
result.to_csv("C:/Users/hp/PycharmProjects/realestate_prjt/location_scraping/location_scraping.csv", index=False)

