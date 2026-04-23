import joson

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps('Hello updated CICD Lambda from vscode')
    }