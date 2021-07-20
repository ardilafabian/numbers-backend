from flask import Blueprint, jsonify, request
from flask_cors import cross_origin
from src.controllers.numbers_controller import process_number_sum

numbers = Blueprint(name="numbers", import_name=__name__)

@numbers.route('/sum', methods=['POST'])
@cross_origin()
def process_sum():
    data = request.get_json()
    array = data['array']
    index, sumResult, leftArray, rightArray = process_number_sum(array)
    response = { "index": index, "sum": sumResult, "leftArray": leftArray, "rightArray": rightArray}
    return jsonify(response)