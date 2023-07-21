OmniChat
OmniChat is an AI-powered chatbot web application developed using Django for the backend, the OpenAI API for natural language processing, and HTML, CSS, and JavaScript for the frontend. The chatbot is designed to interact with users and provide responses based on the AI model's understanding of the input.

OmniChat Screenshot

Features
AI-powered chatbot responses using the OpenAI API.
Interactive and user-friendly frontend design.
FetchAPI and AJAX utilized to communicate with the backend.
SQLite database for storing user interactions (messages).
Installation
Clone the repository to your local machine:

bash
Copy code
git clone https://github.com/your-username/OmniChat.git
Create a virtual environment and activate it:

bash
Copy code
cd OmniChat
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Apply the database migrations:

bash
Copy code
python manage.py migrate
Obtain your OpenAI API key and set it as an environment variable:

bash
Copy code
export OPENAI_API_KEY=your_api_key_here  # On Windows, use `set OPENAI_API_KEY=your_api_key_here`
Run the development server:

bash
Copy code
python manage.py runserver
The web application will be accessible at http://127.0.0.1:8000/.

Usage
Access the OmniChat web application using your web browser.

Start interacting with the AI-powered chatbot.

Type your message in the chat input box and press "Enter" to send it.

The chatbot will respond with an appropriate AI-generated message based on your input.

Contributing
Contributions to OmniChat are welcome! If you find any issues or have ideas for improvements, please feel free to open an issue or submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.
