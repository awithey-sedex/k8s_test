virtualenv venv
source venv/bin/activate

pip install -r src/backend/requirements.txt
python src/backend/backend.py

deactivate