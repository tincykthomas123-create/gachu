"""SAMT - Smart Automated Monitoring Technology (Prototype)

Simple prototype script that models a Patient, computes a small risk score, and generates alerts.
"""

class Patient:
    def __init__(self, name, temperature, cough_days, oxygen_level):
        self.name = name
        self.temperature = temperature
        self.cough_days = cough_days
        self.oxygen_level = oxygen_level


def analyze_patient(patient):
    risk_score = 0

    if patient.temperature > 38:
        risk_score += 2
    if patient.cough_days > 14:
        risk_score += 3
    if patient.oxygen_level < 92:
        risk_score += 3

    return risk_score


def generate_alert(patient, risk_score):
    if risk_score >= 5:
        return f"⚠ ALERT: {patient.name} is at HIGH RISK. Immediate medical check needed."
    elif risk_score >= 3:
        return f"⚠ WARNING: {patient.name} shows moderate symptoms."
    else:
        return f"✅ {patient.name} is stable."


if __name__ == "__main__":
    # Example usage
    patient1 = Patient("Ravi", 38.5, 20, 90)

    score = analyze_patient(patient1)
    alert = generate_alert(patient1, score)

    print("Risk Score:", score)
    print(alert)