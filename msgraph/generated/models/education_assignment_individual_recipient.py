from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

education_assignment_recipient = lazy_import('msgraph.generated.models.education_assignment_recipient')

class EducationAssignmentIndividualRecipient(education_assignment_recipient.EducationAssignmentRecipient):
    def __init__(self,) -> None:
        """
        Instantiates a new EducationAssignmentIndividualRecipient and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.educationAssignmentIndividualRecipient"
        # A collection of IDs of the recipients.
        self._recipients: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EducationAssignmentIndividualRecipient:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EducationAssignmentIndividualRecipient
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EducationAssignmentIndividualRecipient()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "recipients": lambda n : setattr(self, 'recipients', n.get_collection_of_primitive_values(str)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def recipients(self,) -> Optional[List[str]]:
        """
        Gets the recipients property value. A collection of IDs of the recipients.
        Returns: Optional[List[str]]
        """
        return self._recipients
    
    @recipients.setter
    def recipients(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the recipients property value. A collection of IDs of the recipients.
        Args:
            value: Value to set for the recipients property.
        """
        self._recipients = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_primitive_values("recipients", self.recipients)
    

