from flask import Flask, request
from ecs import ECS
from ec2 import EC2
from dynamo import DYNAMODB
import boto3

#client = boto3.client('ecs')
#ec2 = boto3.resource('ec2')

app = Flask(__name__)
ecs = ECS()
ec2 = EC2()
dynamodb = DYNAMODB()


@app.route('/<userName>')
def welcome(userName):
    return "Welcome, " + userName

######
# ECS Rest Endpoints
######


@app.route('/getECSClusters')
def getECSClusters():
    response = ecs.getCluststerList()
    return response


@app.route('/createCluster/<customClusterName>', methods=['POST'])
def createCluster(customClusterName):
    response = ecs.createCluster(customClusterName, request)
    return response


@app.route('/deleteCluster/<customClusterName>', methods=['POST'])
def deleteCluster(customClusterName):
    response = ecs.deleteCluster(customClusterName, request)
    return response

######
# EC2 Rest Endpoints
######


@app.route('/getInstanceIp/<instaceid>')
def getEC2InstanceIp(instaceid):
    response = ec2.getEC2Ip(instaceid)
    return response


######
# DB Rest Endpoints
######

@app.route('/createDynamoDBTable/<tableName>', methods=['POST'])
def createDynamoDBTable(tableName):
    response = dynamodb.createDynamoDBTable(tableName, request)
    return response


@app.route('/addItemToDynamoDb', methods=['PUT'])
# http://127.0.0.1:5000/addItemToDynamoDb?title=GOT&year=2019&plot=basic%20movie2&rating=2.5
def addItemToDynamoDb():
    year = request.args.get('year')
    title = request.args.get('title')
    plot = request.args.get('plot')
    rating = request.args.get('rating')
    response = dynamodb.addItemToDynamoDb(year, title, plot, rating, request)
    return response


@app.route('/getItemsFromDB', methods=['GET'])
# http://127.0.0.1:5000/getItemsFromDB?title=GOT&year=2019
def getItemsFromDB():
    titleKey = request.args.get('title')
    yearKey = request.args.get('year')
    response = dynamodb.getItemsFromDB(titleKey, yearKey)
    return response


@app.route('/deleteTable/<tableName>', methods=['GET'])
# http://127.0.0.1:5000/deleteTable/movies
def deleteDynamoTable(tableName):
    response = dynamodb.deleteTableFromDb(tableName)
    return response


######
# S3Rest Endpoints
######


if __name__ == "__main__":
    app.run()
