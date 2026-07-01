import os
from flask import Flask, render_template, request

app = Flask(__name__)

# A simple starter word dictionary
WORD_DICTIONARY = ["cat", "act", "dog", "god", "python", "luxury", "cipher", "matrix", "unscramble"]

def solve_words(letters):
    letters = letters.lower().strip()
    sorted_input = sorted(letters)
    matches = []
    for word in WORD_DICTIONARY:
        if sorted(word) == sorted_input:
            matches.append(word)
    return matches

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/word-unscrambler', methods=['GET', 'POST'])
def word_tool():
    results = None
    if request.method == 'POST':
        user_input = request.form.get('letters', '')
        results = solve_words(user_input)
    return render_template('word.html', results=results)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
