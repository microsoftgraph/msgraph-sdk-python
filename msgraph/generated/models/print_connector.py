from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .printer_location import PrinterLocation

from .entity import Entity

@dataclass
class PrintConnector(Entity, Parsable):
    # The connector's version.
    app_version: Optional[str] = None
    # The name of the connector.
    display_name: Optional[str] = None
    # The connector machine's hostname.
    fully_qualified_domain_name: Optional[str] = None
    # The physical and/or organizational location of the connector.
    location: Optional[PrinterLocation] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The connector machine's operating system version.
    operating_system: Optional[str] = None
    # The DateTimeOffset when the connector was registered.
    registered_date_time: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PrintConnector:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PrintConnector
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PrintConnector()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .printer_location import PrinterLocation

        from .entity import Entity
        from .printer_location import PrinterLocation

        fields: dict[str, Callable[[Any], None]] = {
            "appVersion": lambda n : setattr(self, 'app_version', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "fullyQualifiedDomainName": lambda n : setattr(self, 'fully_qualified_domain_name', n.get_str_value()),
            "location": lambda n : setattr(self, 'location', n.get_object_value(PrinterLocation)),
            "operatingSystem": lambda n : setattr(self, 'operating_system', n.get_str_value()),
            "registeredDateTime": lambda n : setattr(self, 'registered_date_time', n.get_datetime_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("appVersion", self.app_version)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("fullyQualifiedDomainName", self.fully_qualified_domain_name)
        writer.write_object_value("location", self.location)
        writer.write_str_value("operatingSystem", self.operating_system)
        writer.write_datetime_value("registeredDateTime", self.registered_date_time)
    

