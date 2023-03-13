from flask import Flask, request
from ecs import ECS
from ec2 import EC2
import boto3

#client = boto3.client('ecs')
#ec2 = boto3.resource('ec2')

app = Flask(__name__)
ecs = ECS()
ec2 = EC2()



@app.route('/<userName>')
def welcome(userName):
    return "Welcome, " + userName

######
#ECS Rest Endpoints
######

@app.route('/getECSClusters')
def getECSClusters():
    response = ecs.getCluststerList()
    return response

@app.route('/createCluster/<customClusterName>', methods = ['POST'])
def createCluster(customClusterName): 
    response = ecs.createCluster(customClusterName, request)
    return response

@app.route('/deleteCluster/<customClusterName>', methods = ['POST'])
def deleteCluster(customClusterName): 
    response = ecs.deleteCluster(customClusterName, request)
    return response

######
#EC2 Rest Endpoints
######
@app.route('/getInstanceIp/<instaceid>')
def getEC2InstanceIp(instaceid):
    response = ec2.getEC2Ip(instaceid)
    return response


######
#DB Rest Endpoints
######


######
#S3Rest Endpoints
######



if __name__ == "__main__":
    app.run()