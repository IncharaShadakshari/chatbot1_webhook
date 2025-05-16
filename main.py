from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.post("/webhook")
async def dialogflow_webhook(request: Request):
    req_data = await request.json()
    
    # Extract user query or intent name if needed
    query_text = req_data.get("queryResult", {}).get("queryText", "No query")

    # Sample response to Dialogflow
    response = {
        "fulfillmentText": f"You said: {query_text}"
    }

    return JSONResponse(content=response)
