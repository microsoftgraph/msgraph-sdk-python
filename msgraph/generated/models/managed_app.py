from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

managed_app_availability = lazy_import('msgraph.generated.models.managed_app_availability')
mobile_app = lazy_import('msgraph.generated.models.mobile_app')

class ManagedApp(mobile_app.MobileApp):
    @property
    def app_availability(self,) -> Optional[managed_app_availability.ManagedAppAvailability]:
        """
        Gets the appAvailability property value. A managed (MAM) application's availability.
        Returns: Optional[managed_app_availability.ManagedAppAvailability]
        """
        return self._app_availability
    
    @app_availability.setter
    def app_availability(self,value: Optional[managed_app_availability.ManagedAppAvailability] = None) -> None:
        """
        Sets the appAvailability property value. A managed (MAM) application's availability.
        Args:
            value: Value to set for the appAvailability property.
        """
        self._app_availability = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new ManagedApp and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.managedApp"
        # A managed (MAM) application's availability.
        self._app_availability: Optional[managed_app_availability.ManagedAppAvailability] = None
        # The Application's version.
        self._version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ManagedApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ManagedApp
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ManagedApp()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "app_availability": lambda n : setattr(self, 'app_availability', n.get_enum_value(managed_app_availability.ManagedAppAvailability)),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
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
        writer.write_enum_value("appAvailability", self.app_availability)
        writer.write_str_value("version", self.version)
    
    @property
    def version(self,) -> Optional[str]:
        """
        Gets the version property value. The Application's version.
        Returns: Optional[str]
        """
        return self._version
    
    @version.setter
    def version(self,value: Optional[str] = None) -> None:
        """
        Sets the version property value. The Application's version.
        Args:
            value: Value to set for the version property.
        """
        self._version = value
    

