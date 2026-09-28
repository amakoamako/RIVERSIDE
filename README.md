# Riverside Hospital Specialist Referral Workflow

## 1. Project Overview

This project develops an information-system prototype for the Riverside Hospital specialist referral workflow. It combines socio-technical modelling, business-process modelling, Camunda workflow automation, user forms, automated service tasks, testing, configuration management and supporting documentation.

The operational workflow covers the referral journey from receipt of a GP referral through referral validation, appointment scheduling, specialist consultation, optional laboratory investigation, final outcome selection and communication of the final outcome to the patient and referring GP.

## 2. Project Scope

The process starts when Riverside Hospital receives a referral from an external GP Practice and ends when the final clinical outcome has been communicated to both the patient and referring GP.

The workflow includes:

- Referral receipt and referral-data capture
- Automated referral completeness checking
- Referral clarification where information is missing
- Initial consultation scheduling and confirmation
- Specialist consultation and outcome capture
- Laboratory investigation where required
- Laboratory result capture and specialist review
- Final outcome selection
- Discharge, follow-up or treatment pathways
- Follow-up or treatment appointment scheduling where required
- Draft outcome communication generation
- Medical Secretary review and finalisation
- Final communication to the patient and GP

The prototype does not include real NHS, GP, email or laboratory-system integration, emergency-department activity or inpatient treatment processes. External interactions are simulated within the workflow where required.

For the detailed process boundary, participants, variables, automated activities, forms and expected test pathways, see [`docs/process-scope-and-variables.md`](docs/process-scope-and-variables.md).

## 3. Repository Structure

```text
models/bpmn/        Strategic and operational BPMN models
models/i-star/      Strategic Dependency and Strategic Rationale models
forms/              Camunda user forms used by the workflow
service-tasks/      Automated Python service-task implementations
testing/            Test scenarios, evidence and testing report
docs/               Supporting process and project documentation
```

## 4. Main Participants

### External

- GP Practice
- Patient

### Internal Riverside Hospital

- Patient Booking Team
- Specialist Doctor
- Laboratory Team
- Medical Secretary
- Workflow Automation System (Camunda)

The detailed responsibilities and process interactions are documented in [`docs/process-scope-and-variables.md`](docs/process-scope-and-variables.md).

## 5. Workflow Automation

The workflow uses Camunda service tasks for automated information-processing activities, including:

1. Referral completeness checking
2. Appointment reference and confirmation generation
3. Laboratory appointment reference and confirmation generation
4. Notification when laboratory results are available
5. Draft outcome communication generation

The corresponding Python implementations are located in `service-tasks/`. The BPMN model connects these automated tasks to the wider operational process so that they operate as part of the integrated workflow rather than as isolated scripts.

## 6. Forms

The `forms/` directory contains the user forms used by the operational workflow, including referral, clarification, consultation, laboratory, final outcome, next appointment and outcome communication forms.

The mapping between forms and BPMN activities is documented in [`docs/process-scope-and-variables.md`](docs/process-scope-and-variables.md).

## 7. Testing

Testing evaluates both individual workflow components and the integrated business process. The test evidence covers the principal process pathways, including:

- Complete referral
- Incomplete referral and clarification
- Laboratory pathway
- Follow-up outcome
- Treatment outcome
- Discharge outcome

The testing evidence is organised under `testing/TC01/` through `testing/TC10/`, with the final testing report stored in `testing/TESTING_REPORT_RIVERSIDE_HOSPITAL.pdf`.

Testing covers process routes, decision outcomes, forms, gateways, process variables, automated service tasks and completed process instances.

## 8. Supporting Documentation

Key supporting documentation includes:

- [`docs/process-scope-and-variables.md`](docs/process-scope-and-variables.md) — process boundary, actors, variables, automated activities, forms and expected pathways.
- [`testing/TESTING_REPORT_RIVERSIDE_HOSPITAL.pdf`](testing/TESTING_REPORT_RIVERSIDE_HOSPITAL.pdf) — testing strategy, test coverage, evidence, defects, corrective actions and limitations.

## 9. Development and Configuration Management

The project is developed incrementally using Git and GitHub. Changes to modelling, forms, service tasks, testing evidence and supporting documentation are maintained as separate project artefacts so that the development history remains traceable.

## 10. Running the Prototype

The operational solution is intended to be run locally using Camunda with the BPMN process, deployed forms and Python service-task implementations available in this repository.

The service-task implementations use the Camunda Orchestration SDK and are associated with the job types configured in the BPMN model. The local Camunda environment, deployed process and worker processes should therefore be available before executing an end-to-end test scenario.

The repository contains the implementation artefacts required to reproduce the workflow: BPMN models, forms, service-task implementations and supporting documentation.

## 11. Prototype Limitations

This project is a workflow prototype. It does not provide live integration with NHS, GP, email or laboratory information systems. External interactions are simulated within the Camunda workflow, and the prototype should not be interpreted as a production clinical system.
