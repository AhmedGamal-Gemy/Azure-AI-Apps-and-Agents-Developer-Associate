1. for code interpreter tool ( which execute code in a sandboxed container in azure and return the results ) there are some notes for it 

any the specifics is in the lab

Best practices
Be specific: Describe the data format and expected output clearly. Many models internally use the name python tool to identify the code_interpreter tool - so use this language in your instructions.
Provide context: Include relevant domain knowledge in your prompts
Validate results: Always review AI-generated code for correctness before using in production
Monitor costs: Code execution adds tokens; complex operations may use more resources
Leverage libraries: Common packages like pandas, numpy, and matplotlib are pre-installed
Error handling: The model can see errors and will attempt to fix them automatically
Limitations to know about
Executions run in a sandboxed environment with no external network access
Some libraries may not be available; let the model know if a standard library fails
Timeout limits apply to long-running operations
Code runs with memory constraints—massive datasets may need streaming or chunking



2. another day another tool. tool lazy to extract notes from this here is the all thing :

Skip to main content
Learn

Training
Level 3

0/3699 XP
LearnTrainingBrowseDevelop generative AI apps in AzureDevelop generative AI apps that use tools
Use the web_search tool
Completed
100 XP
5 minutes
Choose your preferred content format
The web_search tool enables your model to retrieve fresh information from the web while generating a response.

What is the web_search tool?
The web_search tool gives a generative AI model access to current, external information at runtime. Instead of relying only on training data, the model can issue a search query, review relevant sources, and produce an answer grounded in up-to-date content.

This is especially useful when facts may change frequently, such as pricing, product releases, policy updates, or current events.

Key features include:

Live information retrieval - Get recent information not available in static model training data
Source-grounded responses - Build answers from retrieved web content
Reduced hallucination risk - Improve reliability by checking external sources
Automatic query generation - The model decides when and how to search based on user intent
Seamless user experience - Search and response generation happen in one flow
Common use cases
Use Case	Example
Current Events	Summarize key updates on a breaking technology announcement
Market Research	Compare recent product features or pricing across vendors
Policy Monitoring	Check whether regulations or guidance have changed
Fact Verification	Validate claims against reputable public sources
A simple example
Here's a minimal example using the OpenAI Responses API with web search enabled:

Python
from openai import OpenAI

client = OpenAI(
    base_url={openai_endpoint},
    api_key={auth_key_or_token}
)

# Get response using the web_search tool
response = client.responses.create(
    model={model_deployment},
    instructions="You are an AI assistant. Use web search when current information is required.",
    input="What are three major announcements from Microsoft Build this week?",
    tools=[{"type": "web_search"}]
)

print(response.output_text)
The output will vary based on current web results, but it should include a concise answer grounded in recent sources.

How the web_search tool works
The general process for using the web_search tool is:

You send a request - Include a web search tool in the tools array.
Model evaluates the question - It decides whether fresh web data is needed.
Search is performed - The model issues one or more search queries.
Results are reviewed - Relevant pages are selected and summarized.
Response is generated - The model combines search findings into the final answer.
Best practices
Ask time-aware questions clearly - Include words like "latest", "current", or date ranges when needed
Set expectations for sources - Prompt for reputable or official sources when accuracy matters
Request concise outputs - Ask for short summaries with key points to reduce noise
Verify critical facts - For high-stakes scenarios, independently validate important claims
Track usage and latency - Web retrieval can increase response time and token usage
Limitations to know about
Results depend on what is publicly available and indexable at query time
Source quality can vary, so output may still require human review
Retrieved content may change over time, so repeated runs can produce different answers
Some environments may apply regional, policy, or network restrictions to web access
Used well, web_search helps your model move from static knowledge to timely, source-aware answers that are more useful in real-world workflows.

Next unit: Use the file_search tool
Need help? See our troubleshooting guide or provide specific feedback by reporting an issue.
Feedback
Was this page helpful?

AI Disclaimer
Previous Versions
Blog
Contribute
Privacy
Consumer Health Privacy
Terms of Use
Trademarks
© Microsoft 2026

3. file search tool is essentially a rag. too lazy this time too :

Skip to main content
Learn

Training
Level 3

100/3699 XP
LearnTrainingBrowseDevelop generative AI apps in AzureDevelop generative AI apps that use tools
Use the file_search tool
Completed
100 XP
5 minutes
Choose your preferred content format
The file_search tool lets your model retrieve relevant information from your own uploaded documents during a response.

