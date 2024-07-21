# WineChatBot
Overview
This project is a chatbot built using Flask and the OpenAI API. It is designed to answer customer queries related to wines and services offered by the business.

Prerequisites
Python 3.8 or higher
pip (Python package installer)
Git (for version control and cloning the repository)
Setup Instructions
Follow these steps to set up and run the chatbot application:

# 1. Clone the Repository
First, clone the repository from GitHub to your local machine:

bash
Copy code
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
# 2. Create a Virtual Environment
It’s recommended to use a virtual environment to manage dependencies:

bash
Copy code
python -m venv venv
Activate the virtual environment:

Windows:

bash
Copy code
venv\Scripts\activate
macOS/Linux:

bash
Copy code
source venv/bin/activate

# 3. Install Dependencies
Install the required Python libraries using pip:

bash
Copy code
pip install -r requirements.txt

# 4. Configure API Keys
To use the OpenAI API, you need an API key. Set up your OpenAI API key in your environment variables:

Windows:

bash
Copy code
set OPENAI_API_KEY=your_openai_api_key
macOS/Linux:

bash
Copy code
export OPENAI_API_KEY=your_openai_api_key
Alternatively, you can add your API key directly in the app.py file (not recommended for security reasons).

# 5. Run the Flask Application
Start the Flask application by running:

bash
Copy code
python app.py
The application will start running on http://127.0.0.1:5000. Open this URL in your web browser to access the chatbot.

# 6. Accessing the Application
Open your web browser and go to http://127.0.0.1:5000 to interact with the chatbot.
# 7. Testing the Application
You can test the chatbot by typing various queries in the chat interface. The chatbot should respond based on the corpus of FAQs and the OpenAI API.

Troubleshooting
If you encounter issues with the OpenAI API:

Ensure that your API key is correctly set and valid.
Check the API documentation for any updates or changes.
If the application is not starting:

Make sure all dependencies are installed correctly.
Check for any syntax errors or issues in the app.py file.
Future Enhancements
Enhanced NLP capabilities
Multi-language support
Integration with external data sources
Contact
For any issues or questions, please contact sharmapavitra316@gmail.com .
