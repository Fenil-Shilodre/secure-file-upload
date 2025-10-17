# Secure File Upload Web App

A simple and secure file upload system demonstrating Software Development Security (SDS) principles.

## Features

- File type validation (.png, .jpg, .jpeg, .pdf)
- File size restriction (max 2MB)
- Secure filename sanitization using `secure_filename()`
- Randomized filenames to prevent overwriting
- Safe upload folder (no code execution possible)

## Tech Stack

- Python (Flask)
- HTML, CSS
- Werkzeug for secure file handling

## INSTALLATION STEPS:
-----------------------------------------------------------
1️⃣  Make sure Python 3.x is installed.

2️⃣  Install Flask:
     pip install flask

3️⃣  Save this file as: app.py

4️⃣  Run the app:
     python app.py

5️⃣  Open your browser and go to:
     http://127.0.0.1:5000
