import os
import json
import random
from dateutil.parser import parse, ParserError
from calendar import IllegalMonthError
from jsons_files_handler import load_jsons_images, load_jsons_questions


def get_all_documents_from_mongo_collection(collection):
    return list(collection.find({}))


def delete_all_documents_in_mongo_collection(collection):
    collection.delete_many({})


def insert_images_to_mongo(curr_dir, images_jsons_dir, images_collection):
    images_list = load_jsons_images(curr_dir, images_jsons_dir)
    for image_dict in images_list['d']:
        try:
            doc_year = parse(image_dict["title"], fuzzy=True).year
            desired_document = {
                "book_id": image_dict["book_id"],
                "multimedia": image_dict["multimedia"],
                "multimedia_bk": image_dict["multimedia_bk"],
                "title": image_dict["title"],
                "archivalsignature": image_dict["archivalsignature"],
                "credit": image_dict["credit"],
                "year": doc_year
            }
            doc_id = images_collection.insert_one(desired_document).inserted_id
            print(doc_id)
        except (ParserError, IllegalMonthError, TypeError):
            pass


def insert_questions_to_mongo(curr_dir, questions_jsons_dir, questions_collection):
    questions_list = load_jsons_questions(curr_dir, questions_jsons_dir)
    for question_dict in questions_list:
        try:
            doc_id = questions_collection.insert_one(question_dict).inserted_id
            print(doc_id)
        except (ParserError, IllegalMonthError, TypeError):
            pass


def _get_images_from_mongo_by_year(images_collection, year):
    cursor = images_collection.find({"year": year})
    return [image["multimedia"] for image in cursor]


def get_random_image_from_mongo_by_year(images_collection, year):
    try:
        images = _get_images_from_mongo_by_year(images_collection, year)
        return random.choice(images)
    except IndexError:
        return None
