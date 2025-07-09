# 🔍 Duplicate Value Checker (JSON Edition)

A simple yet powerful tool to identify duplicate entries inside a JSON-formatted file — using Python and a batch file for easy execution.

## 💡 What It Does

This project scans a JSON file (`find.txt`) for repeated values within a specified field, then lists those duplicates in `output.txt`. It’s perfect for quick data validation, especially when working with structured content, such as API responses or export files.

## 📁 Folder Contents

- `main.py` — Python script to parse JSON and check for duplicate values.
- `main.bat` — Batch file to execute the script and open the results.
- `find.txt` — JSON input file (array of objects).
- `output.txt` — Output file displaying duplicate values found.

## 📦 JSON Format Example

Your `find.txt` should contain JSON data in this structure:

``json
[
  {"name": "Alice"},
  {"ID": "1234"},
  {"PIN": "02380276823"},
  {"address": "USA"}
]``

## 🚀 How to Use

1. Put all files (`main.py`, `main.bat`, and `find.txt`) in one folder — name it anything you like.
2. Add your data to `find.txt` (JSON format, use Notepad++).
3. Double-click `main.bat` to run the tool.
4. After a moment, `output.txt` will automatically be created, and clicking this file will show any duplicate values found.

```🐍 Make sure Python is installed and added to your system's PATH.```

## 📄 Why Use This Tool?

- No extra software needed — just Python and Notepad++.
- Automatically create the output file for quick results.
- Great for simple list cleanups and validation tasks.

`## 👨‍💻 Created By

```**Tamim Rahman Riyad**```
