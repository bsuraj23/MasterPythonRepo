#!/usr/bin/env python
"""
Server Startup Script for Advanced Routing Example

This script starts the FastAPI server with proper configuration.
"""

import uvicorn
import sys
import os

def main():
    """
    Start the FastAPI server
    """
    print("="*60)
    print("Starting FastAPI Advanced Routing Example Server")
    print("="*60)
    print()
    print("📚 API Documentation: http://127.0.0.1:8000/docs")
    print("📖 Alternative Docs:  http://127.0.0.1:8000/redoc")
    print("🏠 Root Endpoint:     http://127.0.0.1:8000/")
    print("💊 Schemas Endpoint:  http://127.0.0.1:8000/schemas")
    print("❤️  Health Check:     http://127.0.0.1:8000/health")
    print()
    print("Press Ctrl+C to stop the server")
    print("="*60)
    print()
    
    try:
        # Run the server
        uvicorn.run(
            "main:app",
            host="127.0.0.1",
            port=8000,
            reload=True,
            log_level="info"
        )
    except KeyboardInterrupt:
        print("\n\nServer stopped by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n\n❌ Error starting server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()