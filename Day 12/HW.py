try:
    name = input("Enter your name: ")
    feedback = input("Enter your feedback: ")

    if not name:
        raise ValueError("Name cannot be empty.")

    if not feedback:
        raise ValueError("Feedback cannot be empty.")

    print(f"Thank you, {name}!")
    print(f"Your feedback: {feedback}")

except ValueError as e:
    print("Error:", e)

finally:
    print("Feedback process completed.")