virtualenv venv
source venv/bin/activate
pip install -r src/api/requirements.txt

export APIENDPOINTURL=http://127.0.0.1:5000
export PORT=5001

python src/api/api.py

deactivate