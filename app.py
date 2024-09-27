from flask import Flask, render_template
import os

app = Flask(__name__)

# Route to serve the HTML page
@app.route("/")
def home():
    return render_template('index.html')

@app.route('/chatbot.html')
def chatbot():
    return render_template('chatbot.html')

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/onboard.html')
def onboard():
    return render_template('onboard.html')

if __name__ == "__main__":
    app.run(debug=True)  # Set debug=True for development
