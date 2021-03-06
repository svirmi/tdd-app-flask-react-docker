##### ~/testdriven-app/services/users$ 
```bash
python3 -m venv env # at first run after repo cloning
source env/bin/activate
pip3 install -r requirements.txt
(env)$ export FLASK_APP=project/__init__.py
(env)$ export FLASK_DEBUG=1
(env)$ python manage.py run
```

##### Navigate to http://localhost:5001/users/ping in your browser. You should see:
```bash
{
"message": "pong!",
"status": "success"
}
```

##### To build the image run from project root folder (~/testdriven-app/)
```bash
docker-compose -f docker-compose-dev.yml build
```

##### To spin up the container, run
```bash
docker-compose -f docker-compose-dev.yml up -d
```

##### To enter postgres container run
```bash
docker exec -ti $(docker ps -aqf "name=users-db") psql -U postgres
```

##### To rebuild and run container at dev environment, run 
```bash
docker-compose -f docker-compose-dev.yml up -d --build
```

##### To run tests:
```bash
docker-compose -f docker-compose-dev.yml run users python manage.py test
```