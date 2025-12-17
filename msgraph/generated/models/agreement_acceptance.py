from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .agreement_acceptance_state import AgreementAcceptanceState
    from .entity import Entity

from .entity import Entity

@dataclass
class AgreementAcceptance(Entity, Parsable):
    # The identifier of the agreement file accepted by the user.
    agreement_file_id: Optional[str] = None
    # The identifier of the agreement.
    agreement_id: Optional[str] = None
    # The display name of the device used for accepting the agreement.
    device_display_name: Optional[str] = None
    # The unique identifier of the device used for accepting the agreement. Supports $filter (eq) and eq for null values.
    device_id: Optional[str] = None
    # The operating system used to accept the agreement.
    device_o_s_type: Optional[str] = None
    # The operating system version of the device used to accept the agreement.
    device_o_s_version: Optional[str] = None
    # The expiration date time of the acceptance. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Supports $filter (eq, ge, le) and eq for null values.
    expiration_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    recorded_date_time: Optional[datetime.datetime] = None
    # The state of the agreement acceptance. The possible values are: accepted, declined. Supports $filter (eq).
    state: Optional[AgreementAcceptanceState] = None
    # Display name of the user when the acceptance was recorded.
    user_display_name: Optional[str] = None
    # Email of the user when the acceptance was recorded.
    user_email: Optional[str] = None
    # The identifier of the user who accepted the agreement. Supports $filter (eq).
    user_id: Optional[str] = None
    # UPN of the user when the acceptance was recorded.
    user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AgreementAcceptance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AgreementAcceptance
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AgreementAcceptance()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .agreement_acceptance_state import AgreementAcceptanceState
        from .entity import Entity

        from .agreement_acceptance_state import AgreementAcceptanceState
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "agreementFileId": lambda n : setattr(self, 'agreement_file_id', n.get_str_value()),
            "agreementId": lambda n : setattr(self, 'agreement_id', n.get_str_value()),
            "deviceDisplayName": lambda n : setattr(self, 'device_display_name', n.get_str_value()),
            "deviceId": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "deviceOSType": lambda n : setattr(self, 'device_o_s_type', n.get_str_value()),
            "deviceOSVersion": lambda n : setattr(self, 'device_o_s_version', n.get_str_value()),
            "expirationDateTime": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "recordedDateTime": lambda n : setattr(self, 'recorded_date_time', n.get_datetime_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(AgreementAcceptanceState)),
            "userDisplayName": lambda n : setattr(self, 'user_display_name', n.get_str_value()),
            "userEmail": lambda n : setattr(self, 'user_email', n.get_str_value()),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("agreementFileId", self.agreement_file_id)
        writer.write_str_value("agreementId", self.agreement_id)
        writer.write_str_value("deviceDisplayName", self.device_display_name)
        writer.write_str_value("deviceId", self.device_id)
        writer.write_str_value("deviceOSType", self.device_o_s_type)
        writer.write_str_value("deviceOSVersion", self.device_o_s_version)
        writer.write_datetime_value("expirationDateTime", self.expiration_date_time)
        writer.write_datetime_value("recordedDateTime", self.recorded_date_time)
        writer.write_enum_value("state", self.state)
        writer.write_str_value("userDisplayName", self.user_display_name)
        writer.write_str_value("userEmail", self.user_email)
        writer.write_str_value("userId", self.user_id)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
    

