import json


def filter_residences(query, value):
    with open('dataset/residencias.json') as file:
        residences = []
        for residence in json.loads(file.read()):
            if str(residence[query]) == str(value):
                residences.append(residence)
    return residences


def filter_average_price(query, value):
    with open('dataset/media_preco.json') as file:
        average_price = []
        for residence in json.loads(file.read()):
            if str(residence[query]) == str(value):
                average_price.append(residence)
    return average_price
