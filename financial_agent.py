from phi.agent import Agent
from phi.model.groq import Groq 
from dotenv import load_dotenv
from phi.tools.yfinance import YFinanceTools
from phi.tools.csv_tools import CsvTools
# loading the environment variables
load_dotenv() 
# Create the groq API key & load the requiredModel
Model_name= "llama-3.3-70b-versatile"

# Tools: Tools are functions that an Agent can run like searching the web, running SQL, sending an email or calling APIs. 
# Use tools integrate Agents with external systems. You can use any python function as a tool or use a pre-built toolkit. The general syntax is:

# YFinanceTools enable an Agent to access stock data, financial information and more from Yahoo Finance.

agent= Agent(
    model= Groq(id=Model_name),
    tools=[YFinanceTools(stock_price=True,
                         analyst_recommendations=True,
                         stock_fundamentals=True,
                         company_info=True
                         )],
    description="You are an investment analyst who researches stock prices, analyst recommendation and stock fundamentals",
    instructions=["use tables to display data."],
    show_tool_calls=True,
    debug_mode=True

)
agent.print_response("Share the INFY stock prices and analyst recommendation.", markdown=True)



