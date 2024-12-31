from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/questions', methods=['GET'])
def get_questions():
    questions = [
        {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Madrid"], "answer": "Paris"},
        {"question": "Which language is used for web development?", "options": ["Python", "JavaScript", "C++", "Java"], "answer": "JavaScript"},
        {"question": "What is 2 + 2?", "options": ["3", "4", "5", "6"], "answer": "4"}
    ]
    return jsonify(questions)

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Run Flask app on a different port
