from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class RubricQualitySelectedColumnModel(AdditionalDataHolder, Parsable):
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
    
    @property
    def column_id(self,) -> Optional[str]:
        """
        Gets the columnId property value. ID of the selected level for this quality.
        Returns: Optional[str]
        """
        return self._column_id
    
    @column_id.setter
    def column_id(self,value: Optional[str] = None) -> None:
        """
        Sets the columnId property value. ID of the selected level for this quality.
        Args:
            value: Value to set for the columnId property.
        """
        self._column_id = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new rubricQualitySelectedColumnModel and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # ID of the selected level for this quality.
        self._column_id: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # ID of the associated quality.
        self._quality_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RubricQualitySelectedColumnModel:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RubricQualitySelectedColumnModel
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RubricQualitySelectedColumnModel()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "column_id": lambda n : setattr(self, 'column_id', n.get_str_value()),
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
        Gets the qualityId property value. ID of the associated quality.
        Returns: Optional[str]
        """
        return self._quality_id
    
    @quality_id.setter
    def quality_id(self,value: Optional[str] = None) -> None:
        """
        Sets the qualityId property value. ID of the associated quality.
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
        writer.write_str_value("columnId", self.column_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("qualityId", self.quality_id)
        writer.write_additional_data_value(self.additional_data)
    

