# from fastapi import FastAPI, Request
# from fastapi.responses import JSONResponse  # Fixed import typo

# app = FastAPI()

# @app.post("/")
# async def handle_request(request: Request):
#     payload = await request.json()
#     intent = payload['queryResult']['intent']['displayName']  # Fixed typo in 'displayName'
#     parameters = payload['queryResult']['parameters']
#     output_contexts = payload['queryResult']['outputContexts']
#     if intent == "Default Welcome Intent":
#         return JSONResponse(content={"fulfillmentText": "arre bhai"})  # Fixed 'return' statement
print("hello world")