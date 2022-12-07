from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class MacOSLobChildApp(AdditionalDataHolder, Parsable):
    """
    Contains properties of a macOS .app in the package
    """
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def build_number(self,) -> Optional[str]:
        """
        Gets the buildNumber property value. The build number of the app.
        Returns: Optional[str]
        """
        return self._build_number
    
    @build_number.setter
    def build_number(self,value: Optional[str] = None) -> None:
        """
        Sets the buildNumber property value. The build number of the app.
        Args:
            value: Value to set for the buildNumber property.
        """
        self._build_number = value
    
    @property
    def bundle_id(self,) -> Optional[str]:
        """
        Gets the bundleId property value. The bundleId of the app.
        Returns: Optional[str]
        """
        return self._bundle_id
    
    @bundle_id.setter
    def bundle_id(self,value: Optional[str] = None) -> None:
        """
        Sets the bundleId property value. The bundleId of the app.
        Args:
            value: Value to set for the bundleId property.
        """
        self._bundle_id = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new macOSLobChildApp and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The build number of the app.
        self._build_number: Optional[str] = None
        # The bundleId of the app.
        self._bundle_id: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The version number of the app.
        self._version_number: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MacOSLobChildApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MacOSLobChildApp
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MacOSLobChildApp()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "build_number": lambda n : setattr(self, 'build_number', n.get_str_value()),
            "bundle_id": lambda n : setattr(self, 'bundle_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "version_number": lambda n : setattr(self, 'version_number', n.get_str_value()),
        }
        return fields
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("buildNumber", self.build_number)
        writer.write_str_value("bundleId", self.bundle_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("versionNumber", self.version_number)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def version_number(self,) -> Optional[str]:
        """
        Gets the versionNumber property value. The version number of the app.
        Returns: Optional[str]
        """
        return self._version_number
    
    @version_number.setter
    def version_number(self,value: Optional[str] = None) -> None:
        """
        Sets the versionNumber property value. The version number of the app.
        Args:
            value: Value to set for the versionNumber property.
        """
        self._version_number = value
    

