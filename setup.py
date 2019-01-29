from setuptools import setup

setup(
    name='snapshotalyzer-30000',
    version='0.1',
    author='Robin Norwood',
    author_email='robin@acloud.guru',
    description='SnapshotAlyzer 30000 is a tool to manage EC2 snapshots',
    license='GPLv3+',
    packages=['ec2snap'],
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points="""
        [console_scripts]
        ec2snap=ec2snap.ec2snap:cli
    """
)
