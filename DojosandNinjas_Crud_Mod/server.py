from flask_app import app
from flask_app.controllers.dojo_controllers import Dojo
from flask_app.controllers.dojo_controllers import Ninja

if __name__ == '__main__':
    app.run(debug = True)