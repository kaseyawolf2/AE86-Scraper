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
from sqlite3.dbapi2 import Row

import flask


def SaveListing(Listing):
    #print("INSERT INTO Listings VALUES ('{ListPicture}','{ListHeading}','{ListLink}','{ListCity}','{ListState}','{ListDate}','{ListAuctionEndDate}','{ListPrice}','{ListBuyout}','{CarTitle}','{CarFuelType}','{CarMileage}','{CarYear}','{CarBodyType}','{CarBodyColor}','{CarCondition}','{CarTransmission}','{CarWheelDrive}','{CarSteerLoc}')".format(ListPicture = Listing.ListPicture,ListHeading = Listing.ListHeading,ListLink = Listing.ListLink,ListCity = Listing.ListCity,ListState = Listing.ListState,ListDate = Listing.ListDate,ListAuctionEndDate = Listing.ListAuctionEndDate,ListPrice = Listing.ListPrice,ListBuyout = Listing.ListBuyout,CarTitle = Listing.CarTitle,CarFuelType = Listing.CarFuelType,CarMileage = Listing.CarMileage,CarYear = Listing.CarYear,CarBodyType = Listing.CarBodyType,CarBodyColor = Listing.CarBodyColor,CarCondition = Listing.CarCondition,CarTransmission = Listing.CarTransmission,CarWheelDrive = Listing.CarWheelDrive,CarSteerLoc = Listing.CarSteerLoc))
    dbconn.execute("INSERT OR REPLACE INTO Listings VALUES ('{ListPicture}','{ListHeading}','{ListLink}','{ListCity}','{ListState}','{ListDate}','{ListAuctionEndDate}','{ListPrice}','{ListBuyout}','{CarTitle}','{CarFuelType}','{CarMileage}','{CarYear}','{CarBodyType}','{CarBodyColor}','{CarCondition}','{CarTransmission}','{CarWheelDrive}','{CarSteerLoc}')".format(ListPicture = Listing.ListPicture,ListHeading = Listing.ListHeading,ListLink = Listing.ListLink,ListCity = Listing.ListCity,ListState = Listing.ListState,ListDate = Listing.ListDate,ListAuctionEndDate = Listing.ListAuctionEndDate,ListPrice = Listing.ListPrice,ListBuyout = Listing.ListBuyout,CarTitle = Listing.CarTitle,CarFuelType = Listing.CarFuelType,CarMileage = Listing.CarMileage,CarYear = Listing.CarYear,CarBodyType = Listing.CarBodyType,CarBodyColor = Listing.CarBodyColor,CarCondition = Listing.CarCondition,CarTransmission = Listing.CarTransmission,CarWheelDrive = Listing.CarWheelDrive,CarSteerLoc = Listing.CarSteerLoc))
    dbconn.commit()



dbconn = sqlite3.connect('test.db')
dbconn.execute("CREATE TABLE IF NOT EXISTS Listings(ListPicture,ListHeading,ListLink type UNIQUE,ListCity,ListState,ListDate,ListAuctionEndDate,ListPrice,ListBuyout,CarTitle,CarFuelType,CarMileage,CarYear,CarBodyType,CarBodyColor,CarCondition,CarTransmission,CarWheelDrive,CarSteerLoc)")
#dbconn.commit()

testList = CarListing()
testList.ListPicture = "4201"
testList.ListLink = "3"
SaveListing(testList)


dbconn.close()
from flask import Flask, render_template, request
from flask_restful import Api, Resource, reqparse


app = Flask(__name__)
api = Api(app)


class AE86(Resource):
    def get(self, id=0):
        with sqlite3.connect('test.db') as dbconn:
            #dbconn.row_factory = sqlite3.Row       
            if id == 0 :
                cur = dbconn.cursor()
                res = cur.execute("select * from Listings")
                return res.fetchall()
            cur = dbconn.cursor()
            res = cur.execute("select * from Listings LIMIT 1 OFFSET {}".format(id-1))
            #res.row_factory = sqlite3.Row
            return res.fetchone()
class Headers(Resource):
    def get(self):
        with sqlite3.connect('test.db') as dbconn:
            cur = dbconn.cursor()
            res = cur.execute("select name from PRAGMA_TABLE_INFO('Listings')")
            return res.fetchall()


api.add_resource(AE86,"/ae86","/ae86/","/ae86/<int:id>", "/AE86", "/AE86/", "/AE86/<int:id>")
api.add_resource(Headers,"/")

if __name__ == '__main__':
    app.run(debug=True)


dbconn.close()