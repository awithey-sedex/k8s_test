virtualenv venv
source venv/bin/activate

export BACKENDURL=http://127.0.0.1:5000
export PORT=5001

pip install -r src/frontend/requirements.txt
python src/frontend/web.py

deactivate