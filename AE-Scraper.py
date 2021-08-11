import time
import datetime
import re
import sqlite3
from logging import currentframe, exception
from typing import List
from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')

#driver = webdriver.Chrome(executable_path='/usr/lib/chromium-browser/chromedriver', options=chrome_options)
driver = webdriver.Chrome("C:\Program Files (x86)\Selenium Drivers\chromedriver.exe")
driver.set_window_size(1024,786)

dbconn = sqlite3.connect('test.db')
dbconn.execute("CREATE TABLE IF NOT EXISTS Listings(ListPicture,ListHeading,ListLink type UNIQUE,ListCity,ListState,ListDate,ListAuctionEndDate,ListPrice,ListBuyout,CarTitle,CarFuelType,CarMileage,CarYear,CarBodyType,CarBodyColor,CarCondition,CarTransmission,CarWheelDrive,CarSteerLoc,ListUpdateDate)")

class CarListing:
    #Listing Info
    ListPicture = ""
    ListHeading = ""
    ListLink = ""
    ListCity = ""
    ListState = ""
    ListDate = ""
    ListAuctionEndDate = ""
    ListPrice = ""
    ListBuyout = ""
    #Car Info
    CarTitle = ""
    CarFuelType = ""
    CarMileage = ""
    CarYear = ""
    CarBodyType = ""
    CarBodyColor = ""
    CarCondition = ""
    CarTransmission = ""
    CarWheelDrive = ""
    CarSteerLoc = ""
    ListUpdateDate = datetime.datetime.now()

def SaveListing(Listing):
    #print("INSERT INTO Listings VALUES ('{ListPicture}','{ListHeading}','{ListLink}','{ListCity}','{ListState}','{ListDate}','{ListAuctionEndDate}','{ListPrice}','{ListBuyout}','{CarTitle}','{CarFuelType}','{CarMileage}','{CarYear}','{CarBodyType}','{CarBodyColor}','{CarCondition}','{CarTransmission}','{CarWheelDrive}','{CarSteerLoc}')".format(ListPicture = Listing.ListPicture,ListHeading = Listing.ListHeading,ListLink = Listing.ListLink,ListCity = Listing.ListCity,ListState = Listing.ListState,ListDate = Listing.ListDate,ListAuctionEndDate = Listing.ListAuctionEndDate,ListPrice = Listing.ListPrice,ListBuyout = Listing.ListBuyout,CarTitle = Listing.CarTitle,CarFuelType = Listing.CarFuelType,CarMileage = Listing.CarMileage,CarYear = Listing.CarYear,CarBodyType = Listing.CarBodyType,CarBodyColor = Listing.CarBodyColor,CarCondition = Listing.CarCondition,CarTransmission = Listing.CarTransmission,CarWheelDrive = Listing.CarWheelDrive,CarSteerLoc = Listing.CarSteerLoc))
    dbconn.execute("INSERT OR REPLACE INTO Listings VALUES ('{ListPicture}','{ListHeading}','{ListLink}','{ListCity}','{ListState}','{ListDate}','{ListAuctionEndDate}','{ListPrice}','{ListBuyout}','{CarTitle}','{CarFuelType}','{CarMileage}','{CarYear}','{CarBodyType}','{CarBodyColor}','{CarCondition}','{CarTransmission}','{CarWheelDrive}','{CarSteerLoc}','{ListUpdateDate}')".format(ListPicture = Listing.ListPicture,ListHeading = Listing.ListHeading,ListLink = Listing.ListLink,ListCity = Listing.ListCity,ListState = Listing.ListState,ListDate = Listing.ListDate,ListAuctionEndDate = Listing.ListAuctionEndDate,ListPrice = Listing.ListPrice,ListBuyout = Listing.ListBuyout,CarTitle = Listing.CarTitle,CarFuelType = Listing.CarFuelType,CarMileage = Listing.CarMileage,CarYear = Listing.CarYear,CarBodyType = Listing.CarBodyType,CarBodyColor = Listing.CarBodyColor,CarCondition = Listing.CarCondition,CarTransmission = Listing.CarTransmission,CarWheelDrive = Listing.CarWheelDrive,CarSteerLoc = Listing.CarSteerLoc,ListUpdateDate = Listing.ListUpdateDate))
    dbconn.commit()






