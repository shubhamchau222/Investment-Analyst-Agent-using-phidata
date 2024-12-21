from phi.agent import Agent
from phi.model.groq import Groq 
from dotenv import load_dotenv

# loading the environment variables
load_dotenv() 

# Create the groq API key & load the requiredModel
Model_name= "llama-3.3-70b-versatile"

agent= Agent(
    model= Groq(id=Model_name),
    description="You are a funny poet, who writes poems on given topic in hindi."
)

agent.print_response('write poem on girl whos name is Hemangi, who cries everytime & seek money from brother.', markdown=True)
# agent.print_response('Why 2+2 = 4 ?', markdown=True)