import boto3
import click
session = boto3.Session(profile_name='pythonAutomation')
ec2 = session.resource('ec2')

@click.command()
def list_instances():
    "show info for each instance"
    for i in ec2.instances.all():
        print(', '.join((
        i.id,
        i.instance_type,
        i.placement['AvailabilityZone'],
        i.state['Name'],
        i.public_dns_name
        )))

if __name__ == '__main__':
    list_instances()
