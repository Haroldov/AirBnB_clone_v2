#!/usr/bin/python3
""" starts a Flask web application """

from flask import Flask, render_template
from os import environ
import models
app = Flask(__name__)


@app.route("/states", strict_slashes=False)
@app.route("/states/<ids>", strict_slashes=False)
def listStates(ids=None):
    """ return HTML template for listing states and cities """

    states = models.storage.all("State")
    cities = None
    title = "States"
    if ids is not None and "State." + str(ids) in states:
        if 'HBNB_TYPE_STORAGE' in environ and\
           environ['HBNB_TYPE_STORAGE'] == 'db':
            title = "State: " + states["State." + str(ids)].name
            cities = states["State." + str(ids)].cities
            states = "yes"
        else:
            title = "State: " + states["State." + str(ids)].name
            states = "yes"
            cities = states["State." + str(ids)].cities()
    elif ids is not None and "State." + str(ids) not in states:
        states = None
        title = "Not found!"
    return render_template('9-states.html',
                           states=states,
                           title=title,
                           cities=cities)


@app.teardown_appcontext
def teardown_db(listStates):
    """ close db """

    models.storage.close()


if __name__ == '__main__':
    app.run()
