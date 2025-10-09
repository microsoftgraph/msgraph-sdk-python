from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .education_ai_feedback_settings import EducationAiFeedbackSettings
    from .education_speech_type import EducationSpeechType

@dataclass
class EducationAiFeedbackCriteria(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The aiFeedbackSettings property
    ai_feedback_settings: Optional[EducationAiFeedbackSettings] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The speechType property
    speech_type: Optional[EducationSpeechType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EducationAiFeedbackCriteria:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EducationAiFeedbackCriteria
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EducationAiFeedbackCriteria()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .education_ai_feedback_settings import EducationAiFeedbackSettings
        from .education_speech_type import EducationSpeechType

        from .education_ai_feedback_settings import EducationAiFeedbackSettings
        from .education_speech_type import EducationSpeechType

        fields: dict[str, Callable[[Any], None]] = {
            "aiFeedbackSettings": lambda n : setattr(self, 'ai_feedback_settings', n.get_object_value(EducationAiFeedbackSettings)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "speechType": lambda n : setattr(self, 'speech_type', n.get_enum_value(EducationSpeechType)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("aiFeedbackSettings", self.ai_feedback_settings)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("speechType", self.speech_type)
        writer.write_additional_data_value(self.additional_data)
    

