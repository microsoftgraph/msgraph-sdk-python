from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

education_item_body = lazy_import('msgraph.generated.models.education_item_body')
identity_set = lazy_import('msgraph.generated.models.identity_set')

class EducationFeedback(AdditionalDataHolder, Parsable):
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
        Instantiates a new educationFeedback and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # User who created the feedback.
        self._feedback_by: Optional[identity_set.IdentitySet] = None
        # Moment in time when the feedback was given. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        self._feedback_date_time: Optional[datetime] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Feedback.
        self._text: Optional[education_item_body.EducationItemBody] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EducationFeedback:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EducationFeedback
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EducationFeedback()
    
    @property
    def feedback_by(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the feedbackBy property value. User who created the feedback.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._feedback_by
    
    @feedback_by.setter
    def feedback_by(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the feedbackBy property value. User who created the feedback.
        Args:
            value: Value to set for the feedbackBy property.
        """
        self._feedback_by = value
    
    @property
    def feedback_date_time(self,) -> Optional[datetime]:
        """
        Gets the feedbackDateTime property value. Moment in time when the feedback was given. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Returns: Optional[datetime]
        """
        return self._feedback_date_time
    
    @feedback_date_time.setter
    def feedback_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the feedbackDateTime property value. Moment in time when the feedback was given. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Args:
            value: Value to set for the feedbackDateTime property.
        """
        self._feedback_date_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "feedback_by": lambda n : setattr(self, 'feedback_by', n.get_object_value(identity_set.IdentitySet)),
            "feedback_date_time": lambda n : setattr(self, 'feedback_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "text": lambda n : setattr(self, 'text', n.get_object_value(education_item_body.EducationItemBody)),
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("feedbackBy", self.feedback_by)
        writer.write_datetime_value("feedbackDateTime", self.feedback_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("text", self.text)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def text(self,) -> Optional[education_item_body.EducationItemBody]:
        """
        Gets the text property value. Feedback.
        Returns: Optional[education_item_body.EducationItemBody]
        """
        return self._text
    
    @text.setter
    def text(self,value: Optional[education_item_body.EducationItemBody] = None) -> None:
        """
        Sets the text property value. Feedback.
        Args:
            value: Value to set for the text property.
        """
        self._text = value
    

