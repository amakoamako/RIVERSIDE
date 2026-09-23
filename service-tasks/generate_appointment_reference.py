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

    confirmation_message = (
        f"Appointment successfully created. "
        f"Reference: {appointment_reference}"
    )

    result = {
        "appointmentReference": appointment_reference,
        "appointmentConfirmation": confirmation_message,
    }

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