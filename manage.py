from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from info import db
from info import create_app

app = create_app('pro')


manage = Manager(app)

# mysql数据迁移
Migrate(app, db)

manage.add_command('sql', MigrateCommand)



@app.route("/")
def index():

    # redis_store.set('name','zhangsnan')

    from flask import session
    session['name'] = 'zd'

    return "index"

if __name__ == '__main__':
    manage.run()