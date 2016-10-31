# README #

### How do I get set up? ###

* You need to install python 3
* Write your and-or graph structure along with input and output data in graph.json
* Run and-or.py 

### Graph structure file declaration ###

Structure file conventionally consists of three parts:

* Input data part
* Intermediate data part
* Output data part

Data entity template:


```
#!json
{
    "[vertex name]" : {
        "input": true,
        "output": false,
        "weights": ["value"],
        "ref": ["[ref name] | [ref name 1]&[ref name 2]"],
        "p": "null | float"
    }
}

```


### Who do I talk to? ###

petrunin.nikon@outlook.com