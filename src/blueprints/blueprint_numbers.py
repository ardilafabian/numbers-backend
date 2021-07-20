from flask import Blueprint, jsonify

numbers = Blueprint(name="numbers", import_name=__name__)

@numbers.route('/sum', methods=['GET'])
def process_sum():
    output = {"msg": "I'm the test endpoint from blueprint_x."}
    return jsonify(output)