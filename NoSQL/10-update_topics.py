#!/usr/bin/env python3
"""Update topics of a school document"""


def update_topics(mongo_collection, name, topics):
    """Update all documents with the given name
    Set the topics field to the provided list
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
