from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .app_management_configuration import AppManagementConfiguration
    from .directory_object import DirectoryObject
    from .policy_base import PolicyBase

from .policy_base import PolicyBase

@dataclass
class AppManagementPolicy(PolicyBase):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.appManagementPolicy"
    # Collection of applications and service principals to which the policy is applied.
    applies_to: Optional[List[DirectoryObject]] = None
    # Denotes whether the policy is enabled.
    is_enabled: Optional[bool] = None
    # Restrictions that apply to an application or service principal object.
    restrictions: Optional[AppManagementConfiguration] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AppManagementPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AppManagementPolicy
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AppManagementPolicy()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .app_management_configuration import AppManagementConfiguration
        from .directory_object import DirectoryObject
        from .policy_base import PolicyBase

        from .app_management_configuration import AppManagementConfiguration
        from .directory_object import DirectoryObject
        from .policy_base import PolicyBase

        fields: Dict[str, Callable[[Any], None]] = {
            "appliesTo": lambda n : setattr(self, 'applies_to', n.get_collection_of_object_values(DirectoryObject)),
            "isEnabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
            "restrictions": lambda n : setattr(self, 'restrictions', n.get_object_value(AppManagementConfiguration)),
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
        writer.write_collection_of_object_values("appliesTo", self.applies_to)
        writer.write_bool_value("isEnabled", self.is_enabled)
        writer.write_object_value("restrictions", self.restrictions)
    

