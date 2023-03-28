from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models import json

class AmorLincPostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new amorLincPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The basis property
        self._basis: Optional[json.Json] = None
        # The cost property
        self._cost: Optional[json.Json] = None
        # The datePurchased property
        self._date_purchased: Optional[json.Json] = None
        # The firstPeriod property
        self._first_period: Optional[json.Json] = None
        # The period property
        self._period: Optional[json.Json] = None
        # The rate property
        self._rate: Optional[json.Json] = None
        # The salvage property
        self._salvage: Optional[json.Json] = None
    
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
    def basis(self,) -> Optional[json.Json]:
        """
        Gets the basis property value. The basis property
        Returns: Optional[json.Json]
        """
        return self._basis
    
    @basis.setter
    def basis(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the basis property value. The basis property
        Args:
            value: Value to set for the basis property.
        """
        self._basis = value
    
    @property
    def cost(self,) -> Optional[json.Json]:
        """
        Gets the cost property value. The cost property
        Returns: Optional[json.Json]
        """
        return self._cost
    
    @cost.setter
    def cost(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the cost property value. The cost property
        Args:
            value: Value to set for the cost property.
        """
        self._cost = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AmorLincPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AmorLincPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AmorLincPostRequestBody()
    
    @property
    def date_purchased(self,) -> Optional[json.Json]:
        """
        Gets the datePurchased property value. The datePurchased property
        Returns: Optional[json.Json]
        """
        return self._date_purchased
    
    @date_purchased.setter
    def date_purchased(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the datePurchased property value. The datePurchased property
        Args:
            value: Value to set for the date_purchased property.
        """
        self._date_purchased = value
    
    @property
    def first_period(self,) -> Optional[json.Json]:
        """
        Gets the firstPeriod property value. The firstPeriod property
        Returns: Optional[json.Json]
        """
        return self._first_period
    
    @first_period.setter
    def first_period(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the firstPeriod property value. The firstPeriod property
        Args:
            value: Value to set for the first_period property.
        """
        self._first_period = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ........models import json

        fields: Dict[str, Callable[[Any], None]] = {
            "basis": lambda n : setattr(self, 'basis', n.get_object_value(json.Json)),
            "cost": lambda n : setattr(self, 'cost', n.get_object_value(json.Json)),
            "datePurchased": lambda n : setattr(self, 'date_purchased', n.get_object_value(json.Json)),
            "firstPeriod": lambda n : setattr(self, 'first_period', n.get_object_value(json.Json)),
            "period": lambda n : setattr(self, 'period', n.get_object_value(json.Json)),
            "rate": lambda n : setattr(self, 'rate', n.get_object_value(json.Json)),
            "salvage": lambda n : setattr(self, 'salvage', n.get_object_value(json.Json)),
        }
        return fields
    
    @property
    def period(self,) -> Optional[json.Json]:
        """
        Gets the period property value. The period property
        Returns: Optional[json.Json]
        """
        return self._period
    
    @period.setter
    def period(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the period property value. The period property
        Args:
            value: Value to set for the period property.
        """
        self._period = value
    
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
    
    @property
    def salvage(self,) -> Optional[json.Json]:
        """
        Gets the salvage property value. The salvage property
        Returns: Optional[json.Json]
        """
        return self._salvage
    
    @salvage.setter
    def salvage(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the salvage property value. The salvage property
        Args:
            value: Value to set for the salvage property.
        """
        self._salvage = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("basis", self.basis)
        writer.write_object_value("cost", self.cost)
        writer.write_object_value("datePurchased", self.date_purchased)
        writer.write_object_value("firstPeriod", self.first_period)
        writer.write_object_value("period", self.period)
        writer.write_object_value("rate", self.rate)
        writer.write_object_value("salvage", self.salvage)
        writer.write_additional_data_value(self.additional_data)
    

