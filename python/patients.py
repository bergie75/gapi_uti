import numpy as np
from transitions import Machine

class Patient:

    def __init__(self, strategy, true_state, upper_uti_sepsis, machine):
        # true biological state variables
        self.true_state = true_state
        self.upper_uti_sepsis = upper_uti_sepsis
        self.strategy = strategy

        # state machine to keep track of current module
        self.machine = machine

        # variables based on current treatments
        self.current_anti = None
        self.days_on_current = 0
        self.risk_level = None
        self.other_method = None

        # variables referring to time in healthcare system
        self.final_results = None
        self.total_cost = 0
        self.qalys = 0
        self.total_symptom_days = 0
        self.first_anti_treatment = 0  # day where antibiotic is first given
        self.num_consultations = 0
        self.num_cultures = 0
        self.anti_prescriptions = []
        self.appropriate_anti_used = []
        self.inappropriate_anti_used = []
        self.adverse_effects = []
        self.pyelonephritis = False
        self.sepsis = False
        self.outpatient = False
        self.hospitalized = False
