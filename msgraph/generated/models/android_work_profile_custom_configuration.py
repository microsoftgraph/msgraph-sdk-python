from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_configuration = lazy_import('msgraph.generated.models.device_configuration')
oma_setting = lazy_import('msgraph.generated.models.oma_setting')

class AndroidWorkProfileCustomConfiguration(device_configuration.DeviceConfiguration):
    def __init__(self,) -> None:
        """
        Instantiates a new AndroidWorkProfileCustomConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.androidWorkProfileCustomConfiguration"
        # OMA settings. This collection can contain a maximum of 500 elements.
        self._oma_settings: Optional[List[oma_setting.OmaSetting]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidWorkProfileCustomConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AndroidWorkProfileCustomConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AndroidWorkProfileCustomConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "oma_settings": lambda n : setattr(self, 'oma_settings', n.get_collection_of_object_values(oma_setting.OmaSetting)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def oma_settings(self,) -> Optional[List[oma_setting.OmaSetting]]:
        """
        Gets the omaSettings property value. OMA settings. This collection can contain a maximum of 500 elements.
        Returns: Optional[List[oma_setting.OmaSetting]]
        """
        return self._oma_settings
    
    @oma_settings.setter
    def oma_settings(self,value: Optional[List[oma_setting.OmaSetting]] = None) -> None:
        """
        Sets the omaSettings property value. OMA settings. This collection can contain a maximum of 500 elements.
        Args:
            value: Value to set for the omaSettings property.
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
    

