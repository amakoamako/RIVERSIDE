import asyncio
import uuid

from camunda_orchestration_sdk import (
    CamundaAsyncClient,
    ConnectedJobContext,
    WorkerConfig,
)


async def generate_lab_appointment_reference(
    job: ConnectedJobContext,
) -> dict[str, object]:

    variables = job.variables.to_dict()

    print("\n--------------------------------")
    print("GENERATE LAB APPOINTMENT REFERENCE")
    print("--------------------------------")
    print("Received variables:")
    print(variables)

    patient_name = str(
        variables.get("patientName", "")
    ).strip()

    lab_appointment_date = str(
        variables.get("labAppointmentDate", "")
    ).strip()

    lab_appointment_time = str(
        variables.get("labAppointmentTime", "")
    ).strip()

    laboratory_test_reason = str(
        variables.get("laboratoryTestReason", "")
    ).strip()

    if not lab_appointment_date:
        raise ValueError(
            "Cannot generate laboratory appointment reference: "
            "labAppointmentDate is missing."
        )

    unique_part = uuid.uuid4().hex[:6].upper()

    lab_appointment_reference = f"LAB-{unique_part}"

    if lab_appointment_time:
        appointment_details = (
            f"{lab_appointment_date} at {lab_appointment_time}"
        )
    else:
        appointment_details = lab_appointment_date

    lab_appointment_confirmation_message = (
        f"Laboratory appointment confirmed for {patient_name}. "
        f"Appointment: {appointment_details}. "
        f"Reference: {lab_appointment_reference}."
    )

    if laboratory_test_reason:
        lab_appointment_confirmation_message += (
            f" Test reason: {laboratory_test_reason}."
        )

    result = {
        "labAppointmentReference": lab_appointment_reference,
        "labAppointmentConfirmation":
            lab_appointment_confirmation_message,
    }

    print("Generated laboratory appointment reference:")
    print(lab_appointment_reference)

    print("Returning to Camunda:")
    print(result)
    print("--------------------------------\n")

    return result


async def main() -> None:

    async with CamundaAsyncClient() as client:

        worker_config = WorkerConfig(
            job_type="generate-lab-appointment-reference",
            job_timeout_milliseconds=30_000,
        )

        client.create_job_worker(
            config=worker_config,
            callback=generate_lab_appointment_reference,
        )

        print("Riverside laboratory appointment worker is running.")
        print("Waiting for: generate-lab-appointment-reference")
        print("Press Ctrl+C to stop the worker.\n")

        await client.run_workers()


if __name__ == "__main__":
    asyncio.run(main())