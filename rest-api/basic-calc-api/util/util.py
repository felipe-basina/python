def get_numbers_from_request(request):
    json_request = request.get_json()
    return json_request['numbers']

def get_number_and_power_from_request(request):
    json_request = request.get_json()
    return json_request['number'], json_request['power']

def response_as_json(total, status_code=201, default_message=''):
    message = total
    if status_code == 400:
        message = "Empty list"
        if default_message:
            message = default_message
    elif status_code == 500:        
        message = "A list of valid numbers must be provided"
        if default_message:
            message = default_message        

    from flask import jsonify
    return jsonify({"result": message}), status_code