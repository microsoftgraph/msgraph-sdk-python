from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
workbook_chart_axis_title_format = lazy_import('msgraph.generated.models.workbook_chart_axis_title_format')

class WorkbookChartAxisTitle(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new workbookChartAxisTitle and sets the default values.
        """
        super().__init__()
        # Represents the formatting of chart axis title. Read-only.
        self._format: Optional[workbook_chart_axis_title_format.WorkbookChartAxisTitleFormat] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Represents the axis title.
        self._text: Optional[str] = None
        # A boolean that specifies the visibility of an axis title.
        self._visible: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WorkbookChartAxisTitle:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookChartAxisTitle
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WorkbookChartAxisTitle()
    
    @property
    def format(self,) -> Optional[workbook_chart_axis_title_format.WorkbookChartAxisTitleFormat]:
        """
        Gets the format property value. Represents the formatting of chart axis title. Read-only.
        Returns: Optional[workbook_chart_axis_title_format.WorkbookChartAxisTitleFormat]
        """
        return self._format
    
    @format.setter
    def format(self,value: Optional[workbook_chart_axis_title_format.WorkbookChartAxisTitleFormat] = None) -> None:
        """
        Sets the format property value. Represents the formatting of chart axis title. Read-only.
        Args:
            value: Value to set for the format property.
        """
        self._format = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "format": lambda n : setattr(self, 'format', n.get_object_value(workbook_chart_axis_title_format.WorkbookChartAxisTitleFormat)),
            "text": lambda n : setattr(self, 'text', n.get_str_value()),
            "visible": lambda n : setattr(self, 'visible', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("format", self.format)
        writer.write_str_value("text", self.text)
        writer.write_bool_value("visible", self.visible)
    
    @property
    def text(self,) -> Optional[str]:
        """
        Gets the text property value. Represents the axis title.
        Returns: Optional[str]
        """
        return self._text
    
    @text.setter
    def text(self,value: Optional[str] = None) -> None:
        """
        Sets the text property value. Represents the axis title.
        Args:
            value: Value to set for the text property.
        """
        self._text = value
    
    @property
    def visible(self,) -> Optional[bool]:
        """
        Gets the visible property value. A boolean that specifies the visibility of an axis title.
        Returns: Optional[bool]
        """
        return self._visible
    
    @visible.setter
    def visible(self,value: Optional[bool] = None) -> None:
        """
        Sets the visible property value. A boolean that specifies the visibility of an axis title.
        Args:
            value: Value to set for the visible property.
        """
        self._visible = value
    

