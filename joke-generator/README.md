# Joke Generator - Google Cloud Function

This repository contains an example Google Cloud Function that generates a joke using the OpenAI API with the GPT-3.5-turbo model. The function is designed to be deployed as a serverless application on Google Cloud Functions.

## Deployment

To deploy the joke_generator function on Google Cloud Functions, follow these steps:

1. Install the [Google Cloud SDK](https://cloud.google.com/sdk/docs/install) if you haven't already.
2. Authenticate with your Google Cloud account using the command: `gcloud auth login`.
3. Set the project you want to use for the deployment with the command: `gcloud config set project YOUR_PROJECT_ID`.
4. Clone this repository or download the `main.py` file containing the `joke_generator` function and `requirements.txt`.
5. Navigate to the folder containing the `main.py` and `requirements.txt` files.
6. Run the following command to deploy the function:
```
gcloud functions deploy joke_generator \
--entry-point joke_generator \
--runtime python39 \
--trigger-http \
--set-env-vars OPENAI_API_KEY=<your-openai-api-key>
```

## Usage 

After deployment, you will receive a URL for your function. Use this URL to access the Joke Generator. You can append the topic of a joke in the URL to generate ASCII art based on your input:

```
https://<REGION-PROJECT_ID>.cloudfunctions.net/joke_generator?about=programmers
```

For more information on deploying Google Cloud Functions, refer to the official documentation.
