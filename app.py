from flask import Flask, request, jsonify
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone
from langchain_huggingface import HuggingFaceEmbeddings

app = Flask(__name__)

# Initialize Pinecone with the API key
pc = Pinecone(api_key="a6c11326-2437-43d7-9f84-ecc973c83a67")

# Connect to the existing Pinecone index
index = pc.Index("cve-index")

# Initialize the LLM with Groq API
llm = ChatGroq(
    model="llama3-70b-8192",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    api_key="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"
)

# Define a prompt template
template = """Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you do not know the answer.
{context}
Question: {question}
Helpful Answer:"""
QA_CHAIN_PROMPT = PromptTemplate.from_template(template)

# Create a retriever using the Pinecone vector store
db = PineconeVectorStore(
    index=index, # This should be a Pinecone index object, not the index name
    embedding=HuggingFaceEmbeddings()
)
retriever = db.as_retriever()

# Create a RetrievalQA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    chain_type_kwargs={"prompt": QA_CHAIN_PROMPT}
)

@app.route('/ask', methods=['POST'])
def ask_question():
    data = request.get_json()

    question = data.get("question", "")
    if not question:
        return jsonify({"error": "No question provided"}), 400
    
    try:
        response = qa_chain.invoke(question)
        return jsonify({"answer": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
