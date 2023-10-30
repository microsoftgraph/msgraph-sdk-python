from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .remote_assistance_onboarding_status import RemoteAssistanceOnboardingStatus

from .entity import Entity

@dataclass
class RemoteAssistancePartner(Entity):
    """
    RemoteAssistPartner resources represent the metadata and status of a given Remote Assistance partner service.
    """
    # Display name of the partner.
    display_name: Optional[str] = None
    # Timestamp of the last request sent to Intune by the TEM partner.
    last_connection_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The current TeamViewer connector status
    onboarding_status: Optional[RemoteAssistanceOnboardingStatus] = None
    # URL of the partner's onboarding portal, where an administrator can configure their Remote Assistance service.
    onboarding_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RemoteAssistancePartner:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RemoteAssistancePartner
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return RemoteAssistancePartner()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .remote_assistance_onboarding_status import RemoteAssistanceOnboardingStatus

        from .entity import Entity
        from .remote_assistance_onboarding_status import RemoteAssistanceOnboardingStatus

        fields: Dict[str, Callable[[Any], None]] = {
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "last_connection_date_time": lambda n : setattr(self, 'last_connection_date_time', n.get_datetime_value()),
            "onboarding_status": lambda n : setattr(self, 'onboarding_status', n.get_enum_value(RemoteAssistanceOnboardingStatus)),
            "onboarding_url": lambda n : setattr(self, 'onboarding_url', n.get_str_value()),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("display_name", self.display_name)
        writer.write_datetime_value("last_connection_date_time", self.last_connection_date_time)
        writer.write_enum_value("onboarding_status", self.onboarding_status)
        writer.write_str_value("onboarding_url", self.onboarding_url)
    

