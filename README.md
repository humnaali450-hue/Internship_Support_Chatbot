# 🎓 Internship Support Chatbot

<p align="center">

**An AI-powered NLP chatbot designed to provide real-time support and answer common internship-related questions.**

</p>

<p align="center">

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python\&logoColor=white)](https://www.python.org/)
[![NLP](https://img.shields.io/badge/NLP-Natural%20Language%20Processing-orange)](https://en.wikipedia.org/wiki/Natural_language_processing)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-F7931E?logo=scikit-learn\&logoColor=white)](https://scikit-learn.org/)
[![NLTK](https://img.shields.io/badge/NLTK-NLP-green)](https://www.nltk.org/)
[![Gradio](https://img.shields.io/badge/Gradio-Interface-orange)](https://www.gradio.app/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-150458?logo=pandas\&logoColor=white)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-013243?logo=numpy\&logoColor=white)](https://numpy.org/)

</p>

---

## 📌 Project Overview

The **Internship Support Chatbot** is an NLP-based conversational system developed to assist interns with frequently asked questions related to their internship experience.

The chatbot uses **Natural Language Processing**, **TF-IDF vectorization**, and **cosine similarity** to understand user queries and retrieve the most relevant answer from an internship FAQ knowledge base.

A professional **Gradio web interface** allows users to interact with the chatbot in real time.

### 🎯 Objective

The main objective of this project is to:

* Automate responses to common intern questions
* Reduce repetitive support requests
* Provide instant access to internship information
* Demonstrate practical NLP and machine-learning techniques
* Provide a simple and professional conversational interface

---

## ✨ Features

* 🤖 FAQ-based AI chatbot
* 🧠 Natural Language Processing
* 🔤 Text preprocessing
* 📊 TF-IDF vectorization
* 🔎 Cosine similarity matching
* 💬 Automatic response generation
* 🛡️ Unknown-question / fallback handling
* 🌐 Interactive Gradio web interface
* 📈 Model evaluation
* 📋 Confusion matrix visualization
* 💾 Trained model and vectorizer persistence
* 📁 Structured and reusable project architecture

---

## 🛠️ Technologies Used

| Technology                                                                                                             | Purpose                                      |
| ---------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- |
| [Python](https://www.python.org/)                                                                                      | Core programming language                    |
| [Pandas](https://pandas.pydata.org/)                                                                                   | Data manipulation and processing             |
| [NumPy](https://numpy.org/)                                                                                            | Numerical operations                         |
| [Scikit-learn](https://scikit-learn.org/)                                                                              | Machine-learning and similarity calculations |
| [NLTK](https://www.nltk.org/)                                                                                          | Natural language preprocessing               |
| [TF-IDF](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html)       | Text feature extraction                      |
| [Cosine Similarity](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html) | Finding the most relevant FAQ                |
| [Joblib](https://joblib.readthedocs.io/)                                                                               | Saving and loading trained objects           |
| [Gradio](https://www.gradio.app/)                                                                                      | Web-based chatbot interface                  |
| [Matplotlib](https://matplotlib.org/)                                                                                  | Evaluation visualization                     |

---

## 🧠 How It Works

The chatbot follows a simple NLP retrieval pipeline:

```text
User Question
      │
      ▼
Text Preprocessing
      │
      ▼
TF-IDF Vectorization
      │
      ▼
Cosine Similarity
      │
      ▼
Find Most Relevant FAQ
      │
      ▼
Similarity Threshold Check
      │
 ┌────┴─────┐
 │          │
 ▼          ▼
Relevant   Unknown
Answer     Question
 │          │
 ▼          ▼
Response   Fallback
```

### 1. User Input

The user enters an internship-related question through the chatbot interface.

Example:

> How can I submit my internship report?

### 2. Text Preprocessing

The input is cleaned using NLP preprocessing techniques such as:

* Lowercasing
* Punctuation removal
* Number removal
* Stop-word removal
* Tokenization

### 3. TF-IDF Vectorization

The processed FAQ questions are converted into numerical vectors using **Term Frequency-Inverse Document Frequency (TF-IDF)**.

### 4. Similarity Matching

The chatbot calculates **cosine similarity** between the user's question and the questions stored in the FAQ dataset.

### 5. Response Selection

The FAQ with the highest similarity score is selected.

If the similarity score meets the predefined threshold, the corresponding answer is returned.

Otherwise, the chatbot provides a fallback response directing the intern to the appropriate support person or department.

---

## 🗂️ Project Structure

```text
Internship-Support-Chatbot/
│
├── 📁 data/
│   └── internship_faq.csv
│
│
├── 📁 src/
│   └── train_model.py
│
├── 📁 tests/
│   └── test_chatbot.py
│
├── 📁 notebooks/
│   └── internship_chatbot.ipynb
│
├── 📁 screenshots/
│   ├── Confusion Matrix.png
│   └── Interface.png
│
├── 📄 requirements.txt
├── 📄 README.md
├── 📄 .gitignore
└── 📄 run.py
```

---

# 🖥️ User Interface

The chatbot includes a professional web interface built with **Gradio**.

It provides:

* Clean conversational layout
* Internship-support categories
* User-friendly input box
* Real-time responses
* Example questions
* Clear conversation functionality

-----


## 💬 Example Questions

The chatbot can answer questions such as:

```text
How do I submit my internship report?

What are the internship working hours?

How can I contact my supervisor?

How many days of leave can I take?

When will I receive my internship certificate?

How is my internship performance evaluated?

What documents are required?

How can I contact HR?

When will I receive my stipend?
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Internship-Support-Chatbot.git
```

```bash
cd Internship-Support-Chatbot
```

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🚀 Running the Project

## Train the Model

```bash
python src/train_model.py
```

This creates the trained TF-IDF vectorizer and chatbot model inside the `models/` directory.

## Run the Chatbot

```bash
python run.py
```

The Gradio interface will then provide a local web address where the chatbot can be accessed.

---

# 📚 Dataset

The chatbot uses an internship FAQ dataset containing questions and answers related to areas such as:

* Internship reports
* Supervisors
* Working hours
* Attendance
* Leave
* Certificates
* Performance evaluation
* Required documents
* HR support
* Stipends
* Internship tasks
* Training
* Internship extensions
* Internship completion

Each FAQ contains:

```text
Question
Answer
Category
```

---

# 🔬 NLP Methodology

The project demonstrates a classical NLP information-retrieval approach rather than a generative large language model.

### Text Processing

```text
Raw Question
      ↓
Lowercase
      ↓
Remove Punctuation
      ↓
Remove Numbers
      ↓
Remove Stop Words
      ↓
Processed Text
```

### Feature Extraction

The processed questions are transformed into TF-IDF feature vectors.

### Similarity Measurement

Cosine similarity is used to determine how closely the user's question matches each FAQ question.

### Response Retrieval

The answer associated with the highest-scoring FAQ is returned when the similarity exceeds the defined threshold.

---

# 📈 Evaluation Metrics

The project evaluates chatbot performance using:

### Accuracy

Measures the percentage of test questions assigned to the correct category.

### Confusion Matrix

Shows the relationship between the expected and predicted FAQ categories.

---

# ⭐ Project Highlights

```text
✓ NLP-based chatbot
✓ TF-IDF text representation
✓ Cosine similarity matching
✓ FAQ knowledge base
✓ Fallback handling
✓ Model evaluation
✓ Confusion matrix
✓ Professional Gradio interface
✓ Modular project structure
```

---

## 📄 License

This project is intended for educational and portfolio purposes.
