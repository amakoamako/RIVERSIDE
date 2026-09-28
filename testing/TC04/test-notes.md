# TC04 – Follow-Up Outcome Pathway

## Scenario
A completed specialist assessment results in a follow-up clinical outcome and the process proceeds through follow-up appointment scheduling and subsequent outcome communication.

## Input Data
- Patient: Lab Test Patient
- Clinical outcome: followUp
- Consultation outcome: Specialist consultation completed and follow-up recommended.

## Expected Result
Where the final clinical outcome requires follow-up, the process should follow the follow-up pathway, including scheduling the follow-up consultation, generating appointment confirmation, informing the patient of the next appointment and progressing to final outcome communication.

## Actual Result
Available integrated Camunda execution evidence shows the follow-up pathway and subsequent final outcome communication stages within the operational process.

## Status
PASS

## Evidence
Evidence should demonstrate:
1. Final outcome type decision
2. Follow-up consultation scheduling
3. Appointment reference and confirmation generation
4. Patient notification of the next appointment
5. Final outcome communication
6. Completed process instance

## Defects
None recorded for the available execution.

## Corrective Action
Not applicable.

## Retest
Not applicable to the available successful execution.

## Limitations
This test demonstrates the follow-up outcome pathway. Additional testing of the alternative treatment/outcome branch would provide broader outcome coverage.
