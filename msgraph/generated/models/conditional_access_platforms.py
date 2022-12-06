from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

conditional_access_device_platform = lazy_import('msgraph.generated.models.conditional_access_device_platform')

class ConditionalAccessPlatforms(AdditionalDataHolder, Parsable):
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new conditionalAccessPlatforms and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Possible values are: android, iOS, windows, windowsPhone, macOS, linux, all, unknownFutureValue.
        self._exclude_platforms: Optional[List[conditional_access_device_platform.ConditionalAccessDevicePlatform]] = None
        # Possible values are: android, iOS, windows, windowsPhone, macOS, linux, all, unknownFutureValue.
        self._include_platforms: Optional[List[conditional_access_device_platform.ConditionalAccessDevicePlatform]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ConditionalAccessPlatforms:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ConditionalAccessPlatforms
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ConditionalAccessPlatforms()
    
    @property
    def exclude_platforms(self,) -> Optional[List[conditional_access_device_platform.ConditionalAccessDevicePlatform]]:
        """
        Gets the excludePlatforms property value. Possible values are: android, iOS, windows, windowsPhone, macOS, linux, all, unknownFutureValue.
        Returns: Optional[List[conditional_access_device_platform.ConditionalAccessDevicePlatform]]
        """
        return self._exclude_platforms
    
    @exclude_platforms.setter
    def exclude_platforms(self,value: Optional[List[conditional_access_device_platform.ConditionalAccessDevicePlatform]] = None) -> None:
        """
        Sets the excludePlatforms property value. Possible values are: android, iOS, windows, windowsPhone, macOS, linux, all, unknownFutureValue.
        Args:
            value: Value to set for the excludePlatforms property.
        """
        self._exclude_platforms = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "exclude_platforms": lambda n : setattr(self, 'exclude_platforms', n.get_collection_of_enum_values(conditional_access_device_platform.ConditionalAccessDevicePlatform)),
            "include_platforms": lambda n : setattr(self, 'include_platforms', n.get_collection_of_enum_values(conditional_access_device_platform.ConditionalAccessDevicePlatform)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def include_platforms(self,) -> Optional[List[conditional_access_device_platform.ConditionalAccessDevicePlatform]]:
        """
        Gets the includePlatforms property value. Possible values are: android, iOS, windows, windowsPhone, macOS, linux, all, unknownFutureValue.
        Returns: Optional[List[conditional_access_device_platform.ConditionalAccessDevicePlatform]]
        """
        return self._include_platforms
    
    @include_platforms.setter
    def include_platforms(self,value: Optional[List[conditional_access_device_platform.ConditionalAccessDevicePlatform]] = None) -> None:
        """
        Sets the includePlatforms property value. Possible values are: android, iOS, windows, windowsPhone, macOS, linux, all, unknownFutureValue.
        Args:
            value: Value to set for the includePlatforms property.
        """
        self._include_platforms = value
    
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
        writer.write_enum_value("excludePlatforms", self.exclude_platforms)
        writer.write_enum_value("includePlatforms", self.include_platforms)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

