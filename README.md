OpsBot Log Automator

-- Project Overview

OpsBot is a Python-based automation tool designed to help IT Operations teams quickly identify potential security threats in server log files.

Instead of manually scanning thousands of log lines, OpsBot:

1. Filters out irrelevant "Info" messages
2. Detects critical issues like failed login attempts
3. Generates a summarized security report

-- Business Problem

Servers generate massive log data (≈5000 lines/day).

Manually identifying FAILED LOGIN, ERROR, and CRITICAL events is:

1. Time-consuming 
2. Error-prone 

OpsBot automates this process and reduces manual effort significantly.

-- Features

1.Reads log files line by line

2.Detects important patterns using:

  * String methods
  * Regular Expressions ('re module)

3.Counts frequency of each error type
4.Generates a filtered security report
5.Displays output file size using `os` module

-- Keywords Detected

* 'ERROR'
  
* 'CRITICAL'
  
* 'FAILED LOGIN'

-- Technologies Used

* Python 3
* 're' (Regular Expressions)
* 'os' module
* 'datetime' module

-- Project Structure

OpsBot/

│── opsbot.py

│── server.log

│── security_alert_YYYY-MM-DD.txt

│── README.md

--How to Run

1. Place your log file as:

   server.log
  
2. Run the script:

   python opsbot.py
  
3. Output will be:

   * Filtered lines printed on console
   * Count summary displayed
   * Security report file generated

-- Sample Input (server.log)

INFO: Server started

ERROR: Database connection failed

CRITICAL: System crash detected

User login successful

FAILED LOGIN attempt from IP 192.168.1.1

- Sample Output

- Console Output:

Filtered Lines:

ERROR: Database connection failed

CRITICAL: System crash detected

FAILED LOGIN attempt from IP 192.168.1.1

Count:
ERROR : 1
CRITICAL : 1
FAILED LOGIN : 1

-Generated File:

security_alert_2026-04-24.txt

-- Explanation of Two Approaches

1.Basic String Matching

* Uses 'if keyword in line'
  
* Simple and easy to understand
  
* Slightly less flexible

2.Regex-Based Matching 

* Uses 're.compile()'
  
* More powerful and scalable
  
* Handles case-insensitive matching efficiently

-- Output Details

* Total lines processed
* Filtered critical lines
* Frequency of each error type
* Output file size (in bytes)

-- Future Enhancements

1. Email alerts for critical logs 📧
2. Real-time log monitoring 🔴
3. Dashboard visualization 📊
4. IP tracking for suspicious activity 🌐

👨‍💻 Author

Developed as part of a Core Python Project .
