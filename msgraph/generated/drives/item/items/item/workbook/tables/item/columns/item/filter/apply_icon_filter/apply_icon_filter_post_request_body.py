from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ............models import workbook_icon

class ApplyIconFilterPostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new applyIconFilterPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The icon property
        self._icon: Optional[workbook_icon.WorkbookIcon] = None
    
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
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ApplyIconFilterPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ApplyIconFilterPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ApplyIconFilterPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ............models import workbook_icon

        fields: Dict[str, Callable[[Any], None]] = {
            "icon": lambda n : setattr(self, 'icon', n.get_object_value(workbook_icon.WorkbookIcon)),
        }
        return fields
    
    @property
    def icon(self,) -> Optional[workbook_icon.WorkbookIcon]:
        """
        Gets the icon property value. The icon property
        Returns: Optional[workbook_icon.WorkbookIcon]
        """
        return self._icon
    
    @icon.setter
    def icon(self,value: Optional[workbook_icon.WorkbookIcon] = None) -> None:
        """
        Sets the icon property value. The icon property
        Args:
            value: Value to set for the icon property.
        """
        self._icon = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("icon", self.icon)
        writer.write_additional_data_value(self.additional_data)
    

