import os
from werkzeug.utils import secure_filename
from supporting import get_files_names

from flask import Flask, request, jsonify, send_from_directory

from docx2pdf import convert

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/files', methods=["GET"])
def get_files():
    return jsonify({"files": get_files_names("files")})


@app.route('/update', methods=["POST"])
def upload_file():
    f = request.files['file']
    f.save(f'docx/{f.filename}')
    convert(f'docx/{f.filename}', f'pdf/{f.name}.pdf')

    # return jsonify({'message': 'File successfully uploaded'})
    return send_from_directory("pdf", f'{f.name}.pdf', as_attachment=True)


# curl -F "file=@1" -F "file=@2" http://127.0.0.1:5000/upload-multiple
@app.route('/upload-multiple', methods=["POST"])
def upload_multiple():
    files = request.files.getlist("file")
    print(files)
    for file in files:
        sec_name = secure_filename(file.filename)
        print(sec_name)
        file.save(f"files/{sec_name}")
    return jsonify({'message': 'Files successfully uploaded'})


@app.route("/get/<filename>", methods=["GET"])
def get_file(filename):
    return send_from_directory("files", filename, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
