import os
from app import create_app
from flask_script import Manager, Server

app = create_app("dev")
manager = Manager(app)

if __name__ == '__main__':
    manager.run()
