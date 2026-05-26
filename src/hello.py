from flask import Flask, jsonify
import os

app = Flask(__name__)

COUNT_FILE = "count.txt"

def get_count():
    if not os.path.exists(COUNT_FILE):
        return 0
    with open(COUNT_FILE, "r") as f:
        try:
            return int(f.read().strip())
        except ValueError:
            return 0

def increment_count():
    count = get_count() + 1
    with open(COUNT_FILE, "w") as f:
        f.write(str(count))
    return count

@app.route("/api/hello", methods=["GET"])
def hello():
    count = increment_count()
    return jsonify({
        "message": "Hello Spencer",
        "status": "success",
        "counter": count
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5556, debug=False)