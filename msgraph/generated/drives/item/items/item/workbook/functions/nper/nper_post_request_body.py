from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models import json

class NperPostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new nperPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The fv property
        self._fv: Optional[json.Json] = None
        # The pmt property
        self._pmt: Optional[json.Json] = None
        # The pv property
        self._pv: Optional[json.Json] = None
        # The rate property
        self._rate: Optional[json.Json] = None
        # The type property
        self._type: Optional[json.Json] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> NperPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: NperPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return NperPostRequestBody()
    
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
            "pmt": lambda n : setattr(self, 'pmt', n.get_object_value(json.Json)),
            "pv": lambda n : setattr(self, 'pv', n.get_object_value(json.Json)),
            "rate": lambda n : setattr(self, 'rate', n.get_object_value(json.Json)),
            "type": lambda n : setattr(self, 'type', n.get_object_value(json.Json)),
        }
        return fields
    
    @property
    def pmt(self,) -> Optional[json.Json]:
        """
        Gets the pmt property value. The pmt property
        Returns: Optional[json.Json]
        """
        return self._pmt
    
    @pmt.setter
    def pmt(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the pmt property value. The pmt property
        Args:
            value: Value to set for the pmt property.
        """
        self._pmt = value
    
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
    
    @property
    def rate(self,) -> Optional[json.Json]:
        """
        Gets the rate property value. The rate property
        Returns: Optional[json.Json]
        """
        return self._rate
    
    @rate.setter
    def rate(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the rate property value. The rate property
        Args:
            value: Value to set for the rate property.
        """
        self._rate = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("fv", self.fv)
        writer.write_object_value("pmt", self.pmt)
        writer.write_object_value("pv", self.pv)
        writer.write_object_value("rate", self.rate)
        writer.write_object_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def type(self,) -> Optional[json.Json]:
        """
        Gets the type property value. The type property
        Returns: Optional[json.Json]
        """
        return self._type
    
    @type.setter
    def type(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the type property value. The type property
        Args:
            value: Value to set for the type property.
        """
        self._type = value
    

