import asyncio
from datetime import datetime
import uuid

from camunda_orchestration_sdk import (
    CamundaAsyncClient,
    ConnectedJobContext,
    WorkerConfig,
)


async def generate_appointment_reference(
    job: ConnectedJobContext,
) -> dict[str, object]:

    variables = job.variables.to_dict()

    print("\n--------------------------------")
    print("GENERATE APPOINTMENT REFERENCE")
    print("--------------------------------")
    print("Received variables:")
    print(variables)

    timestamp = datetime.now().strftime("%Y%m%d")
    unique_code = uuid.uuid4().hex[:6].upper()
    appointment_reference = f"RIV-APT-{timestamp}-{unique_code}"

    consultation_date = str(variables.get("consultationDate", "")).strip()
    consultation_time = str(variables.get("consultationTime", "")).strip()
    next_date = str(variables.get("nextAppointmentDate", "")).strip()
    next_time = str(variables.get("nextAppointmentTime", "")).strip()
    next_notes = str(variables.get("nextAppointmentNotes", "")).strip()
    final_outcome = str(variables.get("finalOutcomeType", "")).strip()

    if consultation_date:
        details = consultation_date
        if consultation_time:
            details += f" at {consultation_time}"
        confirmation_message = (
            f"Appointment successfully created for {details}. "
            f"Reference: {appointment_reference}."
        )
    else:
        confirmation_message = (
            f"Appointment successfully created. "
            f"Reference: {appointment_reference}."
        )

    result: dict[str, object] = {
        "appointmentReference": appointment_reference,
        "appointmentConfirmation": confirmation_message,
    }

    # Follow-up and treatment use the same worker. When next-appointment
    # details are present, expose the generated values under the variables
    # consumed by the downstream next-appointment form.
    if next_date or next_time or next_notes or final_outcome in {"followUp", "treatment"}:
        next_details = next_date or "Date not supplied"
        if next_time:
            next_details += f" at {next_time}"

        outcome_label = {
            "followUp": "follow-up consultation",
            "treatment": "treatment appointment",
        }.get(final_outcome, "next appointment")

        next_confirmation = (
            f"{outcome_label.capitalize()} scheduled for {next_details}. "
            f"Reference: {appointment_reference}."
        )
        if next_notes:
            next_confirmation += f" Notes: {next_notes}"

        result.update({
            "nextAppointmentReference": appointment_reference,
            "nextAppointmentConfirmation": next_confirmation,
        })

    print("Generated appointment reference:")
    print(appointment_reference)
    print("Returning to Camunda:")
    print(result)
    print("--------------------------------\n")

    return result


async def main() -> None:

    async with CamundaAsyncClient() as client:

        worker_config = WorkerConfig(
            job_type="generate-appointment-reference",
            job_timeout_milliseconds=30_000,
        )

        client.create_job_worker(
            config=worker_config,
            callback=generate_appointment_reference,
        )

        print("Riverside appointment worker is running.")
        print("Waiting for: generate-appointment-reference")
        print("Press Ctrl+C to stop the worker.\n")

        await client.run_workers()


if __name__ == "__main__":
    asyncio.run(main())
