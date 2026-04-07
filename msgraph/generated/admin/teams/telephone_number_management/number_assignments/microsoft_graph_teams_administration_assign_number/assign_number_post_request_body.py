from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ......models.teams_administration.assignment_category import AssignmentCategory
    from ......models.teams_administration.number_type import NumberType

@dataclass
class AssignNumberPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The assignmentCategory property
    assignment_category: Optional[AssignmentCategory] = None
    # The assignmentTargetId property
    assignment_target_id: Optional[str] = None
    # The locationId property
    location_id: Optional[str] = None
    # The numberType property
    number_type: Optional[NumberType] = None
    # The telephoneNumber property
    telephone_number: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AssignNumberPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AssignNumberPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AssignNumberPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ......models.teams_administration.assignment_category import AssignmentCategory
        from ......models.teams_administration.number_type import NumberType

        from ......models.teams_administration.assignment_category import AssignmentCategory
        from ......models.teams_administration.number_type import NumberType

        fields: dict[str, Callable[[Any], None]] = {
            "assignmentCategory": lambda n : setattr(self, 'assignment_category', n.get_enum_value(AssignmentCategory)),
            "assignmentTargetId": lambda n : setattr(self, 'assignment_target_id', n.get_str_value()),
            "locationId": lambda n : setattr(self, 'location_id', n.get_str_value()),
            "numberType": lambda n : setattr(self, 'number_type', n.get_enum_value(NumberType)),
            "telephoneNumber": lambda n : setattr(self, 'telephone_number', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_enum_value("assignmentCategory", self.assignment_category)
        writer.write_str_value("assignmentTargetId", self.assignment_target_id)
        writer.write_str_value("locationId", self.location_id)
        writer.write_enum_value("numberType", self.number_type)
        writer.write_str_value("telephoneNumber", self.telephone_number)
        writer.write_additional_data_value(self.additional_data)
    

