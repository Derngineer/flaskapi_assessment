# flaskapi_assessment
TASK 3: Develop and Deploy an API on AWS Lambda or Azure

Solution: Flask Calculator app via Azure App service


Endpoint: https://flaskttest.azurewebsites.net/

The app runs basic addition and subtraction operations for two variable x and y

Recommend using postman to send request in json format
Pick url endpoint:

Add - ‘add/’
Subtract -’subtract/’

Navigate to postman, under Body choose raw and set request data in json format as follows

{
 "x": 20,
 "y": 10
}
Send  a post request

Your response will be as follows

{
   "result": 30
}
