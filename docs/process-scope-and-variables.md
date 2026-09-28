# Riverside Hospital Process Scope

## Process Start

A GP referral is received by the Riverside Hospital Specialist Referral and Consultation Unit.


## Process End

The final clinical outcome is communicated to both the patient and the referring GP.


## Process Boundary

The process begins when Riverside Hospital receives a referral from an external GP Practice.

The process covers:

- Referral receipt and referral-data capture
- Automated referral completeness checking
- Referral clarification where information is missing
- Initial specialist consultation scheduling
- Appointment reference and confirmation generation
- Patient appointment communication
- Specialist consultation
- Consultation notes and outcome capture
- Laboratory investigation where required
- Laboratory appointment scheduling
- Laboratory result capture
- Specialist review of laboratory results
- Final clinical outcome confirmation
- Discharge, follow-up, or treatment pathway selection
- Follow-up or treatment appointment scheduling where required
- Automated draft outcome communication generation
- Medical Secretary review and finalisation
- Final communication to the patient and GP

The process does not include:

- Real NHS-system integration
- Real GP-system integration
- Real email-system integration
- Real laboratory-platform integration
- Emergency-department activity
- Inpatient treatment processes

External interactions are simulated within the workflow where required.


# Actors / Participants

- GP Practice
- Patient
- Patient Booking Team
- Specialist Doctor
- Laboratory Team
- Medical Secretary
- Workflow Automation System (Camunda)


# External Participants

## GP Practice

The GP Practice is external to Riverside Hospital.

It:

- Sends the initial referral
- Receives requests for missing referral information
- Provides referral clarification
- Receives the final clinical outcome communication


## Patient

The Patient is external to Riverside Hospital.

The patient:

- Receives the initial consultation appointment information
- Receives laboratory appointment information where required
- Receives follow-up or treatment appointment information where required
- Receives the final outcome communication


# Internal Riverside Hospital Responsibilities

## Patient Booking Team

Responsible for:

- Entering and reviewing referral information
- Requesting referral clarification
- Receiving referral clarification
- Updating referral information
- Scheduling the initial specialist consultation
- Informing the patient of the initial consultation
- Scheduling laboratory appointments
- Informing the patient of laboratory appointments
- Scheduling follow-up consultations
- Scheduling treatment appointments
- Informing the patient of subsequent appointments


## Specialist Doctor

Responsible for:

- Conducting the specialist consultation
- Recording consultation notes
- Recording consultation outcome information
- Deciding whether laboratory investigation is required
- Reviewing laboratory results
- Confirming the final clinical outcome
- Selecting the final outcome type


## Laboratory Team

Responsible for:

- Performing laboratory investigations
- Uploading laboratory results


## Medical Secretary

Responsible for:

- Reviewing generated outcome communication
- Editing and finalising patient communication
- Editing and finalising GP communication
- Sending / confirming final outcome communication to both the patient and GP


## Workflow Automation System

Responsible for:

- Checking referral completeness
- Identifying missing referral information
- Generating appointment references
- Generating appointment confirmation messages
- Generating laboratory appointment references and confirmations
- Notifying the Specialist Doctor that laboratory results are available
- Generating draft patient outcome communication
- Generating draft GP outcome communication


# High-Level Process

1. A GP Practice sends a referral to Riverside Hospital.

2. Riverside Hospital receives the GP referral.

3. The Patient Booking Team enters or reviews the referral details.

4. The Workflow Automation System automatically checks whether the referral contains all required information.

5. The referral completeness result is evaluated.

6. If the referral is incomplete:
   - The Workflow Automation System identifies the missing information.
   - The Patient Booking Team prepares a clarification request.
   - The clarification request is communicated to the GP Practice.
   - The GP Practice provides the missing information.
   - The Patient Booking Team confirms that clarification has been received.
   - The referral details are updated.
   - The automated referral completeness check is performed again.

7. Once the referral is complete, the Patient Booking Team schedules and confirms the initial specialist consultation.

8. The Workflow Automation System generates:
   - An appointment reference
   - An appointment confirmation message

9. The Patient Booking Team informs the patient of the consultation appointment.

10. The Specialist Doctor conducts the specialist consultation.

11. The Specialist Doctor records:
    - Consultation notes
    - Consultation outcome information
    - Whether laboratory investigation is required
    - Laboratory test details where applicable

12. The process evaluates whether a laboratory investigation is required.

13. If no laboratory investigation is required, the process proceeds to final clinical outcome confirmation.

14. If a laboratory investigation is required:
    - The Patient Booking Team schedules the laboratory appointment.
    - The Workflow Automation System generates the laboratory appointment reference and confirmation.
    - The Patient Booking Team informs the patient of the laboratory appointment.
    - The Laboratory Team performs the investigation.
    - The Laboratory Team uploads the laboratory result.
    - The Workflow Automation System records/notifies that laboratory results are available.
    - The Specialist Doctor reviews the laboratory results.

