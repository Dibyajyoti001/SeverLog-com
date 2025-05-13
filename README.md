ServerLog-com

This is a small Python project that simulates a real-time server logging system.
It creates fake server logs, compresses them on the go using `.xz` compression (LZMA), and lets you view the compressed logs later in a readable format.

---

 📚 Why this project?

It's not a fancy or real-world server tool, but it's a good learning project if you're trying to understand:

* how file reading/writing works in real time
* how compression works (specifically with LZMA)
* how to use threads in Python
* how different parts of a system can work together

---

 🔧 How this works

This project has 3 main parts:

 1. Log Writer

Keeps generating fake log messages every second and writes them to a file called `server.log`.
The messages look like real logs (timestamps, log levels, etc.), but they’re just dummy data.

 2. Compressor

Watches the `server.log` file.
Whenever a new line is added, it compresses that line and writes it into `server_compressed.xz` using LZMA compression.
This happens live (in real time).

 3. Viewer

Lets you read the compressed `.xz` log file and see what's inside in a human-readable way.

---

🚀 Future Plans

Further improvements like making it a scalable production-grade log handler with real-time streaming and multiple user support will be added as soon as I learn more or get help from the community. 😄


