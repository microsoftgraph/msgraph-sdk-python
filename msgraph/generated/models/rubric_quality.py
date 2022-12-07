from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

education_item_body = lazy_import('msgraph.generated.models.education_item_body')
rubric_criterion = lazy_import('msgraph.generated.models.rubric_criterion')

class RubricQuality(AdditionalDataHolder, Parsable):
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
        Instantiates a new rubricQuality and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The collection of criteria for this rubric quality.
        self._criteria: Optional[List[rubric_criterion.RubricCriterion]] = None
        # The description of this rubric quality.
        self._description: Optional[education_item_body.EducationItemBody] = None
        # The name of this rubric quality.
        self._display_name: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The ID of this resource.
        self._quality_id: Optional[str] = None
        # If present, a numerical weight for this quality.  Weights must add up to 100.
        self._weight: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RubricQuality:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RubricQuality
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RubricQuality()
    
    @property
    def criteria(self,) -> Optional[List[rubric_criterion.RubricCriterion]]:
        """
        Gets the criteria property value. The collection of criteria for this rubric quality.
        Returns: Optional[List[rubric_criterion.RubricCriterion]]
        """
        return self._criteria
    
    @criteria.setter
    def criteria(self,value: Optional[List[rubric_criterion.RubricCriterion]] = None) -> None:
        """
        Sets the criteria property value. The collection of criteria for this rubric quality.
        Args:
            value: Value to set for the criteria property.
        """
        self._criteria = value
    
    @property
    def description(self,) -> Optional[education_item_body.EducationItemBody]:
        """
        Gets the description property value. The description of this rubric quality.
        Returns: Optional[education_item_body.EducationItemBody]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[education_item_body.EducationItemBody] = None) -> None:
        """
        Sets the description property value. The description of this rubric quality.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The name of this rubric quality.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The name of this rubric quality.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "criteria": lambda n : setattr(self, 'criteria', n.get_collection_of_object_values(rubric_criterion.RubricCriterion)),
            "description": lambda n : setattr(self, 'description', n.get_object_value(education_item_body.EducationItemBody)),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "quality_id": lambda n : setattr(self, 'quality_id', n.get_str_value()),
            "weight": lambda n : setattr(self, 'weight', n.get_float_value()),
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
        Gets the qualityId property value. The ID of this resource.
        Returns: Optional[str]
        """
        return self._quality_id
    
    @quality_id.setter
    def quality_id(self,value: Optional[str] = None) -> None:
        """
        Sets the qualityId property value. The ID of this resource.
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
        writer.write_collection_of_object_values("criteria", self.criteria)
        writer.write_object_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("qualityId", self.quality_id)
        writer.write_float_value("weight", self.weight)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def weight(self,) -> Optional[float]:
        """
        Gets the weight property value. If present, a numerical weight for this quality.  Weights must add up to 100.
        Returns: Optional[float]
        """
        return self._weight
    
    @weight.setter
    def weight(self,value: Optional[float] = None) -> None:
        """
        Sets the weight property value. If present, a numerical weight for this quality.  Weights must add up to 100.
        Args:
            value: Value to set for the weight property.
        """
        self._weight = value
    

