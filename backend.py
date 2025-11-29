# run this backend as 1 workers 1 threads
from flask import Flask, request, jsonify
from flask import send_file
import base64
import threading
import time

app = Flask(__name__)

try:
    html = open("index_patched.html", "rb").read().decode("utf-8")
    print("Using patched index.html")
except FileNotFoundError:
    html = open("index.html", "rb").read().decode("utf-8")
    print("Using original index.html")

# routine for / GET
@app.route("/", methods=["GET"])
def index():
    return html, 200

# routine for /index.html GET
# for restoring original HTML access
@app.route("/index.html", methods=["GET"])
def serve_index():
    return send_file("index.html"), 200

# routine for *.js
@app.route("/<path:filename>.js", methods=["GET"])
def serve_js(filename):
    return send_file(f"{filename}.js"), 200

# routine for *.css
@app.route("/<path:filename>.css", methods=["GET"])
def serve_css(filename):
    return send_file(f"{filename}.css"), 200

# routine for *.png
@app.route("/<path:filename>.png", methods=["GET"])
def serve_png(filename):
    return send_file(f"{filename}.png"), 200

# routine for /update_html POST
@app.route("/update_html", methods=["POST"])
def update_html():
    data = request.get_json()
    new_html_base64 = data["html_base64"]
    global html; html = base64.b64decode(new_html_base64).decode("utf-8")
    print("HTML content updated !")
    return jsonify({"status": "success"}), 200

def save_html_worker():
    while True:
        time.sleep(60)  # Save every 60 seconds
        open("index_patched.html", "wb").write(html.encode("utf-8"))
        print("Patched HTML content saved to index_patched.html")

threading.Thread(target=save_html_worker, daemon=True).start()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)