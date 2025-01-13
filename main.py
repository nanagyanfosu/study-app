def display_welcome_message():
    """Display a welcome message to the user."""
    print("=" * 50)
    print("🎓 Welcome to the Study Strategy Recommendation System 🎓")
    print("=" * 50)
    print("Answer a few questions, and we'll recommend study strategies tailored to you!")
    print()

def get_user_input():
    """Collect user preferences from the user."""
    print("Please answer the following questions:")
    style = input("1. What is your preferred learning style (visual/auditory/kinesthetic)? ").strip().lower()
    time = input("2. How much time do you have for studying (short/long)? ").strip().lower()
    difficulty = input("3. How difficult is the subject you're studying (easy/medium/hard)? ").strip().lower()
    motivation = input("4. What is your current motivation level (low/high)? ").strip().lower()
    print()
    return {"style": style, "time": time, "difficulty": difficulty, "motivation": motivation}

def display_recommendation(recommendation):
    """Display the recommendation to the user."""
    print("=" * 50)
    print("📚 Your Personalized Study Recommendation 📚")
    print("=" * 50)
    print(recommendation)
    print("=" * 50)

if __name__ == "__main__":
    # Welcome message
    display_welcome_message()
    
    # Collect user input
    user_input = get_user_input()

    # Define the rules (from the previous steps)
    rules = [
        {"condition": {"style": "visual", "time": "short"}, "recommendation": "Use mind maps or flashcards to quickly review concepts."},
        {"condition": {"style": "visual", "time": "long"}, "recommendation": "Create detailed diagrams or charts to organize the material."},
        {"condition": {"style": "visual", "difficulty": "hard"}, "recommendation": "Watch video tutorials that explain the subject visually."},
        {"condition": {"style": "visual", "motivation": "low"}, "recommendation": "Use colorful notes or apps to make studying visually appealing."},
        {"condition": {"style": "auditory", "time": "short"}, "recommendation": "Listen to quick summary podcasts or recorded lectures."},
        {"condition": {"style": "auditory", "time": "long"}, "recommendation": "Record yourself reading notes and play them back for review."},
        {"condition": {"style": "auditory", "difficulty": "hard"}, "recommendation": "Join study groups and engage in discussions to clarify concepts."},
        {"condition": {"style": "auditory", "motivation": "low"}, "recommendation": "Pair up with a friend and teach each other concepts aloud."},
        {"condition": {"style": "kinesthetic", "time": "short"}, "recommendation": "Use hands-on methods like building models or using physical flashcards."},
        {"condition": {"style": "kinesthetic", "time": "long"}, "recommendation": "Incorporate real-world examples or experiments into your study routine."},
        {"condition": {"style": "kinesthetic", "difficulty": "hard"}, "recommendation": "Break down the material into smaller tasks and practice repeatedly."},
        {"condition": {"style": "kinesthetic", "motivation": "low"}, "recommendation": "Take frequent breaks and include movement, like pacing while reviewing notes."},
        {"condition": {"time": "short", "difficulty": "hard"}, "recommendation": "Focus on the most critical topics and practice with quick quizzes."},
        {"condition": {"motivation": "low", "difficulty": "hard"}, "recommendation": "Set small, achievable goals and reward yourself after completing each task."},
        {"condition": {"style": "visual", "style": "auditory", "motivation": "high"}, "recommendation": "Combine video tutorials and podcasts for a comprehensive review."},
    ]

    # Inference engine to get recommendation
    def get_recommendation(user_input, rules):
        for rule in rules:
            if all(user_input.get(k) == v for k, v in rule["condition"].items()):
                return rule["recommendation"]
        return "No specific recommendation found for your input. Try refining your details."

    # Generate and display the recommendation
    recommendation = get_recommendation(user_input, rules)
    display_recommendation(recommendation)
