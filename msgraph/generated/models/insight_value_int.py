from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .user_experience_analytics_insight_value import UserExperienceAnalyticsInsightValue

from .user_experience_analytics_insight_value import UserExperienceAnalyticsInsightValue

@dataclass
class InsightValueInt(UserExperienceAnalyticsInsightValue):
    odata_type = "#microsoft.graph.insightValueInt"
    # The int value of the user experience analytics insight.
    value: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> InsightValueInt:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: InsightValueInt
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return InsightValueInt()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .user_experience_analytics_insight_value import UserExperienceAnalyticsInsightValue

        from .user_experience_analytics_insight_value import UserExperienceAnalyticsInsightValue

        fields: Dict[str, Callable[[Any], None]] = {
            "value": lambda n : setattr(self, 'value', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_int_value("value", self.value)
    

