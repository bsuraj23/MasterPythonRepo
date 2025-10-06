from fastapi import FastAPI, BackgroundTasks, WebSocket

app = FastAPI()

def send_email(email: str, message: str):
    print(f"Sending email to {email}: {message}")

@app.post("/send-email/")
def send_email_endpoint(email: str, message: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(send_email, email, message)
    return {"message": "Email will be sent in the background"}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message received: {data}")