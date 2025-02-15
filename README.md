# linkedin-ai-agent

## Project Overview

The linkedin-ai-agent is an AI-driven tool that automates LinkedIn engagement using OpenAI. It can perform tasks such as sending connection requests, messages, and interacting with posts.

## Features

- Automated LinkedIn engagement
- Customizable interaction settings
- Integration with OpenAI for natural language processing

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/cordz-del/linkedin-ai-agent.git
   cd linkedin-ai-agent
   ```
2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set environment variables (replace with actual credentials):
   ```bash
   export LINKEDIN_USERNAME="your_email@example.com"
   export LINKEDIN_PASSWORD="your_password"
   export OPENAI_API_KEY="your_openai_api_key"
   ```
5. Run the application:
   ```bash
   python app.py
   ```
AI agent that automates LinkedIn engagement using OpenAI.
## Deployment Steps

### Clone the Repository
```bash
git clone https://github.com/your-username/linkedin-ai-agent.git
cd linkedin-ai-agent
```

### Set Up a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Set Environment Variables (Replace with actual credentials)
```bash
export LINKEDIN_USERNAME="your_email@example.com"
export LINKEDIN_PASSWORD="your_password"
export OPENAI_API_KEY="your_openai_api_key"
```

### Run the AI Agent
```bash
python scheduler.py
```

### Deploy on a Cloud Server (Optional)
- Use AWS Lambda, Google Cloud Functions, or DigitalOcean.
- Alternatively, run it on a VPS (Ubuntu/Debian) with a screen session:
```bash
screen -S linkedin-bot
python scheduler.py
```

Now, the AI agent will run continuously in the background! 🚀
