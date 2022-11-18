from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, Union

from . import entity, json, workbook_chart_point_format

class WorkbookChartPoint(entity.Entity):
    """
    Provides operations to manage the collection of agreementAcceptance entities.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new workbookChartPoint and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.workbookChartPoint"
        # Encapsulates the format properties chart point. Read-only.
        self._format: Optional[workbook_chart_point_format.WorkbookChartPointFormat] = None
        # Returns the value of a chart point. Read-only.
        self._value: Optional[json.Json] = None

    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WorkbookChartPoint:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookChartPoint
        """
        if not parse_node:
            raise Exception("parse_node cannot be undefined")
        return WorkbookChartPoint()

    @property
    def format(self,) -> Optional[workbook_chart_point_format.WorkbookChartPointFormat]:
        """
        Gets the format property value. Encapsulates the format properties chart point. Read-only.
        Returns: Optional[workbook_chart_point_format.WorkbookChartPointFormat]
        """
        return self._format

    @format.setter
    def format(self,value: Optional[workbook_chart_point_format.WorkbookChartPointFormat] = None) -> None:
        """
        Sets the format property value. Encapsulates the format properties chart point. Read-only.
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
            "format": lambda n : setattr(self, 'format', n.get_object_value(workbook_chart_point_format.WorkbookChartPointFormat)),
            "value": lambda n : setattr(self, 'value', n.get_object_value(json.Json)),
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
        if not writer:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("format", self.format)
        writer.write_object_value("value", self.value)

    @property
    def value(self,) -> Optional[json.Json]:
        """
        Gets the value property value. Returns the value of a chart point. Read-only.
        Returns: Optional[json.Json]
        """
        return self._value

    @value.setter
    def value(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the value property value. Returns the value of a chart point. Read-only.
        Args:
            value: Value to set for the value property.
        """
        self._value = value


