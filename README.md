

# 🧩 Kata 3 – Password Input Field Validation

## 📖 Description

This kata focuses on creating a **password validation function** that checks whether a user’s password meets specific security requirements.
The goal is to implement it using **Test-Driven Development (TDD)** and validate it with **pytest**.

---

## 🧠 Requirements

A valid password must satisfy **all** the following rules:

1. Must be **at least 8 characters long**.
2. Must contain **at least 2 digits**.
3. Must contain **at least one lowercase letter**.
4. Must contain **at least one uppercase letter**.
5. Must contain **at least one special character** (e.g. @, #, $, !, etc.).
6. Cannot consist of symbols only.

---

## ⚙️ Implementation

The validation function is implemented in the `src` directory using **regular expressions (Regex)** to check all password conditions.
It returns a dictionary containing a boolean (`is_valid`) and a list of error messages (if any).

---

## 🧪 Testing

All test cases are written with **pytest** inside the `testes` folder.
The tests cover multiple scenarios, including:

* Too short passwords
* Missing digits, letters, or symbols
* Valid passwords that meet all rules
* Passwords containing only symbols or spaces

---

## ▶️ How to Run

1. Install pytest:

   ```bash
   pip install pytest
   ```
2. Run the tests:

   ```bash
   pytest
   ```

---

## ✅ Expected Result

When all conditions are correctly implemented, all test cases should pass without any errors.

---

## 🧾 Information

* **Author:** Hala Mohamed
* **Project:** Password Validation Kata (TDD)
* **Year:** 2025

---

Would you like me to make a **short version (for GitHub README)** — just 2–3 sections with a professional summary and setup instructions?
