from flask import Flask, request
from botocore.exceptions import ClientError
import boto3

app = Flask(__name__)

client = boto3.client('dynamodb')


class DYNAMODB:

    def createDynamoDBTable(self, tableName, request):
        if request.method == 'POST':
            table = client.create_table(
                TableName='ccproj2-' + tableName,
                KeySchema=[
                    {
                        'AttributeName': 'year',
                        'KeyType': 'HASH'  # Partition key
                    },
                    {
                        'AttributeName': 'title',
                        'KeyType': 'RANGE'  # Sort key
                    }
                ],
                AttributeDefinitions=[
                    {
                        'AttributeName': 'year',
                        'AttributeType': 'N'
                    },
                    {
                        'AttributeName': 'title',
                        'AttributeType': 'S'
                    },

                ],
                ProvisionedThroughput={
                    'ReadCapacityUnits': 10,
                    'WriteCapacityUnits': 10
                }
            )
        return table

    def addItemToDynamoDb(self, year, title, plot, rating, request):
        if request.method == 'PUT':
            response = client.put_item(
                TableName='ccproj2-movies',
                Item={
                    'year': {
                        'N': "{}".format(year),
                    },
                    'title': {
                        'S': "{}".format(title),
                    },
                    'plot': {
                        "S": "{}".format(plot),
                    },
                    'rating': {
                        "N": "{}".format(rating),
                    }
                }
            )
        return response

    def getItemsFromDB(self, titleKey, yearKey):
        try:
            response = client.get_item(
                TableName='ccproj2-movies',
                Key={
                    'year': {
                        'N': "{}".format(yearKey),
                    },
                    'title': {
                        'S': "{}".format(titleKey),
                    }
                }
            )
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            return response['Item']

    def deleteTableFromDb(self, tableName):
        response = client.delete_table(
            TableName='ccproj2-' + tableName,

        )
        return response
