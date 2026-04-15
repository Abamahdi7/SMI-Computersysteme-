# SMI-Computersysteme-
Description

This is a simple Python program that reads a log file and analyzes its content. It identifies and counts different types of messages such as ERROR, WARNING, and INFO, and highlights the critical issues.

Features
Counts the number of:
ERROR messages
WARNING messages
INFO messages
Displays all error messages separately
Outputs a clear summary report in the terminal
Example Input (log.txt)
ERROR: Disk full
INFO: User login
WARNING: CPU high
ERROR: Connection failed
How to Run
Ensure Python 3 is installed on your system
Place the log.txt file in the same directory as the script
Run the program using:
python log_analyzer.py
Example Output
=== Log Report ===
Errors: 2
Warnings: 1
Info: 1

Critical Issues:
- ERROR: Disk full
- ERROR: Connection failed
Purpose

This project demonstrates fundamental Python skills, including file handling, loops, and conditional logic. It also reflects a practical use case in IT environments, where analyzing log files is a common task for monitoring systems and identifying issues.
