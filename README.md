# create-lambda-alarm

Lambda function which creates a cloudwatch alarm for a number of functions provided the below JSON input:
```
{
    "metrics":[
     {
        "alarm_name":"LambdaErrorCount-Function1",
        "alarm_description":"Alarm - function Function1 threw an error",
        "dimensions_function_name" : "Function1"
    },    
    {
        "alarm_name":"LambdaErrorCount-Function2",
        "alarm_description":"Alarm - function Function2 threw an error",
        "dimensions_function_name":"Function2"
    },
    {
        "alarm_name":"LambdaErrorCount-Function3",
        "alarm_description":"Alarm - function Function3 threw an error",
        "dimensions_function_name" : "Function3"
    },
    {
        "alarm_name":"LambdaErrorCount-Function4",
        "alarm_description":"Alarm - function Function4 threw an error",
        "dimensions_function_name" : "Function4"
    }
    ]
}
```
NOTE:
1. lambda_function.py creates an alarm for each Lambda function name provided within the metrics list(dimensions_function_name). This can be inserted into as a 'test event' within the AWS Lambda console. 
2. This function triggeres an SNS topic (insert SNS ARN in line 36) in which you can get email notified whenever your function throws an error. 
