import os

from mongo_headler import get_all_documents_from_mongo_collection, get_random_image_from_mongo_by_year
from flask import Flask
from pymongo import MongoClient
from flask import request


app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"


@app.route("/get_questions")
def get_questions():
    try:
        questions = get_all_documents_from_mongo_collection(QUESTIONS_COLLECTION)
        for question in questions:
            question.pop('_id', None)
            question["type"] = "img"
            question["image_url"] = get_random_image_from_mongo_by_year(IMAGES_COLLECTION, int(question["year"]))
        return {"questions": questions}
    except KeyError:
        return


@app.route("/get_random_image_by_year")
def get_random_image_by_year():
    try:
        year = int(request.args.get('year'))
        image = get_random_image_from_mongo_by_year(IMAGES_COLLECTION, year)
        return {"image": image}
    except KeyError:
        return None


if __name__ == '__main__':
    mongo_client = MongoClient("localhost", 27017)
    heroes_mongo_db = mongo_client["heroes_hackathon"]
    QUESTIONS_COLLECTION = heroes_mongo_db["questions_collection"]
    IMAGES_COLLECTION = heroes_mongo_db["images_collection"]

    curr_dirname = os.path.dirname(__file__)
    app.run()
