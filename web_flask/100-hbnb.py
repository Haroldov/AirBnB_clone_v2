#!/usr/bin/python3
""" starts a Flask web application """

from flask import Flask, render_template
import models
app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def listStates():
    """ return HTML template for listing states and cities """

    return render_template('100-hbnb.html',
                           states=models.storage.all("State"),
                           amenities=models.storage.all("Amenity"),
                           places=models.storage.all("Place"),
                           users=models.storage.all("User")
    )


@app.teardown_appcontext
def teardown_db(listStates):
    """ close db """

    models.storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
