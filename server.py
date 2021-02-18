from flask import request
import flask
from scraper import search
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    if 'query' in request.args:
        search_results = search(request.args.get('query'))

        json_data = json.dumps(
            search_results, default=lambda o: o.__dict__, sort_keys=True, indent=4
        )

        return app.response_class(
            response=json_data,
            status=200,
            mimetype='application/json'
        )

    return 'Error: No query was given'

app.run()