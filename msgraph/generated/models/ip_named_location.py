from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

ip_range = lazy_import('msgraph.generated.models.ip_range')
named_location = lazy_import('msgraph.generated.models.named_location')

class IpNamedLocation(named_location.NamedLocation):
    def __init__(self,) -> None:
        """
        Instantiates a new IpNamedLocation and sets the default values.
        """
        super().__init__()
        # List of IP address ranges in IPv4 CIDR format (e.g. 1.2.3.4/32) or any allowable IPv6 format from IETF RFC596. Required.
        self._ip_ranges: Optional[List[ip_range.IpRange]] = None
        # true if this location is explicitly trusted. Optional. Default value is false.
        self._is_trusted: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IpNamedLocation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IpNamedLocation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IpNamedLocation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "ip_ranges": lambda n : setattr(self, 'ip_ranges', n.get_collection_of_object_values(ip_range.IpRange)),
            "is_trusted": lambda n : setattr(self, 'is_trusted', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def ip_ranges(self,) -> Optional[List[ip_range.IpRange]]:
        """
        Gets the ipRanges property value. List of IP address ranges in IPv4 CIDR format (e.g. 1.2.3.4/32) or any allowable IPv6 format from IETF RFC596. Required.
        Returns: Optional[List[ip_range.IpRange]]
        """
        return self._ip_ranges
    
    @ip_ranges.setter
    def ip_ranges(self,value: Optional[List[ip_range.IpRange]] = None) -> None:
        """
        Sets the ipRanges property value. List of IP address ranges in IPv4 CIDR format (e.g. 1.2.3.4/32) or any allowable IPv6 format from IETF RFC596. Required.
        Args:
            value: Value to set for the ipRanges property.
        """
        self._ip_ranges = value
    
    @property
    def is_trusted(self,) -> Optional[bool]:
        """
        Gets the isTrusted property value. true if this location is explicitly trusted. Optional. Default value is false.
        Returns: Optional[bool]
        """
        return self._is_trusted
    
    @is_trusted.setter
    def is_trusted(self,value: Optional[bool] = None) -> None:
        """
        Sets the isTrusted property value. true if this location is explicitly trusted. Optional. Default value is false.
        Args:
            value: Value to set for the isTrusted property.
        """
        self._is_trusted = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("ipRanges", self.ip_ranges)
        writer.write_bool_value("isTrusted", self.is_trusted)
    

