# ASCII Art Generator

This serverless application takes an input message and returns its ASCII art representation. It's designed to work as a Google Cloud Function, responding to HTTP requests.

## How it works

The function listens for an incoming HTTP request and checks for a query parameter named `message`. If the parameter is present, the function generates ASCII art based on the input message. If no message is provided, it defaults to "Hello World!".

The output is wrapped in `<pre>` tags to ensure correct formatting when displayed in a browser.
Deployment

To deploy this function on Google Cloud Functions, follow these steps:

1. Install the art library and the Google Cloud SDK, if you haven't already.

2. Create a requirements.txt file in the same directory as your main.py file (which contains the hello_world function). Add the following line to the file:

```
art
```

You can deploy the function from Console or via gcloud command-line tool:

```
gcloud functions deploy hello_ascii \
  --runtime python310 \
  --trigger-http \
  --allow-unauthenticated \
  --entry-point hello_ascii
```

You can replace `python310` with the appropriate Python runtime if necessary.

After deployment, you will receive a URL for your function. Use this URL to access the ASCII art generator. You can append the message query parameter to the URL to generate ASCII art based on your input:

```
https://<REGION-PROJECT_ID>.cloudfunctions.net/hello_world?message=example
```

For more information on deploying Google Cloud Functions, refer to the official documentation.

## License

This application is released under the Apache License 2.0. For more information, see the LICENSE file in the main repository.