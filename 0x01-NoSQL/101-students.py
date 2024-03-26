#!/usr/bin/env python3
"""
function that returns all students sorted by average score
average score must be part of each item returns with key = averageScore
"""


def top_students(mongo_collection):
    """
    returns all students sorted by average score
    Args:
        mongo_collection: the pymongo collection object
    """
    top_students = mongo_collection.aggregate([
        {
            "$project": {
                "name": "$anme",
                "average_score": {"average": "$topic.score"}
                }
            },
        {"$sort": {"average_score": -1}}
        ])
    return top_students
