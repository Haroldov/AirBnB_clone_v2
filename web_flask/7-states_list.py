#!/usr/bin/python3
""" starts a Flask web application """

from flask import Flask, render_template
import models
app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def listStates():
    """ return HTML template for listing states """

    return render_template('7-states_list.html',
                           states=models.storage.all("State"))


@app.teardown_appcontext
def teardown_db(listStates):
    """ close db """

    models.storage.close()


if __name__ == '__main__':
    app.run()
