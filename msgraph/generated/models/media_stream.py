from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

media_direction = lazy_import('msgraph.generated.models.media_direction')
modality = lazy_import('msgraph.generated.models.modality')

class MediaStream(AdditionalDataHolder, Parsable):
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
        Instantiates a new mediaStream and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The direction property
        self._direction: Optional[media_direction.MediaDirection] = None
        # The media stream label.
        self._label: Optional[str] = None
        # The mediaType property
        self._media_type: Optional[modality.Modality] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # If the media is muted by the server.
        self._server_muted: Optional[bool] = None
        # The source ID.
        self._source_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MediaStream:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MediaStream
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MediaStream()
    
    @property
    def direction(self,) -> Optional[media_direction.MediaDirection]:
        """
        Gets the direction property value. The direction property
        Returns: Optional[media_direction.MediaDirection]
        """
        return self._direction
    
    @direction.setter
    def direction(self,value: Optional[media_direction.MediaDirection] = None) -> None:
        """
        Sets the direction property value. The direction property
        Args:
            value: Value to set for the direction property.
        """
        self._direction = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "direction": lambda n : setattr(self, 'direction', n.get_enum_value(media_direction.MediaDirection)),
            "label": lambda n : setattr(self, 'label', n.get_str_value()),
            "media_type": lambda n : setattr(self, 'media_type', n.get_enum_value(modality.Modality)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "server_muted": lambda n : setattr(self, 'server_muted', n.get_bool_value()),
            "source_id": lambda n : setattr(self, 'source_id', n.get_str_value()),
        }
        return fields
    
    @property
    def label(self,) -> Optional[str]:
        """
        Gets the label property value. The media stream label.
        Returns: Optional[str]
        """
        return self._label
    
    @label.setter
    def label(self,value: Optional[str] = None) -> None:
        """
        Sets the label property value. The media stream label.
        Args:
            value: Value to set for the label property.
        """
        self._label = value
    
    @property
    def media_type(self,) -> Optional[modality.Modality]:
        """
        Gets the mediaType property value. The mediaType property
        Returns: Optional[modality.Modality]
        """
        return self._media_type
    
    @media_type.setter
    def media_type(self,value: Optional[modality.Modality] = None) -> None:
        """
        Sets the mediaType property value. The mediaType property
        Args:
            value: Value to set for the mediaType property.
        """
        self._media_type = value
    
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
        writer.write_enum_value("direction", self.direction)
        writer.write_str_value("label", self.label)
        writer.write_enum_value("mediaType", self.media_type)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("serverMuted", self.server_muted)
        writer.write_str_value("sourceId", self.source_id)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def server_muted(self,) -> Optional[bool]:
        """
        Gets the serverMuted property value. If the media is muted by the server.
        Returns: Optional[bool]
        """
        return self._server_muted
    
    @server_muted.setter
    def server_muted(self,value: Optional[bool] = None) -> None:
        """
        Sets the serverMuted property value. If the media is muted by the server.
        Args:
            value: Value to set for the serverMuted property.
        """
        self._server_muted = value
    
    @property
    def source_id(self,) -> Optional[str]:
        """
        Gets the sourceId property value. The source ID.
        Returns: Optional[str]
        """
        return self._source_id
    
    @source_id.setter
    def source_id(self,value: Optional[str] = None) -> None:
        """
        Sets the sourceId property value. The source ID.
        Args:
            value: Value to set for the sourceId property.
        """
        self._source_id = value
    

