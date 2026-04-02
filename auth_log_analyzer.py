import re

from collections import defaultdict
from datetime import datetime

LOG_FILE = "/var/log/auth.log"

failed_attempts = defaultdict(int)
successful_logins = set()
ip_timestamps = defaultdict(list)

# Regex pattern
failed_pattern = re.compile(r"Failed password.*from (\d+\.\d+\.\d+\.\d+)")
successful_pattern = re.compile(r"Accepted password.*from (\d+.\d+\.\d+\.\d+)")
timestamp_pattern = re.compile(r'^(\w+\s+\d+\s+\d+:\d+)')

with open (LOG_FILE, "r") as file:
     for line in file:
         # Detect failed attempts
         failed_match = failed_pattern.search(line)
         if failed_match:
            ip = failed_match.group(1)
            failed_attempts [ip] += 1

            timestamp_match = timestamp_pattern.search(line)
            if timestamp_match:
                timesatmp = timesatmp_match.group(1)
                ip_timestamps[ip].append(timestamp)
         # Detect successful login
         success_match = successful_pattern.search(line)
         if success_match:
             ip = success_match.group(1)
             successful_logins.add(ip)


# Detection threshold
THRESHOLD = 5
compromised = False

#  Find top attacker if failed_attempts:
if failed_attempts:
    top_ip = max(failed_attempts, key=failed_attempts.get)
    top_count = failed_attempts[top_ip]
    print(f"[Top] Most failed attempts from {top_ip}: {top_count}")

print("\n=== SSH Brute Force Detection Report ===\n")

# Report timestamp
now = datetime.now()
print(f"Report generated at: {now.strftime('%Y-%m-%d %H:%m')}\n")

compromised = False

output_lines = []

for ip, count in failed_attempts.items():
    if count >= THRESHOLD:
      msg1 = f"[ALERT] Suspicious activity detected from IP: {ip}"
      msg2 = f"Failed Attempts: {count}"

      print(msg1)
      print(msg2)

      output_lines.append(msg1)
      output_lines.append(msg2)

      compromised = True

if ip in successful_logins:
       msg3 = "[CRITICAL] Successful login after multiple failures!"
       print(msg3)
       output_lines.append(msg3) 

# OUTSIDE logo

if compromised:
           print("\nStatus: SYSTEM COMPROMISED!")
else:
           print("\nStatus: System Secure")

with open("report.txt", "w") as f:
       for line in output_lines:
           f.write(line + "\n")

