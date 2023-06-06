from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import app_management_configuration, directory_object, policy_base

from . import policy_base

@dataclass
class AppManagementPolicy(policy_base.PolicyBase):
    odata_type = "#microsoft.graph.appManagementPolicy"
    # Collection of applications and service principals to which the policy is applied.
    applies_to: Optional[List[directory_object.DirectoryObject]] = None
    # Denotes whether the policy is enabled.
    is_enabled: Optional[bool] = None
    # Restrictions that apply to an application or service principal object.
    restrictions: Optional[app_management_configuration.AppManagementConfiguration] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AppManagementPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AppManagementPolicy
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AppManagementPolicy()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import app_management_configuration, directory_object, policy_base

        fields: Dict[str, Callable[[Any], None]] = {
            "appliesTo": lambda n : setattr(self, 'applies_to', n.get_collection_of_object_values(directory_object.DirectoryObject)),
            "isEnabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
            "restrictions": lambda n : setattr(self, 'restrictions', n.get_object_value(app_management_configuration.AppManagementConfiguration)),
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
        writer.write_collection_of_object_values("appliesTo", self.applies_to)
        writer.write_bool_value("isEnabled", self.is_enabled)
        writer.write_object_value("restrictions", self.restrictions)
    

