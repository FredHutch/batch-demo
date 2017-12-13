#!/usr/bin/env python3
"add 1 to a number"

# copy this script to s3://$BUCKET_NAME/$BATCH_USER/batch-demo/process.py
# before demoing....


import sys

def main():
    "do the work"
    inp = sys.stdin.read() # read standard input
    try:
        num = int(inp) # make sure it can be converted to an integer
    except ValueError:
        raise ValueError
    print(num + 1) # add 1, and print

if __name__ == '__main__':
    main()
