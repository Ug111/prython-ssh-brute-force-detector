# SSH Brute Force Detector (Learning Project)

## 📌 Overview of this Lab
This project analyzes SSH authentication logs to detect potential brute-force  attacks.

## 🎯 Goal
I built this to better understand howfailed log patterns can indicate malicious activities.

## SOC Use Case
This tool simulates a SOC detection workflow where authentication logs are analyzed to identify
brute-force attacks and potential account compromise.

## 🔍 what it does:
- Parses auth logs
- Tracks failed login attempts per IP
- Identifies suspicious activity
- Flags successful login after multiple failures

## 🧠 what i learned 
- Regex parsing for log analysis
- How attackers behave during brute-force attempts
- Structuring detection logic in Python

## ⚠️ Limitations
- Detection is not yet time-based
- No real-time monitoring

##  🚀 Next Steps
- implement time-based detection (e.g., x attempts in Y seconds)
- Improve reporting format
