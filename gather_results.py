#!/usr/bin/env python3
"gather results from demo AWS Batch job"

import boto3

def main():
    "do the work"
    client = boto3.client("s3")
    listing = client.list_objects(Bucket="fh-div-adm-scicomp",
                                  Prefix="dtenenba/batch-demo-output/")
    keys = sorted([int(x['Key'].split("/")[-1]) for x in listing['Contents']])
    for key in keys:
        response = client.get_object(Bucket="fh-div-adm-scicomp",
                                     Key="dtenenba/batch-demo-output/{}".format(key))
        result = int(response['Body'].read()) # FIXME what if result is not numeric?
        print("{} plus one equals {}! Who knew?".format(key, result))

if __name__ == "__main__":
    main()
