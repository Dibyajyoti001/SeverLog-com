# SeverLog-com
This is a small Python project that simulates a real-time server logging system. It creates fake server logs, compresses them on the go using .xz compression (LZMA), and lets you view the compressed logs later in a readable format.

->It's not a fancy or real-world server tool, but it's a good learning project if you're trying to understand:
->how file reading/writing works in real time
->how compression works (specifically with LZMA)
->how to use threads in Python and how different parts of a system can work together
This project has 3 main parts:

Log Writer
This keeps generating fake log messages every second and writes them to a file called server.log. The messages look like real logs (with timestamps, log levels, etc.), but they’re just dummy data.

Compressor
This part keeps watching the server.log file. Whenever a new line is added, it compresses that line and writes it into server_compressed.xz using LZMA compression. This happens live (in real time).

Viewer
This lets you read the compressed .xz log file and see what’s inside in a human-readable way.

Further improvents of making it a scalable production code with real time server log handling will be done as soon as i learn or this community helps me 
----------------------------------------------------------------------*******************------------------------------------------------------------------------------
