# Endpoints


## **/sumToTarget**

**URI:** https://puzzapi.herokuapp.com/sumToTarget

Gets a solution to the 2SUM and 3SUM problem.

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
