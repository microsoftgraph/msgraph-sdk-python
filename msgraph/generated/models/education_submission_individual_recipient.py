from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

education_submission_recipient = lazy_import('msgraph.generated.models.education_submission_recipient')

class EducationSubmissionIndividualRecipient(education_submission_recipient.EducationSubmissionRecipient):
    def __init__(self,) -> None:
        """
        Instantiates a new EducationSubmissionIndividualRecipient and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.educationSubmissionIndividualRecipient"
        # User ID of the user to whom the submission is assigned.
        self._user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EducationSubmissionIndividualRecipient:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EducationSubmissionIndividualRecipient
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EducationSubmissionIndividualRecipient()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "user_id": lambda n : setattr(self, 'user_id', n.get_str_value()),
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
        writer.write_str_value("userId", self.user_id)
    
    @property
    def user_id(self,) -> Optional[str]:
        """
        Gets the userId property value. User ID of the user to whom the submission is assigned.
        Returns: Optional[str]
        """
        return self._user_id
    
    @user_id.setter
    def user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the userId property value. User ID of the user to whom the submission is assigned.
        Args:
            value: Value to set for the userId property.
        """
        self._user_id = value
    

