import io
import os
import subprocess
import tempfile

from werkzeug.utils import secure_filename
from flask import Flask, request, jsonify, send_file, render_template

app = Flask(__name__)

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
            subprocess.run(
                ["soffice", "--headless", "--convert-to", "pdf", docx.name, "--outdir", os.path.dirname(pdf.name)])
            pdf = open(docx.name[:-5] + ".pdf", "rb")
            mem = io.BytesIO(pdf.read())
            mem.seek(0)
            return send_file(mem, as_attachment=True, attachment_filename=f.name[:-5] + ".pdf")
        finally:
            docx.close()
            os.remove(docx.name[:-5] + ".pdf")
            
@app.route('/api/convertDocx', methods=["POST"])
def upload_file():
    f = request.files['file']
    docx = tempfile.NamedTemporaryFile(suffix=".docx", delete=True)
    try:
        pdf = open(docx.name[:-5] + ".pdf", "w")
        pdf.close()
        f.save(docx)
        subprocess.run(
            ["soffice", "--headless", "--convert-to", "pdf", docx.name, "--outdir", os.path.dirname(pdf.name)])
        pdf = open(docx.name[:-5] + ".pdf", "rb")
        mem = io.BytesIO(pdf.read())
        mem.seek(0)
        return send_file(mem, as_attachment=True, attachment_filename=f.name[:-5] + ".pdf")
    finally:
        docx.close()
        os.remove(docx.name[:-5] + ".pdf")


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
    app.run(debug=True, port=5000)
