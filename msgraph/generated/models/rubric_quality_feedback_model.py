from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

education_item_body = lazy_import('msgraph.generated.models.education_item_body')

class RubricQualityFeedbackModel(AdditionalDataHolder, Parsable):
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
        Instantiates a new rubricQualityFeedbackModel and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Specific feedback for one quality of this rubric.
        self._feedback: Optional[education_item_body.EducationItemBody] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The ID of the rubricQuality that this feedback is related to.
        self._quality_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RubricQualityFeedbackModel:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RubricQualityFeedbackModel
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RubricQualityFeedbackModel()
    
    @property
    def feedback(self,) -> Optional[education_item_body.EducationItemBody]:
        """
        Gets the feedback property value. Specific feedback for one quality of this rubric.
        Returns: Optional[education_item_body.EducationItemBody]
        """
        return self._feedback
    
    @feedback.setter
    def feedback(self,value: Optional[education_item_body.EducationItemBody] = None) -> None:
        """
        Sets the feedback property value. Specific feedback for one quality of this rubric.
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
            "feedback": lambda n : setattr(self, 'feedback', n.get_object_value(education_item_body.EducationItemBody)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "quality_id": lambda n : setattr(self, 'quality_id', n.get_str_value()),
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
    def quality_id(self,) -> Optional[str]:
        """
        Gets the qualityId property value. The ID of the rubricQuality that this feedback is related to.
        Returns: Optional[str]
        """
        return self._quality_id
    
    @quality_id.setter
    def quality_id(self,value: Optional[str] = None) -> None:
        """
        Sets the qualityId property value. The ID of the rubricQuality that this feedback is related to.
        Args:
            value: Value to set for the qualityId property.
        """
        self._quality_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("feedback", self.feedback)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("qualityId", self.quality_id)
        writer.write_additional_data_value(self.additional_data)
    

