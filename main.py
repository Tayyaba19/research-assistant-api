from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from julep import Client
import os
import yaml

from api.agent.researchHandler import ResearchHandler

JULEP_API_KEY = os.environ["JULEP_API_KEY"]
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


async def initialize_client():
    client = Client(api_key=JULEP_API_KEY)

    agent = client.agents.create(
        name="Writing Assistant",
        model="gpt-4o-mini",
        about="A helpful AI assistant that specializes in writing and editing."
    )

    with open('api/agent/research_agent.yaml', 'r') as file:
        task_definition = yaml.safe_load(file)

    task = client.tasks.create(
        agent_id=agent.id,
        **task_definition
    )
    return client, task

class ResearchRequest(BaseModel):
    topic: str
    response_format: str

@app.on_event("startup")
async def startup_event():
    client, task = await initialize_client()
    app.state.client = client
    app.state.task = task

@app.post("/research")
async def research(data: ResearchRequest):
    try:
        handler = ResearchHandler(
            topic=data.topic,
            response_format=data.response_format,
            client=app.state.client,
            task=app.state.task
        )
        result = handler.generate_response()
        return {"result": result}
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        print(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail="Something went wrong.")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
