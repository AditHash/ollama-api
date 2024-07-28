# llava
import base64
from io import BytesIO
from flask import Flask, request, jsonify
from PIL import Image
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

def convert_to_base64(pil_image):
    """
    Convert PIL images to Base64 encoded strings

    :param pil_image: PIL image
    :return: Re-sized Base64 string
    """
    buffered = BytesIO()
    pil_image.save(buffered, format="PNG")  # JPEG, JPG, PNG
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return img_str

@app.route('/image-chat', methods=['POST'])
def generate_with_image():
    if 'image_input' not in request.files:
        return jsonify({"error": "No image input provided"}), 400

    image_file = request.files['image_input']
    user_input = request.form.get('user_input')

    if not user_input:
        return jsonify({"error": "No user input provided"}), 400

    # Process the image
    pil_image = Image.open(image_file)
    image_b64 = convert_to_base64(pil_image)

    # Generate the response with image context
    llm_with_image_context = model.bind(images=[image_b64])
    chain_with_image_context = prompt | llm_with_image_context | memory
    response = chain_with_image_context.invoke({"question": user_input})

    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
