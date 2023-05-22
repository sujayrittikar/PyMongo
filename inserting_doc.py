from __init__ import *

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
PROF_PAY = 125000
ASSOC_PROF_PAY = 80000
DEPARTMENT = "Computer Science"


def insert_test_doc() -> None:
    test_document = {
        "_id": "A1",
        "place": "Mumbai",
        "type": "Test"
    }

    inserted_id = TEST_COLLECTION.insert_one(test_document).inserted_id
    print(inserted_id)


def generate_prod_docs() -> list:
    uni_emp_dicts_list = []

    for prof in PROF_NAMES:
        prof_dict = {
            "emp_name": prof,
            "position": "Professor",
            "department": DEPARTMENT,
            "university": UNIVERSITY_NAME,
            "pay_in_usd": PROF_PAY
        }
        uni_emp_dicts_list.append(prof_dict)

    for assoc_prof in ASSOC_PROF_NAMES:
        assoc_prof_dict = {
            "emp_name": assoc_prof,
            "position": "Associate Professor",
            "department": DEPARTMENT,
            "university": UNIVERSITY_NAME,
            "pay_in_usd": ASSOC_PROF_PAY
        }
        uni_emp_dicts_list.append(assoc_prof_dict)

    return uni_emp_dicts_list


def insert_prod_docs():
    emp_docs_list = generate_prod_docs()
    EMPLOYEES_COLLECTION.insert_many(emp_docs_list)

    print(
        f"""
            Done with Inserting {len(emp_docs_list)} documents
            to the Production DB."""
    )


def insert_aggreg_samples():
    UNIVERSITIES_COLLECTION.insert_many([
        {
            "country" : 'Spain',
            "city" : 'Salamanca',
            "name" : 'USAL',
            "location" : {
                "type" : 'Point',
                "coordinates" : [ -5.6722512,17, 40.9607792 ]
            },
            "students" : [
                { "year" : 2014, "number" : 24774 },
                { "year" : 2015, "number" : 23166 },
                { "year" : 2016, "number" : 21913 },
                { "year" : 2017, "number" : 21715 }
            ]
        },
        {
            "country" : 'Spain',
            "city" : 'Salamanca',
            "name" : 'UPSA',
            "location" : {
                "type" : 'Point',
                "coordinates" : [ -5.6691191,17, 40.9631732 ]
            },
            "students" : [
                { "year" : 2014, "number" : 4788 },
                { "year" : 2015, "number" : 4821 },
                { "year" : 2016, "number" : 6550 },
                { "year" : 2017, "number" : 6125 }
            ]
        }
        
    ])

    COURSES_COLLECTION.insert_many([
        {
            "university" : 'USAL',
            "name" : 'Computer Science',
            "level" : 'Excellent'
        },
        {
            "university" : 'USAL',
            "name" : 'Electronics',
            "level": 'Intermediate'
        },
        {
            "university" : 'USAL',
            "name" : 'Communication',
            "level" : 'Excellent'
        }
    ])


if __name__ == '__main__':
    # insert_test_doc()
    # insert_prod_docs()
    insert_aggreg_samples()

