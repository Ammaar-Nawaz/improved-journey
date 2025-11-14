My Python Utility Belt

A collection of professional, robust Python scripts built from scratch, focusing on clean code, safety, and modern structure.

1. Professional File Renamer 

A command-line utility to safely batch-rename files in any directory.

Features:

Modern: Uses the pathlib module for object-oriented path handling.

Safe "Plan & Confirm" Design: Runs a full "Preview" loop, then asks for user confirmation (y/n) before making any permanent changes.

Robust: Gracefully handles Folder not found errors and empty folders.

2. 4-Function Calculator

A robust command-line calculator that handles all user and math errors.

Features:

Error Handling: Gracefully handles ValueError (bad input) and ZeroDivisionError.

Professional Structure: Refactored into "specialist" functions (Single Responsibility Principle) and uses the if __name__ == "__main__": guard to be reusable as a module.
