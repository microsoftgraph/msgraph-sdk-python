from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

tone = lazy_import('msgraph.generated.models.tone')

class ToneInfo(AdditionalDataHolder, Parsable):
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
        Instantiates a new toneInfo and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # An incremental identifier used for ordering DTMF events.
        self._sequence_id: Optional[int] = None
        # The tone property
        self._tone: Optional[tone.Tone] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ToneInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ToneInfo
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ToneInfo()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "sequence_id": lambda n : setattr(self, 'sequence_id', n.get_int_value()),
            "tone": lambda n : setattr(self, 'tone', n.get_enum_value(tone.Tone)),
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
    def sequence_id(self,) -> Optional[int]:
        """
        Gets the sequenceId property value. An incremental identifier used for ordering DTMF events.
        Returns: Optional[int]
        """
        return self._sequence_id
    
    @sequence_id.setter
    def sequence_id(self,value: Optional[int] = None) -> None:
        """
        Sets the sequenceId property value. An incremental identifier used for ordering DTMF events.
        Args:
            value: Value to set for the sequenceId property.
        """
        self._sequence_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("sequenceId", self.sequence_id)
        writer.write_enum_value("tone", self.tone)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def tone(self,) -> Optional[tone.Tone]:
        """
        Gets the tone property value. The tone property
        Returns: Optional[tone.Tone]
        """
        return self._tone
    
    @tone.setter
    def tone(self,value: Optional[tone.Tone] = None) -> None:
        """
        Sets the tone property value. The tone property
        Args:
            value: Value to set for the tone property.
        """
        self._tone = value
    

