import boto3

def create_instance():
    ec2_resource = boto3.resource('ec2')
    instances = ec2_resource.create_instances(ImageId='ami-6871a115',
                MinCount=1, MaxCount=3,InstanceType='t2.micro',
                SecurityGroupIds=['launch-wizard-7'],KeyName='fullstack')
   
    instancelists =[]
    for instance in instances.items():
        print instance
    
        instancelists = instance.append('id')
   
    ec2_client = boto3.client('ec2')
    waiter=ec2_client.get_waiter('instance_running')
    waiter.wait(InstanceIds=[instances[0].id])
    print ("Instance is Running now!")

create_instance()
