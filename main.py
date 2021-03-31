import os
import random

from mongo_headler import get_all_documents_from_mongo_collection, get_random_image_from_mongo_by_category, \
    repopulate_images_collection, repopulate_questions_collection
from flask import Flask
from pymongo import MongoClient
from flask import request
from flask_cors import CORS, cross_origin


app = Flask(__name__)
CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"


@app.route('/')
@cross_origin()
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
            # question["type"] = "img"
            # question["image_url"] = get_random_image_from_mongo_by_category(IMAGES_COLLECTION, question["category"])
        return {"questions": questions}
    except (KeyError, ValueError):
        return {"error": "error"}


@app.route("/get_top_10_random_sorted_questions")
@cross_origin()
def get_top_10_random_sorted_questions():
    try:
        questions = get_all_documents_from_mongo_collection(QUESTIONS_COLLECTION)
        random.shuffle(questions)
        questions = questions[:10]
        questions = sorted(questions, key=lambda k: k["year"])
        for question in questions[:10]:
            question.pop('_id', None)
            # question["type"] = "img"
            # question["image_url"] = get_random_image_from_mongo_by_category(IMAGES_COLLECTION, question["category"])
        return {"questions": questions}
    except (KeyError, ValueError):
        return {"error": "error"}


# @app.route("/get_random_image_by_year")
# @cross_origin()
# def get_random_image_by_year():
#     try:
#         year = int(request.args.get('year'))
#         image = get_random_image_from_mongo_by_year(IMAGES_COLLECTION, year)
#         return {"image": image}
#     except KeyError:
#         return {"error": "error"}


if __name__ == '__main__':
    mongo_client = MongoClient("localhost", 27017)
    heroes_mongo_db = mongo_client["heroes_hackathon"]
    QUESTIONS_COLLECTION = heroes_mongo_db["questions_collection"]
    IMAGES_COLLECTION = heroes_mongo_db["images_collection"]

    curr_dirname = os.path.dirname(__file__)
    app.run()

    # repopulate_questions_collection(curr_dirname, "jsons/questions", QUESTIONS_COLLECTION)
    # repopulate_images_collection(curr_dirname, "jsons/images", IMAGES_COLLECTION)

