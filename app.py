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
    # Get the PORT and HOST from environment variables
    port = int(os.environ.get("PORT", 5000))  # Default to 5000 if not set
    host = os.environ.get("HOST", "0.0.0.0")  # Default to 0.0.0.0 if not set

    app.run(host=host, port=port)
