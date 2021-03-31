import os
import random

from mongo_headler import get_all_documents_from_mongo_collection, get_random_image_from_mongo_by_year
from flask import Flask
from pymongo import MongoClient
from flask import request
from flask_cors import CORS, cross_origin


app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"


@app.route('/')
def hello():
    return "Hello World!"


@app.route("/get_all_questions")
@cross_origin()
def get_all_questions():
    try:
        questions = get_all_documents_from_mongo_collection(QUESTIONS_COLLECTION)
        for question in questions:
            # if question["title"] == "מה הקשר בין כרזת התעמולה הנאצית לבין עליית הנאצים לשלטון?":
            question.pop('_id', None)
            question["type"] = "img"
            question["image_url"] = get_random_image_from_mongo_by_year(IMAGES_COLLECTION, int(question["year"]))
        return {"questions": questions}
    except KeyError:
        return {"error": "error"}


@app.route("/get_top_10_random_questions")
@cross_origin()
def get_top_10_random_questions():
    try:
        questions = get_all_documents_from_mongo_collection(QUESTIONS_COLLECTION)
        random.shuffle(questions)
        questions = questions[:10]
        for question in questions[:10]:
            question.pop('_id', None)
            question["type"] = "img"
            question["image_url"] = get_random_image_from_mongo_by_year(IMAGES_COLLECTION, int(question["year"]))
        return {"questions": questions}
    except KeyError:
        return {"error": "error"}


@app.route("/get_random_image_by_year")
@cross_origin()
def get_random_image_by_year():
    try:
        year = int(request.args.get('year'))
        image = get_random_image_from_mongo_by_year(IMAGES_COLLECTION, year)
        return {"image": image}
    except KeyError:
        return {"error": "error"}


if __name__ == '__main__':
    mongo_client = MongoClient("localhost", 27017)
    heroes_mongo_db = mongo_client["heroes_hackathon"]
    QUESTIONS_COLLECTION = heroes_mongo_db["questions_collection"]
    IMAGES_COLLECTION = heroes_mongo_db["images_collection"]

    curr_dirname = os.path.dirname(__file__)
    app.run()
