# 🛡️ Self-Healing RAG Pipeline

A production-ready **Self-Healing Retrieval-Augmented Generation (RAG) Pipeline** that allows users to upload PDF/TXT documents, ask questions, and receive grounded answers with citations, confidence scoring, and automatic query improvement.

🔗 **Live Demo:** https://self-healing-rag-pipeline-mk.streamlit.app/

---

## 🚀 Project Overview

Traditional RAG systems often fail when a user asks a vague or unclear question. They may retrieve weak context, hallucinate answers, or provide responses without confidence scores.

This project solves that problem using a **Self-Healing RAG Pipeline**.

When the system detects low retrieval confidence, it automatically performs healing actions such as:

* Query rewriting
* Retrieval retry
* Better question suggestions
* Grounding verification
* Confidence scoring
* Citation-based answer generation

---

## 🎯 Project Goal

The goal of this project is to build a reliable document-based AI assistant that can:

1. Understand uploaded documents
2. Retrieve relevant information
3. Detect weak retrieval
4. Improve the user query internally
5. Generate grounded answers
6. Show confidence score and citations
7. Suggest better questions when confidence is low

---

## ✨ Key Features

### 📄 Document Upload

* Upload PDF or TXT files
* Extract document text
* Process resumes, reports, notes, policies, and research documents

### 🔍 RAG-Based Question Answering

* Ask natural language questions
* Retrieve relevant document chunks
* Generate answers using LLMs
* Display source citations

### 🛡️ Self-Healing Mechanism

* Detects low-confidence retrieval
* Performs internal query rewriting
* Retries retrieval with improved query
* Generates better question suggestions for users

### 📊 Confidence Scoring

* Shows answer confidence percentage
* Helps users understand answer reliability
* Useful for evaluating AI-generated responses

### 💡 Suggested Better Questions

When confidence is low, the system suggests clearer user questions, helping improve retrieval quality.

Example:

```text
Original Question:
Which device uses more power?

Suggested Better Questions:
- Which appliance consumes the most electricity?
- Which device has the highest energy usage?
- What appliance runs continuously throughout the year?
```

---

## 🧠 How It Works

```text
User Uploads Document
        ↓
Text Extraction
        ↓
Document Chunking
        ↓
Embedding Generation
        ↓
Vector Search
        ↓
Confidence Check
        ↓
If Confidence is Low:
    → Rewrite Query
    → Retrieve Again
    → Suggest Better Questions
        ↓
Answer Generation
        ↓
Grounding Verification
        ↓
Final Answer + Confidence + Citations
```

---

## 🆚 Normal RAG vs Self-Healing RAG

### Normal RAG

```text
Question → Retrieve → Generate Answer
```

If retrieval is poor, the answer may be wrong.

### Self-Healing RAG

```text
Question → Retrieve → Check Confidence → Rewrite Query → Retrieve Again → Verify → Answer
```

This makes the system more reliable and transparent.

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit**
* **FAISS**
* **Sentence Transformers**
* **Cross Encoder Reranker**
* **Groq LLM**
* **PyPDF**
* **Pandas**
* **NumPy**

---

## 📌 Example Use Cases

### Resume Analysis

Upload a resume and ask:

```text
Who is this resume about?
```

Example answer:

```text
Karthik Yadav M
```

### Report Analysis

Upload an energy report and ask:

```text
Which appliance consumes the most household electricity?
```

Example answer:

```text
Air Conditioning Unit
```

### Document Q&A

Upload any PDF/TXT file and ask:

```text
What are the main points in this document?
```

---

## 📷 App Screens

The deployed Streamlit app includes:

* File uploader
* Question input box
* AI-generated answer
* Confidence score
* Healing actions
* Suggested better questions
* Source citations

---

## 📁 Recommended Project Structure

```text
Self-Healing-RAG-Pipeline/
│
├── README.md
├── requirements.txt
├── app.py
├── rag_pipeline.py
├── healing.py
├── vector_store.py
├── document_loader.py
├── logger.py
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Karthikyadav611/Self-Healing-RAG-Pipeline.git
```

Move into the project folder:

```bash
cd Self-Healing-RAG-Pipeline
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit app:

```bash
streamlit run app.py
```

---

## 🔐 Environment Variables

Create a `.env` file or use Streamlit Secrets.

Example:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Do not push `.env` files or API keys to GitHub.

---

## 🚀 Deployment

This project is deployed using **Streamlit Community Cloud**.

Live app:

```text
https://self-healing-rag-pipeline-mk.streamlit.app/
```

To deploy:

1. Push project files to GitHub
2. Go to Streamlit Community Cloud
3. Connect GitHub repository
4. Select `app.py` as the main file
5. Add API key in Streamlit Secrets
6. Deploy

---

## 🧪 Sample Test Questions

### Resume

```text
Who is this resume about?
What skills are mentioned in the resume?
What projects are listed?
What is the candidate's email?
```

### Report

```text
Which appliance consumes the most electricity?
What is the main topic of this report?
What are the key findings?
```

### General Document

```text
Summarize this document.
What are the important points?
What conclusion does the document provide?
```

---

## 📈 Future Improvements

* Hybrid Search using BM25 + Vector Search
* Multi-document support
* LangGraph-based agent workflow
* User feedback learning loop
* Evaluation dashboard
* Persistent vector database
* Chat history support
* PDF page-level citations
* Authentication system

---

## 🎓 Skills Demonstrated

This project demonstrates practical experience in:

* Generative AI
* Retrieval-Augmented Generation
* LLM Integration
* Vector Databases
* Semantic Search
* Query Rewriting
* Reranking
* Prompt Engineering
* Streamlit Deployment
* AI Reliability
* Document Intelligence

---

## 👨‍💻 Author

**Karthik Yadav M**

* GitHub: https://github.com/Karthikyadav611
* LinkedIn: https://linkedin.com/in/karthikyadavm
* Portfolio: https://my-portfolio-mky.vercel.app

---

## ⭐ Support

If you found this project useful, consider giving it a star on GitHub.
