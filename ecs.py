from flask import Flask
import boto3

app = Flask(__name__)

client = boto3.client('ecs')

class ECS:

    def welcomeToECS():
        return "Hello!"
    
    def getCluststerList(self):
        response = client.list_clusters()
        return response
    
    def createCluster(self, customClusterName, request): 
        if request.method == 'POST':
            response = client.create_cluster(
            #clusterName='ccproj2-mycluster2'
            clusterName=customClusterName
        )
        return response
    
    def deleteCluster(self, customClusterName, request): 
        if request.method == 'POST':
            response = client.delete_cluster(
            cluster=customClusterName
            )
        return response

