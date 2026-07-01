from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_package_suggestion_reason import AccessPackageSuggestionReason
    from .identity import Identity

from .access_package_suggestion_reason import AccessPackageSuggestionReason

@dataclass
class AccessPackageSuggestionRelatedPeopleBased(AccessPackageSuggestionReason, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.accessPackageSuggestionRelatedPeopleBased"
    # A collection of identities representing people related to the current user who may have access to similar resources. This property is only populated when the tenant's endUserSettings have relatedPeopleInsightLevel set to countAndNames. This includes both the user ID and display name information.
    related_people: Optional[list[Identity]] = None
    # The number of related people who have assignments to this access package. This count is always provided regardless of the relatedPeopleInsightLevel setting.
    related_people_assignment_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AccessPackageSuggestionRelatedPeopleBased:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageSuggestionRelatedPeopleBased
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AccessPackageSuggestionRelatedPeopleBased()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .access_package_suggestion_reason import AccessPackageSuggestionReason
        from .identity import Identity

        from .access_package_suggestion_reason import AccessPackageSuggestionReason
        from .identity import Identity

        fields: dict[str, Callable[[Any], None]] = {
            "relatedPeople": lambda n : setattr(self, 'related_people', n.get_collection_of_object_values(Identity)),
            "relatedPeopleAssignmentCount": lambda n : setattr(self, 'related_people_assignment_count', n.get_int_value()),
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
        writer.write_collection_of_object_values("relatedPeople", self.related_people)
        writer.write_int_value("relatedPeopleAssignmentCount", self.related_people_assignment_count)
    

