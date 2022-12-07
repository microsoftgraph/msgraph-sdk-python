from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class WorkbookRangeBorder(entity.Entity):
    """
    Provides operations to manage the collection of agreement entities.
    """
    @property
    def color(self,) -> Optional[str]:
        """
        Gets the color property value. HTML color code representing the color of the border line, of the form #RRGGBB (e.g. 'FFA500') or as a named HTML color (e.g. 'orange').
        Returns: Optional[str]
        """
        return self._color
    
    @color.setter
    def color(self,value: Optional[str] = None) -> None:
        """
        Sets the color property value. HTML color code representing the color of the border line, of the form #RRGGBB (e.g. 'FFA500') or as a named HTML color (e.g. 'orange').
        Args:
            value: Value to set for the color property.
        """
        self._color = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new workbookRangeBorder and sets the default values.
        """
        super().__init__()
        # HTML color code representing the color of the border line, of the form #RRGGBB (e.g. 'FFA500') or as a named HTML color (e.g. 'orange').
        self._color: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Constant value that indicates the specific side of the border. The possible values are: EdgeTop, EdgeBottom, EdgeLeft, EdgeRight, InsideVertical, InsideHorizontal, DiagonalDown, DiagonalUp. Read-only.
        self._side_index: Optional[str] = None
        # One of the constants of line style specifying the line style for the border. The possible values are: None, Continuous, Dash, DashDot, DashDotDot, Dot, Double, SlantDashDot.
        self._style: Optional[str] = None
        # Specifies the weight of the border around a range. The possible values are: Hairline, Thin, Medium, Thick.
        self._weight: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WorkbookRangeBorder:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookRangeBorder
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WorkbookRangeBorder()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "color": lambda n : setattr(self, 'color', n.get_str_value()),
            "side_index": lambda n : setattr(self, 'side_index', n.get_str_value()),
            "style": lambda n : setattr(self, 'style', n.get_str_value()),
            "weight": lambda n : setattr(self, 'weight', n.get_str_value()),
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
        writer.write_str_value("color", self.color)
        writer.write_str_value("sideIndex", self.side_index)
        writer.write_str_value("style", self.style)
        writer.write_str_value("weight", self.weight)
    
    @property
    def side_index(self,) -> Optional[str]:
        """
        Gets the sideIndex property value. Constant value that indicates the specific side of the border. The possible values are: EdgeTop, EdgeBottom, EdgeLeft, EdgeRight, InsideVertical, InsideHorizontal, DiagonalDown, DiagonalUp. Read-only.
        Returns: Optional[str]
        """
        return self._side_index
    
    @side_index.setter
    def side_index(self,value: Optional[str] = None) -> None:
        """
        Sets the sideIndex property value. Constant value that indicates the specific side of the border. The possible values are: EdgeTop, EdgeBottom, EdgeLeft, EdgeRight, InsideVertical, InsideHorizontal, DiagonalDown, DiagonalUp. Read-only.
        Args:
            value: Value to set for the sideIndex property.
        """
        self._side_index = value
    
    @property
    def style(self,) -> Optional[str]:
        """
        Gets the style property value. One of the constants of line style specifying the line style for the border. The possible values are: None, Continuous, Dash, DashDot, DashDotDot, Dot, Double, SlantDashDot.
        Returns: Optional[str]
        """
        return self._style
    
    @style.setter
    def style(self,value: Optional[str] = None) -> None:
        """
        Sets the style property value. One of the constants of line style specifying the line style for the border. The possible values are: None, Continuous, Dash, DashDot, DashDotDot, Dot, Double, SlantDashDot.
        Args:
            value: Value to set for the style property.
        """
        self._style = value
    
    @property
    def weight(self,) -> Optional[str]:
        """
        Gets the weight property value. Specifies the weight of the border around a range. The possible values are: Hairline, Thin, Medium, Thick.
        Returns: Optional[str]
        """
        return self._weight
    
    @weight.setter
    def weight(self,value: Optional[str] = None) -> None:
        """
        Sets the weight property value. Specifies the weight of the border around a range. The possible values are: Hairline, Thin, Medium, Thick.
        Args:
            value: Value to set for the weight property.
        """
        self._weight = value
    

