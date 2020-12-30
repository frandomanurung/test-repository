
from pymongo import MongoClient
from bson.json_util import dumps
from fake_data import dummy_data

## Setup MongoDB Client. datasbase=RHAMP
uri="mongodb+srv://m220student:m220password@sandbox.oc3oc.mongodb.net/admin" 
client=MongoClient(uri)
db=client.RHAMP


def get_bp(pid):
    """
    Given a patient pid, return bp with that pid, 
    """
    try:
        pipeline = [
            {"$match": {"pid": pid}},
            {"$project": {"nama":1, "pid":1, "bp sis":1, "bp dias": 1}},
            {"$sort" : {"date": -1 }}
            
        ]

        bp= db.patient_bloodpressure.aggregate(pipeline)
        return bp

    except Exception as e:
        return e


def insert_bp(data):
    """
    Given a patient data, insert blood pressure database, 
    """
    try:
        bp=db.patient_bloodpressure
        insert_result = bp.insert_many (data)    
        
        return insert_result

    except Exception as e:
        return e


