from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

access_review_history_definition = lazy_import('msgraph.generated.models.access_review_history_definition')
access_review_schedule_definition = lazy_import('msgraph.generated.models.access_review_schedule_definition')
entity = lazy_import('msgraph.generated.models.entity')

class AccessReviewSet(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new AccessReviewSet and sets the default values.
        """
        super().__init__()
        # Represents the template and scheduling for an access review.
        self._definitions: Optional[List[access_review_schedule_definition.AccessReviewScheduleDefinition]] = None
        # Represents a collection of access review history data and the scopes used to collect that data.
        self._history_definitions: Optional[List[access_review_history_definition.AccessReviewHistoryDefinition]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessReviewSet:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessReviewSet
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AccessReviewSet()
    
    @property
    def definitions(self,) -> Optional[List[access_review_schedule_definition.AccessReviewScheduleDefinition]]:
        """
        Gets the definitions property value. Represents the template and scheduling for an access review.
        Returns: Optional[List[access_review_schedule_definition.AccessReviewScheduleDefinition]]
        """
        return self._definitions
    
    @definitions.setter
    def definitions(self,value: Optional[List[access_review_schedule_definition.AccessReviewScheduleDefinition]] = None) -> None:
        """
        Sets the definitions property value. Represents the template and scheduling for an access review.
        Args:
            value: Value to set for the definitions property.
        """
        self._definitions = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "definitions": lambda n : setattr(self, 'definitions', n.get_collection_of_object_values(access_review_schedule_definition.AccessReviewScheduleDefinition)),
            "history_definitions": lambda n : setattr(self, 'history_definitions', n.get_collection_of_object_values(access_review_history_definition.AccessReviewHistoryDefinition)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def history_definitions(self,) -> Optional[List[access_review_history_definition.AccessReviewHistoryDefinition]]:
        """
        Gets the historyDefinitions property value. Represents a collection of access review history data and the scopes used to collect that data.
        Returns: Optional[List[access_review_history_definition.AccessReviewHistoryDefinition]]
        """
        return self._history_definitions
    
    @history_definitions.setter
    def history_definitions(self,value: Optional[List[access_review_history_definition.AccessReviewHistoryDefinition]] = None) -> None:
        """
        Sets the historyDefinitions property value. Represents a collection of access review history data and the scopes used to collect that data.
        Args:
            value: Value to set for the historyDefinitions property.
        """
        self._history_definitions = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("definitions", self.definitions)
        writer.write_collection_of_object_values("historyDefinitions", self.history_definitions)
    

