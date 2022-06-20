import io
import os
import subprocess
import tempfile




import json

from werkzeug.utils import secure_filename
from flask import Flask, request, jsonify, send_file, render_template

app = Flask(__name__)


def check_file_extention(file_name: str) -> bool:
    allowed_extentions = app.config["UPLOAD_EXTENSIONS"]
    extention = file_name[file_name.rfind('.'):]
    return extention in allowed_extentions


@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        f = request.files['file']
        docx = tempfile.NamedTemporaryFile(suffix=".docx", delete=True)
        try:
            pdf = open(docx.name[:-5] + ".pdf", "w")
            pdf.close()
            f.save(docx)
            docx.flush()
            subprocess.run(
                ["soffice", "--headless", "--convert-to", "pdf", docx.name, "--outdir", os.path.dirname(pdf.name)])
            try:
                pdf = open(docx.name[:-5] + ".pdf", "rb")
            except FileNotFoundError as e:
                return {"message": "Document conversion error"}, 500
            mem = io.BytesIO(pdf.read())
            mem.seek(0)
            if mem.getbuffer().nbytes == 0:
                return {"message": "Document conversion error"}, 500
            return send_file(mem, as_attachment=True, attachment_filename=f.filename[:-5] + ".pdf")
        finally:
            docx.close()
            os.remove(docx.name[:-5] + ".pdf")


@app.route('/api/convertDocx', methods=["POST"])
def upload_file():
    args = request.args
    if "apiKey" not in args:
        return {"message": "Wrong api key"}, 403

    if args["apiKey"] != app.config["apiKey"]:
        return {"message": "Wrong api key"}, 403

    f = request.files['file']

    if not check_file_extention(f.filename):
        return {"message": "Document conversion error"}, 500

    docx = tempfile.NamedTemporaryFile(suffix=".docx", delete=True)
    try:
        pdf = open(docx.name[:-5] + ".pdf", "w")
        pdf.close()
        f.save(docx)
        docx.flush()
        subprocess.run(
            ["soffice", "--headless", "--convert-to", "pdf", docx.name, "--outdir", os.path.dirname(pdf.name)])
        try:
            pdf = open(docx.name[:-5] + ".pdf", "rb")
        except FileNotFoundError as e:
            return {"message": "Document conversion error"}, 500
        mem = io.BytesIO(pdf.read())
        mem.seek(0)
        if mem.getbuffer().nbytes == 0:
            return {"message": "Document conversion error"}, 500
        return send_file(mem, as_attachment=True, attachment_filename=f.filename[:-5] + ".pdf")
    finally:
        docx.close()
        os.remove(docx.name[:-5] + ".pdf")


@app.route("/test", methods=["GET", "POST"])
def test():
    args = request.args
    if "apiKey" not in args:
        return {"message": "Wrong api key"}, 403

    if app.config["apiKey"] == args["apiKey"]:
        return "Access permitted"
    else:
        return "Access denied"
    return request.args


# curl -F "file=@1" -F "file=@2" http://127.0.0.1:5000/upload-multiple
@app.route('/api/upload-multiple', methods=["POST"])
def upload_multiple():
    files = request.files.getlist("file")
    print(files)
    for file in files:
        sec_name = secure_filename(file.filename)
        print(sec_name)
        file.save(f"files/{sec_name}")
    return jsonify({'message': 'Files successfully uploaded'})


if __name__ == '__main__':
    with open("config.json") as config_file:
        config_data = json.load(config_file)
    app.config.update(config_data)
    print(app.config)
    # UPLOAD_EXTENSIONS
    print("Api key:", app.config["apiKey"])
    app.run(debug=True, port=5000)
