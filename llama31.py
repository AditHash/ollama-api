#llama3.1 


from flask import Flask, request, jsonify
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
from langchain_core.memory import ConversationBufferMemory

app = Flask(__name__)

# Initialize the Langchain components
template = """You are a helpful assistant, you respond concisely and briefly unless asked for detail.

Question: {question}
Answer: """
prompt = ChatPromptTemplate.from_template(template)
model = OllamaLLM(model="llama3.1")
memory = ConversationBufferMemory()  # Initialize the memory
chain = prompt | model | memory  # Add memory to the chain

@app.route('/chat', methods=['POST'])
def generate():
    data = request.json
    user_input = data.get('user_input')
    
    if not user_input:
        return jsonify({"error": "No user input provided"}), 400

    # Generate the response
    response = chain.invoke({"question": user_input})
    
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
