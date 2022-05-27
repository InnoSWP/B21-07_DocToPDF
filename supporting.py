import os
# from docx2pdf import convert
from subprocess import run


def get_files_names(folder: str) -> [str]:
    return os.listdir(folder)

def convert(fr: str, to_dir: str):
    process_convert = run(["soffice", "--headless", "--convert-to", "pdf", fr, "--outdir", to_dir])
    # soffice --headless --convert-to pdf 123.docx
    # soffice --headless --convert-to pdf 123.docx --outdir pdfs/

if __name__ == '__main__':
    convert('api_test/123.docx', "pdfs/")
    # print(get_files_names("files"))
