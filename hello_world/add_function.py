import json

# import requests


def add_handler(event, context):
    """
    Lambda function to add two numbers and greet a user.
    """

     # Get parameters from the event
    body = json.loads(event.get('body', '{}'))
    name = body.get('name', 'Guest')
    num1 = body.get('num1', 0)
    num2 = body.get('num2', 0)

     # Perform addition
    result = num1 + num2

    # Return response
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": f"Hello, {name}! \nThe sum of {num1} and {num2} is {result}."
            }),
    }
