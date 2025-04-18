# 🔢 Perfect Square Factorial Parser

This Python script processes a comma-separated list of numbers, filters out the perfect squares, and performs a unique operation: it calculates each perfect square’s factorial, strips trailing zeroes, and collects the last three non-zero digits. The result is a custom string based on these digits.

---

## 🧠 What It Does

Given a string of comma-separated numbers:
1. ✅ Identifies which numbers are **perfect squares**.
2. 🎯 For each perfect square:
   - Calculates the **factorial**.
   - Removes trailing zeroes.
   - Extracts the **last three** non-zero digits.
3. 🔄 Concatenates those digits into a final output string.

If there are **no perfect squares**, the function returns `-1`.

---

## 📦 Example

```python
input_string = '2,4,8,9,16'
print(perfect_square(input_string))
