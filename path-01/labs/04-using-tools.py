from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import glob

module_path = Path(__file__).resolve().with_name("03-generative-ai-chat-app.py")
spec = spec_from_file_location("chat_app", module_path)
assert spec is not None and spec.loader is not None

chat_app = module_from_spec(spec)
spec.loader.exec_module(chat_app)

client = chat_app.openai_client
model_deployment = chat_app.model_deployment

print("Creating the vector stores and update files")

vector_store = client.vector_stores.create(
    name= "travel-brochures"
)

file_streams = [open(f, "rb") for f in glob.glob("pdfs/*.pdf")]
if not file_streams:
     print("No PDF files found in the brochures folder!")
     

file_batch = client.vector_stores.file_batches.upload_and_poll(
    vector_store_id=vector_store.id,
     files=file_streams
)

for f in file_streams:
     f.close()
print(f"Vector store created with {file_batch.file_counts.completed} files.")

last_response_id = None

# Get a response using tools
response = client.responses.create(
     model=model_deployment,
     instructions="""
     You are a travel assistant that provides information on travel services available from different sources.
     Answer questions about services offered using the provided travel brochures.
     Search the web for general information about destinations or current travel advice.
     """,
     input="I want to plan a trip to the pyramids in giza",
     previous_response_id=last_response_id,
     tools=[
         {
             "type": "file_search",
             "vector_store_ids": [vector_store.id]
         },
         {
             "type": "web_search"
         }
     ]
)
print(response.output_text)
last_response_id = response.id



# response = client.responses.create(
#     model=model_deployment,
#     instructions="You are an AI assistant that provides information. Use the python tool to run code for math problems.",
#     input="What is the square root of 16?",
#     # Specify available tools as a JSON list
#     tools=[
#         { 
#             "type" : "code_interpreter",
#             "container" : {"type" : "auto"}
#         },
#     ]
# )

# print(response)

