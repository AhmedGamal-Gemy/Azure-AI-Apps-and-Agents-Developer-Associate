1. okay first things first 

microsoft foundry is a platform for ai development on top of microsoft azure and has microsoft foundry portal for web based ui




2. okay so everything we are working on from code to connections to data is in projects which ran on top of resources ( the actual processing and data storage and different allowed ai tools)

3. To simplify integration with multiple sources of knowledge, you can use Foundry IQ in a project to create a single, central MCP-based knowledge connection.

interesting stuff this foundry iq

4. Microsoft Foundry includes Foundry Tools like 

Azure Language in Foundry Tools provides models and APIs that you can use to analyze natural language text and perform tasks such as entity extraction, sentiment analysis, and summarization. Azure Language also provides functionality to help you build conversational language models and question answering solutions.

Azure Speech in Foundry Tools provides APIs that you can use to implement text to speech and speech to text transformation, as well as real-time live speech for conversational apps and agents.

Azure Translator in Foundry Tools uses state-of-the-art language models to translate text between a large number of languages.

With Azure Document Intelligence in Foundry Tools, you can use pre-built or custom models to extract fields from complex documents such as invoices, receipts, and forms.

Azure Content Understanding in Foundry Tools provides multi-modal content analysis capabilities that enable you to build models to extract data from forms and documents, images, videos, and audio streams.

5. foundry has extenstion for vs code which help manage resources, deployed agents, models, tools, etc

6. facing problems when trying to deploy models because of quota while in the free tiral

Before you use a resource provider, make sure your Azure subscription is registered for the resource provider. Registration configures your subscription to work with the resource provider.

here's how i guess : https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/resource-providers-and-types

these are the services you should enable from resource providers i guess :

Microsoft.CognitiveServices

Microsoft.MachineLearningServices
Microsoft.Search
Microsoft.


nope this is not the problem



okay something useful here to see the limits of models you can use in the current tier of the resource you should go here and enable show all 

https://ai.azure.com/nextgen/r/lzLKfF_0RzKl0qMRgb3Lrw,rg-ahmed.gamal.work951-1442,,ahmedgamalwork951-5403-resource,ahmedgamalwork951-5403/operate/quota/token-per-minute


okay okay okay i think i solve this ? just fully unlock this free trial by enabling the pay as you go shit ( and i have 200 dollar so it's free )

and i added budget for more secure i guess :

https://portal.azure.com/#view/Microsoft_Azure_GTM/Billing.MenuView/~/budgets/scopeId/%2Fproviders%2FMicrosoft.Billing%2FbillingAccounts%2Fc0729b32-37c3-5764-e188-31618467aa8c%3A00e98025-5297-482d-a2ad-b11b90646d86_2019-05-31/scope/BillingAccount

okay budge is for alerts not true hard limit i guess



7.

In the Foundry portal, in the top menu bar, select Operate.

The operation center is where you can monitor your projects, view alerts, monitor agent performance and quotas, and manage resources.

The resource level relates to the Foundry resource that was created in Azure to support your project. This resource includes connections to Foundry Services and models; and provides a central place to manage user access to AI development projects.
The project level relates to your individual project, where you can add and manage project-specific resources. A resource can support multiple projects (the first one created is the resource’s default project).


Note the key, project endpoint, and Azure OpenAI endpoint.

This information is used to connect to your project-level resouces from client applications.

The key is used for key-based authentication to models and tools (though in most production scenarios you should consider using Microsoft Entra ID authentication based on authenticated user and application identities).
The project endpoint is used to access models provided directly in Foundry (including OpenAI models) using the OpenAI Responses API, and to access Foundry-specific APIs (such as the Foundry Agent service).
The OpenAI endpoint is used to access models using OpenAI APIs, including the Chat Completions API and the Responses API.




7. okay the vs code extension is AMAZING 

https://microsoftlearning.github.io/mslearn-ai-studio/Instructions/Exercises/01-Explore-ai-studio.html


8. here's something in the end that is critical :

Clean up
If you’ve finished exploring Foundry portal, you should delete the resources you have created in this exercise to avoid incurring unnecessary Azure costs.

In the Azure portal at https://portal.azure.com, view the contents of the resource group where you deployed the resources used in this exercise.
On the toolbar, select Delete resource group.
Enter the resource group name and confirm that you want to delete it.