import threading
import time
import sys
import argparse

from log_writer import write_logs_continuously
from compressor import RealTimeCompressor, LOG_FILE, COMPRESSED_FILE
from viewer import read_compressed_logs


def run_writer():
    """
    Run the log writer indefinitely.
    """
    write_logs_continuously()


def run_compressor(compressor):
    """
    Run the compressor until stopped.
    """
    compressor.run()


def main():
    parser = argparse.ArgumentParser(description="Real-Time Log Compression System")
    parser.add_argument(
        "mode",
        choices=["writer", "compressor", "both", "viewer"],
        default="both",
        nargs="?",
        help="Mode to run: writer, compressor, both (default), or viewer"
    )
    args = parser.parse_args()

    if args.mode == "writer":
        run_writer()
    elif args.mode == "compressor":
        compressor = RealTimeCompressor(LOG_FILE, COMPRESSED_FILE)
        run_compressor(compressor)
    elif args.mode == "viewer":
        read_compressed_logs()
    else:  # both
        # Initialize compressor
        compressor = RealTimeCompressor(LOG_FILE, COMPRESSED_FILE)

        # Start writer and compressor threads
        writer_thread = threading.Thread(target=run_writer, daemon=True)
        compressor_thread = threading.Thread(target=run_compressor, args=(compressor,), daemon=True)

        writer_thread.start()
        compressor_thread.start()

        print("[MAIN] Running log writer and compressor. Press Ctrl+C to stop.")

        try:
            # Keep main thread alive
            while True:
                time.sleep(0.5)
        except KeyboardInterrupt:
            print("\n[MAIN] Stopping...")
            compressor.stop()
            sys.exit(0)

if __name__ == "__main__":
    main()