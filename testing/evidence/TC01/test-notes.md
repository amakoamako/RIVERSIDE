# TC01 – Complete End-to-End Riverside Referral

## Scenario
A complete GP referral is processed through the Riverside Hospital specialist referral workflow, including consultation, laboratory investigation, results review, follow-up and final communication.

## Input Data
- Patient: Lab Test Patient
- NHS Number: TEST654321
- Laboratory test: Full Blood Count
- Laboratory appointment: 25/09/2026 at 10:00

## Expected Result
The referral should progress through the complete operational workflow, including the laboratory pathway, and finish with the final outcome communicated to the patient and GP.

## Actual Result
The process progressed through the integrated Camunda workflow and reached the final patient/GP communication stage successfully.

## Status
PASS

## Evidence
Evidence should include screenshots of:
1. Process instance history
2. Process variables
3. Laboratory pathway
4. Review/finalise outcome communication
5. Final communication task
6. Completed process instance

## Defects
None recorded for this execution.

## Corrective Action
Not applicable.

## Retest
Not applicable.

## Limitations
This execution demonstrates one successful end-to-end pathway. Additional pathway and negative testing is required to demonstrate broader coverage.
