from application import app
from application.service.emr_service import EmrService

import json
from datetime import datetime
from flask import jsonify, request

emr_service = EmrService()

# TODO env|region|config-name (yaml)

@app.route('/v1/emr/clusters/create', methods=['POST'])
def route_clusters_create():
    data = emr_service.create_cluster()
    return __build_response(request, data)

@app.route('/v1/emr/clusters/destroy', methods=['POST'])
def route_clusters_destroy():
    data = emr_service.destroy_cluster()
    return __build_response(request, data)

@app.route('/v1/emr/clusters/info')
def route_clusters_info():
    data = emr_service.info_cluster()
    return __build_response(request, data)

def __build_response(request, data = {}, debug = True):
    """
    Build Response
    """

    if debug:
        data_request = {
            'url': request.url,
            'method': request.method,
            'headers': dict(request.headers),
            'params': request.args
        }
        data_response = {
            #'params': request.params,
            #'body': request.body,
            'data': data
        }
        return jsonify({
            'timestamp': datetime.utcnow().isoformat(),
            'request': data_request,
            'response': data_response
        })
    else:
        return jsonify(data)
