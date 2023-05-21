import pprint
from bson.objectid import ObjectId
from __init__ import *

pprinter = pprint.PrettyPrinter()


def count_all_people():
    count = EMPLOYEES_COLLECTION.count_documents(filter={})
    print("Number of Employees: ", count)


def find_all_employees():
    employees = EMPLOYEES_COLLECTION.find()

    for employee in employees:
        pprinter.pprint(employee)


def find_emp_by_name(name):
    doc = EMPLOYEES_COLLECTION.find_one({"emp_name": name})
    pprinter.pprint(doc)


def find_emp_by_id(id):
    _id = ObjectId(id)
    doc = EMPLOYEES_COLLECTION.find_one({"_id": _id})
    pprinter.pprint(doc)


def find_emp_by_salary_range(min_salary, max_salary):
    query = {
        "$and":
        [
            {"pay_in_usd": {"$gt": min_salary}},
            {"pay_in_usd": {"$lt": max_salary}}
        ]
    }
    docs = EMPLOYEES_COLLECTION.find(query).limit(5)

    for doc in docs:
        pprinter.pprint(doc)


if __name__ == '__main__':
    # find_all_employees()
    # find_emp_by_name("Ravindra Kumar")
    # count_all_people()
    # find_emp_by_id("6468d3e9a47add55fc41d778")
    find_emp_by_salary_range(90000, 150000)
