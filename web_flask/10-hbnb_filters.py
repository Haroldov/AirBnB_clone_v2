#!/usr/bin/python3
""" starts a Flask web application """

from flask import Flask, render_template
import models
app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def listStates():
    """ return HTML template for listing states and cities """

    return render_template('10-hbnb_filters.html',
                           states=models.storage.all("State"))


@app.teardown_appcontext
def teardown_db(listStates):
    """ close db """

    models.storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
