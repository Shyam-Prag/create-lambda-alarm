import json
import boto3
client = boto3.client('cloudwatch')
def lambda_handler(event, context):
    # TODO implement
    print(event)
    iteration=1
    for i in event['metrics']:
        
        print(f'iteration => {iteration}')
        iteration +=1
        alarm_name = i['alarm_name']
        print(f'alarm_name => {alarm_name}')
        
        alarm_description = i['alarm_description']
        print(f'alarm_description => {alarm_description}')
        
        dimensions_function_name = i['dimensions_function_name']
        print(f'dimensions_function_name => {dimensions_function_name}')
        
        response = client.put_metric_alarm(
        AlarmName=alarm_name,
        AlarmDescription=alarm_description,
        ActionsEnabled = True,
        MetricName='Errors',
        Namespace='AWS/Lambda',
        Statistic = 'Sum',
        Period=60,
        Threshold=1,
        ComparisonOperator='GreaterThanOrEqualToThreshold',
        Dimensions=[{
            "Name": "FunctionName",
            "Value": dimensions_function_name
        }],
        EvaluationPeriods=1,
        AlarmActions = ['<YOUR_SNS_ARN>'], #SNS ARN to get notified toward
        TreatMissingData='notBreaching'
        )
        
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
