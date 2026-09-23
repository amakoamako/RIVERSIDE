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

    current_date = datetime.now().strftime("%d/%m/%Y")

    draft_letter = (
        f"Riverside Hospital\n\n"
        f"Date: {current_date}\n"
        f"Patient: {patient_name}\n\n"
        f"Clinical Outcome: {final_outcome}\n\n"
        f"Consultation Summary:\n"
        f"{consultation_notes}\n\n"
        f"This is a draft clinical outcome communication "
        f"generated automatically for review."
    )

    result = {
    "draftOutcomeLetter": draft_letter,
    "finalPatientOutcomeCommunication": draft_letter,
    "finalGPOutcomeCommunication": draft_letter,
    "outcomeLetterGenerated": True,
    "outcomeLetterGenerationMessage": "Draft outcome letter generated successfully",
    }

    print("\nDraft outcome letter generated:")
    print(draft_letter)

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