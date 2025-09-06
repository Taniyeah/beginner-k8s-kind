from flask import Flask
import os


app = Flask(__name__)


@app.get("/")
def home():
name = os.getenv("GREETING_NAME", "Beginner")
return f"Hello, {name}!\n"


@app.get("/healthz")
def health():
return "ok\n", 200


@app.get("/ready")
def ready():
# pretend we need a second to warm up on first start
return "ready\n", 200


if __name__ == "__main__":
app.run(host="0.0.0.0", port=8080)