import boto3


def create_instance():
    ec2_resource = boto3.resource('ec2')
    instances = ec2_resource.create_instances(ImageId='ami-6871a115',
                MinCount=1, MaxCount=3,InstanceType='t2.micro',
                SecurityGroupIds=['launch-wizard-7'],KeyName='fullstack')
    instance_ids = []
    for instance in instances:
        instance_ids.append(instance.id)
        #print instance
    ec2_client = boto3.client('ec2')
    waiter=ec2_client.get_waiter('instance_running')
    waiter.wait(InstanceIds=instance_ids)
    print ("Instance is Running now!")

create_instance()

#print instances
#def print_instance():
    #
    #

#delete instances
def delete_instance():
    for instance in instance_ids.items():
        ec2_resource.delete_instances(instance.id)
#ec2_client.terminate_instances(InstanceIds=instance_list,DryRun=False)

delete_instance()
