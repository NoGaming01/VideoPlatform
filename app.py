from flask import Flask, render_template, request, url_for, Response
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage


app: Flask = Flask(__name__)


@app.route('/')
def index() -> Response:
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_file() -> str:
    file: FileStorage = request.files["file"]

    if not file:
        return "No File Selected."

    file.save(f"uploads/{secure_filename(file.filename)}")
    return "Video got uploaded."


@app.route("/user/<username>")
def profile(username: str) -> str:
    return f"{username}'s profile."


with app.test_request_context():
    print(url_for("index"))
    print(url_for("profile", username="Skele"))


if __name__ == "__main__":
    app.run(debug=True)
