from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

permission_grant_condition_set = lazy_import('msgraph.generated.models.permission_grant_condition_set')
policy_base = lazy_import('msgraph.generated.models.policy_base')

class PermissionGrantPolicy(policy_base.PolicyBase):
    def __init__(self,) -> None:
        """
        Instantiates a new PermissionGrantPolicy and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.permissionGrantPolicy"
        # Condition sets which are excluded in this permission grant policy. Automatically expanded on GET.
        self._excludes: Optional[List[permission_grant_condition_set.PermissionGrantConditionSet]] = None
        # Condition sets which are included in this permission grant policy. Automatically expanded on GET.
        self._includes: Optional[List[permission_grant_condition_set.PermissionGrantConditionSet]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PermissionGrantPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PermissionGrantPolicy
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PermissionGrantPolicy()
    
    @property
    def excludes(self,) -> Optional[List[permission_grant_condition_set.PermissionGrantConditionSet]]:
        """
        Gets the excludes property value. Condition sets which are excluded in this permission grant policy. Automatically expanded on GET.
        Returns: Optional[List[permission_grant_condition_set.PermissionGrantConditionSet]]
        """
        return self._excludes
    
    @excludes.setter
    def excludes(self,value: Optional[List[permission_grant_condition_set.PermissionGrantConditionSet]] = None) -> None:
        """
        Sets the excludes property value. Condition sets which are excluded in this permission grant policy. Automatically expanded on GET.
        Args:
            value: Value to set for the excludes property.
        """
        self._excludes = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "excludes": lambda n : setattr(self, 'excludes', n.get_collection_of_object_values(permission_grant_condition_set.PermissionGrantConditionSet)),
            "includes": lambda n : setattr(self, 'includes', n.get_collection_of_object_values(permission_grant_condition_set.PermissionGrantConditionSet)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def includes(self,) -> Optional[List[permission_grant_condition_set.PermissionGrantConditionSet]]:
        """
        Gets the includes property value. Condition sets which are included in this permission grant policy. Automatically expanded on GET.
        Returns: Optional[List[permission_grant_condition_set.PermissionGrantConditionSet]]
        """
        return self._includes
    
    @includes.setter
    def includes(self,value: Optional[List[permission_grant_condition_set.PermissionGrantConditionSet]] = None) -> None:
        """
        Sets the includes property value. Condition sets which are included in this permission grant policy. Automatically expanded on GET.
        Args:
            value: Value to set for the includes property.
        """
        self._includes = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("excludes", self.excludes)
        writer.write_collection_of_object_values("includes", self.includes)
    

