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
        joke_topic = f"Tell me a joke about {about}"

    else:
        joke_topic = 'Tell me a joke'

    joke_topic = escape(joke_topic)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user","content": joke_topic}
        ]
    )

    joke_content = response.choices[0]['message']['content']
    return print_html(joke_topic, joke_content)

def print_html(joke_topic, joke_content):
    """
    This function takes a joke topic and content and wraps them in HTML with a specific style.

    Args:
        joke_topic: The topic of the joke.
        joke_content: The content of the joke.

    Returns:
        An HTML string with the joke nicely formatted.
    """

    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #333;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 30vh;
                margin: 0;
                color: #f2f2f2;
            }}
            .joke-container {{
                background-color: #444;
                border-radius: 8px;
                padding: 20px;
                max-width: 600px;
                box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.2);
            }}
            h2 {{
                font-size: 24px;
                color: #ff6347;
                margin-bottom: 10px;
            }}
            p {{
                font-size: 16px;
                color: #ccc;
                line-height: 1.5;
                margin-bottom: 0;
            }}
        </style>
    </head>
    <body>
        <div class="joke-container">
            <h2>{joke_topic}</h2>
            <p>{joke_content}</p>
        </div>
    </body>
    </html>
    """
    return html
