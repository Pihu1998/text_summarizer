# Text Summarizer

This project implements a web application for summarizing long text articles using an AI-based text summarization model. It consists of a frontend interface for user input, a backend API for text summarization, and a MongoDB database to store the results.

# Technologies Used:

- ***Frontend***: HTML, CSS, JavaScript
- ***Backend***: Python, Flask
- ***Database***: MongoDB
- ***AI Model***: Transformer's model (summarization pipeline)
- ***Deployment***: Waitress (for serving Flask app)

# Assumptions:
- The frontend is designed to be simple, focusing on usability for inputting long text and displaying the summarization result.
- The backend encapsulates the AI logic for text summarization within a single endpoint /summarize.
- MongoDB is chosen as the database for storing summarized text and insights. The results are saved with a timestamp for reference.
- Transformer's model is used for text summarization.
- The application is hosted locally using Waitress for serving the Flask app. Deployment to a cloud provider like AWS is optional and not implemented in this version.

## Prerequisites

Before running the project, ensure you have the following installed:

- Python (3.7 or higher)

## Installation and Usage:

1. Clone the repository:

```bash
git clone https://github.com/yourusername/text-summarizer.git
cd text-summarizer
```

2. Install backend dependencies:
```bash
pip install -r requirements.txt
```

2. Start the backend server:
   
```bash
python main.py
```

3. Access the application in your web browser:
```bash
http://localhost:3000
```

4. Enter a long text article into the text input field and click "Summarize Text" button.
5. Wait for the summarization process to complete. You'll see a spinner while the process is ongoing.
6. Once the summary is generated, it will be displayed below the input field.

# Customization
Changing AI Model: The backend uses an AI model for text summarization. You can modify the summarization logic in the app.py file or replace it with another AI service.
Database Configuration: If you want to use a different database or configure MongoDB settings, update the app.py file accordingly.
Frontend Styling: Customize the frontend appearance by modifying the HTML and CSS files in the frontend/public directory.

# Deployment
To deploy the application to a cloud provider (e.g., AWS, Heroku), follow their respective deployment guides and ensure the necessary configurations are made for the backend, frontend, and database.
