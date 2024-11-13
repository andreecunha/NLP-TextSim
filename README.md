# TextSimApp: Semantic Textual Similarity Tool

**TextSimApp** is a natural language processing (NLP) application designed to assess semantic similarity between sentences in Portuguese. The project integrates rule-based and machine learning approaches, culminating in an application that suggests answers to user queries by analyzing a dataset of frequently asked questions.

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Key Features](#key-features)
3. [System Workflow](#system-workflow)
4. [Installation Guide](#installation-guide)


---

## Project Overview

This project explores the task of **Semantic Textual Similarity (STS)**, which involves quantifying the similarity of meanings between two text sequences. The application uses:
- **Rule-based approaches:** Metrics like Jaccard and Cosine Similarity.
- **Machine learning models:** Linear regression and Transformer-based models.
- **Dataset:** The ASSIN and ASSIN2 datasets, as well as a translated FAQ dataset.

The developed application provides a search mechanism to match user queries with similar FAQ entries and their respective answers.

---

## Key Features

1. **Data Preprocessing:**
   - Lowercasing and lemmatization of sentences.
   - Conversion of sentences into feature vectors using tokenizers (Count and Tfid).

2. **Similarity Analysis:**
   - Rule-based metrics: Jaccard and Cosine Similarity.
   - Machine learning: Linear regression and Transformer models.

3. **Application Development:**
   - Transforms user queries into vectors and matches them with the FAQ dataset.
   - Returns the closest match and a corresponding answer.

4. **Evaluation Metrics:**
   - Pearson Correlation and Mean Squared Error (MSE) for performance evaluation.

---

## System Workflow

1. **Data Preparation:**
   - Utilize the ASSIN and ASSIN2 datasets for training and evaluation.
   - Translate the FAQ dataset into Portuguese.

2. **Feature Engineering:**
   - Extract features like token overlap, similarity scores, and grammatical elements.

3. **Model Training:**
   - Implement and train Linear Regression and Transformer models.

4. **Application Development:**
   - Build the query matching system using pre-trained Transformer embeddings.

5. **Evaluation:**
   - Validate the models using ASSIN and ASSIN2 test datasets.

---

## Installation Guide

1. Clone the repository:
   ```bash
   git clone https://github.com/andreecunha/NLP-TextSim.git
