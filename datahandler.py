from dbasehandler import get_bp, insert_bp
from bson.json_util import dumps
from flask import Flask, jsonify, request
import json
from datetime import datetime




app= Flask (__name__)


# Method for get user data using API, input pid under /bp/<pid> to get user data of that pid
@app.route('/bp/<string:pid>', methods=['GET'])
def api_get_bp_by_pid(pid):
    bp = dumps (get_bp(pid))
    if bp is None:
        return jsonify({
            "error": "Not found"
        }), 400
    elif bp == {}:
        return jsonify({
            "error": "uncaught general exception"
        }), 400
    else:
        return bp
       


@app.route('/bp', methods=['POST'])
def api_post_bp ():
    
    new_bp = [request.get_json(force=True)]
    filename = new_bp[0]["pid"] + "-" + datetime.now().strftime("%d%m%Y-%H%M%S")+".json"
    ack= insert_bp(new_bp)

    if ack is None:
        with open (filename, "w") as outfile:
            json.dump (new_bp, outfile)
        return jsonify({
            "error": "uncaught general exception"
        }), 400
    elif ack.acknowledged==False:
        with open (filename, "w") as outfile:
            json.dump (new_bp, outfile)
        return jsonify({
            "error": " db write fail"
        }), 400
    else:
        return jsonify ({
            "write result": "OK"
        }), 201

    
app.run (host="0.0.0.0", port=5000, debug=True)