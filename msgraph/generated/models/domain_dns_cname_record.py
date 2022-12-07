from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

domain_dns_record = lazy_import('msgraph.generated.models.domain_dns_record')

class DomainDnsCnameRecord(domain_dns_record.DomainDnsRecord):
    @property
    def canonical_name(self,) -> Optional[str]:
        """
        Gets the canonicalName property value. The canonical name of the CNAME record. Used to configure the CNAME record at the DNS host.
        Returns: Optional[str]
        """
        return self._canonical_name
    
    @canonical_name.setter
    def canonical_name(self,value: Optional[str] = None) -> None:
        """
        Sets the canonicalName property value. The canonical name of the CNAME record. Used to configure the CNAME record at the DNS host.
        Args:
            value: Value to set for the canonicalName property.
        """
        self._canonical_name = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new DomainDnsCnameRecord and sets the default values.
        """
        super().__init__()
        # The canonical name of the CNAME record. Used to configure the CNAME record at the DNS host.
        self._canonical_name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DomainDnsCnameRecord:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DomainDnsCnameRecord
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DomainDnsCnameRecord()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "canonical_name": lambda n : setattr(self, 'canonical_name', n.get_str_value()),
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
        writer.write_str_value("canonicalName", self.canonical_name)
    

