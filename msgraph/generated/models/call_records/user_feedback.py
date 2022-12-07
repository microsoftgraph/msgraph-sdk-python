from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

feedback_token_set = lazy_import('msgraph.generated.models.call_records.feedback_token_set')
user_feedback_rating = lazy_import('msgraph.generated.models.call_records.user_feedback_rating')

class UserFeedback(AdditionalDataHolder, Parsable):
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
        Instantiates a new userFeedback and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # The rating property
        self._rating: Optional[user_feedback_rating.UserFeedbackRating] = None
        # The feedback text provided by the user of this endpoint for the session.
        self._text: Optional[str] = None
        # The set of feedback tokens provided by the user of this endpoint for the session. This is a set of Boolean properties. The property names should not be relied upon since they may change depending on what tokens are offered to the user.
        self._tokens: Optional[feedback_token_set.FeedbackTokenSet] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserFeedback:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserFeedback
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserFeedback()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "rating": lambda n : setattr(self, 'rating', n.get_enum_value(user_feedback_rating.UserFeedbackRating)),
            "text": lambda n : setattr(self, 'text', n.get_str_value()),
            "tokens": lambda n : setattr(self, 'tokens', n.get_object_value(feedback_token_set.FeedbackTokenSet)),
        }
        return fields
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def rating(self,) -> Optional[user_feedback_rating.UserFeedbackRating]:
        """
        Gets the rating property value. The rating property
        Returns: Optional[user_feedback_rating.UserFeedbackRating]
        """
        return self._rating
    
    @rating.setter
    def rating(self,value: Optional[user_feedback_rating.UserFeedbackRating] = None) -> None:
        """
        Sets the rating property value. The rating property
        Args:
            value: Value to set for the rating property.
        """
        self._rating = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("rating", self.rating)
        writer.write_str_value("text", self.text)
        writer.write_object_value("tokens", self.tokens)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def text(self,) -> Optional[str]:
        """
        Gets the text property value. The feedback text provided by the user of this endpoint for the session.
        Returns: Optional[str]
        """
        return self._text
    
    @text.setter
    def text(self,value: Optional[str] = None) -> None:
        """
        Sets the text property value. The feedback text provided by the user of this endpoint for the session.
        Args:
            value: Value to set for the text property.
        """
        self._text = value
    
    @property
    def tokens(self,) -> Optional[feedback_token_set.FeedbackTokenSet]:
        """
        Gets the tokens property value. The set of feedback tokens provided by the user of this endpoint for the session. This is a set of Boolean properties. The property names should not be relied upon since they may change depending on what tokens are offered to the user.
        Returns: Optional[feedback_token_set.FeedbackTokenSet]
        """
        return self._tokens
    
    @tokens.setter
    def tokens(self,value: Optional[feedback_token_set.FeedbackTokenSet] = None) -> None:
        """
        Sets the tokens property value. The set of feedback tokens provided by the user of this endpoint for the session. This is a set of Boolean properties. The property names should not be relied upon since they may change depending on what tokens are offered to the user.
        Args:
            value: Value to set for the tokens property.
        """
        self._tokens = value
    

