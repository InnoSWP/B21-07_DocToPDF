import os
from werkzeug.utils import secure_filename
from supporting import get_files_names, convert

from flask import Flask, request, jsonify, send_from_directory

from time import time

# from docx2pdf import convert

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
    a = time()
    convert(f'docx/{f.filename}', f'pdf/')
    print("Consumed time: ", time() - a)
    # return jsonify({'message': 'File successfully uploaded'})
    # os.system(f"open {f.name}.pdf")
    filename_without_extention = f.filename.split('.')[0]
    return send_from_directory("pdf", f'{filename_without_extention}.pdf', as_attachment=True)


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

if __name__ == '__main__':
    app.run(debug=True, port=5000)
