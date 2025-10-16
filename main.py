from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

# your secret (same as submitted in Google Form)
SECRET = "mridul123"

@app.post("/api-endpoint")
async def receive_request(request: Request):
    data = await request.json()

    # 1️⃣ verify secret
    if data.get("secret") != SECRET:
        return JSONResponse({"error": "Invalid secret"}, status_code=403)

    # 2️⃣ acknowledge the request
    return JSONResponse({"status": "ok", "message": "Task received"})
