#!/usr/bin/python3

import boto3
import botocore

s3 = boto3.resource('s3')
s3.Bucket('syseng-artifacts').download_file('/starccm/STAR-CCM+14.04.011_02_linux-x86_64.tar.gz', 'foobar.gz')
