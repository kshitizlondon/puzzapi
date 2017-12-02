# **Endpoints**

## Binary Trees

**URIs:**

- /trees/lca
	
	Returns the lowest common ancestor (node farthest from the root common to a couple of nodes in the tree)
	
	**POST json format example**

	```
	{
		"tree": "20,8,4,-1,-1,12,10,-1,-1,14,-1,-1,22,-1,-1",
		"node1": "8",
		"node2": "4"
	}
	```
	
	**Response example**
	```
	{
	  "lca": "8",
	  "exists": True
	}
	```

## Miscellaneous

#### **/romans**

**URIs:**

- /romans/iTor
	
	Converts an integer (base 10) to a roman numeral
	
	**POST json format example**

	```
	{
	  "number" : "10"
	}
	```
		
	where,
	number: the integer in base 10
	
	**Response example**
	```
	{
	  "roman": "X",
	}
	```
-  /romans/rToi

	Converts a roman numeral to integer (base 10)
	
	**POST json format example**

	```
	{
	  "roman" : "CC"
	}
	```
		
	where,
	roman: the roman numeral to be converted
	
	**Response example**
	```
	{
	  "number": "200",
	}
	```

#### **/sumToTarget**

**URI:** https://puzzapi.herokuapp.com/sumToTarget

Returns a solution to the 2SUM and 3SUM problem.

- **2SUM:** Return a combination of two different indices from a collection of integers whose corresponding elements add up to a target value.

- **3SUM:** Return a combination of three different indicies from a collection of integers whose corresponding elements add up to a target value.


**POST json format example**

```
{
  "collection" : "1,2,3,4,5,6",
  "target": "7",
  "mode" : "two"
}
```

where,

- collection: is comma seperated list of numbers,

- target: is the what the sum of the combination should,

- mode: can take values: "two" (for 2SUM) and "three" (for 3SUM)


**Response example**

If a solution is found:

```
{
  "solution": [0,5],
  "exists": true
}
```

If a solution is not found:
```
{
  "solution": None,
  "exists": false
}
```

If something wrong with the input:
```
{
  "error": "Wrong mode!"
}
```
