import boto3
import sys 

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


def list_volumes_create_sn():
    ec2_resource = boto3.resource('ec2')

    instances = ec2_resource.instances.filter(
        Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    for instance in instances:
        print(instance.id,instance.state)
        for item in instance.volumes.all():
            print item.id
            snapshot = ec2_resource.create_snapshot(VolumeId=item.id, Description="Taking backup")

# def create_image(inst, e2_client, inst_dict):
#     nowtime = datetime.datetime.now().strftime('%Y-%m-%d')
#     try:
#         image = e2_client.create_image(
#             BlockDeviceMappings=[
#                 {
#                     'DeviceName': inst_dict[inst]['root_dev_name'],
#                     'Ebs': {
#                         'Encrypted': inst_dict[inst]['vol_encr'],
#                         'DeleteOnTermination': inst_dict[inst]['vol_del_rule'],
#                         'VolumeSize': inst_dict[inst]['vol_size'],
#                         'VolumeType': inst_dict[inst]['root_dev_type']
#                     },
#                 },
#             ],
#             Description=inst_dict[inst]['inst_name'] + " " + str(nowtime),
#             DryRun=False,
#             Name=inst_dict[inst]['inst_name'] + " " + str(nowtime),
#             NoReboot=True
#         )
#     except Exception, e:
#         logging.error("Failed to create image! Instance: " + inst_dict[inst]['inst_name'])
#         return 1

list_instances()
list_volumes_create_sn()
#create_images()