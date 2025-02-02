import openai
import uvicorn
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
import json

# Your OpenAI API key (don't hardcode in production; use environment variables)
openai.api_key = "sk-..."  # Replace with your OpenAI API key

# Create a FastAPI app
app = FastAPI()

# Function to check for bugs (simple placeholder for now)
def check_for_bugs(code: str, language: str):
    if language == "python":
        if "print" in code and "()" not in code:
            return "Error: Missing parentheses in print function!"
    return "No bugs detected!"

# WebSocket endpoint for code completion and bug checking
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    try:
        while True:
            try:
                # Receive the message from the frontend (code and language)
                data = await websocket.receive_json()
                
                code = data.get("code")
                language = data.get("language")

                # Code suggestion from OpenAI
                openai_response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",  # Use the newer GPT model for code completion
                    messages=[
                        {"role": "system", "content": "You are a helpful coding assistant."},
                        {"role": "user", "content": code}  # Pass the code from the user
                    ],
                    temperature=0.3,
                )

                # Get the suggestion from the OpenAI response
                suggestion = openai_response['choices'][0]['message']['content']

                # Bug detection
                bugs = check_for_bugs(code, language)

                # Send back the suggestion and bug detection result to the frontend
                await websocket.send_text(
                    json.dumps({"suggestion": suggestion, "bugs": bugs})
                )

            except WebSocketDisconnect as e:
                print(f"WebSocket disconnected with code {e.code}. Reason: {e.reason}")
                break  # Exit the loop gracefully

            except Exception as e:
                print(f"Unexpected error: {str(e)}")
                await websocket.send_text(f"Error: {str(e)}")
                break  # Exit the loop if there is a critical error

    finally:
        await websocket.close()

# Optional: HTML frontend for testing the WebSocket (if needed)
@app.get("/")
def get():
    return HTMLResponse(content=open("index.html").read(), status_code=200)

# To run the app using Uvicorn:
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
