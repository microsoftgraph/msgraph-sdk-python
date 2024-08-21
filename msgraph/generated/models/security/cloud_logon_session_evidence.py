from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .alert_evidence import AlertEvidence
    from .user_evidence import UserEvidence

from .alert_evidence import AlertEvidence

@dataclass
class CloudLogonSessionEvidence(AlertEvidence):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.cloudLogonSessionEvidence"
    # The account associated with the sign-in session.
    account: Optional[UserEvidence] = None
    # The browser that is used for the sign-in, if known.
    browser: Optional[str] = None
    # The friendly name of the device, if known.
    device_name: Optional[str] = None
    # The operating system that the device is running, if known.
    operating_system: Optional[str] = None
    # The previous sign-in time for this account, if known.
    previous_logon_date_time: Optional[datetime.datetime] = None
    # The authentication protocol that is used in this session, if known.
    protocol: Optional[str] = None
    # The session ID for the account reported in the alert.
    session_id: Optional[str] = None
    # The session start time, if known.
    start_utc_date_time: Optional[datetime.datetime] = None
    # The user agent that is used for the sign-in, if known.
    user_agent: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudLogonSessionEvidence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudLogonSessionEvidence
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudLogonSessionEvidence()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .alert_evidence import AlertEvidence
        from .user_evidence import UserEvidence

        from .alert_evidence import AlertEvidence
        from .user_evidence import UserEvidence

        fields: Dict[str, Callable[[Any], None]] = {
            "account": lambda n : setattr(self, 'account', n.get_object_value(UserEvidence)),
            "browser": lambda n : setattr(self, 'browser', n.get_str_value()),
            "deviceName": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "operatingSystem": lambda n : setattr(self, 'operating_system', n.get_str_value()),
            "previousLogonDateTime": lambda n : setattr(self, 'previous_logon_date_time', n.get_datetime_value()),
            "protocol": lambda n : setattr(self, 'protocol', n.get_str_value()),
            "sessionId": lambda n : setattr(self, 'session_id', n.get_str_value()),
            "startUtcDateTime": lambda n : setattr(self, 'start_utc_date_time', n.get_datetime_value()),
            "userAgent": lambda n : setattr(self, 'user_agent', n.get_str_value()),
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
        writer.write_str_value("browser", self.browser)
        writer.write_str_value("deviceName", self.device_name)
        writer.write_str_value("operatingSystem", self.operating_system)
        writer.write_datetime_value("previousLogonDateTime", self.previous_logon_date_time)
        writer.write_str_value("protocol", self.protocol)
        writer.write_str_value("sessionId", self.session_id)
        writer.write_datetime_value("startUtcDateTime", self.start_utc_date_time)
        writer.write_str_value("userAgent", self.user_agent)
    

