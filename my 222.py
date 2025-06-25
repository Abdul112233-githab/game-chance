import openai

# Set your API key
openai.api_key = 'your-api-key-here'

# Define the conversation
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello, how are you?"}
]

# Make the API call
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages
)

# Print the assistant's reply
print("Assistant:", response['choices'][0]['message']['content'])