## Classifeds Search Site used by lots of Newspapers
ClassifedsURL ="https://marketplaceadsonline.com/marketplace/search/query/all?keywords=Toyota+Corolla&size=50"
for Pages in range(1,4):    #50 per page * 5 = 250 Cars... 1 Car is on list currenly so should have no issues. maybe
    URL = (ClassifedsURL+"&page="+str(Pages))
    driver.get(URL)
    time.sleep(1)
    try:
        NoResults = driver.find_element(By.CLASS_NAME,"panel-warning").find_element(By.CLASS_NAME,"panel-heading").text
    except:
        FoundResults = driver.find_elements(By.CLASS_NAME,"searchresults_frame")
        print("Found " + str(len(FoundResults)) +" results, Saving and Moving on")
        for results in range(len(FoundResults)):
            CurList = CarListing()
            CurList.ListLink = FoundResults[results].find_element(By.TAG_NAME,"a").get_attribute("href")
            CurList.ListPrice = FoundResults[results].find_element(By.CLASS_NAME,"sr_ad_price").text 
            CurList.ListDate = FoundResults[results].find_element(By.CLASS_NAME,"time-stamp").text
            SaveListing(CurList)
    else:
        NoResults = driver.find_element(By.CLASS_NAME,"panel-warning").find_element(By.CLASS_NAME,"panel-heading").text
        if NoResults == "No results found"  : # Stop Searching if no more pages
           print("Found no more results, breaking out")
           break

