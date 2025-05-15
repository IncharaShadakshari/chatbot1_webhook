from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/webhook")
async def dialogflow_webhook(request: Request):
    try:
        body = await request.json()
        
        # Extract user's query from Dialogflow request
        user_query = body.get('queryResult', {}).get('queryText', '')
        
        # Simple bot response logic (can be replaced with custom logic)
        reply_text = f"You said: {user_query}"

        return JSONResponse({
            "fulfillmentText": reply_text  # Dialogflow uses this to respond
        })
    
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"fulfillmentText": "Something went wrong on the server!"}
        )
