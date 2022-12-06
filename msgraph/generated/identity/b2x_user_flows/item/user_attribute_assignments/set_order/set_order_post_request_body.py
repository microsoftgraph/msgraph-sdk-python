from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

assignment_order = lazy_import('msgraph.generated.models.assignment_order')

class SetOrderPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the setOrder method.
    """
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
        Instantiates a new setOrderPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The newAssignmentOrder property
        self._new_assignment_order: Optional[assignment_order.AssignmentOrder] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SetOrderPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SetOrderPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SetOrderPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "new_assignment_order": lambda n : setattr(self, 'new_assignment_order', n.get_object_value(assignment_order.AssignmentOrder)),
        }
        return fields
    
    @property
    def new_assignment_order(self,) -> Optional[assignment_order.AssignmentOrder]:
        """
        Gets the newAssignmentOrder property value. The newAssignmentOrder property
        Returns: Optional[assignment_order.AssignmentOrder]
        """
        return self._new_assignment_order
    
    @new_assignment_order.setter
    def new_assignment_order(self,value: Optional[assignment_order.AssignmentOrder] = None) -> None:
        """
        Sets the newAssignmentOrder property value. The newAssignmentOrder property
        Args:
            value: Value to set for the newAssignmentOrder property.
        """
        self._new_assignment_order = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("newAssignmentOrder", self.new_assignment_order)
        writer.write_additional_data_value(self.additional_data)
    

