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

Here's a more detailed description for HealthCalc to provide a comprehensive understanding of the project:
HealthCalc: Intelligent Food Recognition and Nutrition Analysis

HealthCalc is an AI-powered web application designed to help users make informed dietary decisions by analyzing their food intake. By combining machine learning and a user-friendly interface, HealthCalc simplifies the process of tracking nutrition and encourages a healthier lifestyle.
Project Overview

HealthCalc enables users to upload an image of their meal. Using a fine-tuned MobileNetV2 Convolutional Neural Network (CNN), the system identifies the food item in the image and fetches its nutritional information from a curated database stored in a CSV file. This information is presented in an easy-to-read format, helping users monitor their calorie and nutrient consumption.
Key Features

    Food Recognition:
        Leverages MobileNetV2, a lightweight and efficient CNN model fine-tuned for food classification.
        Provides accurate predictions of various food items.

    Nutrition Analysis:
        Retrieves nutritional data such as calories, protein, fat, carbohydrates, vitamins, and minerals.
        Helps users make data-driven dietary choices.

    User-Friendly Interface:
        Built with Flask and styled using Bootstrap for responsiveness.
        Intuitive design for seamless interaction, allowing users to upload images and view results effortlessly.

    Portable and Scalable:
        Lightweight application suitable for deployment on platforms like PythonAnywhere.
        Designed to accommodate future updates, such as adding more food categories and supporting multiple languages.

How It Works

    Image Upload: Users upload an image of their food through the web interface.
    Image Processing: The uploaded image is passed through the fine-tuned MobileNetV2 model to identify the food item.
    Database Query: The identified food item is matched with a record in the nutrition database (CSV file).
    Results Displayed: Nutritional details of the food item are presented to the user, including a breakdown of macronutrients and micronutrients.
