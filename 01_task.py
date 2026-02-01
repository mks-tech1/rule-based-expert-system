class RuleBasedExpertSystem:
    def __init__(self):
        self.rules = []
        self.facts = set()
        self.inference_log = []

    def add_rule(self, conditions, conclusion):
        self.rules.append({
            "conditions": set(conditions),
            "conclusion": conclusion
        })

    def add_fact(self, fact):
        self.facts.add(fact)

    def forward_chaining(self):
        new_inference = True

        while new_inference:
            new_inference = False

            for rule in self.rules:
                if rule["conditions"].issubset(self.facts):
                    if rule["conclusion"] not in self.facts:
                        self.facts.add(rule["conclusion"])
                        self.inference_log.append(
                            f"Applied rule: IF {rule['conditions']} THEN {rule['conclusion']}"
                        )
                        new_inference = True

    def show_results(self):
        print("\n🧠 Inference Steps:")
        for step in self.inference_log:
            print("-", step)

        print("\n✅ Final Facts:")
        for fact in self.facts:
            print("-", fact)
# Create expert system
system = RuleBasedExpertSystem()

# Add rules
system.add_rule(["fever", "cough"], "flu")
system.add_rule(["flu", "headache"], "severe_flu")
system.add_rule(["severe_flu"], "consult_doctor")

# Add user facts
system.add_fact("fever")
system.add_fact("cough")
system.add_fact("headache")

# Run inference
system.forward_chaining()

# Show output
system.show_results()
