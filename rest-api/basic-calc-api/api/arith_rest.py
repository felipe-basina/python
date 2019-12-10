from flask import request, Blueprint

arith_rest = Blueprint('arith_rest', __name__)

EMPTY_LIST = "Empty list"
DIVISION_BY_ZERO_NOT_ALLOWED = "Division by ZERO is not allowed"
VALID_NUMBER_LIST = "A list of valid numbers must be provided"

@arith_rest.route("/sum", methods=["POST"])
def sum_remote():
    try:
        numbers = get_numbers_from_request(request)
        if not numbers:
            return response_as_json(None, 400)
        total = sum(numbers)
        return response_as_json(total)
    except:
        return response_as_json(None, 500)

@arith_rest.route("/subtract", methods=["POST"])
def subtract_remote():
    try:
        numbers = get_numbers_from_request(request)
        if not numbers:
            return response_as_json(None, 400)
        
        if len(numbers) > 1:
            total = numbers[0]
            for index in range(1, len(numbers)):
                total -= numbers[index]
        else:
            total = numbers[0]

        return response_as_json(total)
    except:
        return response_as_json(None, 500)

@arith_rest.route("/multiply", methods=["POST"])
def multiply_remote():
    try:
        numbers = get_numbers_from_request(request)
        if not numbers:
            return response_as_json(None, 400)
        
        if len(numbers) > 1:
            total = numbers[0]
            for index in range(1, len(numbers)):
                total *= numbers[index]
        else:
            total = numbers[0]

        return response_as_json(total)
    except:
        return response_as_json(None, 500)

@arith_rest.route("/divide", methods=["POST"])
def divide_remote():
    try:
        numbers = get_numbers_from_request(request)
        if not numbers:
            return response_as_json(None, 400)
        
        if len(numbers) > 1:
            total = numbers[0]
            for index in range(1, len(numbers)):
                if numbers[index] == 0:
                    return response_as_json(None, 400, DIVISION_BY_ZERO_NOT_ALLOWED)
                total = total / numbers[index]
        else:
            total = numbers[0]

        return response_as_json(total)
    except:
        return response_as_json(None, 500)

@arith_rest.route("/power", methods=["POST"])
def power_remote():
    try:
        number, power = get_number_and_power_from_request(request)
        
        total = pow(number, power)

        return response_as_json(total)
    except:
        return response_as_json(None, 500, 'A valid NUMBER and POWER must be provided')

def get_numbers_from_request(request):
    json_request = request.get_json()
    return json_request['numbers']

def get_number_and_power_from_request(request):
    json_request = request.get_json()
    return json_request['number'], json_request['power']

def response_as_json(total, status_code=201, default_message=''):
    message = total
    if status_code == 400:
        message = EMPTY_LIST
        if default_message:
            message = default_message
    elif status_code == 500:        
        message = VALID_NUMBER_LIST
        if default_message:
            message = default_message        

    from flask import jsonify
    return jsonify({"result": message}), status_code