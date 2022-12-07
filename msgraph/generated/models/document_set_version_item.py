from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class DocumentSetVersionItem(AdditionalDataHolder, Parsable):
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
        Instantiates a new documentSetVersionItem and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The unique identifier for the item.
        self._item_id: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The title of the item.
        self._title: Optional[str] = None
        # The version ID of the item.
        self._version_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DocumentSetVersionItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DocumentSetVersionItem
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DocumentSetVersionItem()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "item_id": lambda n : setattr(self, 'item_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
            "version_id": lambda n : setattr(self, 'version_id', n.get_str_value()),
        }
        return fields
    
    @property
    def item_id(self,) -> Optional[str]:
        """
        Gets the itemId property value. The unique identifier for the item.
        Returns: Optional[str]
        """
        return self._item_id
    
    @item_id.setter
    def item_id(self,value: Optional[str] = None) -> None:
        """
        Sets the itemId property value. The unique identifier for the item.
        Args:
            value: Value to set for the itemId property.
        """
        self._item_id = value
    
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
        writer.write_str_value("itemId", self.item_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("title", self.title)
        writer.write_str_value("versionId", self.version_id)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def title(self,) -> Optional[str]:
        """
        Gets the title property value. The title of the item.
        Returns: Optional[str]
        """
        return self._title
    
    @title.setter
    def title(self,value: Optional[str] = None) -> None:
        """
        Sets the title property value. The title of the item.
        Args:
            value: Value to set for the title property.
        """
        self._title = value
    
    @property
    def version_id(self,) -> Optional[str]:
        """
        Gets the versionId property value. The version ID of the item.
        Returns: Optional[str]
        """
        return self._version_id
    
    @version_id.setter
    def version_id(self,value: Optional[str] = None) -> None:
        """
        Sets the versionId property value. The version ID of the item.
        Args:
            value: Value to set for the versionId property.
        """
        self._version_id = value
    

