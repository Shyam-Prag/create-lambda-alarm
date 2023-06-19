# create-lambda-alarm

Lambda function which loops through a list of function names and creates a cloudwatch alarm for each functions provided the below JSON input:
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
3. No limit to number of Lambda functions you can input into the JSON payload. Adjust according to your use-case. (Do not insert invalid function name.. No error handling has been implemented. Failed requests would need to be retried)
