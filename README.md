# AI Code Editor Hackathon Project

## Overview
This project is an AI-powered code editor with real-time features for code autocompletion, bug detection, and multi-language support. Built with **FastAPI** for the backend and **JavaScript** for the frontend, this tool aims to improve coding productivity by providing intelligent suggestions and detecting potential bugs as you type.

### Features
- **Real-time Autocompletion**: As you type, the editor provides code suggestions in multiple programming languages (Python, JavaScript, C++, Java).
- **Bug Detection**: Identifies potential bugs in your code and provides feedback.
- **Real-time Collaboration**: Multiple users can collaborate on the same code in real time.
- **Multi-language Support**: Supports multiple programming languages, including Python, JavaScript, C++, and Java.
- **Enhanced Error Messages**: Detailed error messages for common issues in code, helping you understand and fix problems faster.
- **Secure Authentication**: Ensures users are securely logged in with authentication features.
  
## Technology Stack
- **Backend**: FastAPI (for handling WebSocket communication and backend logic)
- **Frontend**: HTML, CSS, JavaScript
- **WebSocket**: For real-time communication between the frontend and backend
- **Languages Supported**: Python, JavaScript, C++, Java

## Setup Instructions

### 1. Install Dependencies
To get started, clone the repository and install the necessary dependencies.

#### Backend (Python)
Make sure you have **Python 3.7+** installed. Then, create a virtual environment and install the required libraries:

```bash
git clone https://github.com/your-repo/ai-code-editor.git
cd ai-code-editor
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
