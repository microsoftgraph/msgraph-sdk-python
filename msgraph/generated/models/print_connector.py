from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, printer_location

from . import entity

@dataclass
class PrintConnector(entity.Entity):
    # The connector's version.
    app_version: Optional[str] = None
    # The name of the connector.
    display_name: Optional[str] = None
    # The connector machine's hostname.
    fully_qualified_domain_name: Optional[str] = None
    # The physical and/or organizational location of the connector.
    location: Optional[printer_location.PrinterLocation] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The connector machine's operating system version.
    operating_system: Optional[str] = None
    # The DateTimeOffset when the connector was registered.
    registered_date_time: Optional[datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PrintConnector:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PrintConnector
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PrintConnector()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, printer_location

        fields: Dict[str, Callable[[Any], None]] = {
            "appVersion": lambda n : setattr(self, 'app_version', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "fullyQualifiedDomainName": lambda n : setattr(self, 'fully_qualified_domain_name', n.get_str_value()),
            "location": lambda n : setattr(self, 'location', n.get_object_value(printer_location.PrinterLocation)),
            "operatingSystem": lambda n : setattr(self, 'operating_system', n.get_str_value()),
            "registeredDateTime": lambda n : setattr(self, 'registered_date_time', n.get_datetime_value()),
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
        writer.write_str_value("appVersion", self.app_version)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("fullyQualifiedDomainName", self.fully_qualified_domain_name)
        writer.write_object_value("location", self.location)
        writer.write_str_value("operatingSystem", self.operating_system)
        writer.write_datetime_value("registeredDateTime", self.registered_date_time)
    

