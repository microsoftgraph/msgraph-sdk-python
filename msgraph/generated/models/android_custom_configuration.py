from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_configuration, oma_setting

from . import device_configuration

class AndroidCustomConfiguration(device_configuration.DeviceConfiguration):
    def __init__(self,) -> None:
        """
        Instantiates a new AndroidCustomConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.androidCustomConfiguration"
        # OMA settings. This collection can contain a maximum of 1000 elements.
        self._oma_settings: Optional[List[oma_setting.OmaSetting]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidCustomConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AndroidCustomConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AndroidCustomConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_configuration, oma_setting

        fields: Dict[str, Callable[[Any], None]] = {
            "omaSettings": lambda n : setattr(self, 'oma_settings', n.get_collection_of_object_values(oma_setting.OmaSetting)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def oma_settings(self,) -> Optional[List[oma_setting.OmaSetting]]:
        """
        Gets the omaSettings property value. OMA settings. This collection can contain a maximum of 1000 elements.
        Returns: Optional[List[oma_setting.OmaSetting]]
        """
        return self._oma_settings
    
    @oma_settings.setter
    def oma_settings(self,value: Optional[List[oma_setting.OmaSetting]] = None) -> None:
        """
        Sets the omaSettings property value. OMA settings. This collection can contain a maximum of 1000 elements.
        Args:
            value: Value to set for the oma_settings property.
        """
        self._oma_settings = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("omaSettings", self.oma_settings)
    

