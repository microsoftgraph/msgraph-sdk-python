# Native Python quarantine access: discussion sample

This small extract demonstrates an Exchange quarantine list request using Azure
Identity and Kiota. It authenticates with the caller's own app and sends HTTP
directly; it does not execute PowerShell or import ExchangeOnlineManagement.

The proposal asks where supported Python quarantine management should belong and
which API contract Microsoft recommends. The Exchange route used here is an
internal module transport, separate from Graph and the public Admin API v2 preview.
This sample does not add an API to `GraphServiceClient` or the generated SDK.

The underlying lab client successfully completed one list request on 2026-10-16.
This extracted sample is validated offline only. It covers one read, prints no
message data, and deliberately omits paging, CLIXML parsing, export and mutations.

## Run in a commercial-cloud lab

Use your own single-tenant public-client app with delegated `Exchange.Manage`
consent and a signed-in lab account with the required Exchange RBAC permissions.
This management permission is broader than the sample's read-only operation.
The script does not create an app or grant permissions.

```powershell
python -m pip install azure-identity httpx microsoft-kiota-abstractions microsoft-kiota-authentication-azure microsoft-kiota-http
python docs/proposals/quarantine/quarantine_read.py --tenant-id '<tenant-guid>' --client-id '<your-app-guid>' --anchor-mailbox 'UPN:admin@contoso.onmicrosoft.com'
```

## Related documented interfaces

- [Quarantine management through PowerShell](https://learn.microsoft.com/en-us/defender-office-365/quarantine-admin-manage-messages-files#use-powershell-to-manage-quarantined-messages)
- [Public Exchange Admin API scope](https://learn.microsoft.com/en-us/exchange/reference/admin-api-overview)
- [Graph analyzed-email list](https://learn.microsoft.com/en-us/graph/api/security-collaborationroot-list-analyzedemails?view=graph-rest-1.0) and [remediation](https://learn.microsoft.com/en-us/graph/api/security-analyzedemail-remediate?view=graph-rest-1.0): related APIs whose coverage, application permissions and Defender licensing must be assessed separately.
