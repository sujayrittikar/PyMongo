from __init__ import MONGO_CLIENT
from bson import ObjectId

PERSON_DB = MONGO_CLIENT.person
PERSON_COLLECTION = PERSON_DB.person_collection


def add_address_embed(person_id, address):
    _id = ObjectId(person_id)
    PERSON_COLLECTION.update_one(
        {"_id": _id},
        {"$addToSet":{
                "addresses": address
            }
        }
    )


if __name__ == '__main__':
    person_id = "646a18d979df4a39db88040e"
    address = {
        "_id": "A1",
        "street": "Bay Street",
        "number": 2706,
        "city": "San Francisco",
        "country": "United States",
        "zip": 940107,
        "owner_id": ObjectId(person_id)
    }
    add_address_embed(person_id, address)