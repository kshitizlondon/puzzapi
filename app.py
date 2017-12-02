from flask import Flask, jsonify, request
from misc import sumToK, romans
from trees import treeUtil 

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

#Romans
@app.route('/romans/rToi', methods=['POST'])
def rToi():
	roman = request.json['roman']
	return jsonify({"number": romans.romanToInt(str(roman))})
	
@app.route('/romans/iTor', methods=['POST'])
def iTor():
	numeral = request.json['number']
	return jsonify({"roman": romans.intToRoman(int(numeral))})


#Trees
@app.route('/trees/lca', methods=['POST'])
def trees_lca():
	tree = request.json['tree'].split(",")
	node1 = request.json['node1']
	node2 = request.json['node2']

	lca = treeUtil.getLCA(tree, node1, node2)
	if lca == None:
		return jsonify({"lca": "None", "exists": False})
	else:
		return jsonify({"lca": lca.data, "exists": True})

if __name__ == '__main__':
	app.run()