from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
workbook_chart_title_format = lazy_import('msgraph.generated.models.workbook_chart_title_format')

class WorkbookChartTitle(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new workbookChartTitle and sets the default values.
        """
        super().__init__()
        # Represents the formatting of a chart title, which includes fill and font formatting. Read-only.
        self._format: Optional[workbook_chart_title_format.WorkbookChartTitleFormat] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Boolean value representing if the chart title will overlay the chart or not.
        self._overlay: Optional[bool] = None
        # Represents the title text of a chart.
        self._text: Optional[str] = None
        # A boolean value the represents the visibility of a chart title object.
        self._visible: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WorkbookChartTitle:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookChartTitle
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WorkbookChartTitle()
    
    @property
    def format(self,) -> Optional[workbook_chart_title_format.WorkbookChartTitleFormat]:
        """
        Gets the format property value. Represents the formatting of a chart title, which includes fill and font formatting. Read-only.
        Returns: Optional[workbook_chart_title_format.WorkbookChartTitleFormat]
        """
        return self._format
    
    @format.setter
    def format(self,value: Optional[workbook_chart_title_format.WorkbookChartTitleFormat] = None) -> None:
        """
        Sets the format property value. Represents the formatting of a chart title, which includes fill and font formatting. Read-only.
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
            "format": lambda n : setattr(self, 'format', n.get_object_value(workbook_chart_title_format.WorkbookChartTitleFormat)),
            "overlay": lambda n : setattr(self, 'overlay', n.get_bool_value()),
            "text": lambda n : setattr(self, 'text', n.get_str_value()),
            "visible": lambda n : setattr(self, 'visible', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def overlay(self,) -> Optional[bool]:
        """
        Gets the overlay property value. Boolean value representing if the chart title will overlay the chart or not.
        Returns: Optional[bool]
        """
        return self._overlay
    
    @overlay.setter
    def overlay(self,value: Optional[bool] = None) -> None:
        """
        Sets the overlay property value. Boolean value representing if the chart title will overlay the chart or not.
        Args:
            value: Value to set for the overlay property.
        """
        self._overlay = value
    
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
        writer.write_bool_value("overlay", self.overlay)
        writer.write_str_value("text", self.text)
        writer.write_bool_value("visible", self.visible)
    
    @property
    def text(self,) -> Optional[str]:
        """
        Gets the text property value. Represents the title text of a chart.
        Returns: Optional[str]
        """
        return self._text
    
    @text.setter
    def text(self,value: Optional[str] = None) -> None:
        """
        Sets the text property value. Represents the title text of a chart.
        Args:
            value: Value to set for the text property.
        """
        self._text = value
    
    @property
    def visible(self,) -> Optional[bool]:
        """
        Gets the visible property value. A boolean value the represents the visibility of a chart title object.
        Returns: Optional[bool]
        """
        return self._visible
    
    @visible.setter
    def visible(self,value: Optional[bool] = None) -> None:
        """
        Sets the visible property value. A boolean value the represents the visibility of a chart title object.
        Args:
            value: Value to set for the visible property.
        """
        self._visible = value
    

