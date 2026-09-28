# TC03 – Laboratory Investigation Pathway

## Scenario
A referral requiring laboratory investigation progresses through the laboratory pathway before the final clinical outcome is confirmed.

## Input Data
- Patient: Lab Test Patient
- NHS Number: TEST654321
- Laboratory test: Full Blood Count
- Laboratory appointment: 25/09/2026 at 10:00

## Expected Result
Where laboratory investigation is required, the process should follow the laboratory pathway, including appointment scheduling, laboratory investigation, result submission, notification and review before the final clinical outcome is confirmed.

## Actual Result
The available integrated Camunda execution evidence shows the laboratory pathway progressing through the required laboratory stages and continuing to the final clinical outcome process.

## Status
PASS

## Evidence
Evidence should include screenshots demonstrating:
1. Laboratory test required decision
2. Laboratory appointment scheduling
3. Laboratory appointment/reference generation
4. Laboratory investigation and result upload
5. Laboratory results notification/review
6. Final clinical outcome
7. Completed process instance

## Defects
None recorded for this execution.

## Corrective Action
Not applicable.

## Retest
Not applicable to this successful execution.

## Limitations
This test demonstrates the laboratory-required pathway. Additional testing of the alternative non-laboratory route would provide broader gateway coverage.
