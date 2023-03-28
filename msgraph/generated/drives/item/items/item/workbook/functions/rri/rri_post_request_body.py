from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models import json

class RriPostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new rriPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The fv property
        self._fv: Optional[json.Json] = None
        # The nper property
        self._nper: Optional[json.Json] = None
        # The pv property
        self._pv: Optional[json.Json] = None
    
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
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RriPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RriPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RriPostRequestBody()
    
    @property
    def fv(self,) -> Optional[json.Json]:
        """
        Gets the fv property value. The fv property
        Returns: Optional[json.Json]
        """
        return self._fv
    
    @fv.setter
    def fv(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the fv property value. The fv property
        Args:
            value: Value to set for the fv property.
        """
        self._fv = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ........models import json

        fields: Dict[str, Callable[[Any], None]] = {
            "fv": lambda n : setattr(self, 'fv', n.get_object_value(json.Json)),
            "nper": lambda n : setattr(self, 'nper', n.get_object_value(json.Json)),
            "pv": lambda n : setattr(self, 'pv', n.get_object_value(json.Json)),
        }
        return fields
    
    @property
    def nper(self,) -> Optional[json.Json]:
        """
        Gets the nper property value. The nper property
        Returns: Optional[json.Json]
        """
        return self._nper
    
    @nper.setter
    def nper(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the nper property value. The nper property
        Args:
            value: Value to set for the nper property.
        """
        self._nper = value
    
    @property
    def pv(self,) -> Optional[json.Json]:
        """
        Gets the pv property value. The pv property
        Returns: Optional[json.Json]
        """
        return self._pv
    
    @pv.setter
    def pv(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the pv property value. The pv property
        Args:
            value: Value to set for the pv property.
        """
        self._pv = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("fv", self.fv)
        writer.write_object_value("nper", self.nper)
        writer.write_object_value("pv", self.pv)
        writer.write_additional_data_value(self.additional_data)
    

