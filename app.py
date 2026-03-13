from flask import Flask, render_template, url_for

app = Flask(__name__)

# Basic routes with strict_slashes=False to prevent 404s on trailing slashes
# Added /index for broader compatibility
@app.route("/", strict_slashes=False)
@app.route("/index", strict_slashes=False)
def home():
    return render_template("index.html")

@app.route("/dashboard", strict_slashes=False)
@app.route("/dashboard/", strict_slashes=False)
def dashboard():
    return render_template("dashboard.html")

@app.route("/story", strict_slashes=False)
@app.route("/story/", strict_slashes=False)
def story():
    return render_template("story.html")

# Error handler for 404 to provide a better user experience
@app.errorhandler(404)
def page_not_found(e):
    return render_template("index.html"), 404

if __name__ == "__main__":
    app.run(debug=True)