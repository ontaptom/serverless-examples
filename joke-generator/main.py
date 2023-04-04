from flask import escape
import openai

def joke_generator(request):
    """
    A Google Cloud Function that generates a joke using the OpenAI API with the GPT-3.5-turbo model.

    The function takes an optional 'about' query parameter to request a joke about a specific topic.
    It sanitizes the user input using the 'escape' function from the Flask library to prevent cross-site scripting (XSS) attacks.
    The generated joke is returned as an HTML response.

    Args:
        request: A Flask request object containing the query parameters.

    Returns:
        An HTML string with the generated joke.
    """

    if request.args and 'about' in request.args:
        about = request.args.get('about')
        msg = f"Tell me a joke about {about}"

    else:
        msg = 'Tell me a joke'

    msg = escape(msg)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user","content": msg}
        ]
    )
    return f"<h2>{msg}</h2> <p>{response.choices[0]['message']['content']}</p>"
