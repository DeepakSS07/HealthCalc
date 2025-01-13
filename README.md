# HealthCalc
HealthCalc is a web application designed to promote healthy living by leveraging machine learning. It allows users to upload an image of food, predicts the food item using a fine-tuned MobileNetV2 CNN model, and provides detailed nutritional information.

Features:

    Food recognition via fine-tuned MobileNetV2 CNN.
    Detailed nutritional analysis based on a curated database.
    User-friendly interface built with Flask.
    Designed for individuals seeking to monitor their dietary intake.

Tech Stack:

    Backend: Flask
    Frontend: HTML, CSS, Bootstrap
    Machine Learning Model: MobileNetV2
    Database: CSV for nutrition values

How It Works

    Image Upload: Users upload an image of their food through the web interface.
    Image Processing: The uploaded image is passed through the fine-tuned MobileNetV2 model to identify the food item.
    Database Query: The identified food item is matched with a record in the nutrition database (CSV file).
    Results Displayed: Nutritional details of the food item are presented to the user, including a breakdown of macronutrients and micronutrients.

HomePage
![image](https://github.com/user-attachments/assets/d987f304-931d-4d23-a45d-69a7c52450c1)

How to Fork This Project:

If you would like to fork this project and make it your own, follow these steps:

Fork the Repository:
Click on the Fork button at the top-right corner of this repository's page on GitHub.
This will create a copy of the repository in your GitHub account.

Clone the Forked Repository:
Navigate to your forked repository on GitHub.
Click the green Code button and copy the repository's URL.
Use the following command in your terminal to clone the repository:

    git clone https://github.com/your-username/HealthCalc.git

Navigate to the Project Directory:

    cd HealthCalc

Set Up the Environment:
Install Python (if not already installed).
Create and activate a virtual environment:

    python -m venv venv
    source venv/bin/activate  # For Linux/Mac
    venv\Scripts\activate     # For Windows

Install dependencies from requirements.txt:

    pip install -r requirements.txt

Run the Project:
Start the Flask development server:

    flask run

Open your browser and visit http://127.0.0.1:5000 to use the application.

