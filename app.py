from flask import Flask, render_template, request


app: Flask = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_file():
    file = request.files["file"]
    print(type(file))

    if not file:
        return "No File Selected."

    file.save(f"uploads/idk_the_name")
    return "File Saved"


if __name__ == "__main__":
    app.run(debug=True)
