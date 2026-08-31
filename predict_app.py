import joblib
import pandas as pd

def start_prediction_app():
    print("=" * 50)
    print("   STUDENT EXAM SCORE PREDICTION SYSTEM   ")
    print("=" * 50)

    # Step 1: Load the trained model file
    try:
        model = joblib.load('student_score_model.pkl')
        print("Model loaded successfully!\n")
    except FileNotFoundError:
        print("Error: 'student_score_model.pkl' not found.")
        print("Please run your Jupyter Notebook first to train and export the model.")
        return

    # Step 2: Interactive input loop
    while True:
        user_input = input("Enter daily study hours (or type 'exit' to quit): ").strip()

        # Allow user to quit
        if user_input.lower() == 'exit':
            print("\nThank you for using the Prediction System! Goodbye!")
            break

        # Step 3: Validate input
        try:
            hours = float(user_input)

            if hours < 0:
                print("Study hours cannot be negative. Please enter a valid number.\n")
                continue
            elif hours > 24:
                print("A day has only 24 hours! Please enter a realistic number.\n")
                continue

            # Step 4: Format input into a DataFrame matching training features
            input_data = pd.DataFrame({'Hours': [hours]})

            # Step 5: Generate score prediction
            predicted_score = model.predict(input_data)[0]

            # Step 6: Cap percentage output logically between 0% and 100%
            final_score = max(0, min(100, predicted_score))

            print("-" * 40)
            print(f"Study Duration : {hours:.2f} hours/day")
            print(f"Predicted Score: {final_score:.2f}%")
            print("-" * 40 + "\n")

        except ValueError:
            print("Invalid input! Please enter a numeric value for study hours.\n")

if __name__ == "__main__":
    start_prediction_app()