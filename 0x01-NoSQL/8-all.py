#!/usr/bin/env python3

"""
function that lists all documents in a collection
"""


def list_all(mongo_collection):
    """
    lists all docuents in a  collection
    returns a list of all dicuents or empty list
    """
    if mongo_collection.count_documents({}) == 0:
        return []
    return mongo_collection.find()
