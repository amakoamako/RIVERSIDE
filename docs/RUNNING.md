# Running the Riverside Hospital Prototype

## Environment

- Python 3.11
- Local Camunda environment compatible with the deployed BPMN/forms
- Camunda Orchestration SDK 9.0.1

## Python environment

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Service-task workers

Run the required worker script(s) from the repository root, one per terminal, depending on the pathway being exercised:

```bash
python service-tasks/check_referral_completeness.py
python service-tasks/generate_appointment_reference.py
python service-tasks/generate_lab_appointment_reference.py
python service-tasks/notify_specialist_results_available.py
python service-tasks/generate_draft_outcome_letter.py
```

The BPMN model must be deployed to the local Camunda environment before end-to-end execution.
