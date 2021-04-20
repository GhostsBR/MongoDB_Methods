import pymongo
import pandas as pd


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Database:
    conn = pymongo.MongoClient("mongodb+srv://system:vD1TyTbZuwz2XI29@cluster0.8ehcf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = conn["methods"]


class Users(Database):
    def __init__(self):
        self.users = self.db["users"]

    def insert(self, values):
        if not values:
            return False

        if type(values) == dict:
            self.users.insert_one(values)
        elif type(values) == list:
            self.users.insert_many(values)
        else:
            print(f"{bcolors.WARNING}O valor a ser inserido precisa ser uma lista ou dicionário!{bcolors.ENDC}")

    def update(self, values):
        if type(values) == dict:
            self.users.update_one(values)
        elif type(values) == list:
            self.users.update_many(values)
        else:
            print(f"{bcolors.WARNING}O valor a ser inserido precisa ser uma lista ou dicionário!{bcolors.ENDC}")

    def get(self, find_one, values):
        if find_one:
            return self.users.find_one(values)
        else:
            return self.users.find(values)

    def list(self, value):
        if type(value) == object:
            value = list(value)
        return pd.json_normalize(value)

    def delete(self, values):
        if type(values) == dict:
            self.users.delete_one(values)
        elif type(values) == list:
            self.users.delete_many(values)
        else:
            print(f"{bcolors.WARNING}O valor a ser inserido precisa ser uma lista ou dicionário!{bcolors.ENDC}")