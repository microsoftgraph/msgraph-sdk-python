from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

application_type = lazy_import('msgraph.generated.models.application_type')
entity = lazy_import('msgraph.generated.models.entity')

class WindowsInformationProtectionAppLearningSummary(entity.Entity):
    """
    Windows Information Protection AppLearning Summary entity.
    """
    @property
    def application_name(self,) -> Optional[str]:
        """
        Gets the applicationName property value. Application Name
        Returns: Optional[str]
        """
        return self._application_name
    
    @application_name.setter
    def application_name(self,value: Optional[str] = None) -> None:
        """
        Sets the applicationName property value. Application Name
        Args:
            value: Value to set for the applicationName property.
        """
        self._application_name = value
    
    @property
    def application_type(self,) -> Optional[application_type.ApplicationType]:
        """
        Gets the applicationType property value. Possible types of Application
        Returns: Optional[application_type.ApplicationType]
        """
        return self._application_type
    
    @application_type.setter
    def application_type(self,value: Optional[application_type.ApplicationType] = None) -> None:
        """
        Sets the applicationType property value. Possible types of Application
        Args:
            value: Value to set for the applicationType property.
        """
        self._application_type = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new windowsInformationProtectionAppLearningSummary and sets the default values.
        """
        super().__init__()
        # Application Name
        self._application_name: Optional[str] = None
        # Possible types of Application
        self._application_type: Optional[application_type.ApplicationType] = None
        # Device Count
        self._device_count: Optional[int] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsInformationProtectionAppLearningSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsInformationProtectionAppLearningSummary
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsInformationProtectionAppLearningSummary()
    
    @property
    def device_count(self,) -> Optional[int]:
        """
        Gets the deviceCount property value. Device Count
        Returns: Optional[int]
        """
        return self._device_count
    
    @device_count.setter
    def device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the deviceCount property value. Device Count
        Args:
            value: Value to set for the deviceCount property.
        """
        self._device_count = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "application_name": lambda n : setattr(self, 'application_name', n.get_str_value()),
            "application_type": lambda n : setattr(self, 'application_type', n.get_enum_value(application_type.ApplicationType)),
            "device_count": lambda n : setattr(self, 'device_count', n.get_int_value()),
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
        writer.write_str_value("applicationName", self.application_name)
        writer.write_enum_value("applicationType", self.application_type)
        writer.write_int_value("deviceCount", self.device_count)
    

