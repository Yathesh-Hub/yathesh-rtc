import boto3

ec2 = boto3.client('ec2', region_name='ap-southeast-1')

response = ec2.terminate_instances(
    InstanceIds=['i-05048bd5635472385']  # replace with your instance ID
)

print("Terminating:", response['TerminatingInstances'])