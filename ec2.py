from flask import Flask
import boto3
#import requests

app = Flask(__name__)
ec2 = boto3.resource('ec2')


class EC2:

    @app.route('/getInstanceIp/<instaceid>')
    def getEC2Ip(self, instaceid):
        #instance_ids = ['i-02e78ed205340ff15']
        instance = ec2.Instance(instaceid)
        print("EC2 server: ", instance.public_dns_name)
        return instance.public_dns_name
