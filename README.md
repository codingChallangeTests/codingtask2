# Coding Task 2

This repo show my solution to a coding challange provided to me as a test.

## Task

Implement a `merge` function that:
 - gets a list of intervals `[[1,2], [2,3]]`
 - detects overlapping intervals
 - merges the overlapping intervals
 - returns the merged results `[[1,3]]`
 - non overlapping intervals will not be touched `[[1,2], [10,12]]`

## Assumptions

- The focus is on the `merge` function and the providing as a python module and the testing of it
- That the order of the intervals in the output is not relevant
- All other code is only for support and showcasing and will not be unit tested
- The input dataset (intervals) will fit in to Memory with free Memory to work on the dataset is left over after loading
- The goal is not to provide the fastest or optimized code, but to showcase the general working, testing and error handling strategies
- The task is not to write a custom input paser or data renderer as a result the assumption is that the dataset is JSON
- The performance questions are theoretical and not expect hard numbers via benchmarking, which is hard to compare
- The code examples are only provided as guidance on how to use the Module and will not include:
    - handling of any errors
    - validating or limiting of inputs
- The code / build is run via one of the following methods:
    - a Linux machine with python 3.10
    - via docker

## local build

use the provided `.envrc` or manualy create the venv

```sh
python3 -m venv .venv
source .venv/bin/activate
pip3 install --requirement requirements.txt
pip3 install --requirement test-requirements.txt
```

### unit tests ###
```sh
tox
```

### build module ###
```sh
python3 setup.py sdist
```

## Examples

### usage as module
```py
from codingtask2.merge import merge

datain = [[25,30], [2,19], [14, 23], [4,8]]
out = merge(datain)
print(out)
```

### demo code

the file `example_merge.py` implements a example
and can read JSON from a file and output the result to stdout as JSON

#### setup ####
Note: this steps are currently optional since the code has no external requiremets

```sh
python3 -m venv .venv
source .venv/bin/activate
pip3 install --requirement requirements.txt
```

#### run ####
```sh
python3 example_merge.py -f example_data.json
```

### Docker build and run

```sh
docker build . -t codingtask2
docker run -ti codingtask2:latest -h
docker run -ti -v "$(pwd)/example_data.json":/app/test.json codingtask2:latest -f test.json
```

## performance ##

the `merge` function consists of 2 parts
1. a Timsort with a worst case performance if O(n log n) and worst case memory of O(n)
2. the merging which has a performance of O(n) and worst case memory of O(n*2)

## Bigdata

its possible to process more data then can fit in the Memmory, but this where out of scope for this code.

### Basic workflow ###
 - split data in to chunks that fit in to Memory and leaf space for a sort
 - create work packages out of the split data
 - may distribute work packages to multible machines
 - for each work packages sort the intervals
 - may do the first merge round (needs performance testing, if this increasses the performance depends on the parrallel workers that can run)
 - store work packages results
 - load each work packages result as steam and sort and merge the incomming data and provide a output stream
 - store output stream

### TODOs ###
 - rethink language for big data
    - for big amounts of data it makes sense to go to a compiled language
