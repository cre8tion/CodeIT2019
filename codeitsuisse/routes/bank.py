import json, logging

from flask import request, jsonify, Response
from codeitsuisse import app

@app.route('/bankbranch', methods=['POST'])
def bank():
    data = request.get_json()
    logging.info("full data {}".format(data))

    n = data['N']
    banks = data['branch_officers_timings']
    length = len(banks)
    total = 0

    for i in banks:
        total += i
    print("toatl {}".format(total))
    reduced = n % total
    result = {}
    if reduced == 0:
        result['answer'] = length
    else:
        for i in range(length):
            reduced -= banks[i]
            print(reduced)
            if reduced < 1:
                result['answer'] = i + 1

    print(result)
    return Response(json.dumps(result), mimetype='application/json')