##CriagsList
CraigsList = [
    "https://grandisland.craigslist.org/search/cta?min_auto_year=1983&max_auto_year=1987&query=%28%22Corolla%22%7CCorolla%7C%22Corolla+iM%22%29&auto_make_model=Toyota&hints=makemodel&sort=priceasc&searchNearby=2&nearbyArea=690&nearbyArea=428&nearbyArea=99&nearbyArea=280&nearbyArea=347&nearbyArea=282&nearbyArea=432&nearbyArea=689&nearbyArea=688&nearbyArea=55&nearbyArea=687&nearbyArea=668&nearbyArea=341&nearbyArea=98&nearbyArea=445&nearbyArea=693&nearbyArea=691&nearbyArea=692&nearbyArea=669",
    "https://columbiamo.craigslist.org/search/cta?min_auto_year=1983&max_auto_year=1987&query=%28%22Corolla%22%7CCorolla%7C%22Corolla+iM%22%29&auto_make_model=Toyota&hints=makemodel&sort=priceasc&searchNearby=2&nearbyArea=694&nearbyArea=30&nearbyArea=423&nearbyArea=695&nearbyArea=221&nearbyArea=222&nearbyArea=696&nearbyArea=29&nearbyArea=566",
    "https://fayar.craigslist.org/search/cta?min_auto_year=1983&max_auto_year=1987&query=%28%22Corolla%22%7CCorolla%7C%22Corolla+iM%22%29&auto_make_model=Toyota&hints=makemodel&sort=priceasc&searchNearby=2&nearbyArea=650&nearbyArea=433&nearbyArea=70&nearbyArea=54&nearbyArea=293&nearbyArea=422&nearbyArea=358&nearbyArea=100&nearbyArea=359&nearbyArea=425",
    "https://denver.craigslist.org/search/cta?min_auto_year=1983&max_auto_year=1987&query=%28%22Corolla%22%7CCorolla%7C%22Corolla+iM%22%29&auto_make_model=Toyota&hints=makemodel&sort=priceasc&searchNearby=2&nearbyArea=713&nearbyArea=315&nearbyArea=210&nearbyArea=13&nearbyArea=287&nearbyArea=319&nearbyArea=197&nearbyArea=288&nearbyArea=320",
    "https://bismarck.craigslist.org/search/cta?min_auto_year=1983&max_auto_year=1987&query=%28%22Corolla%22%7CCorolla%7C%22Corolla+iM%22%29&auto_make_model=Toyota&hints=makemodel&sort=priceasc&searchNearby=2&nearbyArea=679&nearbyArea=681&nearbyArea=195&nearbyArea=682&nearbyArea=680&nearbyArea=435&nearbyArea=666&nearbyArea=196&nearbyArea=667&nearbyArea=192",
    "https://roswell.craigslist.org/search/cta?min_auto_year=1983&max_auto_year=1987&query=%28%22Corolla%22%7CCorolla%7C%22Corolla+iM%22%29&auto_make_model=Toyota&hints=makemodel&sort=priceasc&searchNearby=2&nearbyArea=269&nearbyArea=267&nearbyArea=653&nearbyArea=364&nearbyArea=646&nearbyArea=420&nearbyArea=268&nearbyArea=132&nearbyArea=648",
    "https://chambana.craigslist.org/search/cta?min_auto_year=1983&max_auto_year=1987&query=%28%22Corolla%22%7CCorolla%7C%22Corolla+iM%22%29&auto_make_model=Toyota&hints=makemodel&sort=priceasc&searchNearby=2&nearbyArea=697&nearbyArea=225&nearbyArea=224&nearbyArea=345&nearbyArea=569&nearbyArea=344&nearbyArea=698&nearbyArea=699&nearbyArea=223&nearbyArea=190&nearbyArea=227&nearbyArea=348&nearbyArea=11&nearbyArea=360&nearbyArea=229&nearbyArea=45&nearbyArea=672&nearbyArea=228&nearbyArea=361&nearbyArea=226&nearbyArea=671",
    "https://austin.craigslist.org/search/cta?min_auto_year=1983&max_auto_year=1987&query=%28%22Corolla%22%7CCorolla%7C%22Corolla+iM%22%29&auto_make_model=Toyota&hints=makemodel&sort=priceasc&searchNearby=2&nearbyArea=365&nearbyArea=649&nearbyArea=21&nearbyArea=308&nearbyArea=270&nearbyArea=645&nearbyArea=327&nearbyArea=326&nearbyArea=15&nearbyArea=449&nearbyArea=264&nearbyArea=23&nearbyArea=53&nearbyArea=470&nearbyArea=647&nearbyArea=564&nearbyArea=265&nearbyArea=271&nearbyArea=263&nearbyArea=266",
    "https://eauclaire.craigslist.org/search/cta?min_auto_year=1983&max_auto_year=1987&query=%28%22Corolla%22%7CCorolla%7C%22Corolla+iM%22%29&auto_make_model=Toyota&hints=makemodel&sort=priceasc&searchNearby=2&nearbyArea=567&nearbyArea=339&nearbyArea=340&nearbyArea=665&nearbyArea=421&nearbyArea=307&nearbyArea=362&nearbyArea=316&nearbyArea=363&nearbyArea=19&nearbyArea=369&nearbyArea=165&nearbyArea=242&nearbyArea=553&nearbyArea=631&nearbyArea=664&nearbyArea=552&nearbyArea=47&nearbyArea=458&nearbyArea=243&nearbyArea=663&nearbyArea=571&nearbyArea=255&nearbyArea=241&nearbyArea=262",
    "https://jackson.craigslist.org/search/cta?min_auto_year=1983&max_auto_year=1987&query=%28%22Corolla%22%7CCorolla%7C%22Corolla+iM%22%29&auto_make_model=Toyota&hints=makemodel&sort=priceasc&searchNearby=2&nearbyArea=206&nearbyArea=563&nearbyArea=375&nearbyArea=644&nearbyArea=642&nearbyArea=134&nearbyArea=284&nearbyArea=641&nearbyArea=283&nearbyArea=199&nearbyArea=374&nearbyArea=31&nearbyArea=643&nearbyArea=230",
    "https://nashville.craigslist.org/search/cta?min_auto_year=1983&max_auto_year=1987&query=%28%22Corolla%22%7CCorolla%7C%22Corolla+iM%22%29&auto_make_model=Toyota&hints=makemodel&sort=priceasc&searchNearby=2&nearbyArea=46&nearbyArea=558&nearbyArea=377&nearbyArea=673&nearbyArea=465&nearbyArea=32&nearbyArea=342&nearbyArea=58&nearbyArea=670&nearbyArea=133&nearbyArea=220&nearbyArea=202&nearbyArea=674&nearbyArea=323",
    "https://showlow.craigslist.org/search/cta?min_auto_year=1983&max_auto_year=1987&query=%28%22Corolla%22%7CCorolla%7C%22Corolla+iM%22%29&auto_make_model=Toyota&hints=makemodel&sort=priceasc&searchNearby=2&nearbyArea=218&nearbyArea=50&nearbyArea=568&nearbyArea=334&nearbyArea=651&nearbyArea=244&nearbyArea=419&nearbyArea=468&nearbyArea=57&nearbyArea=18&nearbyArea=565&nearbyArea=370",
    "https://columbusga.craigslist.org/search/cta?min_auto_year=1983&max_auto_year=1987&query=%28%22Corolla%22%7CCorolla%7C%22Corolla+iM%22%29&auto_make_model=Toyota&hints=makemodel&sort=priceasc&searchNearby=2&nearbyArea=560&nearbyArea=231&nearbyArea=371&nearbyArea=127&nearbyArea=559&nearbyArea=636&nearbyArea=207&nearbyArea=200&nearbyArea=372&nearbyArea=14&nearbyArea=203&nearbyArea=343&nearbyArea=640&nearbyArea=258&nearbyArea=467&nearbyArea=257&nearbyArea=562&nearbyArea=637&nearbyArea=256&nearbyArea=186&nearbyArea=427&nearbyArea=635&nearbyArea=205&nearbyArea=570",
    "https://muskegon.craigslist.org/search/cta?min_auto_year=1983&max_auto_year=1987&query=%28%22Corolla%22%7CCorolla%7C%22Corolla+iM%22%29&auto_make_model=Toyota&hints=makemodel&sort=priceasc&searchNearby=2&nearbyArea=572&nearbyArea=630&nearbyArea=554&nearbyArea=261&nearbyArea=129&nearbyArea=628&nearbyArea=426&nearbyArea=212&nearbyArea=434&nearbyArea=172&nearbyArea=260&nearbyArea=629&nearbyArea=259&nearbyArea=309&nearbyArea=22&nearbyArea=627&nearbyArea=555",
    "https://zanesville.craigslist.org/search/cta?min_auto_year=1983&max_auto_year=1987&query=%28%22Corolla%22%7CCorolla%7C%22Corolla+iM%22%29&auto_make_model=Toyota&hints=makemodel&sort=priceasc&searchNearby=2&nearbyArea=35&nearbyArea=437&nearbyArea=131&nearbyArea=204&nearbyArea=42&nearbyArea=701&nearbyArea=573&nearbyArea=436&nearbyArea=442&nearbyArea=438&nearbyArea=702&nearbyArea=27&nearbyArea=441&nearbyArea=439&nearbyArea=251&nearbyArea=703&nearbyArea=443&nearbyArea=700&nearbyArea=252&nearbyArea=440",
    "https://butte.craigslist.org/search/cta?min_auto_year=1983&max_auto_year=1987&query=%28%22Corolla%22%7CCorolla%7C%22Corolla+iM%22%29&auto_make_model=Toyota&hints=makemodel&sort=priceasc&searchNearby=2&nearbyArea=657&nearbyArea=424&nearbyArea=658&nearbyArea=659&nearbyArea=661&nearbyArea=660&nearbyArea=469&nearbyArea=656&nearbyArea=52&nearbyArea=662&nearbyArea=654",
    "https://provo.craigslist.org/search/cta?min_auto_year=1983&max_auto_year=1987&query=%28%22Corolla%22%7CCorolla%7C%22Corolla+iM%22%29&auto_make_model=Toyota&hints=makemodel&sort=priceasc&searchNearby=2&nearbyArea=292&nearbyArea=56&nearbyArea=448&nearbyArea=351&nearbyArea=352",
    "https://fayetteville.craigslist.org/search/cta?min_auto_year=1983&max_auto_year=1987&query=%28%22Corolla%22%7CCorolla%7C%22Corolla+iM%22%29&auto_make_model=Toyota&hints=makemodel&sort=priceasc&searchNearby=2&nearbyArea=171&nearbyArea=253&nearbyArea=446&nearbyArea=462&nearbyArea=41&nearbyArea=272&nearbyArea=101&nearbyArea=61&nearbyArea=464&nearbyArea=353&nearbyArea=36&nearbyArea=273&nearbyArea=128&nearbyArea=254&nearbyArea=335&nearbyArea=274&nearbyArea=634&nearbyArea=336",
    "https://lynchburg.craigslist.org/search/cta?min_auto_year=1983&max_auto_year=1987&query=%28%22Corolla%22%7CCorolla%7C%22Corolla+iM%22%29&auto_make_model=Toyota&hints=makemodel&sort=priceasc&searchNearby=2&nearbyArea=712&nearbyArea=632&nearbyArea=194&nearbyArea=291&nearbyArea=289&nearbyArea=367&nearbyArea=366&nearbyArea=447&nearbyArea=290&nearbyArea=711&nearbyArea=444&nearbyArea=457&nearbyArea=60&nearbyArea=48",
    "https://pennstate.craigslist.org/search/cta?min_auto_year=1983&max_auto_year=1987&query=%28%22Corolla%22%7CCorolla%7C%22Corolla+iM%22%29&auto_make_model=Toyota&hints=makemodel&sort=priceasc&searchNearby=2&nearbyArea=706&nearbyArea=33&nearbyArea=275&nearbyArea=355&nearbyArea=277&nearbyArea=705&nearbyArea=463&nearbyArea=166&nearbyArea=357&nearbyArea=279&nearbyArea=278&nearbyArea=276&nearbyArea=167&nearbyArea=356&nearbyArea=17",
    "https://susanville.craigslist.org/search/cta?min_auto_year=1983&max_auto_year=1987&query=%28%22Corolla%22%7CCorolla%7C%22Corolla+iM%22%29&auto_make_model=Toyota&hints=makemodel&sort=priceasc&searchNearby=2&nearbyArea=652&nearbyArea=92&nearbyArea=707&nearbyArea=373&nearbyArea=96&nearbyArea=97&nearbyArea=12&nearbyArea=675&nearbyArea=187&nearbyArea=456&nearbyArea=188&nearbyArea=708&nearbyArea=1&nearbyArea=216&nearbyArea=454&nearbyArea=189",
    "https://ventura.craigslist.org/search/cta?min_auto_year=1983&max_auto_year=1987&query=%28%22Corolla%22%7CCorolla%7C%22Corolla+iM%22%29&auto_make_model=Toyota&hints=makemodel&sort=priceasc&searchNearby=2&nearbyArea=26&nearbyArea=455&nearbyArea=209&nearbyArea=104&nearbyArea=8&nearbyArea=103&nearbyArea=7&nearbyArea=346&nearbyArea=63&nearbyArea=43&nearbyArea=709&nearbyArea=208&nearbyArea=285&nearbyArea=62&nearbyArea=710&nearbyArea=191&nearbyArea=102",
    "https://rochester.craigslist.org/search/cta?min_auto_year=1983&max_auto_year=1987&query=%28%22Corolla%22%7CCorolla%7C%22Corolla+iM%22%29&auto_make_model=Toyota&hints=makemodel&sort=priceasc&searchNearby=2&nearbyArea=452&nearbyArea=40&nearbyArea=126&nearbyArea=704&nearbyArea=453&nearbyArea=685&nearbyArea=201&nearbyArea=130&nearbyArea=248&nearbyArea=337&nearbyArea=247&nearbyArea=684&nearbyArea=683",
    "https://delaware.craigslist.org/search/cta?min_auto_year=1983&max_auto_year=1987&query=%28%22Corolla%22%7CCorolla%7C%22Corolla+iM%22%29&auto_make_model=Toyota&hints=makemodel&sort=priceasc&searchNearby=2&nearbyArea=329&nearbyArea=633&nearbyArea=10&nearbyArea=34&nearbyArea=460&nearbyArea=556&nearbyArea=328&nearbyArea=193&nearbyArea=286&nearbyArea=349&nearbyArea=561&nearbyArea=170",
    "https://orlando.craigslist.org/search/cta?min_auto_year=1983&max_auto_year=1987&query=%28%22Corolla%22%7CCorolla%7C%22Corolla+iM%22%29&auto_make_model=Toyota&hints=makemodel&sort=priceasc&searchNearby=2&nearbyArea=638&nearbyArea=219&nearbyArea=80&nearbyArea=557&nearbyArea=333&nearbyArea=37&nearbyArea=238&nearbyArea=376&nearbyArea=39&nearbyArea=237&nearbyArea=331&nearbyArea=125&nearbyArea=639&nearbyArea=332&nearbyArea=20&nearbyArea=330",
    "https://yakima.craigslist.org/search/cta?min_auto_year=1983&max_auto_year=1987&query=%28%22Corolla%22%7CCorolla%7C%22Corolla+iM%22%29&auto_make_model=Toyota&hints=makemodel&sort=priceasc&searchNearby=2&nearbyArea=368&nearbyArea=322&nearbyArea=95&nearbyArea=324&nearbyArea=655&nearbyArea=233&nearbyArea=246&nearbyArea=325&nearbyArea=9&nearbyArea=94&nearbyArea=232&nearbyArea=459&nearbyArea=350&nearbyArea=2&nearbyArea=461&nearbyArea=217&nearbyArea=321&nearbyArea=466",
    "https://worcester.craigslist.org/search/cta?min_auto_year=1983&max_auto_year=1987&query=%28%22Corolla%22%7CCorolla%7C%22Corolla+iM%22%29&auto_make_model=Toyota&hints=makemodel&sort=priceasc&searchNearby=2&nearbyArea=3&nearbyArea=249&nearbyArea=451&nearbyArea=59&nearbyArea=686&nearbyArea=250&nearbyArea=173&nearbyArea=354&nearbyArea=338&nearbyArea=168&nearbyArea=93&nearbyArea=44&nearbyArea=281&nearbyArea=240&nearbyArea=198&nearbyArea=38&nearbyArea=4&nearbyArea=378&nearbyArea=239&nearbyArea=169",
    "https://juneau.craigslist.org/search/cta?min_auto_year=1983&max_auto_year=1987&query=%28%22Corolla%22%7CCorolla%7C%22Corolla+iM%22%29&auto_make_model=Toyota&hints=makemodel&sort=priceasc&searchNearby=2&nearbyArea=676",
    "https://puertorico.craigslist.org/search/cta?min_auto_year=1983&max_auto_year=1987&query=(%22Corolla%22%7CCorolla%7C%22Corolla+iM%22)&auto_make_model=Toyota&hints=makemodel&sort=priceasc&searchNearby=2&nearbyArea=180&nearbyArea=616&lang=en&cc=us",
    "https://anchorage.craigslist.org/search/cta?min_auto_year=1983&max_auto_year=1987&query=%28%22Corolla%22%7CCorolla%7C%22Corolla+iM%22%29&auto_make_model=Toyota&hints=makemodel&sort=priceasc&searchNearby=2&nearbyArea=677&nearbyArea=51&nearbyArea=678",
    "https://honolulu.craigslist.org/search/cta?min_auto_year=1983&max_auto_year=1987&query=%28%22Corolla%22%7CCorolla%7C%22Corolla+iM%22%29&auto_make_model=Toyota&hints=makemodel&sort=priceasc&searchNearby=2&nearbyArea=28"
]
for Pages in range(len(CraigsList)):
    driver.get(CraigsList[Pages])
    time.sleep(1)
    try:
        NoResults = driver.find_element(By.CLASS_NAME,"alert-warning")
    except:
        FoundResults = driver.find_element(By.ID,"search-results").find_elements(By.CLASS_NAME, "result-row")
        print("Found " + str(len(FoundResults)) +" results, Saving and Moving on")
        for results in range(len(FoundResults)):
            CurList = CarListing()
            CurList.ListHeading = FoundResults[results].find_element(By.CLASS_NAME, "result-heading").text
            CurList.ListLink = FoundResults[results].find_element(By.TAG_NAME,"a").get_attribute("href")
            CurList.ListDate = FoundResults[results].find_element(By.CLASS_NAME, "result-date").text
            CurList.ListPrice = FoundResults[results].find_element(By.CLASS_NAME, "result-price").text
            #go inside for more info
            #driver.get(FoundResults[results].find_element(By.TAG_NAME,"a").get_attribute("href"))

            SaveListing(CurList)
    else:
        print("Found no results, Moving on")


