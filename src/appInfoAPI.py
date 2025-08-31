from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api/app-info", methods=["GET"])
def app_info():
    data = {
        "name": "My Cool App",
        "icon_url": "https://example.com/icon.png",
        "website_url": "https://mycoolapp.com",
        "redirect_url": "https://mycoolapp.com/redirect"
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)