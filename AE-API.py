import sqlite3
from flask import Flask
from flask_restful import Api, Resource

dbconn = sqlite3.connect('test.db')

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