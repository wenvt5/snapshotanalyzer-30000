# snapshotanalyzer-30000
demo project to manage AWS EC2 instance snapshot

## About

This project is a demo, and uses boto3 to manage AWS EC2 instance snapshots

## Configuring

It uses the configuration file created by the AWS cli. e.g.


## Running

pipenv run python ec2snap/ec2snapshot.py start --project wen
pipenv run python ec2snap/ec2snapshot.py <command> <--project=PROJECT>

*command* is list, start, or stop
*project* is optional 
