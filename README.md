# AG News Text Classification 📰

A simple, end-to-end NLP pipeline that classifies news headlines into four
categories — **World**, **Sports**, **Business**, and **Sci/Tech** — using
TF-IDF features and a Logistic Regression classifier.

## 📓 Notebook

[`document_classifier.ipynb`](document_classifier.ipynb)

## 🧠 What it does

1. Loads the [AG News dataset](https://huggingface.co/datasets/fancyzhx/ag_news)
2. Splits data into train/test sets (dataset ships pre-split)
3. Vectorizes text with `TfidfVectorizer` (unigrams + bigrams)
4. Trains a `LogisticRegression` classifier
5. Evaluates accuracy and per-class precision/recall/F1
6. Runs predictions on brand-new, unseen headlines
7. Saves the trained model with `joblib`

## 📊 Results

Run the notebook top to bottom to fill this in with real numbers, printed
automatically in section 5.

| Metric   | Score |
| -------- | ----- |
| Accuracy | *run notebook to see* |

## 🛠 Tech stack

- Python
- Hugging Face `datasets`
- scikit-learn (TF-IDF, Logistic Regression, Pipeline)
- Jupyter

## 📄 Dataset

**AG News Dataset** — four news categories:

- 🌍 World
- ⚽ Sports
- 💼 Business
- 💻 Sci/Tech

Each record contains a News Title + Description (combined as `text`) and a
Category Label.

## Setup

```bash
python -m venv venv
source venv/bin/activate   # on Windows: venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook document_classifier.ipynb
```

Then click **Run All**. The dataset downloads automatically the first time
— no manual data collection needed.
