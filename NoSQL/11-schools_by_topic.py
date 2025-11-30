#!/usr/bin/env python3
"""Return list of schools with a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """Return list of documents that contain the given topic
    in their topics field
    """
    return list(mongo_collection.find({"topics": topic}))
