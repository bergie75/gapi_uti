from transitions import Machine
from patients import Patient

class PatientSim:
    def __init__(self, patient):
        self.patient = patient

        states = ["start_diagnostic",
        "initial_management",
        "treatment_state",
        "daily_follow_up",
        "reconsultation",
        "culture_result",
        "secondary_treatment",
        "upper_uti_sepsis",
        "death"]

        transitions = [
            {"trigger": "melt", "source": "solid", "dest": "liquid", "conditions": },
            {}
        ]

