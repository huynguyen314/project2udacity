import azure.functions as func
import pymongo

def main(req: func.HttpRequest) -> func.HttpResponse:

    request = req.get_json()

    if request:
        try:
            url = "mongodb://project2huycosmosdbacc:0mzCMIFcxAaq9QMGD1w34wzaBG7faYn39EJa4dWPDVXGvV6AwXTD2TBb9C7neHBwzghLbw9gbKvQACDbfVcDDw==@project2huycosmosdbacc.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@project2huycosmosdbacc@"
            client = pymongo.MongoClient(url)
            database = client['project2huycosmosdb']
            collection = database['advertisements']

            rec_id1 = collection.insert_one(eval(request))

            return func.HttpResponse(req.get_body())

        except ValueError:
            print("could not connect to mongodb")
            return func.HttpResponse('Could not connect to mongodb', status_code=500)

    else:
        return func.HttpResponse(
            "Please pass name in the body",
            status_code=400
        )