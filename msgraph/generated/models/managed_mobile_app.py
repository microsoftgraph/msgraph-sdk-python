from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, mobile_app_identifier

from . import entity

class ManagedMobileApp(entity.Entity):
    """
    The identifier for the deployment an app.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new managedMobileApp and sets the default values.
        """
        super().__init__()
        # The identifier for an app with it's operating system type.
        self._mobile_app_identifier: Optional[mobile_app_identifier.MobileAppIdentifier] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Version of the entity.
        self._version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ManagedMobileApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ManagedMobileApp
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ManagedMobileApp()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, mobile_app_identifier

        fields: Dict[str, Callable[[Any], None]] = {
            "mobileAppIdentifier": lambda n : setattr(self, 'mobile_app_identifier', n.get_object_value(mobile_app_identifier.MobileAppIdentifier)),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def mobile_app_identifier(self,) -> Optional[mobile_app_identifier.MobileAppIdentifier]:
        """
        Gets the mobileAppIdentifier property value. The identifier for an app with it's operating system type.
        Returns: Optional[mobile_app_identifier.MobileAppIdentifier]
        """
        return self._mobile_app_identifier
    
    @mobile_app_identifier.setter
    def mobile_app_identifier(self,value: Optional[mobile_app_identifier.MobileAppIdentifier] = None) -> None:
        """
        Sets the mobileAppIdentifier property value. The identifier for an app with it's operating system type.
        Args:
            value: Value to set for the mobile_app_identifier property.
        """
        self._mobile_app_identifier = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("mobileAppIdentifier", self.mobile_app_identifier)
        writer.write_str_value("version", self.version)
    
    @property
    def version(self,) -> Optional[str]:
        """
        Gets the version property value. Version of the entity.
        Returns: Optional[str]
        """
        return self._version
    
    @version.setter
    def version(self,value: Optional[str] = None) -> None:
        """
        Sets the version property value. Version of the entity.
        Args:
            value: Value to set for the version property.
        """
        self._version = value
    

