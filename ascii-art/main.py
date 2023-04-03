from flask import escape
from art import *

def hello_ascii(request):
    """
    Responds to an HTTP request with ASCII art representation of the provided message.
    
    Args:
        request (flask.Request): HTTP request object containing query parameters.
    
    Query Parameters:
        message (str): The input message to be converted into ASCII art. If not provided,
                       the function will use the default message 'Hello World!'.
    
    Returns:
        str: The ASCII art representation of the input message wrapped in <pre> tags.
    """
    if request.args and 'message' in request.args:
        msg = request.args.get('message')

    else:
        msg = 'Hello'

    msg = escape(msg)
    Art = text2art(msg, font='block', chr_ignore=True)
    return f"<pre>{Art}</pre>"
