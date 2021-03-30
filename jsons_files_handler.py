import os
import json
import matplotlib.pyplot as plt

from dateutil.parser import parse, ParserError
from calendar import IllegalMonthError


def count_images_in_jsons(curr_dir, images_jsons_dir):
    documents_count = 0
    for filename in os.listdir(images_jsons_dir):
        full_filename = os.path.join(curr_dir, '{}/{}'.format(images_jsons_dir, filename))
        with open(full_filename, 'r') as f:
            documents_dict = json.load(f)
            documents_count += len(documents_dict['d'])
    return documents_count


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
