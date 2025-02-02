from fastapi import FastAPI, Request
from pydantic import BaseModel
import ast

app = FastAPI()

class CodeRequest(BaseModel):
    code: str

@app.post("/detect_bugs/")
async def detect_bugs(code_request: CodeRequest):
    code = code_request.code
    try:
        ast.parse(code)  # Basic syntax check
        return {"status": "success", "message": "No syntax errors detected."}
    except SyntaxError as e:
        return {
            "status": "error",
            "error": f"Syntax Error: {e.msg}",
            "line": e.lineno,
            "details": e.text.strip() if e.text else ""
        }
