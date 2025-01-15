from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .pstn_call_duration_source import PstnCallDurationSource

@dataclass
class PstnCallLogRow(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The source of the call duration data. If the call uses a third-party telecommunications operator via the Operator Connect Program, the operator can provide their own call duration data. In this case, the property value is operator. Otherwise, the value is microsoft.
    call_duration_source: Optional[PstnCallDurationSource] = None
    # Call identifier. Not guaranteed to be unique.
    call_id: Optional[str] = None
    # Indicates whether the call was a PSTN outbound or inbound call and the type of call, such as a call placed by a user or an audio conference.
    call_type: Optional[str] = None
    # Number dialed in E.164 format.
    callee_number: Optional[str] = None
    # Number that received the call for inbound calls or the number dialed for outbound calls. E.164 format.
    caller_number: Optional[str] = None
    # Amount of money or cost of the call that is charged to your account.
    charge: Optional[float] = None
    # ID of the audio conference.
    conference_id: Optional[str] = None
    # Connection fee price.
    connection_charge: Optional[float] = None
    # Type of currency used to calculate the cost of the call. For details, see (ISO 4217.
    currency: Optional[str] = None
    # Whether the call was domestic (within a country or region) or international (outside a country or region), based on the user's location.
    destination_context: Optional[str] = None
    # Country or region dialed.
    destination_name: Optional[str] = None
    # How long the call was connected, in seconds.
    duration: Optional[int] = None
    # Call end time.
    end_date_time: Optional[datetime.datetime] = None
    # Unique call identifier. GUID.
    id: Optional[str] = None
    # User's phone number type, such as a service of toll-free number.
    inventory_type: Optional[str] = None
    # The license used for the call.
    license_capability: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The telecommunications operator which provided PSTN services for this call. This might be Microsoft, or it might be a third-party operator via the Operator Connect Program.
    operator: Optional[str] = None
    # Call start time.
    start_date_time: Optional[datetime.datetime] = None
    # Country code of the tenant. For details, see ISO 3166-1 alpha-2.
    tenant_country_code: Optional[str] = None
    # Country code of the user. For details, see ISO 3166-1 alpha-2.
    usage_country_code: Optional[str] = None
    # Display name of the user.
    user_display_name: Optional[str] = None
    # Calling user's ID in Microsoft Graph. GUID. This and other user info will be null/empty for bot call types (ucapin, ucapout).
    user_id: Optional[str] = None
    # The user principal name (sign-in name) in Microsoft Entra ID. This is usually the same as the user's SIP address, and can be the same as the user's email address.
    user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PstnCallLogRow:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PstnCallLogRow
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PstnCallLogRow()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .pstn_call_duration_source import PstnCallDurationSource

        from .pstn_call_duration_source import PstnCallDurationSource

        fields: dict[str, Callable[[Any], None]] = {
            "callDurationSource": lambda n : setattr(self, 'call_duration_source', n.get_enum_value(PstnCallDurationSource)),
            "callId": lambda n : setattr(self, 'call_id', n.get_str_value()),
            "callType": lambda n : setattr(self, 'call_type', n.get_str_value()),
            "calleeNumber": lambda n : setattr(self, 'callee_number', n.get_str_value()),
            "callerNumber": lambda n : setattr(self, 'caller_number', n.get_str_value()),
            "charge": lambda n : setattr(self, 'charge', n.get_float_value()),
            "conferenceId": lambda n : setattr(self, 'conference_id', n.get_str_value()),
            "connectionCharge": lambda n : setattr(self, 'connection_charge', n.get_float_value()),
            "currency": lambda n : setattr(self, 'currency', n.get_str_value()),
            "destinationContext": lambda n : setattr(self, 'destination_context', n.get_str_value()),
            "destinationName": lambda n : setattr(self, 'destination_name', n.get_str_value()),
            "duration": lambda n : setattr(self, 'duration', n.get_int_value()),
            "endDateTime": lambda n : setattr(self, 'end_date_time', n.get_datetime_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "inventoryType": lambda n : setattr(self, 'inventory_type', n.get_str_value()),
            "licenseCapability": lambda n : setattr(self, 'license_capability', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "operator": lambda n : setattr(self, 'operator', n.get_str_value()),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
            "tenantCountryCode": lambda n : setattr(self, 'tenant_country_code', n.get_str_value()),
            "usageCountryCode": lambda n : setattr(self, 'usage_country_code', n.get_str_value()),
            "userDisplayName": lambda n : setattr(self, 'user_display_name', n.get_str_value()),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_enum_value("callDurationSource", self.call_duration_source)
        writer.write_str_value("callId", self.call_id)
        writer.write_str_value("callType", self.call_type)
        writer.write_str_value("calleeNumber", self.callee_number)
        writer.write_str_value("callerNumber", self.caller_number)
        writer.write_float_value("charge", self.charge)
        writer.write_str_value("conferenceId", self.conference_id)
        writer.write_float_value("connectionCharge", self.connection_charge)
        writer.write_str_value("currency", self.currency)
        writer.write_str_value("destinationContext", self.destination_context)
        writer.write_str_value("destinationName", self.destination_name)
        writer.write_int_value("duration", self.duration)
        writer.write_datetime_value("endDateTime", self.end_date_time)
        writer.write_str_value("id", self.id)
        writer.write_str_value("inventoryType", self.inventory_type)
        writer.write_str_value("licenseCapability", self.license_capability)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("operator", self.operator)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_str_value("tenantCountryCode", self.tenant_country_code)
        writer.write_str_value("usageCountryCode", self.usage_country_code)
        writer.write_str_value("userDisplayName", self.user_display_name)
        writer.write_str_value("userId", self.user_id)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
        writer.write_additional_data_value(self.additional_data)
    

