import pprint
from bson.objectid import ObjectId
from __init__ import *

pprinter = pprint.PrettyPrinter()


def update_employee_by_id(_id):
    obj_id = ObjectId(_id)

    all_updates = {
        "$set": {
            "association_member": True,
            "emp_name": "Liam Payne"
        },
        "$inc": {"pay_in_usd": 50000},
    }

    EMPLOYEES_COLLECTION.update_one({"_id": obj_id}, all_updates)


def replace_doc(_id):
    obj_id = ObjectId(_id)

    new_doc = {
        "emp_name": "Dr. Prashant Damale",
        "position": "Chair Member",
        "department": "Computer Science",
        "university": "University of Alberta",
        "pay_in_usd": 100000
    }

    EMPLOYEES_COLLECTION.replace_one({"_id": obj_id}, new_doc)


if __name__ == '__main__':
    _id = "6468ded7af26b7f54dd91ce7"
    update_employee_by_id(_id)
    print(f"Done with updating Employee with ID: {_id}")
