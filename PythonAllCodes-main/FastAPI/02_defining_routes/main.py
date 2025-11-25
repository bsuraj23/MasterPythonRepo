# fastapi below write api which will lgive back response from this curl 

#curl -X 'GET' \
#   'https://data.healthcare.gov/api/1/metastore/schemas' \
#   -H 'accept: application/json'


from fastapi import FastAPI
import requests
app = FastAPI()
@app.get("/schemas")
def get_schemas():
    url = "https://data.healthcare.gov/api/1/metastore/schemas"
    headers = {
        "accept": "application/json"
    }
    response = requests.get(url, headers=headers)
    return response.json()

# uvicorn Class1.firstTemp:app --reload   
# http://127.0.0.1:8000/schemas

