import openai
import os
from langchain_community.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import AgentType, initialize_agent, load_tools
import wikipedia
from serpapi import GoogleSearch
import requests
import webbrowser
from langchain.agents import ZeroShotAgent
from langchain.tools.wikipedia.tool import WikipediaQueryRun


os.environ["OPEN_API_KEY"] = "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"
os.environ["SERPAPI_API_KEY"] = "65b20c8bc27a214cd606f503bd03b3248367ca8718bc3168e16f9f37382b6784"
llm = OpenAI(openai_api_key=os.environ["OPEN_API_KEY"], temperature=0.6)

tools = load_tools(["wikipedia", "serpapi"], llm=llm)

tools = []

agent = initialize_agent(
    tools,
    llm=llm,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

PROMPT = ""

agent = ZeroShotAgent(prompt="You a", tools=, llm=)

agent()

print("Please give a short description about yourself including your intrests,\n skills, qualifications, work experience (optional), career goals \n and salary expectations.")
prompt = PromptTemplate.from_template("What is the most relevant detailed and suitable technical position for the given description {text}?")
chain = LLMChain(llm = llm, prompt = prompt)
text = input()
output = chain.run(text)
print("Suitable professions suggested :",output)

profession = output
city = input("Enter the desired city")
url = "https://serpapi.com/search.json"
params = {
    "engine": "google_jobs",
    "q": f"{profession} {city}",
    "api_key": "4068e2eebdae236291dbeb5195be7274ae5f734a0c4789e23f5a19aee04050d2"
}

response = requests.get(url, params=params)
data = response.json()
#print(data)

if 'jobs_results' in data:
    for job in data['jobs_results']:
        print("Title:", job['title'])
        print("Company:", job['company_name'])
        print("Location:", job['location'])
        print("Salary:", job.get('salary', 'Not provided'))
        print("link:", job['related_links'])

       
        print()
else:
    print("No job results found.")


def get_wikipedia_summary(career):
    try:
        summary = wikipedia.summary(career)
    except wikipedia.exceptions.DisambiguationError as e:
        # If there are multiple results, choose the first one
        summary = wikipedia.summary(e.options[0])
    except wikipedia.exceptions.PageError:
        summary = "No Wikipedia page found for this topic."
    return summary

# Get user input for the desired career
career = output

# Recommend job postings based on the input career
job_postings = recommend_job_postings(career)

# Get Wikipedia summary for the input career
wikipedia_summary = get_wikipedia_summary(career)

# Display recommended job postings
if job_postings:
    print("Recommended job postings for", career, ":")
    for i, job in enumerate(job_postings, 1):
        print(f"{i}. {job}")
else:
    print("No job postings found for", career)

# Display Wikipedia summary
print("\nWikipedia Summary:")
print(wikipedia_summary)
