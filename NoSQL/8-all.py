#!/usr/bin/env python3
# list all documents in a collection

def list_all(mongo_collection):
    """Return list of all documents"""
    return list(mongo_collection.find())
