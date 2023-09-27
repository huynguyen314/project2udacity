import logging
import azure.functions as func
import pymongo
import json
from bson.json_util import dumps


def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python getPosts trigger function processed a request.')

    try:
        url = "mongodb://project2huycosmosdbacc:0mzCMIFcxAaq9QMGD1w34wzaBG7faYn39EJa4dWPDVXGvV6AwXTD2TBb9C7neHBwzghLbw9gbKvQACDbfVcDDw==@project2huycosmosdbacc.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@project2huycosmosdbacc@"
        client = pymongo.MongoClient(url)
        database = client['project2huycosmosdb']
        collection = database['posts']

        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8', status_code=200)
    except:
        return func.HttpResponse("Bad request.", status_code=400)