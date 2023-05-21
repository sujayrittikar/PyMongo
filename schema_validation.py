import pymongo
from traceback import print_exc
from __init__ import MONGO_CLIENT

db = MONGO_CLIENT.production


validator = {
    "$jsonSchema": {
        "bsonType": "object",
        "title": "Student Object Validation",
        "required": [ "address", "major", "name", "year" ],
        "properties": {
        "name": {
            "bsonType": "string",
            "description": "'name' must be a string and is required"
        },
        "year": {
            "bsonType": "int",
            "minimum": 2017,
            "maximum": 3017,
            "description": "'year' must be an integer in [ 2017, 3017 ] and is required"
        },
        "gpa": {
            "bsonType": [ "double" ],
            "description": "'gpa' must be a double if the field exists"
        }
        }
    }
}


try:
    db.create_collection("students")
except pymongo.errors.CollectionInvalid:
    pass

db.command("collMod", "students", validator=validator)

# Invalid Insert - Schema Validation should fail due to double gpa
# db.students.insert_one(
#     {
#         "name": "Alice",
#         "year": 2019,
#         "major": "History",
#         "gpa": 3,
#         "address": {
#             "city": "NYC",
#             "street": "33rd Street"
#         }
#     }
# )

db.students.insert_one(
    {
        "name": "Alice",
        "year": 2019,
        "major": "History",
        "gpa": 3.0,
        "address": {
            "city": "NYC",
            "street": "33rd Street"
        }
    }
)