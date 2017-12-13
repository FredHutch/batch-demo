# Simple Array Job example in AWS Batch

Before trying this example, please read the
[documentation](https://fredhutch.github.io/aws-batch-at-hutch-docs/)
for using AWS Batch at Fred Hutch. In particular, be sure you understand
how to set up your AWS credentials, and make sure you have asked for
and received the permissions necessary to run AWS Batch.

## Running the example

The following commands should be run on one of the Center's Linux servers (you should either be connected to one of the *rhino* machines via
`ssh` or to one of the NX servers (`manx, sphinx, lynx`, etc.) via NoMachine).

### Step 1: Clone the repository

Clone this repository:

```
git clone https://github.com/FredHutch/batch-demo.git
cd batch-demo
```

### Step 2: Edit variables

Edit the file `setup.sh`.
Change the value of `BUCKET_NAME` to your lab's
bucket. If your PI's name is Jane Doe, your
lab's bucket name is `fh-pi-doe-j`.

Change the value of `BATCH_USER` to your HutchNet ID
(your email address without the `@fredhutch.org`).

These changes are necessary because each user only has permission to write to their own PI's bucket.
Within that bucket, your username will make it clear who the files belong to.

#### Source the setup file

Now source the file `setup.sh` as follows:

```
source setup.sh
```

This will export the variables `BUCKET_NAME` and
`BATCH_USER` to your shell and make them
available to the commands you are now going to run.

### Step 3: Set up the Job Definition
