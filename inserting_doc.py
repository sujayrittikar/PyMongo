from connection import get_mongo_conn

PROF_NAMES = (
    "Dr. Santosh Nakimara",
    "Dr. Mahesh Patole",
    "Dr. Umesh Jambhale",
)
ASSOC_PROF_NAMES = (
    "Ravindra Kumar",
    "Dr. Prashant Damale",
    "Jaikumar Raghurao",
    "Dr. Sabarmati Patil",
    "Dr. Pankaj Tripathi"
)
UNIVERSITY_NAME = "The University of Doing"
PROF_PAY = "$125,000"
ASSOC_PROF_PAY = "$80,000"
DEPARTMENT = "Computer Science"

mongo_conn = get_mongo_conn()


def insert_test_doc() -> None:
    test_db = mongo_conn.test
    collection = test_db.test
    test_document = {
        "_id": "A1",
        "place": "Mumbai",
        "type": "Test"
    }

    inserted_id = collection.insert_one(test_document).inserted_id
    print(inserted_id)


def generate_prod_docs() -> list:
    uni_emp_dicts_list = []

    for prof in PROF_NAMES:
        prof_dict = {
            "emp_name": prof,
            "department": DEPARTMENT,
            "university": UNIVERSITY_NAME,
            "pay": PROF_PAY
        }
        uni_emp_dicts_list.append(prof_dict)

    for assoc_prof in ASSOC_PROF_NAMES:
        assoc_prof_dict = {
            "emp_name": assoc_prof,
            "department": DEPARTMENT,
            "university": UNIVERSITY_NAME,
            "pay": ASSOC_PROF_PAY
        }
        uni_emp_dicts_list.append(assoc_prof_dict)

    return uni_emp_dicts_list


def insert_prod_docs():
    emp_docs_list = generate_prod_docs()
    production = mongo_conn.production
    employees_collection = production.employees_collection
    employees_collection.insert_many(emp_docs_list)

    print(
        f"""
            Done with Inserting {len(emp_docs_list)} documents
            to the Production DB."""
    )


if __name__ == '__main__':
    # insert_test_doc()
    insert_prod_docs()
