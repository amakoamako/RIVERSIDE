import asyncio

from camunda_orchestration_sdk import (
    CamundaAsyncClient,
    ConnectedJobContext,
    WorkerConfig,
)


async def notify_specialist_results_available(
    job: ConnectedJobContext,
) -> dict[str, object]:

    variables = job.variables.to_dict()

    print("\n--------------------------------")
    print("NOTIFY SPECIALIST RESULTS AVAILABLE")
    print("--------------------------------")
    print("Received variables:")
    print(variables)

    patient_name = str(variables.get("patientName", "")).strip()
    nhs_number = str(variables.get("nhsNumber", "")).strip()
    lab_appointment_reference = str(
        variables.get("labAppointmentReference", "")
    ).strip()
    lab_result = variables.get("labResult")

    if lab_result is None or str(lab_result).strip() == "":
        raise ValueError(
            "Cannot notify specialist: labResult is missing."
        )

    notification = (
        f"Laboratory results are now available for {patient_name}"
    )

    if nhs_number:
        notification += f" (NHS Number: {nhs_number})"

    if lab_appointment_reference:
        notification += (
            f". Laboratory reference: {lab_appointment_reference}"
        )

    notification += ". The results are ready for specialist review."

    result = {
        "labResultAvailable": True,
        "specialistResultNotification": notification,
    }

    print("Laboratory result found.")
    print("Specialist notification generated:")
    print(notification)
    print("Returning to Camunda:")
    print(result)
    print("--------------------------------\n")

    return result


async def main() -> None:

    async with CamundaAsyncClient() as client:

        worker_config = WorkerConfig(
            job_type="notify-specialist-results-available",
            job_timeout_milliseconds=30_000,
        )

        client.create_job_worker(
            config=worker_config,
            callback=notify_specialist_results_available,
        )

        print("Riverside specialist results notification worker is running.")
        print("Waiting for: notify-specialist-results-available")
        print("Press Ctrl+C to stop the worker.\n")

        await client.run_workers()


if __name__ == "__main__":
    asyncio.run(main())
