#!/usr/bin/env python3
"gather results from demo AWS Batch job"

import os
import sys
import boto3

def main():
    "do the work"
    bucket = os.getenv("BUCKET_NAME")
    user = os.getenv("BATCH_USER")
    if not (bucket and user):
        print("BUCKET and BATCH_USER are not both defined in the environment!")
        sys.exit(1)
    client = boto3.client("s3")
    listing = client.list_objects(Bucket=bucket,
                                  Prefix="{}/batch-demo-output/".format(user))
    keys = sorted([int(x['Key'].split("/")[-1]) for x in listing['Contents']])
    for key in keys:
        response = client.get_object(Bucket=bucket,
                                     Key="{}/batch-demo-output/{}".format(user, key))
        result = int(response['Body'].read()) # FIXME what if result is not numeric?
        print("{} plus one equals {}! Who knew?".format(key, result))

if __name__ == "__main__":
    main()
