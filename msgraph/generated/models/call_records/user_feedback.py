from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import feedback_token_set, user_feedback_rating

@dataclass
class UserFeedback(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    # The rating property
    rating: Optional[user_feedback_rating.UserFeedbackRating] = None
    # The feedback text provided by the user of this endpoint for the session.
    text: Optional[str] = None
    # The set of feedback tokens provided by the user of this endpoint for the session. This is a set of Boolean properties. The property names should not be relied upon since they may change depending on what tokens are offered to the user.
    tokens: Optional[feedback_token_set.FeedbackTokenSet] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserFeedback:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserFeedback
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return UserFeedback()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import feedback_token_set, user_feedback_rating

        from . import feedback_token_set, user_feedback_rating

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "rating": lambda n : setattr(self, 'rating', n.get_enum_value(user_feedback_rating.UserFeedbackRating)),
            "text": lambda n : setattr(self, 'text', n.get_str_value()),
            "tokens": lambda n : setattr(self, 'tokens', n.get_object_value(feedback_token_set.FeedbackTokenSet)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("rating", self.rating)
        writer.write_str_value("text", self.text)
        writer.write_object_value("tokens", self.tokens)
        writer.write_additional_data_value(self.additional_data)
    

