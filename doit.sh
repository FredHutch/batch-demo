#!/bin/bash

# copy this script to s3://fh-div-adm-scicomp/dtenenba/batch-demo/doit.sh
# before demoing....

aws s3 cp s3://fh-div-adm-scicomp/dtenenba/batch-demo/process.py .

chmod +x process.py

aws s3 cp s3://fh-div-adm-scicomp/dtenenba/batch-demo-input/$AWS_BATCH_JOB_ARRAY_INDEX - | \
   ./process.py | aws s3 cp --sse AES256 - s3://fh-div-adm-scicomp/dtenenba/batch-demo-output/$AWS_BATCH_JOB_ARRAY_INDEX
