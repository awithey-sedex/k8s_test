virtualenv venv
source venv/bin/activate

export APIENDPOINTURL=http://127.0.0.1:5000
export PORT=5001

pip install -r src/api/requirements.txt
python src/api/api_rest.py

deactivate