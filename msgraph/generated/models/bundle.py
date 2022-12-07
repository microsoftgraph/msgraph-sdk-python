from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

album = lazy_import('msgraph.generated.models.album')

class Bundle(AdditionalDataHolder, Parsable):
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
    def album(self,) -> Optional[album.Album]:
        """
        Gets the album property value. If the bundle is an [album][], then the album property is included
        Returns: Optional[album.Album]
        """
        return self._album
    
    @album.setter
    def album(self,value: Optional[album.Album] = None) -> None:
        """
        Sets the album property value. If the bundle is an [album][], then the album property is included
        Args:
            value: Value to set for the album property.
        """
        self._album = value
    
    @property
    def child_count(self,) -> Optional[int]:
        """
        Gets the childCount property value. Number of children contained immediately within this container.
        Returns: Optional[int]
        """
        return self._child_count
    
    @child_count.setter
    def child_count(self,value: Optional[int] = None) -> None:
        """
        Sets the childCount property value. Number of children contained immediately within this container.
        Args:
            value: Value to set for the childCount property.
        """
        self._child_count = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new bundle and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # If the bundle is an [album][], then the album property is included
        self._album: Optional[album.Album] = None
        # Number of children contained immediately within this container.
        self._child_count: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Bundle:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Bundle
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Bundle()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "album": lambda n : setattr(self, 'album', n.get_object_value(album.Album)),
            "child_count": lambda n : setattr(self, 'child_count', n.get_int_value()),
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
        writer.write_object_value("album", self.album)
        writer.write_int_value("childCount", self.child_count)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

