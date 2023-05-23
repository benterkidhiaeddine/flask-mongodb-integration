from flask import Blueprint
from .extensions import mongo


main = Blueprint('main',__name__)

@main.route("/")
def home():
    
    books_collection = mongo.db.books
    books_collection.insert_one({"title":"pensées"})

    return "book inserted !"