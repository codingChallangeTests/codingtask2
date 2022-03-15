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

- The focus is on the `merge` function and the providing as a python module testing of it
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
