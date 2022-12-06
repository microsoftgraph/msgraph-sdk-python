from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
ocr_settings = lazy_import('msgraph.generated.models.security.ocr_settings')
redundancy_detection_settings = lazy_import('msgraph.generated.models.security.redundancy_detection_settings')
topic_modeling_settings = lazy_import('msgraph.generated.models.security.topic_modeling_settings')

class EdiscoveryCaseSettings(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new ediscoveryCaseSettings and sets the default values.
        """
        super().__init__()
        # The OCR (Optical Character Recognition) settings for the case.
        self._ocr: Optional[ocr_settings.OcrSettings] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The redundancy (near duplicate and email threading) detection settings for the case.
        self._redundancy_detection: Optional[redundancy_detection_settings.RedundancyDetectionSettings] = None
        # The Topic Modeling (Themes) settings for the case.
        self._topic_modeling: Optional[topic_modeling_settings.TopicModelingSettings] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EdiscoveryCaseSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EdiscoveryCaseSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EdiscoveryCaseSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "ocr": lambda n : setattr(self, 'ocr', n.get_object_value(ocr_settings.OcrSettings)),
            "redundancy_detection": lambda n : setattr(self, 'redundancy_detection', n.get_object_value(redundancy_detection_settings.RedundancyDetectionSettings)),
            "topic_modeling": lambda n : setattr(self, 'topic_modeling', n.get_object_value(topic_modeling_settings.TopicModelingSettings)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def ocr(self,) -> Optional[ocr_settings.OcrSettings]:
        """
        Gets the ocr property value. The OCR (Optical Character Recognition) settings for the case.
        Returns: Optional[ocr_settings.OcrSettings]
        """
        return self._ocr
    
    @ocr.setter
    def ocr(self,value: Optional[ocr_settings.OcrSettings] = None) -> None:
        """
        Sets the ocr property value. The OCR (Optical Character Recognition) settings for the case.
        Args:
            value: Value to set for the ocr property.
        """
        self._ocr = value
    
    @property
    def redundancy_detection(self,) -> Optional[redundancy_detection_settings.RedundancyDetectionSettings]:
        """
        Gets the redundancyDetection property value. The redundancy (near duplicate and email threading) detection settings for the case.
        Returns: Optional[redundancy_detection_settings.RedundancyDetectionSettings]
        """
        return self._redundancy_detection
    
    @redundancy_detection.setter
    def redundancy_detection(self,value: Optional[redundancy_detection_settings.RedundancyDetectionSettings] = None) -> None:
        """
        Sets the redundancyDetection property value. The redundancy (near duplicate and email threading) detection settings for the case.
        Args:
            value: Value to set for the redundancyDetection property.
        """
        self._redundancy_detection = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("ocr", self.ocr)
        writer.write_object_value("redundancyDetection", self.redundancy_detection)
        writer.write_object_value("topicModeling", self.topic_modeling)
    
    @property
    def topic_modeling(self,) -> Optional[topic_modeling_settings.TopicModelingSettings]:
        """
        Gets the topicModeling property value. The Topic Modeling (Themes) settings for the case.
        Returns: Optional[topic_modeling_settings.TopicModelingSettings]
        """
        return self._topic_modeling
    
    @topic_modeling.setter
    def topic_modeling(self,value: Optional[topic_modeling_settings.TopicModelingSettings] = None) -> None:
        """
        Sets the topicModeling property value. The Topic Modeling (Themes) settings for the case.
        Args:
            value: Value to set for the topicModeling property.
        """
        self._topic_modeling = value
    

