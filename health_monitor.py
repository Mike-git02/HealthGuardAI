from datetime import datetime

def health_advice(data):
    print("🧠 HealthMate says:\n")

    if data["heart_rate"] > 100:
        print("⚠️ Your heart rate is a bit high. Please rest and hydrate.")
    elif data["heart_rate"] < 60:
        print("⚠️ Your heart rate is below normal. Monitor it closely.")
    else:
        print("✅ Your heart rate looks good.")

    if data["temperature"] > 37.5:
        print("🌡️ You have a fever. Consider seeing a doctor.")
    elif data["temperature"] < 36.0:
        print("❄️ Body temperature is low. Keep warm and check again.")
    else:
        print("✅ Temperature is within the healthy range.")

    if data["steps_today"] < 4000:
        print("🚶 Try to move around more today for better health.")
    elif data["steps_today"] > 8000:
        print("🏆 Excellent activity level today!")
    else:
        print("✅ You're on track with your steps!")

    if data["sleep_hours"] < 6:
        print("😴 You need more rest. Aim for at least 6–8 hours.")
    elif data["sleep_hours"] > 9:
        print("💤 Oversleeping isn't ideal either. Try balancing your sleep.")
    else:
        print("✅ Great sleep routine!")

    print("\n📅 Advice generated on:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("\n🔔 Reminder: This is not medical advice. Consult a doctor if symptoms persist.")

# Example usage
user_data = {
    "heart_rate": 105,
    "temperature": 38.2,
    "steps_today": 2500,
    "sleep_hours": 5
}

health_advice(user_data)