15. The Specialist Doctor confirms the final clinical outcome.

16. The final outcome is classified as one of:
    - Discharge back to GP
    - Follow-up consultation
    - Treatment appointment

17. If the outcome is discharge:
    - No further appointment is scheduled.
    - The process proceeds toward final outcome communication.

18. If the outcome is follow-up:
    - The Patient Booking Team schedules a follow-up consultation.
    - The Workflow Automation System generates the next appointment reference and confirmation.
    - The patient is informed of the next appointment.

19. If the outcome is treatment:
    - The Patient Booking Team schedules a treatment appointment.
    - The Workflow Automation System generates the next appointment reference and confirmation.
    - The patient is informed of the next appointment.

20. All final outcome routes converge.

21. The Workflow Automation System generates:
    - Draft patient outcome communication
    - Draft GP outcome communication

22. The Medical Secretary reviews and finalises both communications.

23. The Medical Secretary confirms that the final outcome communication has been sent to both the patient and GP.

24. The process ends when the final outcome has been communicated.


# Main Process Decisions

## Referral Complete?

Controlled by:

referralComplete

Possible values:

true
false

Gateway conditions:

YES:
referralComplete = true

NO:
referralComplete = false


## Laboratory Test Required?

Controlled by:

labRequired

Possible values:

true
false

Gateway conditions:

YES:
labRequired = true

NO:
labRequired = false


## Final Outcome Type?

Controlled by:

finalOutcomeType

Possible values:

discharge
followUp
treatment

Gateway conditions:

DISCHARGE:
finalOutcomeType = "discharge"

FOLLOW-UP:
finalOutcomeType = "followUp"

TREATMENT:
finalOutcomeType = "treatment"


# Process Variables


## Referral Information

patientName
nhsNumber
dateOfBirth
contactDetails
referringGP
gpPractice
referralReason
referralPriority


## Referral Validation

referralComplete
missingFields


## Referral Clarification

clarificationRequest
clarificationReceived


## Initial Consultation Appointment

consultationDate
consultationTime
specialistDoctor
appointmentReference
appointmentConfirmation


## Specialist Consultation

consultationCompleted
consultationNotes
consultationOutcomeSummary
labRequired
laboratoryTestType
laboratoryTestReason


## Laboratory Appointment

labAppointmentDate
labAppointmentTime
labAppointmentReference
labAppointmentConfirmation


## Laboratory Investigation and Results

laboratoryInvestigationCompleted
laboratoryResultDate
laboratoryResult
labResultAvailable
specialistResultNotification
laboratoryReviewNotes


## Final Clinical Outcome

finalClinicalOutcomeSummary
finalOutcomeType
clinicalPlan
followUpRequirements
treatmentPlan
dischargeAdvice


## Follow-Up / Treatment Appointment

nextAppointmentDate
nextAppointmentTime
nextAppointmentNotes
nextAppointmentReference
nextAppointmentConfirmation


## Outcome Communication

draftPatientOutcomeLetter
draftGPOutcomeLetter
finalPatientOutcomeCommunication
finalGPOutcomeCommunication
outcomeCommunicationConfirmed


# Variable Purpose Reference


## Referral Variables

### patientName

Stores the patient's full name.


### nhsNumber

Stores the patient's NHS number.


### dateOfBirth

Stores the patient's date of birth.


### contactDetails

Stores the patient's contact information.


### referringGP

Stores the name/details of the referring GP.


### gpPractice

Stores the referring GP Practice.


### referralReason

Stores the clinical reason for referral.


### referralPriority

Stores the referral priority.

Expected values:

routine
urgent


### referralComplete

Boolean generated by the automated referral completeness check.

Expected values:

true
false


### missingFields

List generated by the referral completeness Service Task.

Contains the names of referral fields that are missing.


### clarificationRequest

Stores the clarification message prepared by the Patient Booking Team.


### clarificationReceived

Boolean confirmation that clarification has been received from the GP Practice.


# Initial Appointment Variables

### consultationDate

Stores the scheduled initial consultation date.


### consultationTime

Stores the scheduled initial consultation time.


### specialistDoctor

Stores the Specialist Doctor assigned to the consultation.


### appointmentReference

Generated reference for the initial specialist consultation.


### appointmentConfirmation

Generated confirmation message for the initial specialist consultation.


# Consultation Variables

### consultationCompleted

Boolean confirmation that the Specialist Doctor has conducted the consultation.


### consultationNotes

Stores the Specialist Doctor's consultation notes.


### consultationOutcomeSummary

Stores the consultation outcome summary.


### labRequired

Boolean indicating whether laboratory investigation is required.

Expected values:

true
false


### laboratoryTestType

Stores the type of laboratory investigation requested.


