# Insurance Call Quality Analyzer

Insurance Call Quality Analyzer is a tool specific to thoroughly analyzing Call Conversations against predefined Compliance/schema points set by any Insurance company and extracting entities for further Analysis. It uses the Large Language model - Llama-3-70B-instruct by Meta which is hosted on AWS Bedrock service to do compliance check within the transcript and extract necessary entities for further analysis using prompt engineering.

## Potential Use Case
This tool could be used not only for Insurance industry but for a wide variety of domains. This tool can be ideally used for compliance verification, proof-reading legal aggrements, data extraction and much more. The most interesting use case for Insurance industry could be extracting Insurance Agents data from a call and internally analyzing their performance and eventally identifying the gaps to fill in.

## Features

- **Schema verification/Compliance check**: Automatically checks a call transcript text against a set of predefined schema points to determine compliance.
- **Metadata Extraction**: Extracts key information from transcripts, such as dates, agent names, client names and other relevant details.
- **Interactive Web Interface**: Features a web-based interface where users can input transcripts and receive instant analysis results.

## How It Works

The tool processes input text through a series of steps:
1. **Preprocessing**: Text is cleaned and prepared for analysis, including stopword removal and tokenization.
2. **Schema Verification**: Each schema point is checked against the call transcript to verify its presence.
3. **Metadata Extraction**: Specific pieces of metadata are extracted from the call transcript.
4. **Result Presentation**: The analysis results are displayed on a web interface, allowing for easy review and understanding.


## Usage
Simply clone this repository, setup your own AWS Bedrock credentials and then you can run the gradio app using "python app.py"

## Future Work 
- The ouputs generated could be further used for in-depth analysis and internally rating the Insurance Agents performance.
- Current prompts could be further refined to get more accurate results from the model.
- Option for downloading the results could be provided to the user.
- Chats and plots for visualizing the results.

## Contributions
Contributions are welcome! If you would like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch: git checkout -b your-branch-name.
3. Make your changes and commit them: git commit -am 'Add some feature'
4. Push to the original branch: git push origin your-repository-name/your-branch-name
5. Create the pull request.

Feel Free to ping me on Linkedin if you would like to discuss more on this project or just for a chat.