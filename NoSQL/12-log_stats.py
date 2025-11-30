#!/usr/bin/env python3
"""Provide stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


if __name__ == "__main__":
    """Script entry point"""

    client = MongoClient("mongodb://127.0.0.1:27017")
    collection = client.logs.nginx

    # total number of logs
    logs_count = collection.count_documents({})
    print("{} logs".format(logs_count))

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))

    # number of status check logs
    status_count = collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print("{} status check".format(status_count))
    
