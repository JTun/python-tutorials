import boto3

def list_instances():
    ec2_client = boto3.client('ec2')

    response = ec2_client.describe_instances()
    print response

for k,v in response.items():
    if k == 'Reservations':
        for instance in v:
            for i,vv in instance.items():
               if i == 'Instances':
                   for ii in vv:
                    print ii['PublicDnsName']


def list_volumes():
    ec2_resource = boto3.resource('ec2')

    instances = ec2_resource.instances.filter(
        Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    for instance in instances:
        print(instance.id,instance.state)
        for item in instance.volumes.all():
            print item.id
            snapshot = ec2_resource.create_snapshot(VolumeId=item.id, Description="Taking backup")

list_instances()
list_volumes()