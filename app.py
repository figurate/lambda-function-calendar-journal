import boto3


def handler(event, context):
    print(f'Received event: {event}')


def create_entry(data):
    ddb = boto3.client('dynamodb')


def update_entry(data):
    ddb = boto3.client('dynamodb')


def list_revisions(uid):
    ddb = boto3.client('dynamodb')


def search(criteria):
    ddb = boto3.client('dynamodb')
