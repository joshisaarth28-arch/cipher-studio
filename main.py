from flask import Flask, render_template, request
import itertools

app = Flask(__name__)

# A small sample dictionary (In production, load a larger .txt wordlist)
WORD_DICTIONARY = ["cat", "act", "dog", "god", "python", "luxury", "cipher"]

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
    # This serves your luxury introduction page
    return render_template('index.html')

@app.route('/word-unscrambler', methods=['GET', 'POST'])
def word_tool():
    results = None
    if request.method == 'POST':
        user_input = request.form.get('letters', '')
        results = solve_words(user_input)
    return render_template('word.html', results=results)

@app.route('/google4b3180399882f44e.html')
def google_verify():
    return "google-site-verification: google4b3180399882f44e.html"
    
import os

if __name__ == '__main__':
    # This line automatically reads what port the cloud server requires
    port = int(os.environ.get("PORT", 5000))
    # This tells the server to listen to all public internet requests on that port
    app.run(host='0.0.0.0', port=port)