##Collector Car Feed
driver.get("https://collectorcarfeed.com/forum/viewtopic.php?f=2&t=92")
time.sleep(1)

try:
    driver.find_element(By.ID,"facebookTable").find_element(By.CLASS_NAME, "dataTables_empty")
except:
    FoundResults = driver.find_element(By.ID,"facebookTable").find_element(By.TAG_NAME, "tbody").find_elements(By.TAG_NAME,"tr")
    print("Found " + str(len(FoundResults)) +" results, Saving and Moving on")
    for results in range(len(FoundResults)):
        CurList = CarListing()
        CurList.ListLink = FoundResults[results].find_element(By.TAG_NAME,"a").get_attribute("href") #write link to post
else:
    print("Found no Marketplace Items, Moving on")
try:
    driver.find_element(By.ID,"bringatrailerTable").find_element(By.CLASS_NAME, "dataTables_empty")
except:
    FoundResults = driver.find_element(By.ID,"bringatrailerTable").find_element(By.TAG_NAME, "tbody").find_elements(By.TAG_NAME,"tr")
    print("Found " + str(len(FoundResults)) +" results, Saving and Moving on")
    for results in range(len(FoundResults)):
        CurList = CarListing()
        CurList.ListLink = FoundResults[results].find_element(By.TAG_NAME,"a").get_attribute("href") #write link to post
