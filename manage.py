from __future__ import print_function
from flask_script import Manager
from fabch import app, db

manager = Manager(app)

@manager.command
def init_db():
    db.create_all()

app.debug = True

if __name__ == '__main__':
    manager.run()
