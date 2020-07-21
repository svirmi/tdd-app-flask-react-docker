from flask.cli import FlaskGroup
from project import app, db

cli = FlaskGroup(app)

# ~/testdriven-app$ docker-compose -f docker-compose-dev.yml run users python manage.py recreate_db
@cli.command("recreate_db")
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

if __name__ == '__main__':
    cli()