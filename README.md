# improved-journey

# My Python Utility Belt

This repository is a collection of professional, robust Python scripts I'm building as I master my craft in Computer Science.

---

## 1. 4-Function Calculator (v1.0)

A clean, robust, and professional command-line calculator built from scratch in Python.

### Features:

* **Full 4-Function Support:** Handles addition, subtraction, multiplication, and division.
* **Robust Error Handling:**
    * Gracefully handles `ValueError` if the user types a non-numeric input.
    * Gracefully handles `ZeroDivisionError` with a friendly message.
* **Professional Structure:**
    * Code is refactored into "specialist" functions for each operation (Single Responsibility Principle).
    * Uses a `main()` function and the `if __name__ == "__main__":` guard to make the script reusable as a module.
