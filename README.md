# spell_correct

Before running the api install requirements in your python environment.
```bash
pip install -r requirements.txt
```

Run the gunicorn command to start the api.
```bash
gunicorn app:app --bind 0.0.0.0:<port>
```
nohup tool can be used to run the api in the background.
```bash
nohup gunicorn app:app --bind 0.0.0.0:<port> &
```
