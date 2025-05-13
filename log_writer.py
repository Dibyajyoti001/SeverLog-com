# log_writer.py
"""
Log Writer Module
-----------------
Simulates a server writing real-time logs to 'server.log'.
Each log entry includes a timestamp, log level, and message.
"""

import time
import random

# Different types of log levels you might see in real server logs
LOG_LEVELS = ["INFO", "DEBUG", "WARNING", "ERROR", "CRITICAL"]

# Some fake event messages for variety
EVENT_MESSAGES = [
    "User login successful",
    "User logout detected",
    "New connection from IP 192.168.1.10",
    "Database query executed",
    "File upload completed",
    "Cache cleared for session",
    "Unauthorized access attempt",
    "Payment transaction initiated",
    "Server response delayed",
    "Configuration file updated"
]

def generate_log_entry():
    """Creates a realistic log entry string."""
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    level = random.choice(LOG_LEVELS)
    message = random.choice(EVENT_MESSAGES)
    return f"[{timestamp}] [{level}] {message}\n"

def write_logs_continuously():
    """
    Writes a new log entry to server.log every second.
    Appends to the file without overwriting existing content.
    """
    print("[LOG WRITER] Starting to write logs to 'server.log'...")
    
    try:
        with open("server.log", "a", encoding="utf-8") as log_file:
            while True:
                entry = generate_log_entry()
                log_file.write(entry)
                log_file.flush()  # ensures it writes immediately
                print(f"[LOG WRITER] {entry.strip()}")  # Debug log
                time.sleep(1)  # wait for 1 second before next log
    except KeyboardInterrupt:
        print("\n[LOG WRITER] Stopped by user.")


if __name__ == "__main__":
    write_logs_continuously()
