from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class DeviceLocalCredential(Entity, Parsable):
    # The name of the local admin account for which LAPS is enabled.
    account_name: Optional[str] = None
    # The SID of the local admin account for which LAPS is enabled.
    account_sid: Optional[str] = None
    # When the local administrator account credential for the device object was backed up to Azure Active Directory.
    backup_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The password for the local administrator account that is backed up to Azure Active Directory and returned as a Base64 encoded value.
    password_base64: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceLocalCredential:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceLocalCredential
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceLocalCredential()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "accountName": lambda n : setattr(self, 'account_name', n.get_str_value()),
            "accountSid": lambda n : setattr(self, 'account_sid', n.get_str_value()),
            "backupDateTime": lambda n : setattr(self, 'backup_date_time', n.get_datetime_value()),
            "passwordBase64": lambda n : setattr(self, 'password_base64', n.get_str_value()),
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
        writer.write_str_value("accountName", self.account_name)
        writer.write_str_value("accountSid", self.account_sid)
        writer.write_datetime_value("backupDateTime", self.backup_date_time)
        writer.write_str_value("passwordBase64", self.password_base64)
    

