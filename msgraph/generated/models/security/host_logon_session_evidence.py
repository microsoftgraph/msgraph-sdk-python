from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .alert_evidence import AlertEvidence
    from .device_evidence import DeviceEvidence
    from .user_evidence import UserEvidence

from .alert_evidence import AlertEvidence

@dataclass
class HostLogonSessionEvidence(AlertEvidence, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.hostLogonSessionEvidence"
    # The account that is associated with the sign-in session ID.
    account: Optional[UserEvidence] = None
    # The session end time, if known. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2024 is 2024-01-01T00:00:00Z.
    end_utc_date_time: Optional[datetime.datetime] = None
    # The host for the session.
    host: Optional[DeviceEvidence] = None
    # The session ID for the account reported in the alert, for example, 0x3e7.
    session_id: Optional[str] = None
    # The session start time, if known. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2024 is 2024-01-01T00:00:00Z.
    start_utc_date_time: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> HostLogonSessionEvidence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: HostLogonSessionEvidence
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return HostLogonSessionEvidence()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .alert_evidence import AlertEvidence
        from .device_evidence import DeviceEvidence
        from .user_evidence import UserEvidence

        from .alert_evidence import AlertEvidence
        from .device_evidence import DeviceEvidence
        from .user_evidence import UserEvidence

        fields: dict[str, Callable[[Any], None]] = {
            "account": lambda n : setattr(self, 'account', n.get_object_value(UserEvidence)),
            "endUtcDateTime": lambda n : setattr(self, 'end_utc_date_time', n.get_datetime_value()),
            "host": lambda n : setattr(self, 'host', n.get_object_value(DeviceEvidence)),
            "sessionId": lambda n : setattr(self, 'session_id', n.get_str_value()),
            "startUtcDateTime": lambda n : setattr(self, 'start_utc_date_time', n.get_datetime_value()),
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
        writer.write_object_value("account", self.account)
        writer.write_datetime_value("endUtcDateTime", self.end_utc_date_time)
        writer.write_object_value("host", self.host)
        writer.write_str_value("sessionId", self.session_id)
        writer.write_datetime_value("startUtcDateTime", self.start_utc_date_time)
    

