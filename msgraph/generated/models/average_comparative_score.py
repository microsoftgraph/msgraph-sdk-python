from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class AverageComparativeScore(AdditionalDataHolder, Parsable):
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
    def average_score(self,) -> Optional[float]:
        """
        Gets the averageScore property value. Average score within specified basis.
        Returns: Optional[float]
        """
        return self._average_score
    
    @average_score.setter
    def average_score(self,value: Optional[float] = None) -> None:
        """
        Sets the averageScore property value. Average score within specified basis.
        Args:
            value: Value to set for the averageScore property.
        """
        self._average_score = value
    
    @property
    def basis(self,) -> Optional[str]:
        """
        Gets the basis property value. Scope type. The possible values are: AllTenants, TotalSeats, IndustryTypes.
        Returns: Optional[str]
        """
        return self._basis
    
    @basis.setter
    def basis(self,value: Optional[str] = None) -> None:
        """
        Sets the basis property value. Scope type. The possible values are: AllTenants, TotalSeats, IndustryTypes.
        Args:
            value: Value to set for the basis property.
        """
        self._basis = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new averageComparativeScore and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Average score within specified basis.
        self._average_score: Optional[float] = None
        # Scope type. The possible values are: AllTenants, TotalSeats, IndustryTypes.
        self._basis: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AverageComparativeScore:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AverageComparativeScore
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AverageComparativeScore()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "average_score": lambda n : setattr(self, 'average_score', n.get_float_value()),
            "basis": lambda n : setattr(self, 'basis', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_float_value("averageScore", self.average_score)
        writer.write_str_value("basis", self.basis)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

