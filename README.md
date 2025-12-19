# API Fuzz

API Fuzz is a lightweight API endpoint fuzzing tool written in Python.  
It is designed for learning, security testing, and bug bounty reconnaissance.

The tool brute‑forces API paths using a user‑supplied wordlist and identifies
valid endpoints by filtering out non‑useful responses such as HTTP 404.

---

## Features

- User‑supplied target URL
- Custom wordlist support
- Skips 404 responses automatically
- Detects JSON and HTML responses
- Clean and readable output
- Beginner‑friendly and easy to modify

---

## Usage

```bash
python3 api_fuzz.py
```
You will be prompted to enter:

Target URL

Wordlist path

Example:

```
Enter the url to fuzz: https://example.com/api
Enter the wordlist path: /usr/share/wordlists/dirb/small.txt
```

Output
Displays only valid endpoints

Shows HTTP status codes

Prints JSON responses when detected

Prints HTML/text responses with output limit

Requirements
Python 3.x

requests library

Install dependencies:

```
pip3 install requests
```

Disclaimer
This tool is intended only for authorized testing and educational purposes.
Do not use against systems you do not own or have explicit permission to test.

Author
Developed by a cybersecurity learner as part of Python and API security practice.

yaml

```
---

## Why This Looks Professional

✔ Clear purpose  
✔ Ethical disclaimer  
✔ Clean structure  
✔ Bug‑bounty‑ready  
✔ Shows learning + security mindset  

This is **perfect** for:
- SOC Analyst portfolio
- Bug bounty learning
- Python fundamentals
- GitHub showcase

---

If you want, next we can:
- Add `.gitignore`
- Add logging
- Add threading
- Convert it into a CLI tool
- Add screenshots
- Improve README for recruiters

Just tell me.
```
