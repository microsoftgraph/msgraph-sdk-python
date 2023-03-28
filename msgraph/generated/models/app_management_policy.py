from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

app_management_configuration = lazy_import('msgraph.generated.models.app_management_configuration')
directory_object = lazy_import('msgraph.generated.models.directory_object')
policy_base = lazy_import('msgraph.generated.models.policy_base')

class AppManagementPolicy(policy_base.PolicyBase):
    @property
    def applies_to(self,) -> Optional[List[directory_object.DirectoryObject]]:
        """
        Gets the appliesTo property value. The appliesTo property
        Returns: Optional[List[directory_object.DirectoryObject]]
        """
        return self._applies_to
    
    @applies_to.setter
    def applies_to(self,value: Optional[List[directory_object.DirectoryObject]] = None) -> None:
        """
        Sets the appliesTo property value. The appliesTo property
        Args:
            value: Value to set for the applies_to property.
        """
        self._applies_to = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new AppManagementPolicy and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.appManagementPolicy"
        # The appliesTo property
        self._applies_to: Optional[List[directory_object.DirectoryObject]] = None
        # The isEnabled property
        self._is_enabled: Optional[bool] = None
        # The restrictions property
        self._restrictions: Optional[app_management_configuration.AppManagementConfiguration] = None
    
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
        fields = {
            "appliesTo": lambda n : setattr(self, 'applies_to', n.get_collection_of_object_values(directory_object.DirectoryObject)),
            "isEnabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
            "restrictions": lambda n : setattr(self, 'restrictions', n.get_object_value(app_management_configuration.AppManagementConfiguration)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_enabled(self,) -> Optional[bool]:
        """
        Gets the isEnabled property value. The isEnabled property
        Returns: Optional[bool]
        """
        return self._is_enabled
    
    @is_enabled.setter
    def is_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isEnabled property value. The isEnabled property
        Args:
            value: Value to set for the is_enabled property.
        """
        self._is_enabled = value
    
    @property
    def restrictions(self,) -> Optional[app_management_configuration.AppManagementConfiguration]:
        """
        Gets the restrictions property value. The restrictions property
        Returns: Optional[app_management_configuration.AppManagementConfiguration]
        """
        return self._restrictions
    
    @restrictions.setter
    def restrictions(self,value: Optional[app_management_configuration.AppManagementConfiguration] = None) -> None:
        """
        Sets the restrictions property value. The restrictions property
        Args:
            value: Value to set for the restrictions property.
        """
        self._restrictions = value
    
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
    

