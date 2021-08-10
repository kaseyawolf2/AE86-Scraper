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


import sqlite3


def SaveListing(Listing):
    #print("INSERT INTO Listings VALUES ('{ListPicture}','{ListHeading}','{ListLink}','{ListCity}','{ListState}','{ListDate}','{ListAuctionEndDate}','{ListPrice}','{ListBuyout}','{CarTitle}','{CarFuelType}','{CarMileage}','{CarYear}','{CarBodyType}','{CarBodyColor}','{CarCondition}','{CarTransmission}','{CarWheelDrive}','{CarSteerLoc}')".format(ListPicture = Listing.ListPicture,ListHeading = Listing.ListHeading,ListLink = Listing.ListLink,ListCity = Listing.ListCity,ListState = Listing.ListState,ListDate = Listing.ListDate,ListAuctionEndDate = Listing.ListAuctionEndDate,ListPrice = Listing.ListPrice,ListBuyout = Listing.ListBuyout,CarTitle = Listing.CarTitle,CarFuelType = Listing.CarFuelType,CarMileage = Listing.CarMileage,CarYear = Listing.CarYear,CarBodyType = Listing.CarBodyType,CarBodyColor = Listing.CarBodyColor,CarCondition = Listing.CarCondition,CarTransmission = Listing.CarTransmission,CarWheelDrive = Listing.CarWheelDrive,CarSteerLoc = Listing.CarSteerLoc))
    dbconn.execute("INSERT OR REPLACE INTO Listings VALUES ('{ListPicture}','{ListHeading}','{ListLink}','{ListCity}','{ListState}','{ListDate}','{ListAuctionEndDate}','{ListPrice}','{ListBuyout}','{CarTitle}','{CarFuelType}','{CarMileage}','{CarYear}','{CarBodyType}','{CarBodyColor}','{CarCondition}','{CarTransmission}','{CarWheelDrive}','{CarSteerLoc}')".format(ListPicture = Listing.ListPicture,ListHeading = Listing.ListHeading,ListLink = Listing.ListLink,ListCity = Listing.ListCity,ListState = Listing.ListState,ListDate = Listing.ListDate,ListAuctionEndDate = Listing.ListAuctionEndDate,ListPrice = Listing.ListPrice,ListBuyout = Listing.ListBuyout,CarTitle = Listing.CarTitle,CarFuelType = Listing.CarFuelType,CarMileage = Listing.CarMileage,CarYear = Listing.CarYear,CarBodyType = Listing.CarBodyType,CarBodyColor = Listing.CarBodyColor,CarCondition = Listing.CarCondition,CarTransmission = Listing.CarTransmission,CarWheelDrive = Listing.CarWheelDrive,CarSteerLoc = Listing.CarSteerLoc))
    dbconn.commit()



dbconn = sqlite3.connect('test.db')
dbconn.execute("CREATE TABLE IF NOT EXISTS Listings(ListPicture,ListHeading,ListLink type UNIQUE,ListCity,ListState,ListDate,ListAuctionEndDate,ListPrice,ListBuyout,CarTitle,CarFuelType,CarMileage,CarYear,CarBodyType,CarBodyColor,CarCondition,CarTransmission,CarWheelDrive,CarSteerLoc)")
#dbconn.commit()

testList = CarListing()
testList.ListPicture = "4201"
testList.ListLink = "2"
SaveListing(testList)








dbconn.close()