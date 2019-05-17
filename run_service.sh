virtualenv venv
source venv/bin/activate
pip install -r service/requirements.txt
python service/service_rest.py

deactivate