from __init__ import *

def aggregate(country, city):
    aggregate_results = UNIVERSITIES_COLLECTION.aggregate(
        [
            {
                "$match": {
                    "country": country,
                    "city": city
                }
            },
            {
                "$project": {
                    "_id": 0,
                    "country": 1,
                    "city": 1,
                    "name": 1,
                    "total_count": 1
                }
            },
            {
                "$group": {
                    "_id": {"name": "$name", "total_students": "$students"},
                    "total_count": {"$sum": 1}
                }
            },
            {
                "$sort": {
                    "students.number": -1
                }
            }
        ]
    )

    return aggregate_results


if __name__ == '__main__':
    country = "Spain"
    city = "Salamanca"
    aggregate_results = aggregate(country, city)

    for aggregate_result in aggregate_results:
        print(aggregate_result)
