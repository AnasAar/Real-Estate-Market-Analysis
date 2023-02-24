from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


def page_scrapping(url):
    driver = webdriver.Chrome(
        "C:/Users/hp/PycharmProjects/realestate_prjt/venv/Lib/site-packages/chromedriver_autoinstaller/105/chromedriver")
    driver.get(url)
    content = driver.page_source
    soup = BeautifulSoup(content, features="html.parser")
    for scroll in range(3):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(1)
    try:
        type_vente = soup.find("span", attrs={"itemprop": "name"}).contents[0]
    except IndexError:
        type_vente = "NaN"
    #type_vente = soup.find("span", attrs={"itemprop": "name"}).contents[0]
    try:
        prix_obj = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/h1/span[@class='item-price']").text
    except NoSuchElementException:
        prix_obj= "Nan"
    #prix_obj = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/h1/span[@class='item-price']").text
    try:
        adresse_obj = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div[6]/h2").text
    except NoSuchElementException:
        adresse_obj = "NaN"
    #adresse_obj = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div[6]/h2").text
    try:
        details_obj = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div[6]/ul[1]").text
    except NoSuchElementException:
        details_obj= "NaN"
    #details_obj = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div[6]/ul[1]").text
    try:
        desc_obj = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div[6]/div[1]").text
    except NoSuchElementException:
        desc_obj= "Nan"
    #desc_obj = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div[6]/div[1]").text
    #transport_obj = soup.findAll("span", attrs={"class": "label"})
    try:
        transport_obj = soup.findAll("span", attrs={"class": "label"})
        transports = []
        for tr in transport_obj:
            transports.append(tr.text)
        tran = ""
        for t in transports:
            tran = tran + "| " + t
    except IndexError:
        tran = "Nan"
    d= {'type_location':type_vente, 'adresse':adresse_obj, 'prix_par_mois':prix_obj, 'details': details_obj, 'description': desc_obj, 'supplements':tran}
    df = pd.DataFrame(data=d, index=[0])
    return df

if __name__ == '__main__':
    print("done")

