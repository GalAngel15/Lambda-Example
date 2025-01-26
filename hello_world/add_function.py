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


"""
import json

def add_handler(event, context):
    
    Lambda function to add two numbers and greet a user.
    

    try:
        # Get parameters from the event
        body = json.loads(event.get('body', '{}'))
        name = body.get('name', 'Guest')

        # Try to convert numbers safely
        num1 = int(body.get('num1', 0))
        num2 = int(body.get('num2', 0))

        # Perform addition
        result = num1 + num2

        # Return success response
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": f"Hello, {name}! \nThe sum of {num1} and {num2} is {result}."
            }),
        }

    except json.JSONDecodeError:
        # Handle invalid JSON
        return {
            "statusCode": 400,
            "body": json.dumps({
                "error": "Invalid JSON in request body."
            }),
        }

    except ValueError:
        # Handle invalid number conversion
        return {
            "statusCode": 400,
            "body": json.dumps({
                "error": "Invalid numbers provided. Please ensure num1 and num2 are valid integers."
            }),
        }

    except Exception as e:
        # Handle any other unexpected errors
        return {
            "statusCode": 500,
            "body": json.dumps({
                "error": f"An unexpected error occurred: {str(e)}"
            }),
        }

"""