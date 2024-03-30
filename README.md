# PDF Retrieval Augmented Generation (RAG) Application
This is a public repository to build a PDF Retrieval Augmented Generation (RAG) Application for customised queries of any PDF.


## What Is Retrieval Augmented Generation, or RAG?
Retrieval augmented generation, or RAG, is an architectural approach that can improve the efficacy of large language model (LLM) applications by leveraging custom data. This is done by retrieving data/documents relevant to a question or task and providing them as context for the LLM. RAG has shown success in support chatbots and Q&A systems that need to maintain up-to-date information or access domain-specific knowledge.

## Instructions for Usage
To utilize this repository effectively:

1. Navigate to the Directory Where You Want to Clone the Repository:
Use the cd command to navigate to the directory where you want to clone the repository. 
```shell
cd /path/to/destination/directory
```

2. Clone the Repository:
Use the git clone command followed by the URL of this repository:

```shell
git clone https://github.com/stephaniec2020/PDF-RAG-App.git
```

3. Set up Keys File:
Create a `keys.json` file within the repository. Modify the `OPENAI_API_KEY` and `HUGGINGFACEHUB_API_TOKEN` key-value pairs with your respective API keys.

4. Generate `.env` File:
Execute the `dotenv_script.py` script using Python. 
```shell
python dotenv_script.py
```

This script will parse the `keys.json` file and generate a corresponding `.env` file containing the specified keys.

5. Environment Configuration:
Ensure that the generated `.env` file is properly configured with your API keys.

With these steps completed, you can seamlessly integrate your API keys into the application, enabling the functionalities of the PDF Retrieval Augmented Generation (RAG) Application.
