from flask import Flask
from flask_restful import Api
from numbers import AverageCalculator

app = Flask(__name__)
api = Api(app)

# Register the resource
api.add_resource(AverageCalculator, "/numbers/{numberid}")

if __name__ == "__main__":
    app.run(debug=True)
