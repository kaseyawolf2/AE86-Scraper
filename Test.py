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
    dbconn.execute("INSERT INTO Listings VALUES ('{ListPicture}','{ListHeading}','{ListLink}','{ListCity}','{ListState}','{ListDate}','{ListAuctionEndDate}','{ListPrice}','{ListBuyout}','{CarTitle}','{CarFuelType}','{CarMileage}','{CarYear}','{CarBodyType}','{CarBodyColor}','{CarCondition}','{CarTransmission}','{CarWheelDrive}','{CarSteerLoc}')".format(ListPicture = Listing.ListPicture,ListHeading = Listing.ListHeading,ListLink = Listing.ListLink,ListCity = Listing.ListCity,ListState = Listing.ListState,ListDate = Listing.ListDate,ListAuctionEndDate = Listing.ListAuctionEndDate,ListPrice = Listing.ListPrice,ListBuyout = Listing.ListBuyout,CarTitle = Listing.CarTitle,CarFuelType = Listing.CarFuelType,CarMileage = Listing.CarMileage,CarYear = Listing.CarYear,CarBodyType = Listing.CarBodyType,CarBodyColor = Listing.CarBodyColor,CarCondition = Listing.CarCondition,CarTransmission = Listing.CarTransmission,CarWheelDrive = Listing.CarWheelDrive,CarSteerLoc = Listing.CarSteerLoc))
    dbconn.commit()



dbconn = sqlite3.connect('test.db')
#dbconn.execute("CREATE TABLE Listings(ListPicture text,ListHeading text,ListLink text,ListCity text,ListState text,ListDate text,ListAuctionEndDate text,ListPrice text,ListBuyout text,CarTitle text,CarFuelType text,CarMileage text,CarYear text,CarBodyType text,CarBodyColor text,CarCondition text,CarTransmission text,CarWheelDrive text,CarSteerLoc text)")
#dbconn.commit()

testList = CarListing()
testList.ListPrice = "420"
testList.ListPicture = "None"
SaveListing(testList)








dbconn.close()