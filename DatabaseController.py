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
    conn = pymongo.MongoClient("mongodb+srv://system:vD1TyTbZuwz2XI29@cluster0.8ehcf.mongodb.net/"
                               "myFirstDatabase?retryWrites=true&w=majority")
    db = conn["methods"]


class Users(Database):
    def __init__(self):
        self.users = self.db["users"]

    def insert(self, values):
        try:
            if type(values) == dict:
                self.users.insert_one(values)
            elif type(values) == list:
                self.users.insert_many(values)
            else:
                print(f"{bcolors.WARNING}O valor a ser inserido precisa ser uma lista ou dicionário!{bcolors.ENDC}")
        except:
            print(f"{bcolors.FAIL}Não foi possível inserir o USUARIO no banco de dados.{bcolors.ENDC}")
            return False

    def update(self, values):
        try:
            if type(values) == dict:
                self.users.update_one(values)
            elif type(values) == list:
                self.users.update_many(values)
            else:
                print(f"{bcolors.WARNING}O valor a ser inserido precisa ser uma lista ou dicionário!{bcolors.ENDC}")
        except:
            print(f"{bcolors.FAIL}Não foi possível atualizar o USUARIO no banco de dados.{bcolors.ENDC}")
            return False

    def get(self, find_one, values):
        try:
            if find_one:
                return self.users.find_one(values)
            else:
                return self.users.find(values)
        except:
            print(f"{bcolors.FAIL}Não foi possível selecionar o USUARIO no banco de dados.{bcolors.ENDC}")
            return False

    def list(self, value):
        try:
            if type(value) == object:
                value = list(value)
            return pd.json_normalize(value)
        except:
            print(f"{bcolors.FAIL}Não foi mostrar os dados!{bcolors.ENDC}")
            return False

    def delete(self, remove_one, values):
        try:
            if remove_one:
                return self.users.delete_one(values)
            else:
                return self.users.delete_many(values)
        except:
            print(f"{bcolors.FAIL}Não foi possível apagar o USUARIO do banco de dados.{bcolors.ENDC}")
            return False