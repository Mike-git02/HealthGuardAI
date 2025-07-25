# health_monitor.py

def get_health_response(user_input):
    user_input = user_input.strip().lower()

    if user_input in ['exit', 'quit']:
        return "👋 Take care of your health! Goodbye!"

    keywords = {
        "sleep": ["sleep", "rest", "nap", "tired", "fatigue", "can't sleep", "insomnia", "bedtime"],
        "nutrition": ["nutrition", "food", "diet", "eat", "meal", "snack", "healthy eating", "what to eat", "fruits", "vegetables"],
        "exercise": ["exercise", "workout", "fitness", "activity", "gym", "training", "move", "jog", "walk", "burn calories"],
        "stress": ["stress", "anxiety", "tension", "relax", "calm", "panic", "overwhelmed", "pressured", "burnout"],
        "hydration": ["water", "drink", "hydration", "thirst", "fluids", "dehydrated", "how much water"],
        "mental_health": ["mental health", "mind", "wellbeing", "emotions", "depression", "sad", "happy", "feeling down", "mental state"],
        "disclaimer": ["disclaimer", "medical", "doctor", "diagnosis", "serious", "hospital", "emergency"]
    }

    for category, words in keywords.items():
        if any(word in user_input for word in words):
            if category == "sleep":
                return "😴 Try getting 7–9 hours of sleep. Good sleep boosts immunity and memory."
            elif category == "nutrition":
                return "🥗 Eat balanced meals with veggies, fruits, whole grains, and proteins."
            elif category == "exercise":
                return "🏃 Move your body! A 30-minute walk or workout daily is a good start."
            elif category == "stress":
                return "🧘 Practice deep breathing or journaling. Avoid burnout by pacing yourself."
            elif category == "hydration":
                return "💧 Keep sipping water—at least 6–8 glasses a day is recommended."
            elif category == "mental_health":
                return "💬 Mental health matters. Rest, talk to loved ones, and seek support if needed."
            elif category == "disclaimer":
                return "⚠️ I’m not a doctor. For medical advice, please consult a professional."

    return "🤖 I’m still learning. Try asking about sleep, nutrition, exercise, or stress."
