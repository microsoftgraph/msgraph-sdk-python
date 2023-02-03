from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
print_service_endpoint = lazy_import('msgraph.generated.models.print_service_endpoint')

class PrintService(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new PrintService and sets the default values.
        """
        super().__init__()
        # Endpoints that can be used to access the service. Read-only. Nullable.
        self._endpoints: Optional[List[print_service_endpoint.PrintServiceEndpoint]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PrintService:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PrintService
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PrintService()
    
    @property
    def endpoints(self,) -> Optional[List[print_service_endpoint.PrintServiceEndpoint]]:
        """
        Gets the endpoints property value. Endpoints that can be used to access the service. Read-only. Nullable.
        Returns: Optional[List[print_service_endpoint.PrintServiceEndpoint]]
        """
        return self._endpoints
    
    @endpoints.setter
    def endpoints(self,value: Optional[List[print_service_endpoint.PrintServiceEndpoint]] = None) -> None:
        """
        Sets the endpoints property value. Endpoints that can be used to access the service. Read-only. Nullable.
        Args:
            value: Value to set for the endpoints property.
        """
        self._endpoints = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "endpoints": lambda n : setattr(self, 'endpoints', n.get_collection_of_object_values(print_service_endpoint.PrintServiceEndpoint)),
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
        writer.write_collection_of_object_values("endpoints", self.endpoints)
    

