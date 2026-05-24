from flask import Flask, render_with_template, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # The main landing page welcoming visitors
    return render_template('index.html')

@app.route('/lab')
def lab():
    # The resource hub for Class 3 to 10 students
    return render_template('lab.html')

if __name__ == '__main__':
    app.run(debug=True)