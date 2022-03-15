
# this example show
import argparse
import json
import os

from codingtask2.merge import merge

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Merge demo')
    parser.add_argument('-f', '--file', action='store', help='JSON input file', required=True)
    args = parser.parse_args()

    with open(args.file) as json_file_name:
        # parse JSON input data
        intervals = json.load(json_file_name)
        # merge intervals
        merged_intervals = merge(intervals)
        # print as JSON
        print(json.dumps(merged_intervals))
