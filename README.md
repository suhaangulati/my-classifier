# My Document Classifier

A tiny project that teaches a computer to read text and guess its category
(space / hockey / computer graphics / politics), using free built-in data.
No data collection needed — it's all explained below, step by step.

## What's in this folder

- `train.py` — trains the model (run this first)
- `predict.py` — lets you type text and see what category it guesses
- `requirements.txt` — list of tools this project needs
- `model.joblib` — created automatically after you run train.py (not in GitHub, see `.gitignore`)

## Part 1 — Install what you need (one-time setup)

1. **Install Python** (if you don't have it): go to https://python.org/downloads
   and install the latest version. During install on Windows, check the box
   "Add Python to PATH".
2. **Install Git**: go to https://git-scm.com/downloads and install it.
3. **Make a free GitHub account**: go to https://github.com/signup if you
   don't have one yet.

Check both installed correctly by opening a terminal (Command Prompt,
PowerShell, or Terminal app) and typing:
```bash
python --version
git --version
```
Both should print a version number.

## Part 2 — Run the project on your computer

1. Unzip this project folder somewhere, e.g. your Desktop.
2. Open a terminal and go into that folder:
   ```bash
   cd Desktop/beginner-classifier
   ```
3. Install the required tools:
   ```bash
   pip install -r requirements.txt
   ```
4. Train the model (this downloads example data automatically):
   ```bash
   python train.py
   ```
   You'll see progress messages, then an accuracy report. This takes a
   minute or two.
5. Try it out:
   ```bash
   python predict.py
   ```
   Type any sentence (e.g. "the rocket launched into orbit") and press
   Enter to see the predicted category. Type `quit` to stop.

## Part 3 — Put your project on GitHub

1. Go to https://github.com/new
2. Give it a name (e.g. `document-classifier`), leave everything else
   as default (do **not** check "Add a README" since you already have one),
   and click **Create repository**.
3. GitHub will show you a page with a repository URL, like:
   `https://github.com/your-username/document-classifier.git`
   Copy it.
4. Back in your terminal, inside the project folder, run these commands
   one at a time:
   ```bash
   git init
   git add -A
   git commit -m "My first document classifier"
   git branch -M main
   git remote add origin https://github.com/your-username/document-classifier.git
   git push -u origin main
   ```
   (Replace the URL in the `git remote add` line with the one you copied.)
5. GitHub may ask you to log in — follow the prompts. Once it's done,
   refresh your GitHub repository page in the browser. Your files are
   now live at:
   `https://github.com/your-username/document-classifier`
   **That's your GitHub link.**

## What is this actually doing? (plain English)

- The computer can't read words, only numbers. **TF-IDF** is just a way
  of turning each piece of text into a list of numbers based on which
  words appear and how important they are.
- **Logistic Regression** is a simple, well-known method for using those
  numbers to guess a category.
- "Training" means showing the computer thousands of examples that
  already have the correct answer labeled, so it can learn the pattern.
- "Testing" means checking its guesses against examples it has never
  seen, to see how well it actually learned.

## Changing this to your own topic later

Right now it guesses between space / hockey / computer graphics /
politics because that's free, ready-made data. Once you decide what you
actually want to classify (e.g. spam emails, product reviews), replace
the data-loading part of `train.py` with your own text and labels —
happy to help with that when you're ready.
