"""
function that returns the list of school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    returns the list of school having a specific topic
    Args:
        mongo_collection: str
            the pymongo collection object
        topic: str
             topic searched
    """
    return list(mongo_collection.find({"topics": topic}))
