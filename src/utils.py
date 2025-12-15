import json
import re

def validate_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email) is not None

def validate_phone(phone):
    # Simple check for digits and length, allowing mostly international formats
    clean_phone = re.sub(r'\D', '', phone)
    return len(clean_phone) >= 10

def is_info_complete(info_dict):
    """Check if all required fields are filled."""
    required_keys = ["full_name", "email", "phone", "experience", "position", "location", "tech_stack"]
    for key in required_keys:
        if not info_dict.get(key) or info_dict[key] == "Missing":
            return False
    return True

def save_candidate_data(data):
    """Simulates saving data to a backend/DB."""
    # In a real app, this would be a DB call.
    # We will save to a JSON file for local simulation.
    try:
        with open("candidates_db.json", "a") as f:
            f.write(json.dumps(data) + "\n")
        return True
    except Exception as e:
        print(f"Error saving data: {e}")
        return False
