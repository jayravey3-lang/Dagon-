# Dagon - Advanced Conversational AI

An advanced conversational AI assistant inspired by Meta's AI models. Dagon is designed to engage in meaningful conversations, provide helpful information, and assist with various tasks using natural language processing and machine learning.

## ✨ Features

### Core Features
- **Conversational AI**: Natural language understanding and generation using transformer models
- **Context Awareness**: Maintains conversation history for coherent, contextual interactions
- **Multi-task Support**: Can handle various types of requests and intents

### Advanced Features
- **Memory System**: Stores and recalls previous interactions and user preferences
- **Personality Traits**: Adjustable personality (helpfulness, creativity, empathy, humor, formality)
- **Knowledge Base**: Build and query custom domain knowledge
- **Intent Recognition**: Identifies user intents (greeting, question, request, etc.)
- **Sentiment Analysis**: Analyzes emotional tone of user messages
- **Context Analysis**: Determines conversation topic and context
- **Statistics Tracking**: Monitors conversation metrics and user preferences

### Integration
- **REST API**: Flask-based API server for easy integration
- **Easy Integration**: Simple Python API for direct usage
- **Configurable**: Environment-based configuration system

## 📋 Project Structure

```
Dagon-/
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies
├── .env.example             # Environment configuration template
├── .gitignore               # Git ignore rules
├── setup.py                 # Package setup script
├── dagon/
│   ├── __init__.py          # Package initialization
│   ├── core.py              # Core Dagon AI class
│   ├── model.py             # Model handling
│   ├── utils.py             # Utility functions
│   ├── advanced.py          # Memory, personality, knowledge base
│   ├── nlp.py               # NLP utilities
│   ├── enhanced.py          # Enhanced Dagon with all features
│   ├── server.py            # Flask API server
│   └── config.py            # Configuration management
├── examples/
│   ├── basic_chat.py        # Simple chat example
│   └── enhanced_chat.py     # Advanced features example
└── tests/
    ├── test_core.py         # Basic tests
    └── test_advanced.py     # Advanced feature tests
```

## 🚀 Installation

### Prerequisites
- Python 3.8+
- pip

### Setup

```bash
# Clone the repository
git clone https://github.com/jayravey3-lang/Dagon-.git
cd Dagon-

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env
```

## 💬 Quick Start

### Basic Chat

```python
from dagon import DagonAI

# Initialize Dagon
dagon = DagonAI()

# Have a conversation
response = dagon.chat("Hello! What can you do?")
print(response)
```

### Run CLI Chat

```bash
python examples/basic_chat.py
```

### Advanced Features

```python
from dagon.enhanced import EnhancedDagonAI

# Initialize enhanced Dagon
dagon = EnhancedDagonAI()

# Configure personality
dagon.set_personality_trait("empathy", 0.95)
dagon.set_personality_trait("humor", 0.7)

# Add knowledge
dagon.add_knowledge("greeting", "response", "Hello! I'm Dagon.")

# Chat with advanced features
response = dagon.chat("Tell me a joke!")

# Get statistics
stats = dagon.get_statistics()
print(stats)
```

### Run Enhanced CLI Chat

```bash
python examples/enhanced_chat.py
```

## 🔌 API Server

Start the Flask API server:

```bash
python -m dagon.server
```

The server will be available at `http://localhost:5000`

### API Endpoints

#### Chat
```bash
POST /chat
Content-Type: application/json

{
  "message": "Hello, how are you?"
}
```

#### Get Personality
```bash
GET /personality
```

#### Set Personality Trait
```bash
PUT /personality
Content-Type: application/json

{
  "trait": "empathy",
  "value": 0.95
}
```

#### Get Statistics
```bash
GET /statistics
```

#### Add Knowledge
```bash
POST /knowledge
Content-Type: application/json

{
  "domain": "greeting",
  "key": "response",
  "value": "Hello there!"
}
```

#### Get Memories
```bash
GET /memory?query=optional_search
```

#### Reset Conversation
```bash
POST /reset
```

#### Health Check
```bash
GET /health
```

## 🧪 Testing

Run the test suite:

```bash
# Run all tests
python -m unittest discover tests

# Run specific test file
python -m unittest tests.test_core

# Run advanced tests
python -m unittest tests.test_advanced
```

## 🔧 Configuration

Edit `.env` file to configure:

```env
# Model Configuration
MODEL_NAME=gpt2
MAX_HISTORY=5
MAX_MEMORY_SIZE=100

# API Configuration
API_HOST=0.0.0.0
API_PORT=5000
DEBUG=False

# Personality Defaults
DEFAULT_HELPFULNESS=0.9
DEFAULT_CREATIVITY=0.7
DEFAULT_EMPATHY=0.8
DEFAULT_HUMOR=0.6
DEFAULT_FORMALITY=0.5
```

## 📚 Documentation

### Core Classes

#### DagonAI
Main class for basic conversational AI

```python
dagon = DagonAI(model_name="gpt2", max_history=5)
response = dagon.chat("message")
dagon.reset_conversation()
history = dagon.get_history()
```

#### EnhancedDagonAI
Enhanced version with all advanced features

```python
dagon = EnhancedDagonAI()
dagon.set_personality_trait("trait_name", value)
dagon.add_knowledge("domain", "key", "value")
stats = dagon.get_statistics()
memories = dagon.recall_memories(query)
```

### Advanced Features

#### Memory System
```python
dagon.memory.add_memory("content", memory_type="general")
dagon.memory.recall_memories(query="search_term")
dagon.memory.set_user_preference("name", "value")
```

#### Knowledge Base
```python
dagon.knowledge_base.add_fact("domain", "key", "value")
dagon.knowledge_base.get_fact("domain", "key")
dagon.knowledge_base.query_domain("domain")
```

#### NLP Tools
```python
# Intent Recognition
intent = dagon.intent_recognizer.recognize("Hello!")
entities = dagon.intent_recognizer.extract_entities("Email: test@example.com")

# Sentiment Analysis
sentiment = dagon.sentiment_analyzer.analyze("This is great!")

# Context Analysis
topic = dagon.context_analyzer.get_topic(conversation_history)
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

MIT License - see LICENSE file for details

## 👤 Author

jayravey3-lang

## 🙌 Acknowledgments

- Inspired by Meta's AI assistants
- Built with Hugging Face Transformers
- Uses Flask for API serving

## 📞 Support

For issues and questions, please open an issue on GitHub.

---

**Dagon - Empowering conversations with AI** 🤖