import boto3

ec2 = boto3.client("ec2", region_name="ap-south-1")

response = ec2.run_instances(
    ImageId="ami-0d176f79571d18a8f",
    InstanceType="t3.micro",
    MinCount=1,
    MaxCount=1
)

print("Instance ID:", response["Instances"][0]["InstanceId"])
