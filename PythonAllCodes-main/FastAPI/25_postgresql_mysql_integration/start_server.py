#!/usr/bin/env python3
"""
Server startup script for FastAPI Database Integration

This script ensures the server starts from the correct directory.
"""

import subprocess
import os
import sys
from pathlib import Path

def start_server():
    """Start the FastAPI server"""
    # Get the directory where this script is located
    script_dir = Path(__file__).parent.absolute()
    
    # Change to the script directory
    os.chdir(script_dir)
    
    print(f"Starting FastAPI server from: {script_dir}")
    print("Server will be available at: http://localhost:8000")
    print("Swagger docs: http://localhost:8000/docs")
    print("ReDoc: http://localhost:8000/redoc")
    print("Health check: http://localhost:8000/health")
    print("\nPress Ctrl+C to stop the server\n")
    
    try:
        # Start uvicorn server
        cmd = [sys.executable, "-m", "uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
        subprocess.run(cmd, check=True)
    except KeyboardInterrupt:
        print("\n\nServer stopped by user")
    except subprocess.CalledProcessError as e:
        print(f"Error starting server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    start_server()