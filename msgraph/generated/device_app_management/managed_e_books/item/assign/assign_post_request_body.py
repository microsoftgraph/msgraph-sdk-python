from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

managed_e_book_assignment = lazy_import('msgraph.generated.models.managed_e_book_assignment')

class AssignPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the assign method.
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
        Instantiates a new assignPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The managedEBookAssignments property
        self._managed_e_book_assignments: Optional[List[managed_e_book_assignment.ManagedEBookAssignment]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AssignPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AssignPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AssignPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "managed_e_book_assignments": lambda n : setattr(self, 'managed_e_book_assignments', n.get_collection_of_object_values(managed_e_book_assignment.ManagedEBookAssignment)),
        }
        return fields
    
    @property
    def managed_e_book_assignments(self,) -> Optional[List[managed_e_book_assignment.ManagedEBookAssignment]]:
        """
        Gets the managedEBookAssignments property value. The managedEBookAssignments property
        Returns: Optional[List[managed_e_book_assignment.ManagedEBookAssignment]]
        """
        return self._managed_e_book_assignments
    
    @managed_e_book_assignments.setter
    def managed_e_book_assignments(self,value: Optional[List[managed_e_book_assignment.ManagedEBookAssignment]] = None) -> None:
        """
        Sets the managedEBookAssignments property value. The managedEBookAssignments property
        Args:
            value: Value to set for the managedEBookAssignments property.
        """
        self._managed_e_book_assignments = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_object_values("managedEBookAssignments", self.managed_e_book_assignments)
        writer.write_additional_data_value(self.additional_data)
    

