from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .shift_preferences import ShiftPreferences

from .entity import Entity

@dataclass
class UserSettings(Entity):
    # Reflects the organization level setting controlling delegate access to the trending API. When set to true, the organization doesn't have access to Office Delve. The relevancy of the content displayed in Microsoft 365, for example in Suggested sites in SharePoint Home and the Discover view in OneDrive for Business is affected for the whole organization. This setting is read-only and can only be changed by administrators in the SharePoint admin center.
    contribution_to_content_discovery_as_organization_disabled: Optional[bool] = None
    # When set to true, the delegate access to the user's trending API is disabled. When set to true, documents in the user's Office Delve are disabled. When set to true, the relevancy of the content displayed in Microsoft 365, for example in Suggested sites in SharePoint Home and the Discover view in OneDrive for Business is affected. Users can control this setting in Office Delve.
    contribution_to_content_discovery_disabled: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The shiftPreferences property
    shift_preferences: Optional[ShiftPreferences] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserSettings
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return UserSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .shift_preferences import ShiftPreferences

        from .entity import Entity
        from .shift_preferences import ShiftPreferences

        fields: Dict[str, Callable[[Any], None]] = {
            "contributionToContentDiscoveryAsOrganizationDisabled": lambda n : setattr(self, 'contribution_to_content_discovery_as_organization_disabled', n.get_bool_value()),
            "contributionToContentDiscoveryDisabled": lambda n : setattr(self, 'contribution_to_content_discovery_disabled', n.get_bool_value()),
            "shiftPreferences": lambda n : setattr(self, 'shift_preferences', n.get_object_value(ShiftPreferences)),
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
        writer.write_bool_value("contributionToContentDiscoveryAsOrganizationDisabled", self.contribution_to_content_discovery_as_organization_disabled)
        writer.write_bool_value("contributionToContentDiscoveryDisabled", self.contribution_to_content_discovery_disabled)
        writer.write_object_value("shiftPreferences", self.shift_preferences)
    

