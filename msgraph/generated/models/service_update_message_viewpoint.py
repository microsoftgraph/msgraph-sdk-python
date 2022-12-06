from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class ServiceUpdateMessageViewpoint(AdditionalDataHolder, Parsable):
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
        Instantiates a new serviceUpdateMessageViewpoint and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Indicates whether the user archived the message.
        self._is_archived: Optional[bool] = None
        # Indicates whether the user marked the message as favorite.
        self._is_favorited: Optional[bool] = None
        # Indicates whether the user read the message.
        self._is_read: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ServiceUpdateMessageViewpoint:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ServiceUpdateMessageViewpoint
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ServiceUpdateMessageViewpoint()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "is_archived": lambda n : setattr(self, 'is_archived', n.get_bool_value()),
            "is_favorited": lambda n : setattr(self, 'is_favorited', n.get_bool_value()),
            "is_read": lambda n : setattr(self, 'is_read', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def is_archived(self,) -> Optional[bool]:
        """
        Gets the isArchived property value. Indicates whether the user archived the message.
        Returns: Optional[bool]
        """
        return self._is_archived
    
    @is_archived.setter
    def is_archived(self,value: Optional[bool] = None) -> None:
        """
        Sets the isArchived property value. Indicates whether the user archived the message.
        Args:
            value: Value to set for the isArchived property.
        """
        self._is_archived = value
    
    @property
    def is_favorited(self,) -> Optional[bool]:
        """
        Gets the isFavorited property value. Indicates whether the user marked the message as favorite.
        Returns: Optional[bool]
        """
        return self._is_favorited
    
    @is_favorited.setter
    def is_favorited(self,value: Optional[bool] = None) -> None:
        """
        Sets the isFavorited property value. Indicates whether the user marked the message as favorite.
        Args:
            value: Value to set for the isFavorited property.
        """
        self._is_favorited = value
    
    @property
    def is_read(self,) -> Optional[bool]:
        """
        Gets the isRead property value. Indicates whether the user read the message.
        Returns: Optional[bool]
        """
        return self._is_read
    
    @is_read.setter
    def is_read(self,value: Optional[bool] = None) -> None:
        """
        Sets the isRead property value. Indicates whether the user read the message.
        Args:
            value: Value to set for the isRead property.
        """
        self._is_read = value
    
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
        writer.write_bool_value("isArchived", self.is_archived)
        writer.write_bool_value("isFavorited", self.is_favorited)
        writer.write_bool_value("isRead", self.is_read)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

