from flask import Flask 
from langchain_community.llms import Ollama 

app = Flask(__name__)

#llm = Ollama(model='llama3')

#response = llm.invoke("Tell me a soccer joke")

#print(response)

def start_app():
    app.run(host="0.0.0.0", port=8080, debug=True)


if __name__ == "__main__":
    start_app()