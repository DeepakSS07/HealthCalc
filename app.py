from flask import Flask, render_template, request, redirect, url_for
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import pandas as pd
import json
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'

# Load the fine-tuned model
model = load_model('fine_tuned_final.h5')

# Load the class indices
with open('class_indices.json', 'r') as f:
    class_indices = json.load(f)
class_indices = {v: k for k, v in class_indices.items()}  # Reverse mapping

# Load the nutrition information from CSV
nutrition_df = pd.read_csv('final_81.csv')

# Function to load and preprocess the image
def load_and_preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Normalize to [0, 1]
    return img_array

@app.route('/food_analyzer', methods=['GET', 'POST'])
def food_analyzer():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            img_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(img_path)

            if not os.path.exists(img_path):
                return render_template('food_analyzer.html', error="Image upload failed.", img_path=None)

            preprocessed_image = load_and_preprocess_image(img_path)
            predictions = model.predict(preprocessed_image)

            if predictions.size == 0:
                return render_template('food_analyzer.html', error="Model failed to predict.", img_path=img_path)

            predicted_class_index = np.argmax(predictions)
            if predicted_class_index not in class_indices:
                return render_template('food_analyzer.html', error="Predicted class not found in class indices.", img_path=img_path)

            predicted_class = class_indices[predicted_class_index]
            confidence = np.max(predictions)

            # Retrieve nutrition information
            nutrition_info_list = nutrition_df[nutrition_df['Food'] == predicted_class].to_dict(orient='records')
            if not nutrition_info_list:
                return render_template('food_analyzer.html', error="Nutritional information for the predicted class not found.", img_path=img_path, predicted_class=predicted_class, confidence=confidence)

            nutrition_info = nutrition_info_list[0]
            return render_template('food_analyzer.html', img_path=img_path, predicted_class=predicted_class, confidence=confidence, nutrition_info=nutrition_info)

    return render_template('food_analyzer.html')



@app.route('/calculator')
def calculator():
    return render_template('calculator.html')



# Weight Gain Page
@app.route('/weightgain')
def weightgain():
    foods_to_eat = ["Nuts", "Whole grains", "Avocados", "Dairy products", "Lean meats"]
    foods_to_avoid = ["Sugary drinks", "Refined carbs", "Trans fats"]
    tips = ["Eat more calories than you burn.", "Focus on strength training to build muscle.", "Eat protein-rich foods."]
    return render_template('health_template.html', 
                           page_title="Weight Gain Plan", 
                           foods_to_eat=foods_to_eat, 
                           foods_to_avoid=foods_to_avoid, 
                           tips=tips)

# Weight Loss Page
@app.route('/weightloss')
def weightloss():
    foods_to_eat = ["Vegetables", "Lean protein", "Whole grains", "Berries", "Nuts in moderation"]
    foods_to_avoid = ["Processed foods", "Sugary beverages", "White bread", "Junk food"]
    tips = ["Maintain a calorie deficit.", "Drink plenty of water.", "Regular aerobic exercise."]
    return render_template('health_template.html', 
                           page_title="Weight Loss Plan", 
                           foods_to_eat=foods_to_eat, 
                           foods_to_avoid=foods_to_avoid, 
                           tips=tips)

# Height Growth Page
@app.route('/height')
def height():
    foods_to_eat = ["Leafy greens", "Dairy products", "Eggs", "Lean meats", "Fish"]
    foods_to_avoid = ["Junk food", "Sugary drinks", "Processed foods"]
    tips = ["Ensure adequate sleep.", "Engage in stretching exercises.", "Maintain a balanced diet rich in proteins and calcium."]
    return render_template('health_template.html', 
                           page_title="Height Growth Plan", 
                           foods_to_eat=foods_to_eat, 
                           foods_to_avoid=foods_to_avoid, 
                           tips=tips)

# Kidney Stone Page
@app.route('/kidneystone')
def kidneystone():
    foods_to_eat = ["Water", "Citrusy fruits", "Leafy greens", "Calcium-rich foods"]
    foods_to_avoid = ["Oxalate-rich foods (e.g., spinach)", "Excessive salt", "Sugary drinks"]
    tips = ["Stay hydrated.", "Avoid excessive salt intake.", "Limit oxalate-rich foods if prone to calcium oxalate stones."]
    return render_template('health_template.html', 
                           page_title="Kidney Stone Plan", 
                           foods_to_eat=foods_to_eat, 
                           foods_to_avoid=foods_to_avoid, 
                           tips=tips)

# Diabetes Page
@app.route('/diabetes')
def diabetes():
    foods_to_eat = ["Leafy greens", "Whole grains", "Nuts", "Legumes", "Lean protein", "Low-GI fruits (e.g., berries, apples)"]
    foods_to_avoid = ["Sugary drinks", "Refined carbs", "Trans fats", "High-sugar snacks", "White bread", "Processed foods"]
    tips = ["Focus on foods with a low glycemic index.", 
            "Stay physically active to improve insulin sensitivity.", 
            "Eat smaller, more frequent meals.", 
            "Monitor blood sugar levels regularly.", 
            "Maintain a balanced diet with fiber-rich foods."]
    return render_template('health_template.html', 
                           page_title="Diabetes Management Plan", 
                           foods_to_eat=foods_to_eat, 
                           foods_to_avoid=foods_to_avoid, 
                           tips=tips)



# Blood Pressure Page
@app.route('/bp')
def bp():
    foods_to_eat = ["Leafy greens", "Berries", "Oats", "Bananas", "Fatty fish"]
    foods_to_avoid = ["Salt", "Caffeine", "Processed foods", "High-fat dairy products"]
    tips = ["Reduce sodium intake.", "Engage in regular exercise.", "Manage stress effectively."]
    return render_template('health_template.html', 
                           page_title="Blood Pressure Control Plan", 
                           foods_to_eat=foods_to_eat, 
                           foods_to_avoid=foods_to_avoid, 
                           tips=tips)

# Heart Health Page
@app.route('/hearthealth')
def hearthealth():
    foods_to_eat = ["Fatty fish (salmon)", "Nuts", "Olive oil", "Whole grains", "Leafy greens"]
    foods_to_avoid = ["Trans fats", "Processed meats", "Sugary foods", "Excessive salt"]
    tips = ["Regular cardio exercise.", "Quit smoking.", "Monitor cholesterol levels.", "Reduce saturated fat intake."]
    return render_template('health_template.html', 
                           page_title="Heart Health Plan", 
                           foods_to_eat=foods_to_eat, 
                           foods_to_avoid=foods_to_avoid, 
                           tips=tips)



@app.route('/suggestions')
def suggestions():
    return render_template('suggestions.html')


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('home.html')



if __name__ == '__main__':
    app.run(debug=True)
