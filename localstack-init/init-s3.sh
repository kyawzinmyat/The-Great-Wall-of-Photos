#!/bin/bash

# Create S3 bucket for photos
awslocal s3 mb s3://photo-bucket

# Set bucket policy to allow public read (for development)
awslocal s3api put-bucket-acl --bucket photo-bucket --acl public-read

echo "LocalStack initialization completed: S3 bucket 'photo-bucket' created"
