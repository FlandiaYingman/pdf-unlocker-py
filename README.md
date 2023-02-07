# PDF Unlocker Python

Unlocks PDFs with edit-protection.

Note that this project should only be used for unlocking user's own PDF documents the password of which is forgotten.
The author and software have no liability for any consequences.

## Usage (Executable)

Drag & drop any files or folders onto the executable (`pdf-unlocker.exe`). The files or the files in the folder
(recursively) will then be unlocked.

## Usage (Python)

Prerequisites:

- Python 3.11 (or above)
- Poetry

To run the software, install the dependencies first.

```shell
poetry install --without dev
```

Next, the environment is ready. You can run the program by running the following command.

```shell
poetry run main.py <files/folders...>
```

Where `<files/folders...>` are PDF files or folders which contain PDF files (will search recursively).

## Build (Executable)

Prerequisites:

- Python 3.11 (or above)
- Poetry
- PowerShell (PowerShell 7 is tested. Not sure whether other version works)

In order to build the software as an executable, just run the script `./build.ps1` with PowerShell. The executable will
then appear in `./dist/` folder if the build process is successful.