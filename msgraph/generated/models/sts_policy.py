from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

directory_object = lazy_import('msgraph.generated.models.directory_object')
policy_base = lazy_import('msgraph.generated.models.policy_base')

class StsPolicy(policy_base.PolicyBase):
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
            value: Value to set for the appliesTo property.
        """
        self._applies_to = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new StsPolicy and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.stsPolicy"
        # The appliesTo property
        self._applies_to: Optional[List[directory_object.DirectoryObject]] = None
        # A string collection containing a JSON string that defines the rules and settings for a policy. The syntax for the definition differs for each derived policy type. Required.
        self._definition: Optional[List[str]] = None
        # If set to true, activates this policy. There can be many policies for the same policy type, but only one can be activated as the organization default. Optional, default value is false.
        self._is_organization_default: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> StsPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: StsPolicy
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return StsPolicy()
    
    @property
    def definition(self,) -> Optional[List[str]]:
        """
        Gets the definition property value. A string collection containing a JSON string that defines the rules and settings for a policy. The syntax for the definition differs for each derived policy type. Required.
        Returns: Optional[List[str]]
        """
        return self._definition
    
    @definition.setter
    def definition(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the definition property value. A string collection containing a JSON string that defines the rules and settings for a policy. The syntax for the definition differs for each derived policy type. Required.
        Args:
            value: Value to set for the definition property.
        """
        self._definition = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "applies_to": lambda n : setattr(self, 'applies_to', n.get_collection_of_object_values(directory_object.DirectoryObject)),
            "definition": lambda n : setattr(self, 'definition', n.get_collection_of_primitive_values(str)),
            "is_organization_default": lambda n : setattr(self, 'is_organization_default', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_organization_default(self,) -> Optional[bool]:
        """
        Gets the isOrganizationDefault property value. If set to true, activates this policy. There can be many policies for the same policy type, but only one can be activated as the organization default. Optional, default value is false.
        Returns: Optional[bool]
        """
        return self._is_organization_default
    
    @is_organization_default.setter
    def is_organization_default(self,value: Optional[bool] = None) -> None:
        """
        Sets the isOrganizationDefault property value. If set to true, activates this policy. There can be many policies for the same policy type, but only one can be activated as the organization default. Optional, default value is false.
        Args:
            value: Value to set for the isOrganizationDefault property.
        """
        self._is_organization_default = value
    
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
        writer.write_collection_of_primitive_values("definition", self.definition)
        writer.write_bool_value("isOrganizationDefault", self.is_organization_default)
    

