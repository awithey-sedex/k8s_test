virtualenv venv
source venv/bin/activate

pip install -r src/service/requirements.txt
python src/service/service_rest.py

deactivate