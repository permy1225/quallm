import asyncio
from agents import Agent, Runner, gen_trace_id, trace
from agents.mcp import MCPServerStdio
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
import os

load_dotenv()

app = FastAPI()

class ChatInput(BaseModel):
    query: str

@app.post("/chat")
async def chat(input: ChatInput):
    async with MCPServerStdio(
        params={
            "command": "npx",
            "args": ["-y", "@modelcontextprotocol/server-brave-search"],
            "env": {"BRAVE_API_KEY": os.getenv("BRAVE_API_KEY")},
        }
    ) as server:
        trace_id = gen_trace_id()
        with trace(workflow_name="QuaLLM sample", trace_id=trace_id):
            print(f"View trace: https://platform.openai.com/traces/trace?trace_id={trace_id}\n")

            agent = Agent(
                name="web検索アシスタント",
                instructions="最新の情報が必要な場合はBrave検索を活用してユーザーの質問に答えてください。",
                mcp_servers=[server],
            )
    
            result = await Runner.run(starting_agent=agent, input=input.query)
            return result.final_output
        