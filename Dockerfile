#fredhutch/batch-demo
FROM ubuntu:16.04

RUN apt-get update -y && apt-get install -y git curl unzip python3 python3-pip

RUN pip3 install awscli boto3

RUN curl -LO https://github.com/awslabs/aws-batch-helpers/archive/master.zip

RUN unzip master.zip

RUN cp aws-batch-helpers-master/fetch-and-run/fetch_and_run.sh /usr/local/bin/

RUN rm -rf master.zip aws-batch-helpers-master

ENTRYPOINT ["/usr/local/bin/fetch_and_run.sh"]