What is the file_search tool?
The file_search tool helps a model answer questions using private or domain-specific files, such as policy documents, manuals, contracts, and internal knowledge bases. Instead of relying only on general training data, the model can search indexed file content and return grounded answers.

This is especially useful when you need accurate responses from trusted internal documents.

Key features include:

Document-grounded answers - Responses are based on your uploaded files
Semantic retrieval - Finds relevant passages by meaning, not only exact keyword matches
Vector store integration - Search across one or more indexed document collections
Citations and transparency - Include matched results for debugging and traceability
Better enterprise relevance - Use organization-specific knowledge in model outputs
Common use cases
Use Case	Example
Policy Q&A	Answer employee questions from HR policy PDFs
Support Assistants	Retrieve product steps from internal troubleshooting guides
Legal Review	Locate specific clauses across contract documents
Knowledge Discovery	Summarize answers from technical documentation sets
A simple example
Here's an example using the OpenAI Responses API with file_search enabled:

Python
from openai import OpenAI

client = OpenAI(
    base_url={openai_endpoint},
    api_key={auth_key_or_token}
)

# Create vector store and upload a file
vector_store = client.vector_stores.create(name="policy-docs")
client.vector_stores.files.upload_and_poll(
    vector_store_id=vector_store.id,
    file=open("expenses_policy.pdf", "rb")
)

# Get response using the file_search tool
response = client.responses.create(
    model=model_deployment,
    instructions="You are an AI assistant that provides information from HR policy documents.",
    input="What's the maximum amount I can claim for a taxi ride?",
    tools=[{
        "type": "file_search",
        "vector_store_ids": [vector_store.id]
    }],
    include=["file_search_call.results"]
)
print(response.output_text)
In this flow, the model searches the indexed policy file and uses the retrieved passages to produce a grounded answer.

How the file_search tool works
The general process for using the file_search tool is:

You prepare files - Upload documents to a vector store.
You send a request - Include file_search in the tools array with vector store IDs.
Model performs retrieval - It searches indexed chunks for relevant content.
Results are injected - Matching passages are provided to the model.
Response is generated - The model answers using retrieved document context.
Best practices
Use high-quality source files - Clean, current documents improve retrieval accuracy
Write focused prompts - Ask specific questions to reduce ambiguous matches
Scope vector stores carefully - Separate domains (HR, legal, finance) when helpful
Include retrieval results in development - Use response includes for troubleshooting
Review answers for critical workflows - Keep human validation in high-stakes scenarios
Limitations to know about
Answer quality depends on document quality, coverage, and chunk relevance
Very large or mixed-domain stores can return less focused context
Updated source files may require re-indexing before new content is searchable
Retrieval improves grounding but doesn't replace human review for sensitive decisions
Used well, file_search turns a general-purpose model into a domain-aware assistant that can answer from the documents your team actually uses.

 Note

The file_search tool is a great way to ground a model in a specific set of documents or data files. However, for enterprise-scale agents that need to access large quantities of data in multiple data stores, you should consider using the Foundry IQ knowledge store solution with a Microsoft Foundry agent. To learn more, see Build knowledge-enhanced AI agents with Foundry IQ

Next unit: Use the function tool
Need help? See our troubleshooting guide or provide specific feedback by reporting an issue.
Feedback
Was this page helpful?

AI Disclaimer
Previous Versions
Blog
Contribute
Privacy
Consumer Health Privacy
Terms of Use
Trademarks
© Microsoft 2026



IMPORTANT ADDIATION i can make vector stores in azure foundry this way :


# Create vector store and upload a file
vector_store = client.vector_stores.create(name="policy-docs")
client.vector_stores.files.upload_and_poll(
    vector_store_id=vector_store.id,
    file=open("expenses_policy.pdf", "rb")
)


another important note :

 Note

The file_search tool is a great way to ground a model in a specific set of documents or data files. However, for enterprise-scale agents that need to access large quantities of data in multiple data stores, you should consider using the Foundry IQ knowledge store solution with a Microsoft Foundry agent. To learn more, see Build knowledge-enhanced AI agents with Foundry IQ


4. function tools are basicly custom functions implemented by the developers :

        {
            "type": "function",
            "name": "get_time",
            "description": "Get the current time"
        }

5. OKay okay important notes here :

Further reading
To learn more about using tools with models, see the following resources:

OpenAI developer guide: Tools
OpenAI developers Guide: Function calling