else:
    print("Found no Auctions, Moving on")
    



## CoPart
driver.get("https://www.copart.com/vehicleFinderSearch/?displayStr=Toyota,Corolla,%5B1983%20TO%201987%5D&from=%2FvehicleFinder%2F&searchStr=%7B%22MISC%22:%5B%22%23MakeCode:TOYT%20OR%20%23MakeDesc:Toyota%22,%22%23LotModel:Corolla%22,%22%23VehicleTypeCode:VEHTYPE_V%22,%22%23LotYear:%5B1983%20TO%201987%5D%22%5D,%22sortByZip%22:false,%22buyerEnteredZip%22:null,%22milesAway%22:null%7D")
time.sleep(1)
FoundResults = driver.find_element(By.ID,"serverSideDataTable").find_element(By.TAG_NAME, "tbody").find_elements(By.TAG_NAME,"tr")
for results in range(len(FoundResults)):
    CurList = CarListing()
    CurList.ListLink = FoundResults[results].find_element(By.TAG_NAME,"a").get_attribute("href") #write link to post
    SaveListing(CurList)













#Cant Get facebook to work RN to much obsucaftion


FacebookList = [
    "https://www.facebook.com/marketplace/atlanta/vehicles/?maxYear=1987&minYear=1983&sortBy=price_ascend&make=Toyota&model=Corolla&exact=false",
    "https://www.facebook.com/marketplace/nyc/vehicles/?maxYear=1987&minYear=1983&sortBy=price_ascend&make=Toyota&model=Corolla&exact=false",
    "https://www.facebook.com/marketplace/chicago/vehicles/?maxYear=1987&minYear=1983&sortBy=price_ascend&make=Toyota&model=Corolla&exact=false",
    "https://www.facebook.com/marketplace/denver/vehicles/?maxYear=1987&minYear=1983&sortBy=price_ascend&make=Toyota&model=Corolla&exact=false",
    "https://www.facebook.com/marketplace/houston/vehicles/?maxYear=1987&minYear=1983&sortBy=price_ascend&make=Toyota&model=Corolla&exact=false",
    "https://www.facebook.com/marketplace/sanfrancisco/vehicles/?maxYear=1987&minYear=1983&sortBy=price_ascend&make=Toyota&model=Corolla&exact=false",
    "https://www.facebook.com/marketplace/portland/vehicles/?maxYear=1987&minYear=1983&sortBy=price_ascend&make=Toyota&model=Corolla&exact=false",
    "https://www.facebook.com/marketplace/108308852524610/vehicles/?maxYear=1987&minYear=1983&sortBy=price_ascend&make=Toyota&model=Corolla&exact=false"
]
for Pages in range(len(FacebookList)):
    CurList = CarListing()
    CurList.ListLink = FacebookList[Pages]
    SaveListing(CurList)
