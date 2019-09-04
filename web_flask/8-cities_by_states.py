#!/usr/bin/python3
""" starts a Flask web application """

from flask import Flask, render_template
import models
app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def listStates():
    """ return HTML template for listing states and cities """

    return render_template('8-cities_by_states.html',
                           states=models.storage.all("State"))


@app.teardown_appcontext
def teardown_db(listStates):
    """ close db """

    models.storage.close()


if __name__ == '__main__':
    app.run()
