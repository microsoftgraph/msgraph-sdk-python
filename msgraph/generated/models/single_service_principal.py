from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

subject_set = lazy_import('msgraph.generated.models.subject_set')

class SingleServicePrincipal(subject_set.SubjectSet):
    def __init__(self,) -> None:
        """
        Instantiates a new SingleServicePrincipal and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.singleServicePrincipal"
        # Description of this service principal.
        self._description: Optional[str] = None
        # ID of the servicePrincipal.
        self._service_principal_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SingleServicePrincipal:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SingleServicePrincipal
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SingleServicePrincipal()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Description of this service principal.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Description of this service principal.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "service_principal_id": lambda n : setattr(self, 'service_principal_id', n.get_str_value()),
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
        writer.write_str_value("description", self.description)
        writer.write_str_value("servicePrincipalId", self.service_principal_id)
    
    @property
    def service_principal_id(self,) -> Optional[str]:
        """
        Gets the servicePrincipalId property value. ID of the servicePrincipal.
        Returns: Optional[str]
        """
        return self._service_principal_id
    
    @service_principal_id.setter
    def service_principal_id(self,value: Optional[str] = None) -> None:
        """
        Sets the servicePrincipalId property value. ID of the servicePrincipal.
        Args:
            value: Value to set for the servicePrincipalId property.
        """
        self._service_principal_id = value
    