### laboratoryTestReason

Stores the reason the laboratory investigation is required.


# Laboratory Appointment Variables

### labAppointmentDate

Stores the laboratory appointment date.


### labAppointmentTime

Stores the laboratory appointment time.


### labAppointmentReference

Generated laboratory appointment reference.


### labAppointmentConfirmation

Generated laboratory appointment confirmation message.


# Laboratory Result Variables

### laboratoryInvestigationCompleted

Boolean confirmation that the laboratory investigation has been performed.


### laboratoryResultDate

Stores the date of the laboratory result.


### laboratoryResult

Stores the laboratory findings/result.


### labResultAvailable

Boolean generated when laboratory results become available.

Expected value when notification occurs:

true


### specialistResultNotification

Stores the notification generated for the Specialist Doctor when laboratory results become available.


### laboratoryReviewNotes

Stores the Specialist Doctor's review/interpretation of the laboratory results.


# Final Clinical Outcome Variables

### finalClinicalOutcomeSummary

Stores the final clinical outcome determined by the Specialist Doctor.


### finalOutcomeType

Controls the final outcome gateway.

Expected values:

discharge
followUp
treatment


### clinicalPlan

Stores the overall clinical plan following the final decision.


### followUpRequirements

Stores follow-up requirements where the final outcome is follow-up.


### treatmentPlan

Stores treatment information where the final outcome is treatment.


### dischargeAdvice

Stores advice for the GP where the patient is discharged back to primary care.


# Follow-Up / Treatment Appointment Variables

### nextAppointmentDate

Stores the date of a follow-up or treatment appointment.


### nextAppointmentTime

Stores the time of a follow-up or treatment appointment.


### nextAppointmentNotes

Stores additional notes about the next appointment.


### nextAppointmentReference

Generated reference for the follow-up or treatment appointment.


### nextAppointmentConfirmation

Generated confirmation message for the follow-up or treatment appointment.


# Outcome Communication Variables

### draftPatientOutcomeLetter

Automatically generated draft communication intended for the patient.


### draftGPOutcomeLetter

Automatically generated draft clinical outcome communication intended for the referring GP.


### finalPatientOutcomeCommunication

Stores the patient communication after review and finalisation by the Medical Secretary.


### finalGPOutcomeCommunication

Stores the GP communication after review and finalisation by the Medical Secretary.


### outcomeCommunicationConfirmed

Boolean confirmation that the final outcome communication has been sent to both the patient and GP.


# Human Activities


## Patient Booking Team

- Enter / review referral details
- Request referral clarification
- Receive referral clarification
- Update referral details
- Schedule / confirm initial consultation
- Inform patient of appointment
- Schedule laboratory appointment
- Inform patient of laboratory appointment
- Schedule follow-up consultation
- Schedule treatment appointment
- Inform patient of next appointment


## Specialist Doctor

- Conduct specialist consultation
- Record consultation notes and outcome
- Review laboratory results
- Confirm final clinical outcome


## Laboratory Team

- Perform laboratory investigation
- Upload laboratory results


## Medical Secretary

- Review / finalise outcome communication
- Send final outcome to patient and GP


# Automated Service Tasks


## 1. Check Referral Completeness

BPMN Task:

CHECK REFERRAL COMPLETENESS

Job Type:

check-referral-completeness

Reads:

patientName
nhsNumber
dateOfBirth
contactDetails
referringGP
gpPractice
referralReason
referralPriority

Produces:

referralComplete
missingFields


## 2. Generate Appointment Reference and Confirmation

BPMN Tasks:

GENERATE APPOINTMENT REFERENCE & CONFIRMATION

Job Type:

generate-appointment-reference

Used for:

- Initial specialist consultation
- Follow-up consultation
- Treatment appointment

Possible inputs include:

consultationDate
consultationTime
specialistDoctor

or:

nextAppointmentDate
nextAppointmentTime
nextAppointmentNotes
finalOutcomeType

Produces, depending on the appointment stage:

appointmentReference
appointmentConfirmation

or:

nextAppointmentReference
nextAppointmentConfirmation


## 3. Generate Laboratory Appointment Reference and Confirmation

BPMN Task:

GENERATE LAB APPOINTMENT REFERENCE & CONFIRMATION

Job Type:

generate-lab-appointment-reference

Reads:

labAppointmentDate
labAppointmentTime
laboratoryTestType

Produces:

labAppointmentReference
labAppointmentConfirmation


## 4. Notify Specialist Results Available

BPMN Task:

NOTIFY SPECIALIST RESULTS AVAILABLE

Job Type:

notify-specialist-results-available

Reads:

laboratoryResultDate
laboratoryResult
laboratoryTestType

Produces:

labResultAvailable
specialistResultNotification


## 5. Generate Draft Outcome Letter

BPMN Task:

