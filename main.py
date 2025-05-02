from langchain.agents import initialize_agent,AgentType
from langchain_community.tools import TavilySearchResults
from langchain.prompts import PromptTemplate
from langchain.tools import tool
from langchain_groq import ChatGroq
from langchain.memory import ConversationBufferWindowMemory
import  pandas as pd
from fastapi import FastAPI
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

load_dotenv("api.env")
from datetime import datetime

now = datetime.now()

date=now.date()
memory = ConversationBufferWindowMemory(memory_key="chat_history",k=2)
llama=ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct",
    temperature=1,
    max_completion_tokens=1024
    )
data=pd.read_csv("./data.csv")

search=TavilySearchResults(max_results=1,search_depth="basic")

@tool
def schedule(query:str)->str:
    """
    use this to answer the queries about the schedule of the f1 races asked by the user.mostly asking about upcoming races and whats next race
    the only args is query

    """
    template="""
    yourre a f1 ethusiastic chatbot named draggy
    Here is a table of upcoming F1 events todays date is 
    {date}:

    {data}

    Now answer the question: {question}
    """
    prompt=PromptTemplate(template=template,input_variables=["data","question","date"])
    chain=prompt|llama
    response=chain.invoke({"data":data,"question":query,"date":date})
    return response.content
@tool
def about(query:str)->str:
    """
    use this to answer the queries the agent like who are u. and questions regarding who created u and other things that user whats to know about the ai he is using.
    use this whenever the user queries about the chatbot used. and he talks to chatbot if it as a person
    """
    template="""
    youre a f1 ethusiastic chatbot created by tony stark named draggy
    you are obsessed over f1 and a max verstappen fan 
    Now answer the question: {question}
    """
    prompt=PromptTemplate(template=template,input_variables=["question"])
    chain=prompt|llama
    response=chain.invoke({"question":query})
    return response.content


tools=[search,schedule,about]
agent=initialize_agent(llm=llama,tools=tools,agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,verbose=True,memory=memory)
app=FastAPI()



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/chat/{query}")
def chat(query:str):
    return agent.invoke({"input":query})
