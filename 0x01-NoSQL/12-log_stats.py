#!/usr/bin/env python3

"""
provides some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient

METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]

def nginx_logs(mongo_collection, option=None):
    """
    returns stats about Nginx logs stored in MongoDB
    """
    if option:
        value = mongo_collection.count_documents({"method": {"$regex": option}})
        print(f"\tmethod {option}: {value}")
        return

    result = mongo_collection.count_documents({})
    print(f"{result} logs")
    print("Methods :")
    for method in  METHODS:
        value = mongo_collection.count_documents({"method": method})
        print(f"\t{method}: {value}")

    status_check = mongo_collection.count_documents({"path": "/status"})
    print(f"{status_check} status check")


if __name__ == "__main__":
    nginx_collection = MongoClient('mongodb://127.0.0.1:27017').logs.nginx
    nginx_logs(nginx_collection)
