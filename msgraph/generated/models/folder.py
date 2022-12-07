from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

folder_view = lazy_import('msgraph.generated.models.folder_view')

class Folder(AdditionalDataHolder, Parsable):
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
        Instantiates a new folder and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Number of children contained immediately within this container.
        self._child_count: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # A collection of properties defining the recommended view for the folder.
        self._view: Optional[folder_view.FolderView] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Folder:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Folder
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Folder()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "child_count": lambda n : setattr(self, 'child_count', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "view": lambda n : setattr(self, 'view', n.get_object_value(folder_view.FolderView)),
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
        writer.write_int_value("childCount", self.child_count)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("view", self.view)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def view(self,) -> Optional[folder_view.FolderView]:
        """
        Gets the view property value. A collection of properties defining the recommended view for the folder.
        Returns: Optional[folder_view.FolderView]
        """
        return self._view
    
    @view.setter
    def view(self,value: Optional[folder_view.FolderView] = None) -> None:
        """
        Sets the view property value. A collection of properties defining the recommended view for the folder.
        Args:
            value: Value to set for the view property.
        """
        self._view = value
    

