from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

domain_dns_record = lazy_import('msgraph.generated.models.domain_dns_record')

class DomainDnsUnavailableRecord(domain_dns_record.DomainDnsRecord):
    def __init__(self,) -> None:
        """
        Instantiates a new DomainDnsUnavailableRecord and sets the default values.
        """
        super().__init__()
        # Provides the reason why the DomainDnsUnavailableRecord entity is returned.
        self._description: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DomainDnsUnavailableRecord:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DomainDnsUnavailableRecord
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DomainDnsUnavailableRecord()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Provides the reason why the DomainDnsUnavailableRecord entity is returned.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Provides the reason why the DomainDnsUnavailableRecord entity is returned.
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
    

