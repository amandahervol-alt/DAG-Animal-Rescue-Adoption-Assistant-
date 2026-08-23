"""
Deming Animal Guardians (DAG) Adoption Assistant — Local HTTP Server & Runner
-----------------------------------------------------------------------------
Serves the responsive adoption portal and compatibility matcher locally.
"""

import os
import sys
import argparse
import webbrowser
import http.server
import socketserver
from pathlib import Path


def serve_portal(port: int = 8000, open_browser: bool = True):
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass

    current_dir = Path(__file__).parent.resolve()
    os.chdir(current_dir)

    print("\n" + "=" * 65)
    print("🐾 DEMING ANIMAL GUARDIANS (DAG) ADOPTION ASSISTANT")
    print("=" * 65)
    print(f"[*] Serving adoption portal from: {current_dir}")
    print(f"[*] Local URL: http://localhost:{port}")
    print("=" * 65)

    if open_browser:
        webbrowser.open(f"http://localhost:{port}/index.html")

    handler = http.server.SimpleHTTPRequestHandler
    socketserver.TCPServer.allow_reuse_address = True

    try:
        with socketserver.TCPServer(("", port), handler) as httpd:
            print("Press Ctrl+C to stop the local web server.\n")
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[OK] Server stopped.")


def main():
    parser = argparse.ArgumentParser(description="DAG Adoption Assistant Web Server")
    parser.add_argument("--port", type=int, default=8000, help="HTTP port to bind to")
    parser.add_argument("--no-serve", action="store_true", help="Validate files and exit without starting server")

    args = parser.parse_args()

    index_path = Path("index.html")
    if not index_path.exists():
        print(f"[!] Error: index.html not found in {Path.cwd()}")
        sys.exit(1)

    print(f"[OK] Validated index.html ({index_path.stat().st_size:,} bytes)")

    if not args.no_serve:
        serve_portal(port=args.port, open_browser=True)


if __name__ == "__main__":
    main()
