from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_package_suggestion_related_people_insight_level import AccessPackageSuggestionRelatedPeopleInsightLevel
    from .control_configuration import ControlConfiguration

from .control_configuration import ControlConfiguration

@dataclass
class EndUserSettings(ControlConfiguration, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.endUserSettings"
    # The level of related people insights to show in access package suggestions. The possible values are: disabled, count, countAndNames, unknownFutureValue.
    related_people_insight_level: Optional[AccessPackageSuggestionRelatedPeopleInsightLevel] = None
    # Indicates whether approver details are shown to end users. When true, approver information is visible to members.
    show_approver_details_to_members: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EndUserSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EndUserSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EndUserSettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .access_package_suggestion_related_people_insight_level import AccessPackageSuggestionRelatedPeopleInsightLevel
        from .control_configuration import ControlConfiguration

        from .access_package_suggestion_related_people_insight_level import AccessPackageSuggestionRelatedPeopleInsightLevel
        from .control_configuration import ControlConfiguration

        fields: dict[str, Callable[[Any], None]] = {
            "relatedPeopleInsightLevel": lambda n : setattr(self, 'related_people_insight_level', n.get_enum_value(AccessPackageSuggestionRelatedPeopleInsightLevel)),
            "showApproverDetailsToMembers": lambda n : setattr(self, 'show_approver_details_to_members', n.get_bool_value()),
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
        writer.write_enum_value("relatedPeopleInsightLevel", self.related_people_insight_level)
        writer.write_bool_value("showApproverDetailsToMembers", self.show_approver_details_to_members)
    

