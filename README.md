# And/Or Graph
Application for calculating and-or graphs

## Build with
* python 3

## Graph structure file declaration

### Parts:
* Input layer ```"input": true```
* Middle graph layers
* Output layer ```"output": true```

### Template:
```json
{
    "vertices": [
        {
            "[vertexName: string]" : {
                "input": true,
                "output": false,
                "weights": "[array: float]",
                "ref": ["[refName1: string]", "[refName2: string]&[refName3: string]"],
                "p": "[probability: float | null]"
            }
        }
    ]
}
```
### Template Rules:
* The value of the "input" key should not be equals to the "output" key (if false, it can be undefined explicitly)
* The "p" key is required
* If the "ref" key is defined, the "weights" key is required
* Weights array length must be equals to references count
* Reference names are names of the vertices referring this vertex
* Character "&"  in "ref" key are relation between references (relation between elements of array of the "ref" key is "or")