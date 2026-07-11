"""
predict.py
----------
Uses the model you already trained (model.joblib) to guess the category
of any new piece of text you type in.

HOW TO RUN THIS FILE:
    python predict.py

You must run train.py first, at least once, to create model.joblib.
"""

import joblib

print("Loading trained model...")
saved = joblib.load("model.joblib")
pipeline = saved["pipeline"]
categories = saved["categories"]

print("\nType some text and press Enter to see the predicted category.")
print("Type 'quit' to exit.\n")

while True:
    text = input("Your text: ")
    if text.strip().lower() == "quit":
        break
    if not text.strip():
        continue
    prediction = pipeline.predict([text])[0]
    print(f"  -> Predicted category: {categories[prediction]}\n")
