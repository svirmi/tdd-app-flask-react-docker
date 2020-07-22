from flask.cli import FlaskGroup
from project import app, db

import unittest

cli = FlaskGroup(app)

# ~/testdriven-app$ docker-compose -f docker-compose-dev.yml run users python manage.py recreate_db
@cli.command("recreate_db")
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command("test")
def test():
    """ Runs the tests without code coverage"""
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    cli()