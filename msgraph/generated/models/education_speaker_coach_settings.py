from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .education_speaker_coach_audience_engagement_settings import EducationSpeakerCoachAudienceEngagementSettings
    from .education_speaker_coach_content_settings import EducationSpeakerCoachContentSettings
    from .education_speaker_coach_delivery_settings import EducationSpeakerCoachDeliverySettings

@dataclass
class EducationSpeakerCoachSettings(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The audience engagement related feedback types that students should receive from the Speaker Coach.
    audience_engagement_settings: Optional[EducationSpeakerCoachAudienceEngagementSettings] = None
    # The content related feedback types that students should receive from the Speaker Coach.
    content_settings: Optional[EducationSpeakerCoachContentSettings] = None
    # The delivery related feedback types that students should receive from the Speaker Coach.
    delivery_settings: Optional[EducationSpeakerCoachDeliverySettings] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EducationSpeakerCoachSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EducationSpeakerCoachSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EducationSpeakerCoachSettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .education_speaker_coach_audience_engagement_settings import EducationSpeakerCoachAudienceEngagementSettings
        from .education_speaker_coach_content_settings import EducationSpeakerCoachContentSettings
        from .education_speaker_coach_delivery_settings import EducationSpeakerCoachDeliverySettings

        from .education_speaker_coach_audience_engagement_settings import EducationSpeakerCoachAudienceEngagementSettings
        from .education_speaker_coach_content_settings import EducationSpeakerCoachContentSettings
        from .education_speaker_coach_delivery_settings import EducationSpeakerCoachDeliverySettings

        fields: dict[str, Callable[[Any], None]] = {
            "audienceEngagementSettings": lambda n : setattr(self, 'audience_engagement_settings', n.get_object_value(EducationSpeakerCoachAudienceEngagementSettings)),
            "contentSettings": lambda n : setattr(self, 'content_settings', n.get_object_value(EducationSpeakerCoachContentSettings)),
            "deliverySettings": lambda n : setattr(self, 'delivery_settings', n.get_object_value(EducationSpeakerCoachDeliverySettings)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_object_value("audienceEngagementSettings", self.audience_engagement_settings)
        writer.write_object_value("contentSettings", self.content_settings)
        writer.write_object_value("deliverySettings", self.delivery_settings)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

