from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

exchange_id_format = lazy_import('msgraph.generated.models.exchange_id_format')

class TranslateExchangeIdsPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the translateExchangeIds method.
    """
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
        Instantiates a new translateExchangeIdsPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The InputIds property
        self._input_ids: Optional[List[str]] = None
        # The SourceIdType property
        self._source_id_type: Optional[exchange_id_format.ExchangeIdFormat] = None
        # The TargetIdType property
        self._target_id_type: Optional[exchange_id_format.ExchangeIdFormat] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TranslateExchangeIdsPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TranslateExchangeIdsPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TranslateExchangeIdsPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "input_ids": lambda n : setattr(self, 'input_ids', n.get_collection_of_primitive_values(str)),
            "source_id_type": lambda n : setattr(self, 'source_id_type', n.get_enum_value(exchange_id_format.ExchangeIdFormat)),
            "target_id_type": lambda n : setattr(self, 'target_id_type', n.get_enum_value(exchange_id_format.ExchangeIdFormat)),
        }
        return fields
    
    @property
    def input_ids(self,) -> Optional[List[str]]:
        """
        Gets the inputIds property value. The InputIds property
        Returns: Optional[List[str]]
        """
        return self._input_ids
    
    @input_ids.setter
    def input_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the inputIds property value. The InputIds property
        Args:
            value: Value to set for the InputIds property.
        """
        self._input_ids = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_primitive_values("InputIds", self.input_ids)
        writer.write_enum_value("SourceIdType", self.source_id_type)
        writer.write_enum_value("TargetIdType", self.target_id_type)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def source_id_type(self,) -> Optional[exchange_id_format.ExchangeIdFormat]:
        """
        Gets the sourceIdType property value. The SourceIdType property
        Returns: Optional[exchange_id_format.ExchangeIdFormat]
        """
        return self._source_id_type
    
    @source_id_type.setter
    def source_id_type(self,value: Optional[exchange_id_format.ExchangeIdFormat] = None) -> None:
        """
        Sets the sourceIdType property value. The SourceIdType property
        Args:
            value: Value to set for the SourceIdType property.
        """
        self._source_id_type = value
    
    @property
    def target_id_type(self,) -> Optional[exchange_id_format.ExchangeIdFormat]:
        """
        Gets the targetIdType property value. The TargetIdType property
        Returns: Optional[exchange_id_format.ExchangeIdFormat]
        """
        return self._target_id_type
    
    @target_id_type.setter
    def target_id_type(self,value: Optional[exchange_id_format.ExchangeIdFormat] = None) -> None:
        """
        Sets the targetIdType property value. The TargetIdType property
        Args:
            value: Value to set for the TargetIdType property.
        """
        self._target_id_type = value
    

