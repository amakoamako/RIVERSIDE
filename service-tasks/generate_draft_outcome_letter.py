import asyncio
from datetime import datetime

from camunda_orchestration_sdk import (
    CamundaAsyncClient,
    ConnectedJobContext,
    WorkerConfig,
)


async def generate_draft_outcome_letter(
    job: ConnectedJobContext,
) -> dict[str, object]:

    variables = job.variables.to_dict()

    print("\n--------------------------------")
    print("GENERATE DRAFT OUTCOME LETTER")
    print("--------------------------------")
    print("Received variables:")
    print(variables)

    patient_name = variables.get("patientName", "Test Patient")
    final_outcome = variables.get("finalOutcomeType", "treatment")
    consultation_notes = variables.get(
        "consultationNotes",
        "Clinical review completed."
    )
    clinical_plan = variables.get(
        "clinicalPlan",
        "Please follow the clinical plan provided by the Specialist Doctor."
    )
    current_date = datetime.now().strftime("%d/%m/%Y")

    patient_draft = (
        f"Riverside Hospital\n\n"
        f"Date: {current_date}\n"
        f"Patient: {patient_name}\n\n"
        f"Clinical Outcome: {final_outcome}\n\n"
        f"Consultation Summary:\n{consultation_notes}\n\n"
        f"Clinical Plan:\n{clinical_plan}\n\n"
        "This is a draft communication for patient review and finalisation."
    )

    gp_draft = (
        f"Riverside Hospital – Clinical Outcome Communication\n\n"
        f"Date: {current_date}\n"
        f"Patient: {patient_name}\n\n"
        f"Outcome: {final_outcome}\n\n"
        f"Consultation Summary:\n{consultation_notes}\n\n"
        f"Clinical Plan:\n{clinical_plan}\n\n"
        "This is a draft communication for Medical Secretary review and finalisation."
    )

    result = {
        "draftPatientOutcomeLetter": patient_draft,
        "draftGPOutcomeLetter": gp_draft,
        "outcomeLetterGenerated": True,
        "outcomeLetterGenerationMessage": "Draft patient and GP outcome communications generated successfully.",
    }

    print("\nDraft patient communication generated:")
    print(patient_draft)
    print("\nDraft GP communication generated:")
    print(gp_draft)
    print("\nReturning to Camunda:")
    print(result)
    print("--------------------------------\n")

    return result


async def main() -> None:

    async with CamundaAsyncClient() as client:

        worker_config = WorkerConfig(
            job_type="generate-draft-outcome-letter",
            job_timeout_milliseconds=30_000,
        )

        client.create_job_worker(
            config=worker_config,
            callback=generate_draft_outcome_letter,
        )

        print("Riverside outcome letter worker is running.")
        print("Waiting for: generate-draft-outcome-letter")
        print("Press Ctrl+C to stop the worker.\n")

        await client.run_workers()


if __name__ == "__main__":
    asyncio.run(main())
