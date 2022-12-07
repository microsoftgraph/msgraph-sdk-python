from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
printer_location = lazy_import('msgraph.generated.models.printer_location')

class PrintConnector(entity.Entity):
    """
    Provides operations to manage the collection of agreement entities.
    """
    @property
    def app_version(self,) -> Optional[str]:
        """
        Gets the appVersion property value. The connector's version.
        Returns: Optional[str]
        """
        return self._app_version
    
    @app_version.setter
    def app_version(self,value: Optional[str] = None) -> None:
        """
        Sets the appVersion property value. The connector's version.
        Args:
            value: Value to set for the appVersion property.
        """
        self._app_version = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new printConnector and sets the default values.
        """
        super().__init__()
        # The connector's version.
        self._app_version: Optional[str] = None
        # The name of the connector.
        self._display_name: Optional[str] = None
        # The connector machine's hostname.
        self._fully_qualified_domain_name: Optional[str] = None
        # The physical and/or organizational location of the connector.
        self._location: Optional[printer_location.PrinterLocation] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The connector machine's operating system version.
        self._operating_system: Optional[str] = None
        # The DateTimeOffset when the connector was registered.
        self._registered_date_time: Optional[datetime] = None
    
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
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The name of the connector.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The name of the connector.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def fully_qualified_domain_name(self,) -> Optional[str]:
        """
        Gets the fullyQualifiedDomainName property value. The connector machine's hostname.
        Returns: Optional[str]
        """
        return self._fully_qualified_domain_name
    
    @fully_qualified_domain_name.setter
    def fully_qualified_domain_name(self,value: Optional[str] = None) -> None:
        """
        Sets the fullyQualifiedDomainName property value. The connector machine's hostname.
        Args:
            value: Value to set for the fullyQualifiedDomainName property.
        """
        self._fully_qualified_domain_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "app_version": lambda n : setattr(self, 'app_version', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "fully_qualified_domain_name": lambda n : setattr(self, 'fully_qualified_domain_name', n.get_str_value()),
            "location": lambda n : setattr(self, 'location', n.get_object_value(printer_location.PrinterLocation)),
            "operating_system": lambda n : setattr(self, 'operating_system', n.get_str_value()),
            "registered_date_time": lambda n : setattr(self, 'registered_date_time', n.get_datetime_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def location(self,) -> Optional[printer_location.PrinterLocation]:
        """
        Gets the location property value. The physical and/or organizational location of the connector.
        Returns: Optional[printer_location.PrinterLocation]
        """
        return self._location
    
    @location.setter
    def location(self,value: Optional[printer_location.PrinterLocation] = None) -> None:
        """
        Sets the location property value. The physical and/or organizational location of the connector.
        Args:
            value: Value to set for the location property.
        """
        self._location = value
    
    @property
    def operating_system(self,) -> Optional[str]:
        """
        Gets the operatingSystem property value. The connector machine's operating system version.
        Returns: Optional[str]
        """
        return self._operating_system
    
    @operating_system.setter
    def operating_system(self,value: Optional[str] = None) -> None:
        """
        Sets the operatingSystem property value. The connector machine's operating system version.
        Args:
            value: Value to set for the operatingSystem property.
        """
        self._operating_system = value
    
    @property
    def registered_date_time(self,) -> Optional[datetime]:
        """
        Gets the registeredDateTime property value. The DateTimeOffset when the connector was registered.
        Returns: Optional[datetime]
        """
        return self._registered_date_time
    
    @registered_date_time.setter
    def registered_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the registeredDateTime property value. The DateTimeOffset when the connector was registered.
        Args:
            value: Value to set for the registeredDateTime property.
        """
        self._registered_date_time = value
    
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
    