GENERATE DRAFT OUTCOME LETTER

Job Type:

generate-draft-outcome-letter

May read:

patientName
nhsNumber
referringGP
gpPractice
consultationNotes
consultationOutcomeSummary
laboratoryTestType
laboratoryResult
laboratoryReviewNotes
finalClinicalOutcomeSummary
finalOutcomeType
clinicalPlan
followUpRequirements
treatmentPlan
dischargeAdvice
nextAppointmentDate
nextAppointmentTime
nextAppointmentReference

Produces:

draftPatientOutcomeLetter
draftGPOutcomeLetter


# Core Automated Activities Required for the Assessment

The three principal automated information-processing activities are:

1. Referral completeness checking
2. Appointment reference and confirmation generation
3. Draft outcome communication generation

Additional supporting automation includes:

4. Laboratory appointment reference and confirmation generation
5. Specialist notification when laboratory results are available


# Forms Used in the Operational Workflow

## Referral

referral-details.form

Used by:

- ENTER / REVIEW REFERRAL DETAILS
- UPDATE REFERRAL DETAILS


## Referral Clarification Request

referral-clarification.form

Used by:

- REQUEST REFERRAL CLARIFICATION


## Referral Clarification Received

referral-clarification-received.form

Used by:

- RECEIVE REFERRAL CLARIFICATION


## Initial Consultation Appointment

initial-consultation-appointment.form

Used by:

- SCHEDULE / CONFIRM INITIAL CONSULTATION


## Initial Appointment Confirmation

appointment-confirmation.form

Used by:

- INFORM PATIENT OF APPOINTMENT


## Consultation Completion

consultation-completion.form

Used by:

- CONDUCT SPECIALIST CONSULTATION


## Consultation Outcome

consultation-outcome.form

Used by:

- RECORD CONSULTATION NOTES & OUTCOME


## Laboratory Appointment

laboratory-appointment.form

Used by:

- SCHEDULE LABORATORY APPOINTMENT


## Laboratory Appointment Confirmation

lab-appointment-confirmation.form

Used by:

- INFORM PATIENT OF LAB APPOINTMENT


## Laboratory Investigation Completion

laboratory-investigation-completion.form

Used by:

- PERFORM LABORATORY INVESTIGATION


## Laboratory Result

laboratory-result.form

Used by:

- UPLOAD LABORATORY RESULTS


## Laboratory Results Review

laboratory-results-review.form

Used by:

- REVIEW LABORATORY RESULTS


## Final Clinical Outcome

final-clinical-outcome.form

Used by:

- CONFIRM FINAL CLINICAL OUTCOME


## Next Appointment

next-appointment.form

Used by:

- SCHEDULE FOLLOW-UP CONSULTATION
- SCHEDULE TREATMENT APPOINTMENT


## Next Appointment Confirmation

next-appointment-confirmation.form

Used by:

- INFORM PATIENT OF NEXT APPOINTMENT


## Outcome Communication Review

outcome-communication-review.form

Used by:

- REVIEW / FINALISE OUTCOME COMMUNICATION


## Outcome Send Confirmation

outcome-send-confirmation.form

Used by:

- SEND FINAL OUTCOME TO PATIENT AND GP


# Expected Main Test Pathways


## Test Scenario 1 - Complete Referral

Complete referral
→ Referral passes automated validation
→ Initial consultation scheduled
→ Patient informed
→ Consultation performed
→ No laboratory investigation required
→ Final outcome confirmed
→ Outcome communication generated
→ Secretary reviews communication
→ Patient and GP informed


## Test Scenario 2 - Incomplete Referral

Incomplete referral
→ Automated completeness check fails
→ Missing fields identified
→ GP clarification requested
→ Clarification received
→ Referral details updated
→ Completeness check repeated
→ Referral passes validation
→ Process continues


## Test Scenario 3 - Laboratory Pathway

Complete referral
→ Consultation scheduled
→ Consultation conducted
→ Laboratory investigation required
→ Laboratory appointment scheduled
→ Patient informed
→ Laboratory investigation performed
→ Result uploaded
→ Specialist notified
→ Specialist reviews result
→ Final outcome confirmed
→ Outcome communication generated and sent


## Test Scenario 4 - Follow-Up Outcome

Final outcome type = followUp
→ Follow-up consultation scheduled
→ Appointment reference generated
→ Patient informed
→ Outcome communication generated
→ Patient and GP informed


## Test Scenario 5 - Treatment Outcome

Final outcome type = treatment
→ Treatment appointment scheduled
→ Appointment reference generated
→ Patient informed
→ Outcome communication generated
→ Patient and GP informed


## Test Scenario 6 - Discharge Outcome

Final outcome type = discharge
→ No further appointment required
→ Draft outcome communications generated
→ Medical Secretary reviews/finalises
→ Patient and GP informed
→ Process ends