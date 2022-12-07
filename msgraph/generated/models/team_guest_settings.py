from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class TeamGuestSettings(AdditionalDataHolder, Parsable):
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
    def allow_create_update_channels(self,) -> Optional[bool]:
        """
        Gets the allowCreateUpdateChannels property value. If set to true, guests can add and update channels.
        Returns: Optional[bool]
        """
        return self._allow_create_update_channels
    
    @allow_create_update_channels.setter
    def allow_create_update_channels(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowCreateUpdateChannels property value. If set to true, guests can add and update channels.
        Args:
            value: Value to set for the allowCreateUpdateChannels property.
        """
        self._allow_create_update_channels = value
    
    @property
    def allow_delete_channels(self,) -> Optional[bool]:
        """
        Gets the allowDeleteChannels property value. If set to true, guests can delete channels.
        Returns: Optional[bool]
        """
        return self._allow_delete_channels
    
    @allow_delete_channels.setter
    def allow_delete_channels(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowDeleteChannels property value. If set to true, guests can delete channels.
        Args:
            value: Value to set for the allowDeleteChannels property.
        """
        self._allow_delete_channels = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new teamGuestSettings and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # If set to true, guests can add and update channels.
        self._allow_create_update_channels: Optional[bool] = None
        # If set to true, guests can delete channels.
        self._allow_delete_channels: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamGuestSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamGuestSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TeamGuestSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "allow_create_update_channels": lambda n : setattr(self, 'allow_create_update_channels', n.get_bool_value()),
            "allow_delete_channels": lambda n : setattr(self, 'allow_delete_channels', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_bool_value("allowCreateUpdateChannels", self.allow_create_update_channels)
        writer.write_bool_value("allowDeleteChannels", self.allow_delete_channels)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

