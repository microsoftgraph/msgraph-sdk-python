from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .user_experience_analytics_insight_severity import UserExperienceAnalyticsInsightSeverity
    from .user_experience_analytics_insight_value import UserExperienceAnalyticsInsightValue

@dataclass
class UserExperienceAnalyticsInsight(AdditionalDataHolder, BackedModel, Parsable):
    """
    The user experience analytics insight is the recomendation to improve the user experience analytics score.
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The unique identifier of the user experience analytics insight.
    insight_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates severity of insights. Possible values are: None, Informational, Warning, Error.
    severity: Optional[UserExperienceAnalyticsInsightSeverity] = None
    # The unique identifier of the user experience analytics metric.
    user_experience_analytics_metric_id: Optional[str] = None
    # The value of the user experience analytics insight.
    values: Optional[list[UserExperienceAnalyticsInsightValue]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserExperienceAnalyticsInsight:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsInsight
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserExperienceAnalyticsInsight()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .user_experience_analytics_insight_severity import UserExperienceAnalyticsInsightSeverity
        from .user_experience_analytics_insight_value import UserExperienceAnalyticsInsightValue

        from .user_experience_analytics_insight_severity import UserExperienceAnalyticsInsightSeverity
        from .user_experience_analytics_insight_value import UserExperienceAnalyticsInsightValue

        fields: dict[str, Callable[[Any], None]] = {
            "insightId": lambda n : setattr(self, 'insight_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "severity": lambda n : setattr(self, 'severity', n.get_enum_value(UserExperienceAnalyticsInsightSeverity)),
            "userExperienceAnalyticsMetricId": lambda n : setattr(self, 'user_experience_analytics_metric_id', n.get_str_value()),
            "values": lambda n : setattr(self, 'values', n.get_collection_of_object_values(UserExperienceAnalyticsInsightValue)),
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
        writer.write_str_value("insightId", self.insight_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("severity", self.severity)
        writer.write_str_value("userExperienceAnalyticsMetricId", self.user_experience_analytics_metric_id)
        writer.write_collection_of_object_values("values", self.values)
        writer.write_additional_data_value(self.additional_data)
    

