import boto3

def create_ec2_instance():
    ec2 = boto3.resource('ec2', region_name='ap-south-1')

    print("Creating EC2 instance...")

    instance = ec2.create_instances(
        ImageId="ami-02b8269d5e85954ef",     # Amazon Linux 2023 (ap-south-1)
        InstanceType="t3.micro",
        MinCount=1,
        MaxCount=1,
        KeyName="mykey",                      # change your key pair name
        SecurityGroupIds=["sg-026ef5bf0702482a9"], # change security group ID
        SubnetId="subnet-07e1f958d2879970a",       # change subnet ID
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {'Key': 'Name', 'Value': 'Boto3-EC2-Instance'}
                ]
            }
        ],
    )

    instance_id = instance[0].id
    print(f"EC2 Instance creation initiated. Instance ID: {instance_id}")

    instance[0].wait_until_running()
    instance[0].reload()

    print("Instance is now running!")
    print(f"Public IP: {instance[0].public_ip_address}")

if __name__ == "__main__":
    create_ec2_instance()
