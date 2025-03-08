# 🛡️ PS CHECK - DNS Blacklist Checker

PS CHECK is a powerful and automated Python script designed to check whether a domain is blacklisted on multiple well-known DNS-based blackhole lists (DNS RBLs). It provides a sleek, user-friendly interface with high accuracy, making it an essential tool for cybersecurity professionals, network administrators, and security researchers.

---

## 🚀 Features
✅ **Automated Dependency Installation** – The script installs required dependencies automatically.
✅ **Supports Multiple Domains** – Enter a single domain or multiple domains separated by commas.
✅ **Fast & Efficient** – Checks domains against multiple DNS blacklists in seconds.
✅ **Detailed Output** – Displays results in a neatly formatted table.
✅ **Easy to Use** – Just run the script and follow the prompts.

---

## 📦 Installation & Setup
### **Prerequisites**
- Ensure you have Python installed (Python 3.x recommended).
- Clone this repository and navigate to the directory:

```bash
git clone [https://github.com//ps-check.git](https://github.com/prabhatsirvi//ps-check.git)
cd ps-check
```

- Run the script:
```bash
python3 ps_check.py
```

---

## 🔧 How to Use
1. Run the script.
2. Enter a domain or multiple domains (comma-separated) when prompted.
3. The script will check each domain against multiple blacklist providers.
4. The results will be displayed in a structured table format.

### **Example Output**
```
+--------------+-------------+
| Domain      | Blacklisted |
+--------------+-------------+
| example.com | NO         |
| spammy.com  | YES        |
+--------------+-------------+
```

---

## 🛠 Dependencies
- `dnspython`
- `tabulate`

These dependencies will be automatically installed when you run the script.

---

## 📜 License
This project is open-source and available under the MIT License.

---

## 👨‍💻 Author
Developed with ❤️ by **Prabhat Solanki** | [GitHub](https://github.com/prabhatsirvi/)
