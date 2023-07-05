# structuring_helper
This small python program was written to ease the correction of exercises handed in trough ilias, by students of a programming course. It creates valid eclipse project for all hand ins and splits into equal parts.

## Install
Prerequisits:
- Python
- Tkinter

```bash
pip install -r requirements.txt
```

## how to use it

```bash
python3 gui.py
```

With the first file dialog choose the folder containing the ilias download. Each submission should be in a folder. 

The second file dialog is used to choose the output path. This should be an empty folder where the structured output will be generated.

### To open the java submission in eclipse:
Open a eclipse workspace (preferably an empty one).

Import the projects with ``File -> Open Projects from File System``. Make sure to uncheck the top most project called ``java``.

