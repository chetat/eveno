from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import create_app

manager = Manager(create_app)
manager.add_option("-c", "--config", dest="config_module", required=False)
manager.add_command('db', MigrateCommand)
