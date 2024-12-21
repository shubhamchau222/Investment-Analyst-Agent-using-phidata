from phi.agent import Agent
from phi.model.groq import Groq 
from dotenv import load_dotenv
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

load_dotenv() 
Model_name= "llama-3.3-70b-versatile"

# It's better to assign role & approriate name to the agent/tool, so that It can be utilized properly

web_search= Agent(
    name= "web_search",
    role="Search information on web",
    model=Groq(id=Model_name),
    tools=[DuckDuckGo()],
    instructions=['Always include sources'],
    show_tool_calls=True,
    debug_mode=True,
    markdown=True    
)

yahoo_finance_agent= Agent(
    name="yahoo_finance_agent",
    role="Get Financial data",
    model= Groq(id=Model_name),
    tools=[YFinanceTools(stock_price=True,
                         analyst_recommendations=True,
                         stock_fundamentals=True,
                         company_info=True
                         )],
    description="You are an investment analyst who researches stock prices, analyst recommendation and stock fundamentals",
    instructions=["use tables to display data."],
    show_tool_calls=True,
    debug_mode=True )

# phidata uses `openai` as the default model provider. Please provide a `model` or install `openai`.
agent_team= Agent(
    model= Groq(id=Model_name),
    team=[web_search, yahoo_finance_agent],
    instructions=['Always include sources', 'use tables to display data'],
    show_tool_calls=True,
    markdown=True
)

# agent_team.print_response("summarize analyst recommendations and share the latest news for Quation Solutions", markdown=True)

agent_team.print_response("summarize current stock, analyst recommendations and share the latest news for INFY", markdown=True)