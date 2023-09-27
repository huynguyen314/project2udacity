import azure.functions as func
import pymongo
from bson.objectid import ObjectId


def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('id')

    if id:
        try:
            url = "mongodb://project2huycosmosdbacc:0mzCMIFcxAaq9QMGD1w34wzaBG7faYn39EJa4dWPDVXGvV6AwXTD2TBb9C7neHBwzghLbw9gbKvQACDbfVcDDw==@project2huycosmosdbacc.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@project2huycosmosdbacc@"
            client = pymongo.MongoClient(url)
            database = client['project2huycosmosdb']
            collection = database['advertisements']
            
            query = {'_id': ObjectId(id)}
            result = collection.delete_one(query)
            return func.HttpResponse("")

        except:
            print("could not connect to mongodb")
            return func.HttpResponse("could not connect to mongodb", status_code=500)

    else:
        return func.HttpResponse("Please pass an id in the query string",
                                 status_code=400)
