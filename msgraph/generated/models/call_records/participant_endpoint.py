from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

identity_set = lazy_import('msgraph.generated.models.identity_set')
endpoint = lazy_import('msgraph.generated.models.call_records.endpoint')
user_feedback = lazy_import('msgraph.generated.models.call_records.user_feedback')

class ParticipantEndpoint(endpoint.Endpoint):
    def __init__(self,) -> None:
        """
        Instantiates a new ParticipantEndpoint and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.callRecords.participantEndpoint"
        # The feedback provided by the user of this endpoint about the quality of the session.
        self._feedback: Optional[user_feedback.UserFeedback] = None
        # Identity associated with the endpoint.
        self._identity: Optional[identity_set.IdentitySet] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ParticipantEndpoint:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ParticipantEndpoint
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ParticipantEndpoint()
    
    @property
    def feedback(self,) -> Optional[user_feedback.UserFeedback]:
        """
        Gets the feedback property value. The feedback provided by the user of this endpoint about the quality of the session.
        Returns: Optional[user_feedback.UserFeedback]
        """
        return self._feedback
    
    @feedback.setter
    def feedback(self,value: Optional[user_feedback.UserFeedback] = None) -> None:
        """
        Sets the feedback property value. The feedback provided by the user of this endpoint about the quality of the session.
        Args:
            value: Value to set for the feedback property.
        """
        self._feedback = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "feedback": lambda n : setattr(self, 'feedback', n.get_object_value(user_feedback.UserFeedback)),
            "identity": lambda n : setattr(self, 'identity', n.get_object_value(identity_set.IdentitySet)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def identity(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the identity property value. Identity associated with the endpoint.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._identity
    
    @identity.setter
    def identity(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the identity property value. Identity associated with the endpoint.
        Args:
            value: Value to set for the identity property.
        """
        self._identity = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("feedback", self.feedback)
        writer.write_object_value("identity", self.identity)
    

