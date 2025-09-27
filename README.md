# Langchain Output Parsers Demo

A comprehensive collection of demonstrations showcasing different types of output parsers available in LangChain. This repository provides practical examples of how to structure and parse LLM outputs using various parsing techniques.

## 🎯 Overview

LangChain output parsers are essential components that help structure and validate the responses from Large Language Models (LLMs). This repository demonstrates four key types of output parsers:

- **String Output Parser** - Simple string formatting and processing
- **JSON Output Parser** - Structured JSON responses 
- **Pydantic Output Parser** - Type-safe data validation using Pydantic models
- **Structured Output Parser** - Custom structured responses with schema validation

## 📁 Repository Structure

```
Langchain_Output_Parsers_Demo/
├── str_ouput_parser_demo.py          # String Output Parser examples
├── json_output_parser_demo.py        # JSON Output Parser examples  
├── pydantic_output_parser_demo.py    # Pydantic Output Parser examples
├── structured_output_parser_demo.py  # Structured Output Parser examples
├── requirements.txt                   # Project dependencies
├── pyproject.toml                    # Project configuration
├── demo_env/                         # Virtual environment
└── README.md                         # This file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- HuggingFace API key (for running the demos)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ratulchowdhury/Langchain_Output_Parsers_Demo.git
   cd Langchain_Output_Parsers_Demo
   ```

2. **Create and activate virtual environment:**
   ```bash
   python -m venv demo_env
   
   # On Windows
   demo_env\Scripts\activate
   
   # On macOS/Linux
   source demo_env/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Create a `.env` file in the root directory and add your HuggingFace API key:
   ```
   HUGGINGFACE_API_KEY=your_huggingface_api_key_here
   ```

## 📚 Demo Files Description

### 1. String Output Parser (`str_ouput_parser_demo.py`)
Demonstrates the basic string output parsing functionality:
- Simple string responses from LLMs
- Basic text processing and formatting
- Ideal for straightforward text generation tasks

### 2. JSON Output Parser (`json_output_parser_demo.py`)
Shows how to get structured JSON responses:
- Parsing LLM output into JSON format
- Handling structured data extraction
- Error handling for malformed JSON

### 3. Pydantic Output Parser (`pydantic_output_parser_demo.py`)
Illustrates type-safe parsing using Pydantic models:
- Define data models with type hints
- Automatic validation and error handling
- Converting LLM output to Python objects
- Data integrity and type safety

### 4. Structured Output Parser (`structured_output_parser_demo.py`)
Demonstrates custom structured output parsing:
- Define custom response schemas
- Flexible field definitions
- Schema-based validation
- Multiple field types support

## 🛠️ Usage Examples

Each demo file can be run independently:

```bash
# Run String Output Parser demo
python str_ouput_parser_demo.py

# Run JSON Output Parser demo
python json_output_parser_demo.py

# Run Pydantic Output Parser demo
python pydantic_output_parser_demo.py

# Run Structured Output Parser demo
python structured_output_parser_demo.py
```

## 📋 Dependencies

Key packages used in this project:

- **langchain** - Core LangChain framework
- **langchain-core** - Essential LangChain components
- **langchain-huggingface** - HuggingFace integration
- **pydantic** - Data validation and parsing
- **python-dotenv** - Environment variable management
- **transformers** - Transformer models support
- **torch** - PyTorch backend

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Useful Links

- [LangChain Documentation](https://python.langchain.com/)
- [HuggingFace API Documentation](https://huggingface.co/docs/api-inference/index)
- [Pydantic Documentation](https://docs.pydantic.dev/)

## ⚠️ Notes

- Make sure to keep your API keys secure and never commit them to version control
- The demos use HuggingFace endpoints, which may have rate limits
- Some demos may require specific model permissions or subscriptions

---

**Author:** Ratul Chowdhury  
**Repository:** [Langchain_Output_Parsers_Demo](https://github.com/ratulchowdhury/Langchain_Output_Parsers_Demo)