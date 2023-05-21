from bson import ObjectId
from __init__ import *

def delete_doc_by_id(employee_id):
    _id = ObjectId(employee_id)
    EMPLOYEES_COLLECTION.delete_one({"_id": _id})
