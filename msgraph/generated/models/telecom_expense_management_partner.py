from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class TelecomExpenseManagementPartner(Entity):
    """
    telecomExpenseManagementPartner resources represent the metadata and status of a given TEM service. Once your organization has onboarded with a partner, the partner can be enabled or disabled to switch TEM functionality on or off.
    """
    # Whether the partner's AAD app has been authorized to access Intune.
    app_authorized: Optional[bool] = None
    # Display name of the TEM partner.
    display_name: Optional[str] = None
    # Whether Intune's connection to the TEM service is currently enabled or disabled.
    enabled: Optional[bool] = None
    # Timestamp of the last request sent to Intune by the TEM partner.
    last_connection_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # URL of the TEM partner's administrative control panel, where an administrator can configure their TEM service.
    url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TelecomExpenseManagementPartner:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TelecomExpenseManagementPartner
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TelecomExpenseManagementPartner()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "appAuthorized": lambda n : setattr(self, 'app_authorized', n.get_bool_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "enabled": lambda n : setattr(self, 'enabled', n.get_bool_value()),
            "lastConnectionDateTime": lambda n : setattr(self, 'last_connection_date_time', n.get_datetime_value()),
            "url": lambda n : setattr(self, 'url', n.get_str_value()),
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
        writer.write_bool_value("appAuthorized", self.app_authorized)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("enabled", self.enabled)
        writer.write_datetime_value("lastConnectionDateTime", self.last_connection_date_time)
        writer.write_str_value("url", self.url)
    

