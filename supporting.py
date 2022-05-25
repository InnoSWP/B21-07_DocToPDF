import os
from docx2pdf import convert


def get_files_names(folder: str) -> [str]:
    return os.listdir(folder)


if __name__ == '__main__':
    convert('files/123.docx', "output.pdf")
    print(get_files_names("files"))
