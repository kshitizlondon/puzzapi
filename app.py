from flask import Flask, jsonify, request
from misc import sumToK
app = Flask(__name__)

@app.route('/', methods=['GET'])
def test():
	return jsonify({'message': "Hello World! Follow me @mofhasa on github"})


@app.route('/sumToTarget', methods=['POST'])
def sumToTarget():
	collection = request.json['collection']
	target = request.json['target']
	mode = request.json['mode']

	if mode == "two":
		solution = sumToK.twoSum_hash(collection, target)
		if solution == None:
			return jsonify({"solution": solution, "exists": False})
		else:
			return jsonify({"solution": solution, "exists": True})
	elif mode == "three":
		solution = sumToK.threeSum(collection, target)
		if solution == None:
			return jsonify({"solution": solution, "exists": False})
		else:
			return jsonify({"solution": solution, "exists": True})
	else:
		return jsonify({'error': "Wrong mode!"})


if __name__ == '__main__':
	app.run()