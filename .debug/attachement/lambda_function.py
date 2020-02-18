import boto3
import json
import logging
import os
from botocore.vendored import requests
from botocore.exceptions import ClientError
import time


EC2_CLIENT = boto3.client('ec2')
IAM_CLIENT = boto3.client('iam')

SUCCESS = "SUCCESS"
FAILED = "FAILED"


def lambda_handler(event, context):
    get_vpc_response = EC2_CLIENT.describe_vpcs()
    print(get_vpc_response)
    