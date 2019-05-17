virtualenv venv
source venv/bin/activate
pip install -r api/requirements.txt

export APIENDPOINTURL=http://127.0.0.1:5000
export PORT=5001

python api/api.py

deactivate