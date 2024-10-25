# PDF Summarizer

## Description

PDF Summarizer is a tool designed to process and summarize scientific articles in PDF format. It extracts text from PDFs, sends the content to OpenAI's GPT-4 model for summarization, and organizes the responses in designated folders. This tool is particularly useful for researchers and professionals who need concise summaries of extensive documents.

## Features

- **PDF Extraction**: Extracts text from PDF files using `pypdf`.
- **Summarization**: Utilizes OpenAI's GPT-4o-mini model to generate summaries based on user-defined prompts.
- **Organized Output**: Stores summarized responses in a structured folder system for easy access.
- **Error Handling**: Robust error handling to manage issues during PDF processing and API interactions.

## Installation

1. **Clone the Repository**

   ```bash
   gh repo clone javierpa95/Summerize_Articles
   cd Summerize_Articles
   ```

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**

   Create a `.env` file in the root directory and add your OpenAI API key:

   ```env
   OPENAI_API_KEY=your_openai_api_key
   ```

## Usage

1. **Prepare Your PDFs**

   Place all the PDF files you want to summarize in a directory, e.g., `ruta/ejemplo/`.

2. **Run the Summarizer**

   ```bash
   python summerize.py
   ```

   This will process all PDFs in the specified directory, generate summaries using GPT-4o-mini, and save the responses in a `respuestas` folder within each PDF's directory.

## Project Structure

- `summerize.py`: Main script to process and summarize PDFs.
- `resumen/`: Module containing processors and OpenAI client.
  - `processors.py`: Handles the processing of articles and generation of final summaries.
  - `openai_client.py`: Manages interactions with OpenAI's API.
  - `pdf_handler.py`: Manages PDF text extraction.
- `requirements.txt`: Lists all Python dependencies.
- `README.md`: Project documentation.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.



