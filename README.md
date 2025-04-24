# Research Assistant API using Julep AI

This FastAPI application uses [Julep AI](https://www.julep.ai/) to power a writing and research assistant. It initializes a research agent, receives research requests via an API endpoint, and returns concise responses based on the user's topic and desired format.

---

## Features

- Initializes a Julep AI agent and task on app startup  
- Accepts research topics and response formats via a POST endpoint  
- Uses an execution flow to get generated results from the Julep agent  
- Returns structured, helpful AI-generated content

---

## Project Structure

```
project/
│
├── api/
│   └── agent/
│       ├── researchHandler.py  # Logic to handle research execution
│       └── research_agent.yaml # Julep agent task definition
│
├── main.py                     # FastAPI app entry point
├── .env                        # Contains the JULEP_API_KEY
└── README.md                   # You're here!
```

## 🛠️ Requirements

- Python 3.8+
- Julep API key (you can get one from https://dashboard.julep.ai/home/)
- `pip` package manager

---

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/Tayyaba19/research-assistant-api.git
cd research-assistant-api
```

2. **Create and activate a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows
```

3. **Install the dependencies**

```bash
pip install -r requirements.txt
```

Or manually install them:

```bash
pip install fastapi uvicorn pyyaml julep
```

4. **Set your Julep API key**

Create a `.env` file in the project root and add:

```
JULEP_API_KEY=your_julep_api_key_here
```

5. **Start the API server**

```bash
uvicorn main:app --reload
```

Your API will be live at http://127.0.0.1:8000

---

## Sample Request

Send a POST request to `/research` with the following body:

```json
{
  "topic": "Applications of AI in Healthcare",
  "response_format": "bullet points"
}
```

## Try it with curl

```bash
curl -X POST http://127.0.0.1:8000/research \
-H "Content-Type: application/json" \
-d '{"topic": "Climate change impact", "response_format": "summary"}'
```
