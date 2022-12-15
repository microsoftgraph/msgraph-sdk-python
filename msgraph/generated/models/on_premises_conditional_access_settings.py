from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class OnPremisesConditionalAccessSettings(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new onPremisesConditionalAccessSettings and sets the default values.
        """
        super().__init__()
        # Indicates if on premises conditional access is enabled for this organization
        self._enabled: Optional[bool] = None
        # User groups that will be exempt by on premises conditional access. All users in these groups will be exempt from the conditional access policy.
        self._excluded_groups: Optional[List[Guid]] = None
        # User groups that will be targeted by on premises conditional access. All users in these groups will be required to have mobile device managed and compliant for mail access.
        self._included_groups: Optional[List[Guid]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Override the default access rule when allowing a device to ensure access is granted.
        self._override_default_rule: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OnPremisesConditionalAccessSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OnPremisesConditionalAccessSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OnPremisesConditionalAccessSettings()
    
    @property
    def enabled(self,) -> Optional[bool]:
        """
        Gets the enabled property value. Indicates if on premises conditional access is enabled for this organization
        Returns: Optional[bool]
        """
        return self._enabled
    
    @enabled.setter
    def enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the enabled property value. Indicates if on premises conditional access is enabled for this organization
        Args:
            value: Value to set for the enabled property.
        """
        self._enabled = value
    
    @property
    def excluded_groups(self,) -> Optional[List[Guid]]:
        """
        Gets the excludedGroups property value. User groups that will be exempt by on premises conditional access. All users in these groups will be exempt from the conditional access policy.
        Returns: Optional[List[Guid]]
        """
        return self._excluded_groups
    
    @excluded_groups.setter
    def excluded_groups(self,value: Optional[List[Guid]] = None) -> None:
        """
        Sets the excludedGroups property value. User groups that will be exempt by on premises conditional access. All users in these groups will be exempt from the conditional access policy.
        Args:
            value: Value to set for the excludedGroups property.
        """
        self._excluded_groups = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "enabled": lambda n : setattr(self, 'enabled', n.get_bool_value()),
            "excluded_groups": lambda n : setattr(self, 'excluded_groups', n.get_collection_of_primitive_values(guid)),
            "included_groups": lambda n : setattr(self, 'included_groups', n.get_collection_of_primitive_values(guid)),
            "override_default_rule": lambda n : setattr(self, 'override_default_rule', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def included_groups(self,) -> Optional[List[Guid]]:
        """
        Gets the includedGroups property value. User groups that will be targeted by on premises conditional access. All users in these groups will be required to have mobile device managed and compliant for mail access.
        Returns: Optional[List[Guid]]
        """
        return self._included_groups
    
    @included_groups.setter
    def included_groups(self,value: Optional[List[Guid]] = None) -> None:
        """
        Sets the includedGroups property value. User groups that will be targeted by on premises conditional access. All users in these groups will be required to have mobile device managed and compliant for mail access.
        Args:
            value: Value to set for the includedGroups property.
        """
        self._included_groups = value
    
    @property
    def override_default_rule(self,) -> Optional[bool]:
        """
        Gets the overrideDefaultRule property value. Override the default access rule when allowing a device to ensure access is granted.
        Returns: Optional[bool]
        """
        return self._override_default_rule
    
    @override_default_rule.setter
    def override_default_rule(self,value: Optional[bool] = None) -> None:
        """
        Sets the overrideDefaultRule property value. Override the default access rule when allowing a device to ensure access is granted.
        Args:
            value: Value to set for the overrideDefaultRule property.
        """
        self._override_default_rule = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("enabled", self.enabled)
        writer.write_collection_of_primitive_values("excludedGroups", self.excluded_groups)
        writer.write_collection_of_primitive_values("includedGroups", self.included_groups)
        writer.write_bool_value("overrideDefaultRule", self.override_default_rule)
    

