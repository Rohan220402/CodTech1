import re

def password_strength(password):
    score = 0
    feedback = []
    
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")
    
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")
    
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Password should contain at least one digit.")
    
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one special character.")
    
    if len(password) == len(set(password)):
        score += 1
    else:
        feedback.append("Password contains repeating characters.")
    
    if score == 5:
        return "Strong password!", feedback
    elif score >= 3:
        return "Moderate password.", feedback
    else:
        return "Weak password.", feedback

if __name__ == "__main__":
    user_password = input("Enter a password to test its strength: ")
    strength, feedback = password_strength(user_password)
    
    print(f"Password strength: {strength}")
    if feedback:
        print("Suggestions for improvement:")
        for item in feedback:
            print(f"- {item}")
