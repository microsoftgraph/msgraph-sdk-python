"""Discussion sample: one native Python read through Exchange's internal transport."""

import argparse
import asyncio
import json
from uuid import UUID, uuid4

import httpx
from azure.identity import DeviceCodeCredential
from kiota_abstractions.method import Method
from kiota_abstractions.native_response_handler import NativeResponseHandler
from kiota_abstractions.request_information import RequestInformation
from kiota_authentication_azure.azure_identity_authentication_provider import (
    AzureIdentityAuthenticationProvider,
)
from kiota_http.httpx_request_adapter import HttpxRequestAdapter
from kiota_http.kiota_client_factory import KiotaClientFactory
from kiota_http.middleware.options import (
    RedirectHandlerOption,
    ResponseHandlerOption,
    RetryHandlerOption,
)


async def read_quarantine(tenant_id: str, client_id: str, anchor_mailbox: str) -> None:
    """Authenticate with the caller's own app and print a count, without message data."""
    tenant_id, client_id = str(UUID(tenant_id)), str(UUID(client_id))
    if (
        not anchor_mailbox.startswith("UPN:")
        or not anchor_mailbox[4:].strip()
        or any(character in anchor_mailbox for character in "\r\n")
    ):
        raise ValueError(
            "anchor_mailbox must be a nonempty UPN:<lab-user> routing hint"
        )

    request = RequestInformation(Method.POST)
    request.url = (
        f"https://outlook.office365.com/adminapi/beta/{tenant_id}/InvokeCommand"
    )
    for name, value in {
        "Accept": "application/json",
        "Accept-Charset": "UTF-8",
        "Content-Type": "application/json",
        "X-CmdletName": "Get-QuarantineMessage",
        "X-AnchorMailbox": anchor_mailbox,
        "X-ResponseFormat": "auto",
        "X-SerializationLevel": "Partial",
        "Prefer": "odata.maxpagesize=1000",
        "client-request-id": str(uuid4()),
    }.items():
        request.headers.add(name, value)
    request.content = json.dumps(
        {
            "CmdletInput": {
                "CmdletName": "Get-QuarantineMessage",
                "Parameters": {"Page": 1, "PageSize": 1},
            }
        }
    ).encode("utf-8")
    request.add_request_options(
        [
            ResponseHandlerOption(NativeResponseHandler()),
            RedirectHandlerOption(should_redirect=False),
            RetryHandlerOption(max_retries=3),
        ]
    )

    with DeviceCodeCredential(
        tenant_id=tenant_id, client_id=client_id
    ) as credential:
        authentication = AzureIdentityAuthenticationProvider(
            credential,
            scopes=["https://outlook.office365.com/.default"],
            allowed_hosts=["outlook.office365.com"],
        )
        async with KiotaClientFactory.create_with_default_middleware() as http_client:
            adapter = HttpxRequestAdapter(authentication, http_client=http_client)
            response = await adapter.send_primitive_async(request, "bytes", None)
            if not isinstance(response, httpx.Response):
                raise TypeError("Expected the native HTTPX response")
            try:
                response.raise_for_status()
                payload = response.json()
                if not isinstance(payload, dict):
                    raise TypeError("Expected an Exchange response object")
                if "error" in payload or payload.get("@adminapi.errors"):
                    raise RuntimeError("Exchange returned a command error")
                records = payload.get("value")
                if not isinstance(records, list) or any(
                    not isinstance(record, dict) for record in records
                ):
                    raise RuntimeError("Expected a value array of records")
                if any("_cliXml" in record for record in records):
                    raise RuntimeError(
                        "PowerShell CLIXML deserialization is outside this sample"
                    )
                if payload.get("@odata.nextLink"):
                    raise RuntimeError("Transport continuation is outside this sample")
                request_id = response.headers.get("request-id") or response.headers.get(
                    "x-ms-request-id"
                )
                print(f"Returned {len(records)} record(s).")
                print(f"Request ID: {request_id or '(not supplied)'}")
            finally:
                await response.aclose()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tenant-id", required=True)
    parser.add_argument("--client-id", required=True)
    parser.add_argument("--anchor-mailbox", required=True)
    arguments = parser.parse_args()
    asyncio.run(
        read_quarantine(
            arguments.tenant_id, arguments.client_id, arguments.anchor_mailbox
        )
    )
