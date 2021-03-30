import requests
import os
import json
import matplotlib.pyplot as plt
import base64

from flask import Flask
from pymongo import MongoClient
from dateutil.parser import parse
from dateutil.parser import ParserError
from calendar import IllegalMonthError
from bs4 import BeautifulSoup
from flask import request


app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"


@app.route("/get_images_by_year")
def get_images_by_year():
    try:
        year = request.args.get('user')
        images = get_images_from_mongo_by_year(IMAGES_COLLECTION, year)

    except KeyError:
        return


def get_all_documents_from_mongo_collection(collection):
    cursor = collection.find({})
    for document in cursor:
        print(document)


def yad_va_shem():
    content = requests.post("https://photos.yadvashem.org/PhotosWS.asmx/getPhotosList", headers={
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive",
        "Content-Length": "100",
        "Content-Type": "application/json; charset=UTF-8",
        "Cookie": "userShowDonate=1; ASP.NET_SessionId=pikpcli0cm20k0qlh4d3124k; __za_19763107=%7B%22sId%22%3A4975508%2C%22dbwId%22%3A%221%22%2C%22sCode%22%3A%2215d80b973b57b3c0c23a2883a617999e%22%2C%22sInt%22%3A5000%2C%22aLim%22%3A2000%2C%22asLim%22%3A100%2C%22na%22%3A4%2C%22td%22%3A1%2C%22ca%22%3A%221%22%7D; __za_cd_19763107=%7B%22visits%22%3A%22%5B1617052823%5D%22%2C%22campaigns_status%22%3A%7B%2247572%22%3A1617092718%2C%2247599%22%3A1617089520%2C%2251781%22%3A1617052843%7D%7D; TS0182e6e2=016dcde99e15feb180ca5a802c769d9635f7dc12f2e2c6578688b39824719909e03c63644e1f9734d439e00183b5c43fa1cbab3d0e; __atuvc=5%7C13; __atuvs=6062de35aef44f73002",
        "Host": "photos.yadvashem.org",
        "Origin": "https://photos.yadvashem.org",
        "Referer": "https://photos.yadvashem.org/index.html?language=en&displayType=list",
        "sec-ch-ua": "\"Google Chrome\";v=\"89\", \"Chromium\";v=\"89\", \";Not A Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 1 1_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",

    }, data={"uniqueId": "-7682997668154270557", "langApi": "ENG", "rowNum": 980, "orderBy": "BOOK_ID",
             "orderType": "asc"}).content
    print(content)
    # soup = BeautifulSoup(content, 'html.parser')
    # print(soup.findChildren('table'))


def sum_documents_in_jsons(curr_dir, images_jsons_dir):
    documents_sum = 0
    for filename in os.listdir(images_jsons_dir):
        full_filename = os.path.join(curr_dir, '{}/{}'.format(images_jsons_dir, filename))
        with open(full_filename, 'r') as f:
            documents_dict = json.load(f)
            documents_sum += len(documents_dict['d'])
    return documents_sum


def check_images_years_month_dist(curr_dir, images_jsons_dir):
    years = []
    months = []
    for filename in os.listdir(images_jsons_dir):
        full_filename = os.path.join(curr_dir, '{}/{}'.format(images_jsons_dir, filename))
        with open(full_filename, 'r') as f:
            documents_dict = json.load(f)
            for document in documents_dict['d']:
                try:
                    years.append(parse(document["title"], fuzzy=True).year)
                    months.append(parse(document["title"], fuzzy=True).month)
                except (ParserError, IllegalMonthError, TypeError):
                    pass
    plt.hist(years, bins=100, range=[1850, 2100])
    plt.show()
    plt.hist(months, bins=100, range=[0, 30])
    plt.show()


def insert_images_into_mongo(curr_dir, images_jsons_dir, collection):
    for filename in os.listdir(images_jsons_dir):
        full_filename = os.path.join(curr_dir, '{}/{}'.format(images_jsons_dir, filename))
        with open(full_filename, 'r') as f:
            documents_dict = json.load(f)
            for document in documents_dict['d']:
                try:
                    doc_year = parse(document["title"], fuzzy=True).year
                    desired_document = {
                        "book_id": document["book_id"],
                        "multimedia": document["multimedia"],
                        "multimedia_bk": document["multimedia_bk"],
                        "title": document["title"],
                        "archivalsignature": document["archivalsignature"],
                        "credit": document["credit"],
                        "year": doc_year
                    }
                    doc_id = collection.insert_one(desired_document).inserted_id
                    print(doc_id)
                except (ParserError, IllegalMonthError, TypeError):
                    pass


def insert_questions_to_mongo():
    pass


def get_images_from_mongo_by_year(images_collection, year):
    cursor = images_collection.find({"year": year})
    for document in cursor:
        print(document)


if __name__ == '__main__':
    mongo_client = MongoClient("localhost", 27017)
    heroes_db = mongo_client["heroes_hackathon"]
    questions_collection = heroes_db["questions_collection"]
    IMAGES_COLLECTION = heroes_db["images_collection"]

    # print(requests.get("https://namesfs.yadvashem.org//arch_srika//1A-245G/1A-35G/1FO5_.jpg").content)

    curr_dirname = os.path.dirname(__file__)

    get_images_from_mongo_by_year(IMAGES_COLLECTION, 2021)
    # check_images_years_month_dist(curr_dirname, "jsons/images")
    # search_documents_in_mongo(images_collection)
    # insert_images_into_mongo(curr_dirname, "jsons/images", images_collection)
    # questions_collection.delete_many({})
    # app.run()