import os
import time
import lzma
import threading

LOG_FILE = "server.log"
COMPRESSED_FILE = "server_compressed.xz"

class RealTimeCompressor:
    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path
        self.stop_flag = threading.Event()

    def compress_loop(self):
        """
        Monitors the log file and compresses new lines in real-time.
        Appends compressed data to the .xz file using LZMA chunks.
        """
        print("[COMPRESSOR] Starting real-time compression...")

        if not os.path.exists(self.input_path):
            print(f"[COMPRESSOR] Error: '{self.input_path}' not found!")
            return

        try:
            with open(self.input_path, "r", encoding="utf-8") as log_file:
                # Move to end of log file so we only read new lines
                log_file.seek(0, os.SEEK_END)

                while not self.stop_flag.is_set():
                    position = log_file.tell()
                    line = log_file.readline()

                    if not line:
                        time.sleep(0.5)
                        log_file.seek(position)
                        continue

                    print(f"[COMPRESSOR] Read: {line.strip()}")

                    # Compress and append this new line
                    compressed_chunk = lzma.compress(line.encode("utf-8"))
                    with open(self.output_path, "ab") as compressed_file:
                        compressed_file.write(compressed_chunk)
                        print(f"[COMPRESSOR] Compressed and wrote chunk.")

        except KeyboardInterrupt:
            print("\n[COMPRESSOR] Stopped by user.")
        except Exception as e:
            print(f"[COMPRESSOR] Error: {e}")
        finally:
            print("[COMPRESSOR] Exiting compression thread.")

    def run(self):
        """Run the compressor."""
        self.compress_loop()

    def stop(self):
        """Signal to stop compression."""
        self.stop_flag.set()


if __name__ == "__main__":
    compressor = RealTimeCompressor(LOG_FILE, COMPRESSED_FILE)
    try:
        compressor.run()
    except KeyboardInterrupt:
        compressor.stop()
