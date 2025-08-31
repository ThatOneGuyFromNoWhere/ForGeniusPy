
app = Flask(__name__)

@app.route("/api/app-info", methods=["GET"])
def app_info():
    data = {
        "name": "Lyrics Genius",
        "icon_url": "https://cdn.jsdelivr.net/gh/ThatOneGuyFromNoWhere/assets/genius-icon.png",  # Use your own or Genius logo URL
        "website_url": "https://genius.com",
        "redirect_url": "https://genius.com/oauth/authorize"
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)