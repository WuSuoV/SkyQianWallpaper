import json

from flask import request


def value(key):
    if request.method == 'GET':
        return request.args.get(key)

    if request.method == 'POST':
        if request.args.get(key) is not None:
            return request.args.get(key)

        r_type = request.content_type
        if 'application/json' in r_type:
            return request.json.get(key)
        elif 'application/form-data' in r_type or 'application/x-www-form-urlencoded' in r_type:
            return request.form.get(key)
        else:
            try:
                return json.loads(request.get_data()).get(key)
            except Exception:
                return 'Please submit in json format'
