from flask import Flask, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)

# Récupérer l'URL MongoDB depuis une variable d'environnement
MONGO_URI = os.environ.get("MONGO_URI", "mongodb://mongo:27017/")
client = MongoClient(MONGO_URI)

# Sélection d'une base et d'une collection
db = client["mydatabase"]
collection = db["test"]

@app.route("/")
def hello():
    return "Flask + MongoDB avec Docker Compose 🚀"

@app.route("/insert")
def insert_data():
    # Insérer un document exemple
    doc = {"message": "Hello MongoDB"}
    result = collection.insert_one(doc)
    return jsonify({"inserted_id": str(result.inserted_id)})

@app.route("/list")
def list_data():
    # Retourner tous les documents
    docs = list(collection.find({}, {"_id": 0}))
    return jsonify(docs)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
