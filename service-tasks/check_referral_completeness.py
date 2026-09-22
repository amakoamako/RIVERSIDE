import asyncio

from camunda_orchestration_sdk import (
    CamundaAsyncClient,
    ConnectedJobContext,
    WorkerConfig,
)


async def check_referral_completeness(
    job: ConnectedJobContext,
) -> dict[str, object]:

    variables = job.variables.to_dict()

    print("\n--------------------------------")
    print("CHECK REFERRAL COMPLETENESS")
    print("--------------------------------")
    print("Received referral variables:")
    print(variables)

    # Required referral fields from Form_0861rxi
    required_fields = {
        "patientName": "Patient Name",
        "nhsNumber": "NHS Number",
        "dateOfBirth": "Date of Birth",
        "contactDetails": "Contact Details",
        "referringGP": "Referring GP",
        "gpPractice": "GP Practice",
        "referralReason": "Reason for Referral",
        "referralPriority": "Referral Priority",
    }

    missing_fields = []

    for key, label in required_fields.items():
        value = variables.get(key)

        # Treat missing, null or blank values as incomplete
        if value is None:
            missing_fields.append(label)
        elif isinstance(value, str) and not value.strip():
            missing_fields.append(label)
        elif isinstance(value, (list, dict)) and len(value) == 0:
            missing_fields.append(label)

    referral_complete = len(missing_fields) == 0

    if referral_complete:
        referral_check_message = (
            "Referral is complete. All required referral information is present."
        )
    else:
        referral_check_message = (
            "Referral is incomplete. Missing required information: "
            + ", ".join(missing_fields)
        )

    result = {
        "referralComplete": referral_complete,
        "missingReferralFields": missing_fields,
        "referralCheckMessage": referral_check_message,
    }

    print("\nReferral check result:")
    print(f"referralComplete = {referral_complete}")
    print(f"missingReferralFields = {missing_fields}")
    print(f"referralCheckMessage = {referral_check_message}")

    print("\nReturning to Camunda:")
    print(result)
    print("--------------------------------\n")

    return result


async def main() -> None:

    async with CamundaAsyncClient() as client:

        worker_config = WorkerConfig(
            job_type="check-referral-completeness",
            job_timeout_milliseconds=30_000,
        )

        client.create_job_worker(
            config=worker_config,
            callback=check_referral_completeness,
        )

        print("Riverside referral completeness worker is running.")
        print("Waiting for: check-referral-completeness")
        print("Press Ctrl+C to stop the worker.\n")

        await client.run_workers()


if __name__ == "__main__":
    asyncio.run(main())