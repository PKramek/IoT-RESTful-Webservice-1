# pylint: disable=unused-import

import os
from urllib import parse

import pytest
from flask import url_for
from flask_migrate import Migrate
from flask_migrate import MigrateCommand
from flask_script import Manager

import app.main.model
from app import api
from app.main import create_app
from app.main import db

current_env = os.environ.get('APP_ENV', 'dev')
app = create_app(current_env)
app.register_blueprint(api)
app.app_context().push()

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.command
def run():
    app.run()


@manager.command
def test():
    """Runs all tests."""
    if pytest.main(["app/test/",
                    "--cache-clear"]):
        return 0
    return 1


@manager.command
def test_unit():
    """Runs the unit tests."""
    if pytest.main(["app/test/unittest"]):
        return 0
    return 1


@manager.command
def test_integration():
    """Runs the integration tests."""
    if pytest.main(["app/test/integrationtest",
                    "--cache-clear"]):
        return 0
    return 1


@manager.command
def get_routes():
    import urllib
    output = []
    for rule in app.url_map.iter_rules():

        options = {}
        for arg in rule.arguments:
            options[arg] = "[{0}]".format(arg)

        methods = ','.join(rule.methods)
        url = url_for(rule.endpoint, **options)
        line = urllib.parse.unquote(
            "{:50s} {:20s} {}".format(rule.endpoint, methods, url))
        output.append(line)

    for line in sorted(output):
        print(line)


if __name__ == '__main__':
    app.run(debug=True, use_debugger=False, use_reloader=False, passthrough_errors=True)
