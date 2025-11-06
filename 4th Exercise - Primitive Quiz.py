#Exericse 4: Not so primitve quiz!

def european_capitals_quiz():
    questions = {
        "Germany": "Berlin",
        "Greece": "Athens",
        "Sweden": "Stockholm",
        "Norway": "Oslo",
        "Denmark": "Copenhagen",
        "Spain": "Madrid",
        "Italy": "Rome",
        "United Kingdom": "London",
        "Portugal": "Lisbon",
        "Netherlands": "Amsterdam",

    }
    
    score = 0
    print("\nEuropean Capitals Quiz - Answer the following questions:")
    
    answers = {}
    for country in questions:
        answer = input(f"\n---\n\nWhat is the capital of {country}?").strip()
        answers[country] = answer
    
    print("Results:")
    for country, user_answer in answers.items():
        correct_answer = questions[country]
        if user_answer.lower() == correct_answer.lower():
            print(f"(You are correct! {country}:  {correct_answer} is the capital.")
            score += 1
        else:
            print(f"You are Incorrect. {country}: The capital is {correct_answer}.")
    
    print(f"\nFinal Score: {score} out of 10")
    if score < 1:
        print("This is me with my CCL4 quiz exams! :josh crying:")
    
    return score
european_capitals_quiz()