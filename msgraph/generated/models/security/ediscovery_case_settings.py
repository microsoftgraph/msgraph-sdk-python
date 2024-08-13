from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .ocr_settings import OcrSettings
    from .redundancy_detection_settings import RedundancyDetectionSettings
    from .topic_modeling_settings import TopicModelingSettings

from ..entity import Entity

@dataclass
class EdiscoveryCaseSettings(Entity):
    # The OCR (Optical Character Recognition) settings for the case.
    ocr: Optional[OcrSettings] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The redundancy (near duplicate and email threading) detection settings for the case.
    redundancy_detection: Optional[RedundancyDetectionSettings] = None
    # The Topic Modeling (Themes) settings for the case.
    topic_modeling: Optional[TopicModelingSettings] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EdiscoveryCaseSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EdiscoveryCaseSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EdiscoveryCaseSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .ocr_settings import OcrSettings
        from .redundancy_detection_settings import RedundancyDetectionSettings
        from .topic_modeling_settings import TopicModelingSettings

        from ..entity import Entity
        from .ocr_settings import OcrSettings
        from .redundancy_detection_settings import RedundancyDetectionSettings
        from .topic_modeling_settings import TopicModelingSettings

        fields: Dict[str, Callable[[Any], None]] = {
            "ocr": lambda n : setattr(self, 'ocr', n.get_object_value(OcrSettings)),
            "redundancyDetection": lambda n : setattr(self, 'redundancy_detection', n.get_object_value(RedundancyDetectionSettings)),
            "topicModeling": lambda n : setattr(self, 'topic_modeling', n.get_object_value(TopicModelingSettings)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_object_value("ocr", self.ocr)
        writer.write_object_value("redundancyDetection", self.redundancy_detection)
        writer.write_object_value("topicModeling", self.topic_modeling)
    

