from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .education_assignment_recipient import EducationAssignmentRecipient

from .education_assignment_recipient import EducationAssignmentRecipient

@dataclass
class EducationAssignmentIndividualRecipient(EducationAssignmentRecipient, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.educationAssignmentIndividualRecipient"
    # A collection of IDs of the recipients.
    recipients: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EducationAssignmentIndividualRecipient:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EducationAssignmentIndividualRecipient
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EducationAssignmentIndividualRecipient()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .education_assignment_recipient import EducationAssignmentRecipient

        from .education_assignment_recipient import EducationAssignmentRecipient

        fields: dict[str, Callable[[Any], None]] = {
            "recipients": lambda n : setattr(self, 'recipients', n.get_collection_of_primitive_values(str)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_primitive_values("recipients", self.recipients)
    

