# 🔐 Auto Password Generator — A.P.M.

This Python program generates a **secure random password** based on user input and stores it temporarily in a dictionary associated with a website, app name, or identifier.  
A simple command-line tool built to practice randomness, input validation, and secure password generation.

---

## ✅ Features

| Feature | Status |
|--------|--------|
| Secure password generation using `secrets` | ✅ |
| Random mix of letters, digits & punctuation | ✅ |
| Input validation for password length | ✅ |
| Prevents empty URL/service name input | ✅ |
| Stores password in a dictionary `{ name: password }` | ✅ |
| Simple UI and production pause | ✅ |
| Can generate between **8 and 100 characters** | ✅ |
| Persistent storage | ❌ (not yet) |
| Multiple saved passwords | ❌ (currently only 1 per run) |

---

## 🛠 Technologies Used

- Python 3.10+
- `secrets` for strong randomness
- `string` for character set
- `time` module for simple UI timing

---

## 🚀 How to Use

Run in a terminal:

```bash
python3 src/main.py
