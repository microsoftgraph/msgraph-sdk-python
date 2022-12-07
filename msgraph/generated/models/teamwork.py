from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
workforce_integration = lazy_import('msgraph.generated.models.workforce_integration')

class Teamwork(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new Teamwork and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The workforceIntegrations property
        self._workforce_integrations: Optional[List[workforce_integration.WorkforceIntegration]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Teamwork:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Teamwork
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Teamwork()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "workforce_integrations": lambda n : setattr(self, 'workforce_integrations', n.get_collection_of_object_values(workforce_integration.WorkforceIntegration)),
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
        writer.write_collection_of_object_values("workforceIntegrations", self.workforce_integrations)
    
    @property
    def workforce_integrations(self,) -> Optional[List[workforce_integration.WorkforceIntegration]]:
        """
        Gets the workforceIntegrations property value. The workforceIntegrations property
        Returns: Optional[List[workforce_integration.WorkforceIntegration]]
        """
        return self._workforce_integrations
    
    @workforce_integrations.setter
    def workforce_integrations(self,value: Optional[List[workforce_integration.WorkforceIntegration]] = None) -> None:
        """
        Sets the workforceIntegrations property value. The workforceIntegrations property
        Args:
            value: Value to set for the workforceIntegrations property.
        """
        self._workforce_integrations = value
    

