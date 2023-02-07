import sys
from pathlib import Path

import pikepdf


def unlock_pdf(path):
    print(f"Unlocking PDF '{path}'...")
    try:
        pdf = pikepdf.open(path, allow_overwriting_input=True)
        for page in pdf.pages:
            page.get
        pdf.save()
        print(f"Unlocked PDF '{path}'.")
    except pikepdf.PasswordError or pikepdf.PdfError or IOError:
        print(f"Error on unlocking PDF '{path}'!")


def main():
    for p in sys.argv[1:]:
        path = Path(p)
        if path.is_dir():
            for sub_path in path.rglob('*.pdf'):
                unlock_pdf(sub_path)
        else:
            unlock_pdf(path)


if __name__ == '__main__':
    main()
