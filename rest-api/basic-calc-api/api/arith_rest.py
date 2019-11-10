from flask import request, Blueprint

from util.util import get_numbers_from_request, get_number_and_power_from_request, response_as_json

arith_rest = Blueprint('arith_rest', __name__)

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
                    return response_as_json(None, 400, 'Division by ZERO is not allowed')
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