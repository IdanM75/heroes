import os
import json
import matplotlib.pyplot as plt

from dateutil.parser import parse, ParserError
from calendar import IllegalMonthError


def load_jsons_images(curr_dir, images_jsons_dir):
    images_list = []
    for filename in os.listdir(images_jsons_dir):
        full_filename = os.path.join(curr_dir, '{}/{}'.format(images_jsons_dir, filename))
        with open(full_filename, 'r', encoding="utf-8") as f:
            images_dict = json.load(f)
            for image_dict in images_dict['d']:
                images_list.append(image_dict)
    return images_list


def load_jsons_questions(curr_dir, questions_jsons_dir):
    questions_list = []
    for filename in os.listdir(questions_jsons_dir):
        full_filename = os.path.join(curr_dir, '{}/{}'.format(questions_jsons_dir, filename))
        with open(full_filename, 'r', encoding="utf-8") as f:
            questions_dict = json.load(f)
            for question in questions_dict["questions"]:
                questions_list.append(question)
    return questions_list


def count_images_in_jsons(curr_dir, images_jsons_dir):
    documents_count = 0
    for filename in os.listdir(images_jsons_dir):
        full_filename = os.path.join(curr_dir, '{}/{}'.format(images_jsons_dir, filename))
        with open(full_filename, 'r', encoding="utf-8") as f:
            documents_dict = json.load(f)
            documents_count += len(documents_dict['d'])
    return documents_count


def check_images_years_month_dist(curr_dir, images_jsons_dir):
    years = []
    months = []
    for filename in os.listdir(images_jsons_dir):
        full_filename = os.path.join(curr_dir, '{}/{}'.format(images_jsons_dir, filename))
        with open(full_filename, 'r', encoding="utf-8") as f:
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
