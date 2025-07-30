#!/usr/bin/env python3
"""
Run script for Support Assistant
This script helps you start both the backend and frontend services.
"""

import subprocess
import time
import os

def main():
    print("🚀 Starting Flask backend...")
    
    # Start backend
    backend_process = subprocess.Popen(
        ["python", "backend/app.py"],
        env=dict(os.environ, FLASK_RUN_PORT="5001")
    )
    
    print("✅ Backend started on port 5001")
    print("📝 To start frontend, run: cd frontend && streamlit run main.py")
    
    try:
        backend_process.wait()
    except KeyboardInterrupt:
        print("\n🛑 Stopping backend...")
        backend_process.terminate()

if __name__ == "__main__":
    main() 