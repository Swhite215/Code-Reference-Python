from flask import Flask, make_response, request, abort
from flask_cors import CORS
import io
from io import BytesIO
import json
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np
from parser import parserMain

app = Flask(__name__)
CORS(app)

app.config["DEBUG"] = True

@app.route("/parse", methods=['POST'])
def parse_file():
    try:
        # Grab the File
        f = request.files['file']

        # Convert to Byte Stream
        stream = io.BytesIO(f.stream.read())

        # Read Excel from Byte Stream
        df_ = pd.read_excel(stream)

        # Parse to DataFrame
        df = parserMain(df_.to_json(orient='split'))

        # Convert DataFrame to JSON
        myjson = json.dumps(df)

        # Return Data to Browser
        return myjson
    except:
        abort(500, "Error parsing CSV file!")


# Run the Server
app.run()