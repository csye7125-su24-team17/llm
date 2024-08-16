# LLM-Powered RAG-Driven CVE Data Retrieval and Question-Answering Application

## Overview

This project is a cutting-edge application that leverages the power of Large Language Models (LLMs) and Retrieval-Augmented Generation (RAG) to provide intelligent querying and information retrieval from a vector database of Common Vulnerabilities and Exposures (CVE). The system is designed to run on Kubernetes infrastructure and is secured via HTTPS. Using a combination of LangChain, Hugging Face, Pinecone, and the LLaMA model, this application delivers precise answers to CVE-related questions, making it an essential tool for cybersecurity experts and developers.

## Features

- **RAG-Driven**: Combines retrieval of relevant documents with generative capabilities of LLMs for accurate responses.
- **LLM Integration**: Powered by the LLaMA model, offers state-of-the-art language understanding.
- **Vector Database**: Utilizes Pinecone for efficient and scalable vector storage and similarity search.
- **Secure and Scalable**: Designed to be deployed on Kubernetes, ensuring robust and secure operations.

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/csye7125-su24-team17/llm.git

cd llm
```
### 2. Create and Activate Python Virtual Environment
```bash
conda create -n env_langchain1 python=3.10
conda activate env_langchain1
```
### 3. Install Required Packages
```bash
# Install PyTorch and related packages
conda install pytorch torchvision torchaudio cpuonly -c pytorch

# Install Hugging Face and LangChain packages
pip install transformers
pip install sentence-transformers
pip install langchain langchain_community langchain-huggingface langchain_experimental langchainhub

# Install Pinecone and Groq packages
pip install pinecone-client
pip install groq
pip install langchain_pinecone
pip install langchain_groq

# Install Jupyter Notebook
conda install jupyter

```
### 4. Verify Installation
To ensure all packages are installed correctly, run the following in a Jupyter Notebook:
```bash
import torch
import transformers
import sentence_transformers
import langchain

print("PyTorch version:", torch.__version__)
print("Transformers version:", transformers.__version__)
print("Sentence Transformers version:", sentence_transformers.__version__)
print("LangChain version:", langchain.__version__)

```
### 5. Running the Application
Start Jupyter Notebook:
```bash
jupyter notebook
```
Open the notebook and execute the cells in sequence to initialize the Pinecone vector store, embed the CVE documents, and interact with the LLM to retrieve answers based on the CVE data.  

## Conclusion
This project exemplifies the synergy between advanced language models and modern retrieval techniques to create an intelligent, efficient, and secure solution for querying and analyzing CVE data. It serves as a valuable tool for cybersecurity professionals, developers, and researchers, providing quick, reliable, and insightful answers to complex security questions. It represents a significant step forward in utilizing AI for enhanced cybersecurity intelligence.
