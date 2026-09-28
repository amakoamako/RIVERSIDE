# TC05 - Treatment Outcome Pathway

## Scenario

A completed specialist consultation results in a treatment clinical outcome. The process follows the treatment pathway through treatment appointment scheduling, confirmation, patient notification and final outcome communication.

## Input Data

- Patient: Test Patient 5
- Clinical outcome: Treatment
- Consultation outcome: Specialist consultation completed and treatment recommended.
- Laboratory investigation required: No

## Expected Result

When the final clinical outcome is treatment, the process should follow the treatment pathway, including treatment outcome selection, treatment appointment scheduling, appointment confirmation, patient notification and final outcome communication.

## Actual Result

The completed TC05 execution demonstrates the treatment outcome branch through treatment appointment scheduling, appointment confirmation, patient notification and final outcome communication. The completed Operate instance confirms successful completion of the treatment pathway.

## Status

PASS

## Evidence

The evidence set demonstrates:

1. Referral completion and clarification handling.
2. Final clinical outcome selection for treatment.
3. Treatment outcome completion.
4. Treatment appointment scheduling.
5. Treatment appointment confirmation.
6. Patient notification of the next appointment.
7. Final outcome communication.
8. Completed process instance in Operate.

The completed Operate evidence is recorded in:

`TC05_16_completed_operate.png`

## Defects

No process defect was identified in the completed treatment-path execution.

## Corrective Action

Not applicable.

## Retest

Not applicable because the completed execution did not identify a process defect.

## Limitations

This test demonstrates the treatment outcome pathway represented by the completed execution. Additional testing of other clinical outcome branches would provide broader process coverage.
