from flask import Flask, render_template, request

from src.pipeline.prediction_pipepline import PredictPipeline   #PredictionPipeline import predict  # Import your predict function from PredictionPipeline.py

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def prediction():
    if request.method == 'POST':
        heart_rate = int(request.form['heart_rate'])
        cholesterol_level = int(request.form['cholesterol_level'])
        triglycerides_level = int(request.form['triglycerides_level'])
        fasting_blood_sugar = int(request.form['fasting_blood_sugar'])

        # Call the predict function with the user input values
        pd = PredictPipeline()
        # result = pd.predict(heart_rate, cholesterol_level, triglycerides_level, fasting_blood_sugar)

        # return render_template('result.html', prediction=result)
    
        try:
            result = pd.predict(heart_rate, cholesterol_level, triglycerides_level, fasting_blood_sugar)
            print("Prediction Result:", result)  # Check the result in console for debugging
            return render_template('result.html', prediction=result)
        except Exception as e:
            print("Error during prediction:", e)  # Print error for debugging
            return render_template('error.html')  # Render an error template
        

    

if __name__ == '__main__':
    app.run(debug=True)
