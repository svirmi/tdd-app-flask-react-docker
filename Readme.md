##### ~/code/tests/PYTHON/testdriven-app/services/users$ 
```bash
python3 -m venv env
source env/bin/activate
(env)$ export FLASK_APP=project/__init__.py
(env)$ python manage.py run
```

##### Navigate to http://localhost:5000/users/ping in your browser. You should see:
```bash
{
"message": "pong!",
"status": "success"
}
```