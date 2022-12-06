from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class PlannerBucketTaskBoardTaskFormat(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new plannerBucketTaskBoardTaskFormat and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Hint used to order tasks in the bucket view of the task board. For details about the supported format, see Using order hints in Planner.
        self._order_hint: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PlannerBucketTaskBoardTaskFormat:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PlannerBucketTaskBoardTaskFormat
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PlannerBucketTaskBoardTaskFormat()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "order_hint": lambda n : setattr(self, 'order_hint', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def order_hint(self,) -> Optional[str]:
        """
        Gets the orderHint property value. Hint used to order tasks in the bucket view of the task board. For details about the supported format, see Using order hints in Planner.
        Returns: Optional[str]
        """
        return self._order_hint
    
    @order_hint.setter
    def order_hint(self,value: Optional[str] = None) -> None:
        """
        Sets the orderHint property value. Hint used to order tasks in the bucket view of the task board. For details about the supported format, see Using order hints in Planner.
        Args:
            value: Value to set for the orderHint property.
        """
        self._order_hint = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("orderHint", self.order_hint)
    

