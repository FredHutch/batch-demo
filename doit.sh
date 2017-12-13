#!/bin/bash

# copy this script to s3://$BUCKET_NAME/$BATCH_USER/batch-demo/doit.sh
# before demoing....

set -x # echo command lines to stdout
set -e # exit if any command fails
set -o pipefail # even if it's in a pipe (and not the last command)

aws s3 cp s3://$BUCKET_NAME/$BATCH_USER/batch-demo/process.py .

chmod +x process.py

# this command illustrates streaming. We don't have to find disk space to store
# input and output files, we just stream input from S3 through our tool and back
# to S3.
aws s3 cp s3://$BUCKET_NAME/$BATCH_USER/batch-demo-input/$AWS_BATCH_JOB_ARRAY_INDEX - | \
   ./process.py | aws s3 cp --sse AES256 - s3://$BUCKET_NAME/$BATCH_USER/batch-demo-output/$AWS_BATCH_JOB_ARRAY_INDEX
