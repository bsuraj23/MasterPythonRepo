#!/usr/bin/env python3
"""
Startup script for Project2 HR Management System
This script runs the FastAPI server directly
"""

if __name__ == "__main__":
    import uvicorn
    from main import app
    
    print("🚀 Starting HR Management System API...")
    print("📊 API Documentation: http://127.0.0.1:8001/docs")
    print("🔗 API Root: http://127.0.0.1:8001/")
    print("❤️ Health Check: http://127.0.0.1:8001/health")
    print("📈 Analytics: http://127.0.0.1:8001/analytics/summary")
    print()
    
    uvicorn.run(
        app, 
        host="127.0.0.1", 
        port=8001, 
        reload=True,
        log_level="info"
    )