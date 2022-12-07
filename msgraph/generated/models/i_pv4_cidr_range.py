from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

ip_range = lazy_import('msgraph.generated.models.ip_range')

class IPv4CidrRange(ip_range.IpRange):
    @property
    def cidr_address(self,) -> Optional[str]:
        """
        Gets the cidrAddress property value. IPv4 address in CIDR notation. Not nullable.
        Returns: Optional[str]
        """
        return self._cidr_address
    
    @cidr_address.setter
    def cidr_address(self,value: Optional[str] = None) -> None:
        """
        Sets the cidrAddress property value. IPv4 address in CIDR notation. Not nullable.
        Args:
            value: Value to set for the cidrAddress property.
        """
        self._cidr_address = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new IPv4CidrRange and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.iPv4CidrRange"
        # IPv4 address in CIDR notation. Not nullable.
        self._cidr_address: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IPv4CidrRange:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IPv4CidrRange
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IPv4CidrRange()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "cidr_address": lambda n : setattr(self, 'cidr_address', n.get_str_value()),
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
        writer.write_str_value("cidrAddress", self.cidr_address)
    

