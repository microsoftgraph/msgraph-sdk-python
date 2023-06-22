from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import access_review_reviewer_scope, entity

from . import entity

@dataclass
class AdminConsentRequestPolicy(entity.Entity):
    # Specifies whether the admin consent request feature is enabled or disabled. Required.
    is_enabled: Optional[bool] = None
    # Specifies whether reviewers will receive notifications. Required.
    notify_reviewers: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Specifies whether reviewers will receive reminder emails. Required.
    reminders_enabled: Optional[bool] = None
    # Specifies the duration the request is active before it automatically expires if no decision is applied.
    request_duration_in_days: Optional[int] = None
    # The list of reviewers for the admin consent. Required.
    reviewers: Optional[List[access_review_reviewer_scope.AccessReviewReviewerScope]] = None
    # Specifies the version of this policy. When the policy is updated, this version is updated. Read-only.
    version: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AdminConsentRequestPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AdminConsentRequestPolicy
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AdminConsentRequestPolicy()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import access_review_reviewer_scope, entity

        from . import access_review_reviewer_scope, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "isEnabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
            "notifyReviewers": lambda n : setattr(self, 'notify_reviewers', n.get_bool_value()),
            "remindersEnabled": lambda n : setattr(self, 'reminders_enabled', n.get_bool_value()),
            "requestDurationInDays": lambda n : setattr(self, 'request_duration_in_days', n.get_int_value()),
            "reviewers": lambda n : setattr(self, 'reviewers', n.get_collection_of_object_values(access_review_reviewer_scope.AccessReviewReviewerScope)),
            "version": lambda n : setattr(self, 'version', n.get_int_value()),
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
        writer.write_bool_value("isEnabled", self.is_enabled)
        writer.write_bool_value("notifyReviewers", self.notify_reviewers)
        writer.write_bool_value("remindersEnabled", self.reminders_enabled)
        writer.write_int_value("requestDurationInDays", self.request_duration_in_days)
        writer.write_collection_of_object_values("reviewers", self.reviewers)
        writer.write_int_value("version", self.version)
    

