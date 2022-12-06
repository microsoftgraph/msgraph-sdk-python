from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
shift_preferences = lazy_import('msgraph.generated.models.shift_preferences')

class UserSettings(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new userSettings and sets the default values.
        """
        super().__init__()
        # The contributionToContentDiscoveryAsOrganizationDisabled property
        self._contribution_to_content_discovery_as_organization_disabled: Optional[bool] = None
        # The contributionToContentDiscoveryDisabled property
        self._contribution_to_content_discovery_disabled: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The shiftPreferences property
        self._shift_preferences: Optional[shift_preferences.ShiftPreferences] = None
    
    @property
    def contribution_to_content_discovery_as_organization_disabled(self,) -> Optional[bool]:
        """
        Gets the contributionToContentDiscoveryAsOrganizationDisabled property value. The contributionToContentDiscoveryAsOrganizationDisabled property
        Returns: Optional[bool]
        """
        return self._contribution_to_content_discovery_as_organization_disabled
    
    @contribution_to_content_discovery_as_organization_disabled.setter
    def contribution_to_content_discovery_as_organization_disabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the contributionToContentDiscoveryAsOrganizationDisabled property value. The contributionToContentDiscoveryAsOrganizationDisabled property
        Args:
            value: Value to set for the contributionToContentDiscoveryAsOrganizationDisabled property.
        """
        self._contribution_to_content_discovery_as_organization_disabled = value
    
    @property
    def contribution_to_content_discovery_disabled(self,) -> Optional[bool]:
        """
        Gets the contributionToContentDiscoveryDisabled property value. The contributionToContentDiscoveryDisabled property
        Returns: Optional[bool]
        """
        return self._contribution_to_content_discovery_disabled
    
    @contribution_to_content_discovery_disabled.setter
    def contribution_to_content_discovery_disabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the contributionToContentDiscoveryDisabled property value. The contributionToContentDiscoveryDisabled property
        Args:
            value: Value to set for the contributionToContentDiscoveryDisabled property.
        """
        self._contribution_to_content_discovery_disabled = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "contribution_to_content_discovery_as_organization_disabled": lambda n : setattr(self, 'contribution_to_content_discovery_as_organization_disabled', n.get_bool_value()),
            "contribution_to_content_discovery_disabled": lambda n : setattr(self, 'contribution_to_content_discovery_disabled', n.get_bool_value()),
            "shift_preferences": lambda n : setattr(self, 'shift_preferences', n.get_object_value(shift_preferences.ShiftPreferences)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("contributionToContentDiscoveryAsOrganizationDisabled", self.contribution_to_content_discovery_as_organization_disabled)
        writer.write_bool_value("contributionToContentDiscoveryDisabled", self.contribution_to_content_discovery_disabled)
        writer.write_object_value("shiftPreferences", self.shift_preferences)
    
    @property
    def shift_preferences(self,) -> Optional[shift_preferences.ShiftPreferences]:
        """
        Gets the shiftPreferences property value. The shiftPreferences property
        Returns: Optional[shift_preferences.ShiftPreferences]
        """
        return self._shift_preferences
    
    @shift_preferences.setter
    def shift_preferences(self,value: Optional[shift_preferences.ShiftPreferences] = None) -> None:
        """
        Sets the shiftPreferences property value. The shiftPreferences property
        Args:
            value: Value to set for the shiftPreferences property.
        """
        self._shift_preferences = value
    

