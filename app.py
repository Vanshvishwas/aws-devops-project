from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def home():
    return f"""
    <h1>AWS DevOps Demo</h1>
    <p>Application: Container Demo</p>
    <p>Version: 2.0</p>
    <p>Environment: Development</p>
    <p>Hostname: {socket.gethostname()}</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)