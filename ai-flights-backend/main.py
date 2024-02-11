from flask import Flask, request, jsonify, Response
from flask_cors import CORS  # Import the CORS library
from langchain.agents.agent_toolkits.amadeus.toolkit import AmadeusToolkit
from langchain.agents import initialize_agent, AgentType
from langchain import OpenAI
import os, settings
from datetime import datetime

current_date = datetime.now().date()
formatted_date = current_date.strftime("%Y-%m-%d")
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

os.environ["OPENAI_API_KEY"] = settings.config['openai_key']
os.environ["AMADEUS_CLIENT_ID"] = settings.config['amadeus_key']
os.environ["AMADEUS_CLIENT_SECRET"] = settings.config['amadeus_secret']

llm = OpenAI(temperature=0)
toolkit = AmadeusToolkit()
tools = toolkit.get_tools()
agent = initialize_agent(
    tools=tools,
    llm=llm,
    verbose=True,
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
)

@app.route('/run_agent', methods=['POST'])
def run_agent():
    input_text = request.args.get('input_text')
    if input_text is None:
        return "Error: No input_text provided", 400
    combined="Today is "+formatted_date+". "+input_text
    print(combined)
    output = agent.run(combined)
    return output

if __name__ == '__main__':
    app.run(debug=True, port=5050)