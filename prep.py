#!/usr/bin/env python3
"put some dummy objects in s3"

import os
import sys
import boto3

CLIENT = boto3.client('s3')

BUCKET = os.getenv("BUCKET_NAME")
BATCH_USER = os.getenv("BATCH_USER")

if not (BUCKET and BATCH_USER):
    print("BUCKET_NAME and BATCH_USER must both be defined in the environment.")
    sys.exit(1)

for i in range(50):
    byt = bytes(str(i), "utf-8")
    CLIENT.put_object(Body=byt, Bucket=BUCKET,
                      Key='{}/batch-demo-input/{}'.format(BATCH_USER, i),
                      ServerSideEncryption='AES256') # required on all Center buckets
