from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

domain_dns_record = lazy_import('msgraph.generated.models.domain_dns_record')

class DomainDnsTxtRecord(domain_dns_record.DomainDnsRecord):
    def __init__(self,) -> None:
        """
        Instantiates a new DomainDnsTxtRecord and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Value used when configuring the text property at the DNS host.
        self._text: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DomainDnsTxtRecord:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DomainDnsTxtRecord
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DomainDnsTxtRecord()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "text": lambda n : setattr(self, 'text', n.get_str_value()),
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
        writer.write_str_value("text", self.text)
    
    @property
    def text(self,) -> Optional[str]:
        """
        Gets the text property value. Value used when configuring the text property at the DNS host.
        Returns: Optional[str]
        """
        return self._text
    
    @text.setter
    def text(self,value: Optional[str] = None) -> None:
        """
        Sets the text property value. Value used when configuring the text property at the DNS host.
        Args:
            value: Value to set for the text property.
        """
        self._text = value
    