# driver.get(FacebookList[0])
# try:
#     NoResults = driver.find_element(By.ID,"login_form")
# except:
#     print("No Login?")
# else:
#     driver.find_element(By.ID,"email").send_keys("Kasey_Keahey@yahoo.com")
#     driver.find_element(By.ID,"pass").send_keys("Bustercatman6")
#     time.sleep(.5)
#     driver.find_element(By.ID,"loginbutton").click()
# finally:
#     time.sleep(10)
#     try:
#         NoResults = driver.find_element(By.CLASS_NAME,"d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh a8c37x1j keod5gw0 nxhoafnm aigsh9s9 ns63r2gh fe6kdd0r mau55g9w c8b282yb iv3no6db o3w64lxj b2s5l15y hnhda86s m9osqain oqcyycmt")
#     except:
#         CriagsResults = driver.find_element(By.CLASS_NAME,"bq4bzpyk j83agx80 btwxx1t3 lhclo0ds jifvfom9 muag1w35 dlv3wnog enqfppq2 rl04r1d5").find_elements(By.TAG_NAME, "div")
#         print("Found " + str(len(CriagsResults)) +" results, Moving on")

#         for results in range(len(CriagsResults)):
#             ResultsFile.write(CriagsResults[results].text) #write info
#             ResultsFile.write("\n")
#             ResultsFile.write(CriagsResults[results].find_element(By.TAG_NAME,"a").get_attribute("href")) #write link to post
#             ResultsFile.write("\n")
#             ResultsFile.write("\n")
#     else:
#         print("Found no results, Moving on")

driver.close()
dbconn.close()