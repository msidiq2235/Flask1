from flask import Flask, render_template, request

app = Flask(__name__)

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for form submission
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    feedback = request.form.get('feedback')
    return f"Hello, {name}! Thank you for your feedback. We will contact you at {email}."

if __name__ == '__main__':
    app.run(debug=True)
