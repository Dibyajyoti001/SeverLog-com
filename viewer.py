# viewer.py
"""
Viewer Module
-------------
Reads and displays the content of the compressed .xz log file
in a human-readable format.
"""

import lzma
import os

COMPRESSED_FILE = "server_compressed.xz"

def read_compressed_logs():
    """Reads and prints lines from the compressed .xz file."""
    if not os.path.exists(COMPRESSED_FILE):
        print(f"[VIEWER] Error: '{COMPRESSED_FILE}' not found!")
        return

    print(f"[VIEWER] Reading logs from '{COMPRESSED_FILE}'...\n")

    try:
        with lzma.open(COMPRESSED_FILE, "rb") as f:
            for line in f:
                print("[VIEWER]", line.decode("utf-8").strip())
    except lzma.LZMAError:
        print("[VIEWER] LZMAError: Corrupted or invalid compressed file.")
    except Exception as e:
        print(f"[VIEWER] Error: {e}")

if __name__ == "__main__":
    read_compressed_logs()
