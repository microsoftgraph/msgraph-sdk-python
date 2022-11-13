from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, Union

from . import domain_dns_record

class DomainDnsUnavailableRecord(domain_dns_record.DomainDnsRecord):
    def __init__(self,) -> None:
        """
        Instantiates a new DomainDnsUnavailableRecord and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.domainDnsUnavailableRecord"
        # Provides the reason why the DomainDnsUnavailableRecord entity is returned.
        self._description: Optional[str] = None

    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DomainDnsUnavailableRecord:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DomainDnsUnavailableRecord
        """
        if not parse_node:
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
        if not writer:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("description", self.description)


