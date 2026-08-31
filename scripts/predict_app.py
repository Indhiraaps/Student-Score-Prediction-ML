import joblib
import pandas as pd

def start_prediction_app():
    print("=" * 50)
    print("   STUDENT EXAM SCORE PREDICTION SYSTEM   ")
    print("=" * 50)

    # Step 1: Load the trained model from the models/ subdirectory
    try:
        model = joblib.load('models/student_score_model.pkl')
        print("Model loaded successfully from models/ folder!\n")
    except FileNotFoundError:
        print("Error: 'models/student_score_model.pkl' file not found.")
        print("Please train and export the model from your notebook first.")
        return

    # Interactive loop for predictions
    while True:
        user_input = input("Enter daily study hours (or type 'exit' to quit): ").strip()

        if user_input.lower() == 'exit':
            print("\nThank you for using the Prediction System! Good luck!")
            break

        try:
            hours = float(user_input)

            if hours < 0:
                print("Study hours cannot be negative. Please enter a valid number.\n")
                continue
            elif hours > 24:
                print("A day has only 24 hours! Please enter a realistic number.\n")
                continue

            # Format input matching feature DataFrame
            input_data = pd.DataFrame({'Hours': [hours]})

            # Generate score prediction
            predicted_score = model.predict(input_data)[0]
            final_score = max(0, min(100, predicted_score))

            print("-" * 40)
            print(f"Study Duration : {hours:.2f} hours/day")
            print(f"Predicted Score: {final_score:.2f}%")
            print("-" * 40 + "\n")

        except ValueError:
            print("Invalid input! Please enter a numeric value for study hours.\n")

if __name__ == "__main__":
    start_prediction_app()