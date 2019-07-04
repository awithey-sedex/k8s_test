virtualenv venv
source venv/bin/activate
pip install -r src/frontend/requirements.txt

export BACKENDURL=http://127.0.0.1:5000
export PORT=5001

python src/frontend/gateway.py

deactivate