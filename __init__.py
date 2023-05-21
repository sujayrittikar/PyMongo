from connection import get_mongo_conn

MONGO_CLIENT = get_mongo_conn()
TEST_DB = MONGO_CLIENT.test
TEST_COLLECTION = TEST_DB.test
PRODUCTION = MONGO_CLIENT.production
EMPLOYEES_COLLECTION = PRODUCTION.employees_collection
