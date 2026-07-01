from openai import OpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

model_deployment = "DeepSeek-V4-Flash"

# Connecting to the Azure OpenAI endpoint

token_provider = get_bearer_token_provider(
    DefaultAzureCredential(), "https://ai.azure.com/.default"
)

openai_client = OpenAI(  
  base_url = "https://ahmedgamalwork951-5403-resource.openai.azure.com/openai/v1",  
  api_key=token_provider,
)

##### using api key not Azure credential ( which require azure cli to be installed )
# openai_client = OpenAI(
#     api_key=os.getenv("AZURE_OPENAI_API_KEY"),
#     base_url="https://{resource-name}.openai.azure.com/openai/v1/"
# )


#### using environment vairables 
# If you set OPENAI_BASE_URL and OPENAI_API_KEY environment variables, the client uses them automatically:

# from openai import OpenAI

# openai_client = OpenAI()  # Uses environment variables



#### using AzureOpenAI

# import os
# from openai import AzureOpenAI

# openai_client = AzureOpenAI(
#     azure_endpoint = "https://{resource-name}.openai.azure.com"
#     api_key=os.getenv("AZURE_OPENAI_KEY"),  
#     api_version="2024-10-21",
# )



#### chat completions api not Responses API
 
# response = openai_client.chat.completions.create(
#     model="DeepSeek-V4-Flash",
#     input="Write a one-sentence bedtime story about a unicorn."
# )


# Generate a response using the Responses API #######################


##### normal basic query
# response = openai_client.responses.create(
#     model="DeepSeek-V4-Flash",  # Your model deployment name
#     input="What is Microsoft Foundry?"
# )

# print(f"Response: {response.output_text}")
# print(f"Response ID: {response.id}")
# print(f"Tokens used: {response.usage.total_tokens}")
# print(f"Status: {response.status}")

##### adding instruction 
# response = openai_client.responses.create(
#     model="DeepSeek-V4-Flash",
#     instructions="You are a helpful AI assistant that answers questions clearly and concisely.",
#     input="Explain neural networks."
# )

# print(response.output_text)

##### tuning generation params like temp or max output tokens 
# temperature: Controls randomness (0.0-2.0). Higher values make output more creative and varied
# max_output_tokens: Limits the maximum number of tokens in the response
# top_p: Alternative to temperature for controlling randomness

# response = openai_client.responses.create(
#     model="gpt-4.1",
#     instructions="You are a helpful AI assistant that answers questions clearly and concisely.",
#     input="Write a creative story about AI.",
#     temperature=0.8,  # Higher temperature for more creativity
#     max_output_tokens=200  # Limit response length
# )

# print(response.output_text)



##### some multi trun conversation 

# # Track responses
# last_response_id = None

# # Loop until the user wants to quit
# print("Assistant: Enter a prompt (or type 'quit' to exit)")
# while True:
#     input_text = input('\nYou: ')
#     if input_text.lower() == "quit":
#         print("Assistant: Goodbye!")
#         break

#     # Get a response
#     response = openai_client.responses.create(
#                 model="DeepSeek-V4-Flash",
#                 instructions="You are a helpful AI assistant that explains technology concepts clearly.",
#                 input=input_text,
#                 previous_response_id=last_response_id
#     )
#     assistant_text = response.output_text
#     print("\nAssistant:", assistant_text)
#     last_response_id = response.id


##### For streaming baby 

def main():
    stream = openai_client.responses.create(
        model=model_deployment,
        input="Write a short story about a robot learning to paint.",
        stream=True,
    )

    for event in stream:
        if event.type == "response.output_text.delta":
            print(event.delta, end="", flush=True)
        elif event.type == "response.output_text.done":
            print()


if __name__ == "__main__":
    main()
