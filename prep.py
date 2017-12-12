#!/usr/bin/env python3
"put some dummy objects in s3"

import boto3

CLIENT = boto3.client('s3')

for i in range(50):
    byt = bytes(str(i))
    CLIENT.put_object(Body=byt, Bucket='fh-div-adm-scicomp',
                      Key='dtenenba/batch-demo-input/{}'.format(i),
                      ServerSideEncryption='AES256')
