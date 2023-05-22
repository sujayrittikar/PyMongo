from bson import ObjectId
import pyarrow
from pymongoarrow.api import Schema
from pymongoarrow.monkey import patch_all

from __init__ import *

PERSON_DB = MONGO_CLIENT.person
PERSON_COLLECTION = PERSON_DB.person_collection

# Access to all API's in PyMongoArrow
patch_all()

author = Schema(
    {
        "_id": ObjectId,
        "first_name": pyarrow.string(),
        "last_name": pyarrow.string()
    }
)

# df = PERSON_COLLECTION.find_pandas_all({}, schema=author)
arrow_table = PERSON_COLLECTION.find_arrow_all({}, schema=author)
print(arrow_table)
