# Navigate to Project2
cd "C:\Users\Suraj\Desktop\GreenWorkSpace1\A2JulyWorkSpace\PythonAllCodes-main\FastAPI\Project2"

# Create and activate virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn main:app --reload --host 127.0.0.1 --port 8001