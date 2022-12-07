from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

workbook_icon = lazy_import('msgraph.generated.models.workbook_icon')

class WorkbookSortField(AdditionalDataHolder, Parsable):
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
    def ascending(self,) -> Optional[bool]:
        """
        Gets the ascending property value. Represents whether the sorting is done in an ascending fashion.
        Returns: Optional[bool]
        """
        return self._ascending
    
    @ascending.setter
    def ascending(self,value: Optional[bool] = None) -> None:
        """
        Sets the ascending property value. Represents whether the sorting is done in an ascending fashion.
        Args:
            value: Value to set for the ascending property.
        """
        self._ascending = value
    
    @property
    def color(self,) -> Optional[str]:
        """
        Gets the color property value. Represents the color that is the target of the condition if the sorting is on font or cell color.
        Returns: Optional[str]
        """
        return self._color
    
    @color.setter
    def color(self,value: Optional[str] = None) -> None:
        """
        Sets the color property value. Represents the color that is the target of the condition if the sorting is on font or cell color.
        Args:
            value: Value to set for the color property.
        """
        self._color = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new workbookSortField and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Represents whether the sorting is done in an ascending fashion.
        self._ascending: Optional[bool] = None
        # Represents the color that is the target of the condition if the sorting is on font or cell color.
        self._color: Optional[str] = None
        # Represents additional sorting options for this field. The possible values are: Normal, TextAsNumber.
        self._data_option: Optional[str] = None
        # Represents the icon that is the target of the condition if the sorting is on the cell's icon.
        self._icon: Optional[workbook_icon.WorkbookIcon] = None
        # Represents the column (or row, depending on the sort orientation) that the condition is on. Represented as an offset from the first column (or row).
        self._key: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Represents the type of sorting of this condition. The possible values are: Value, CellColor, FontColor, Icon.
        self._sort_on: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WorkbookSortField:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookSortField
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WorkbookSortField()
    
    @property
    def data_option(self,) -> Optional[str]:
        """
        Gets the dataOption property value. Represents additional sorting options for this field. The possible values are: Normal, TextAsNumber.
        Returns: Optional[str]
        """
        return self._data_option
    
    @data_option.setter
    def data_option(self,value: Optional[str] = None) -> None:
        """
        Sets the dataOption property value. Represents additional sorting options for this field. The possible values are: Normal, TextAsNumber.
        Args:
            value: Value to set for the dataOption property.
        """
        self._data_option = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "ascending": lambda n : setattr(self, 'ascending', n.get_bool_value()),
            "color": lambda n : setattr(self, 'color', n.get_str_value()),
            "data_option": lambda n : setattr(self, 'data_option', n.get_str_value()),
            "icon": lambda n : setattr(self, 'icon', n.get_object_value(workbook_icon.WorkbookIcon)),
            "key": lambda n : setattr(self, 'key', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "sort_on": lambda n : setattr(self, 'sort_on', n.get_str_value()),
        }
        return fields
    
    @property
    def icon(self,) -> Optional[workbook_icon.WorkbookIcon]:
        """
        Gets the icon property value. Represents the icon that is the target of the condition if the sorting is on the cell's icon.
        Returns: Optional[workbook_icon.WorkbookIcon]
        """
        return self._icon
    
    @icon.setter
    def icon(self,value: Optional[workbook_icon.WorkbookIcon] = None) -> None:
        """
        Sets the icon property value. Represents the icon that is the target of the condition if the sorting is on the cell's icon.
        Args:
            value: Value to set for the icon property.
        """
        self._icon = value
    
    @property
    def key(self,) -> Optional[int]:
        """
        Gets the key property value. Represents the column (or row, depending on the sort orientation) that the condition is on. Represented as an offset from the first column (or row).
        Returns: Optional[int]
        """
        return self._key
    
    @key.setter
    def key(self,value: Optional[int] = None) -> None:
        """
        Sets the key property value. Represents the column (or row, depending on the sort orientation) that the condition is on. Represented as an offset from the first column (or row).
        Args:
            value: Value to set for the key property.
        """
        self._key = value
    
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
        writer.write_bool_value("ascending", self.ascending)
        writer.write_str_value("color", self.color)
        writer.write_str_value("dataOption", self.data_option)
        writer.write_object_value("icon", self.icon)
        writer.write_int_value("key", self.key)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("sortOn", self.sort_on)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def sort_on(self,) -> Optional[str]:
        """
        Gets the sortOn property value. Represents the type of sorting of this condition. The possible values are: Value, CellColor, FontColor, Icon.
        Returns: Optional[str]
        """
        return self._sort_on
    
    @sort_on.setter
    def sort_on(self,value: Optional[str] = None) -> None:
        """
        Sets the sortOn property value. Represents the type of sorting of this condition. The possible values are: Value, CellColor, FontColor, Icon.
        Args:
            value: Value to set for the sortOn property.
        """
        self._sort_on = value
    

