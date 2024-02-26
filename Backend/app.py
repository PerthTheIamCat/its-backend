from flask import Flask,jsonify,request
from flask_cors import CORS
from pymongo.mongo_client import MongoClient
import certifi

ca = certifi.where()
uri = "mongodb+srv://Pawit:208902546@cluster0.bsumksw.mongodb.net/?retryWrites=true&w=majority"

try:
    client = MongoClient(uri, tlsCAFile=ca)
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


app = Flask(__name__)
CORS(app)
products=[
{"id":0,"name":"Notebook Acer Swift","price":45900,"img":"https://img.advice.co.th/images_nas/pic_product4/A0147295/A0147295_s.jpg"},
{"id":1,"name":"Notebook Asus Vivo","price":19900,"img":"https://img.advice.co.th/images_nas/pic_product4/A0146010/A0146010_s.jpg"},
{"id":2,"name":"Notebook Lenovo Ideapad","price":32900,"img":"https://img.advice.co.th/images_nas/pic_product4/A0149009/A0149009_s.jpg"},
{"id":3,"name":"Notebook MSI Prestige","price":54900,"img":"https://img.advice.co.th/images_nas/pic_product4/A0149954/A0149954_s.jpg"},
{"id":4,"name":"Notebook DELL XPS","price":99900,"img":"https://img.advice.co.th/images_nas/pic_product4/A0146335/A0146335_s.jpg"},
{"id":5,"name":"Notebook HP Envy","price":46900,"img":"https://img.advice.co.th/images_nas/pic_product4/A0145712/A0145712_s.jpg"}]

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/products",methods=["GET"])
def get_all_products():
    try:
        db = client["Product"]
        collection = db["product_info"]
        all_product = list(collection.find())
        return products,200
    except Exception as e:
        print(e)


@app.route("/product",methods=["POST"])
def add_product():
    try:
        db = client["Product"]
        collection = db["product_info"]
        data = request.get_json()
        new_product={
            "_id":data["_id"],
            "name": data["name"],
            "price": data["price"],
            "img": data["img"]
        }
        all_product = list(collection.find())
        if(next((s for s in all_product if s["_id"] == data["_id"]), None)):
            return jsonify( {"error":"Cannot create new product"}),500
        else:
            collection.insert_one(new_product)
            return jsonify(new_product),200
    except Exception as e:
            print(e)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=3000,debug=True)