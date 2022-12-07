from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class FolderView(AdditionalDataHolder, Parsable):
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
        Instantiates a new folderView and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # The method by which the folder should be sorted.
        self._sort_by: Optional[str] = None
        # If true, indicates that items should be sorted in descending order. Otherwise, items should be sorted ascending.
        self._sort_order: Optional[str] = None
        # The type of view that should be used to represent the folder.
        self._view_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> FolderView:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: FolderView
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return FolderView()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "sort_by": lambda n : setattr(self, 'sort_by', n.get_str_value()),
            "sort_order": lambda n : setattr(self, 'sort_order', n.get_str_value()),
            "view_type": lambda n : setattr(self, 'view_type', n.get_str_value()),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("sortBy", self.sort_by)
        writer.write_str_value("sortOrder", self.sort_order)
        writer.write_str_value("viewType", self.view_type)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def sort_by(self,) -> Optional[str]:
        """
        Gets the sortBy property value. The method by which the folder should be sorted.
        Returns: Optional[str]
        """
        return self._sort_by
    
    @sort_by.setter
    def sort_by(self,value: Optional[str] = None) -> None:
        """
        Sets the sortBy property value. The method by which the folder should be sorted.
        Args:
            value: Value to set for the sortBy property.
        """
        self._sort_by = value
    
    @property
    def sort_order(self,) -> Optional[str]:
        """
        Gets the sortOrder property value. If true, indicates that items should be sorted in descending order. Otherwise, items should be sorted ascending.
        Returns: Optional[str]
        """
        return self._sort_order
    
    @sort_order.setter
    def sort_order(self,value: Optional[str] = None) -> None:
        """
        Sets the sortOrder property value. If true, indicates that items should be sorted in descending order. Otherwise, items should be sorted ascending.
        Args:
            value: Value to set for the sortOrder property.
        """
        self._sort_order = value
    
    @property
    def view_type(self,) -> Optional[str]:
        """
        Gets the viewType property value. The type of view that should be used to represent the folder.
        Returns: Optional[str]
        """
        return self._view_type
    
    @view_type.setter
    def view_type(self,value: Optional[str] = None) -> None:
        """
        Sets the viewType property value. The type of view that should be used to represent the folder.
        Args:
            value: Value to set for the viewType property.
        """
        self._view_type = value
    

