import os
import json


def get_all_documents_from_mongo_collection(collection):
    cursor = collection.find({})
    for document in cursor:
        print(document)


def sum_documents_in_jsons(curr_dir, images_jsons_dir):
    documents_sum = 0
    for filename in os.listdir(images_jsons_dir):
        full_filename = os.path.join(curr_dir, '{}/{}'.format(images_jsons_dir, filename))
        with open(full_filename, 'r') as f:
            documents_dict = json.load(f)
            documents_sum += len(documents_dict['d'])
    return documents_sum


def insert_images_into_mongo(curr_dir, images_jsons_dir, images_collection):
    for filename in os.listdir(images_jsons_dir):
        full_filename = os.path.join(curr_dir, '{}/{}'.format(images_jsons_dir, filename))
        with open(full_filename, 'r') as f:
            images_dict_list = json.load(f)
            for image_dict in images_dict_list['d']:
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
    for filename in os.listdir(questions_jsons_dir):
        full_filename = os.path.join(curr_dir, '{}/{}'.format(questions_jsons_dir, filename))
        with open(full_filename, 'r') as f:
            documents_dict = json.load(f)
            for document in documents_dict:
                try:
                    desired_document = {}
                    doc_id = questions_collection.insert_one(desired_document).inserted_id
                    print(doc_id)
                except (ParserError, IllegalMonthError, TypeError):
                    pass


def get_images_from_mongo_by_year(images_collection, year):
    cursor = images_collection.find({"year": year})
    return [image["multimedia"] for image in cursor]
