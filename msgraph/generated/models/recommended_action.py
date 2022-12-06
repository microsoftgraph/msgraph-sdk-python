from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class RecommendedAction(AdditionalDataHolder, Parsable):
    @property
    def action_web_url(self,) -> Optional[str]:
        """
        Gets the actionWebUrl property value. Web URL to the recommended action.
        Returns: Optional[str]
        """
        return self._action_web_url
    
    @action_web_url.setter
    def action_web_url(self,value: Optional[str] = None) -> None:
        """
        Sets the actionWebUrl property value. Web URL to the recommended action.
        Args:
            value: Value to set for the actionWebUrl property.
        """
        self._action_web_url = value
    
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
        Instantiates a new recommendedAction and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Web URL to the recommended action.
        self._action_web_url: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Potential improvement in the tenant security score from the recommended action.
        self._potential_score_impact: Optional[float] = None
        # Title of the recommended action.
        self._title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RecommendedAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RecommendedAction
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RecommendedAction()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "action_web_url": lambda n : setattr(self, 'action_web_url', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "potential_score_impact": lambda n : setattr(self, 'potential_score_impact', n.get_float_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
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
    def potential_score_impact(self,) -> Optional[float]:
        """
        Gets the potentialScoreImpact property value. Potential improvement in the tenant security score from the recommended action.
        Returns: Optional[float]
        """
        return self._potential_score_impact
    
    @potential_score_impact.setter
    def potential_score_impact(self,value: Optional[float] = None) -> None:
        """
        Sets the potentialScoreImpact property value. Potential improvement in the tenant security score from the recommended action.
        Args:
            value: Value to set for the potentialScoreImpact property.
        """
        self._potential_score_impact = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("actionWebUrl", self.action_web_url)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_float_value("potentialScoreImpact", self.potential_score_impact)
        writer.write_str_value("title", self.title)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def title(self,) -> Optional[str]:
        """
        Gets the title property value. Title of the recommended action.
        Returns: Optional[str]
        """
        return self._title
    
    @title.setter
    def title(self,value: Optional[str] = None) -> None:
        """
        Sets the title property value. Title of the recommended action.
        Args:
            value: Value to set for the title property.
        """
        self._title = value
    

