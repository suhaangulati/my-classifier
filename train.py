"""
train.py
--------
This script teaches a computer to read a short piece of text and guess
which category it belongs to. Example categories used here: space,
hockey, computer graphics, and politics/guns.

You don't need to find your own data - this script downloads a free,
ready-made dataset (called "20 Newsgroups") the first time you run it.
That download needs an internet connection on YOUR computer (not this chat).

HOW TO RUN THIS FILE:
    python train.py

WHAT HAPPENS WHEN YOU RUN IT:
    1. It downloads ~4 categories of old newsgroup posts (a classic,
       free text dataset used for learning).
    2. It splits the posts into a "practice set" and a "quiz set".
    3. It turns the words into numbers a computer can understand (TF-IDF).
    4. It trains a simple model (Logistic Regression) on the practice set.
    5. It checks how well the model does on the quiz set and prints a report.
    6. It saves the trained model to a file called model.joblib, so
       predict.py can use it later without retraining.
"""

from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
import joblib

# Step 1: pick which categories to classify between.
# You can change these to any of the 20 available categories later.
CATEGORIES = [
    "sci.space",           # space
    "rec.sport.hockey",    # hockey
    "comp.graphics",       # computer graphics
    "talk.politics.guns",  # politics
]

print("Step 1/5: Downloading example data (first run only)...")
train_data = fetch_20newsgroups(
    subset="train", categories=CATEGORIES, remove=("headers", "footers", "quotes")
)
test_data = fetch_20newsgroups(
    subset="test", categories=CATEGORIES, remove=("headers", "footers", "quotes")
)
print(f"Got {len(train_data.data)} training posts and {len(test_data.data)} test posts.")

# Step 2: build a pipeline that turns text into numbers, then classifies it.
print("Step 2/5: Building the model...")
pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(lowercase=True, stop_words="english")),
    ("clf", LogisticRegression(max_iter=1000)),
])

# Step 3: train (this is the "learning" part).
print("Step 3/5: Training...")
pipeline.fit(train_data.data, train_data.target)

# Step 4: check how good it is on posts it has never seen before.
print("Step 4/5: Evaluating...")
predictions = pipeline.predict(test_data.data)
print(classification_report(test_data.target, predictions, target_names=test_data.target_names))

# Step 5: save the trained model so predict.py can reuse it.
print("Step 5/5: Saving model to model.joblib ...")
joblib.dump({"pipeline": pipeline, "categories": test_data.target_names}, "model.joblib")
print("Done! You can now run: python predict.py")
