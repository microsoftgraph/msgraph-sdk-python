from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class ChannelIdentity(AdditionalDataHolder, Parsable):
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
    def channel_id(self,) -> Optional[str]:
        """
        Gets the channelId property value. The identity of the channel in which the message was posted.
        Returns: Optional[str]
        """
        return self._channel_id
    
    @channel_id.setter
    def channel_id(self,value: Optional[str] = None) -> None:
        """
        Sets the channelId property value. The identity of the channel in which the message was posted.
        Args:
            value: Value to set for the channelId property.
        """
        self._channel_id = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new channelIdentity and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The identity of the channel in which the message was posted.
        self._channel_id: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The identity of the team in which the message was posted.
        self._team_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ChannelIdentity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ChannelIdentity
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ChannelIdentity()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "channel_id": lambda n : setattr(self, 'channel_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "team_id": lambda n : setattr(self, 'team_id', n.get_str_value()),
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
        writer.write_str_value("channelId", self.channel_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("teamId", self.team_id)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def team_id(self,) -> Optional[str]:
        """
        Gets the teamId property value. The identity of the team in which the message was posted.
        Returns: Optional[str]
        """
        return self._team_id
    
    @team_id.setter
    def team_id(self,value: Optional[str] = None) -> None:
        """
        Sets the teamId property value. The identity of the team in which the message was posted.
        Args:
            value: Value to set for the teamId property.
        """
        self._team_id = value
    

