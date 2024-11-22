from flask import Flask, request, jsonify
from langchain_ollama import OllamaLLM

app = Flask(__name__)

cached_llm = OllamaLLM(model='llama3')


@app.route("/ai", methods=["POST"])
def aiPost():
    print("Post /ai called")
    json_content = request.json
    query = json_content.get("query")
    print(f"query: {query}")

    response = cached_llm.invoke(query)
    print(response)

    response_answer = {"answer": response}
    return response_answer

@app.route("/pdf", methods=["POST"])
def pdfPost():
    file = request.files["file"]
    file_name = file.filename
    save_file = "pdf/" + file_name
    file.save(save_file)
    print(f"filename: {file_name}")

    response = {'status': 'Sucessfully uploaded file', 'filename': file_name}
    return response

def start_app():
    app.run(host="0.0.0.0", port=8080, debug=True)


if __name__ == "__main__":
    start_app()