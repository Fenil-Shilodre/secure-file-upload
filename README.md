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

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/secure-file-upload.git
   ```
