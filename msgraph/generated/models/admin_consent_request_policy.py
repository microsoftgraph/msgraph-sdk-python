from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

access_review_reviewer_scope = lazy_import('msgraph.generated.models.access_review_reviewer_scope')
entity = lazy_import('msgraph.generated.models.entity')

class AdminConsentRequestPolicy(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new adminConsentRequestPolicy and sets the default values.
        """
        super().__init__()
        # Specifies whether the admin consent request feature is enabled or disabled. Required.
        self._is_enabled: Optional[bool] = None
        # Specifies whether reviewers will receive notifications. Required.
        self._notify_reviewers: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Specifies whether reviewers will receive reminder emails. Required.
        self._reminders_enabled: Optional[bool] = None
        # Specifies the duration the request is active before it automatically expires if no decision is applied.
        self._request_duration_in_days: Optional[int] = None
        # The list of reviewers for the admin consent. Required.
        self._reviewers: Optional[List[access_review_reviewer_scope.AccessReviewReviewerScope]] = None
        # Specifies the version of this policy. When the policy is updated, this version is updated. Read-only.
        self._version: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AdminConsentRequestPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AdminConsentRequestPolicy
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AdminConsentRequestPolicy()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "is_enabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
            "notify_reviewers": lambda n : setattr(self, 'notify_reviewers', n.get_bool_value()),
            "reminders_enabled": lambda n : setattr(self, 'reminders_enabled', n.get_bool_value()),
            "request_duration_in_days": lambda n : setattr(self, 'request_duration_in_days', n.get_int_value()),
            "reviewers": lambda n : setattr(self, 'reviewers', n.get_collection_of_object_values(access_review_reviewer_scope.AccessReviewReviewerScope)),
            "version": lambda n : setattr(self, 'version', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_enabled(self,) -> Optional[bool]:
        """
        Gets the isEnabled property value. Specifies whether the admin consent request feature is enabled or disabled. Required.
        Returns: Optional[bool]
        """
        return self._is_enabled
    
    @is_enabled.setter
    def is_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isEnabled property value. Specifies whether the admin consent request feature is enabled or disabled. Required.
        Args:
            value: Value to set for the isEnabled property.
        """
        self._is_enabled = value
    
    @property
    def notify_reviewers(self,) -> Optional[bool]:
        """
        Gets the notifyReviewers property value. Specifies whether reviewers will receive notifications. Required.
        Returns: Optional[bool]
        """
        return self._notify_reviewers
    
    @notify_reviewers.setter
    def notify_reviewers(self,value: Optional[bool] = None) -> None:
        """
        Sets the notifyReviewers property value. Specifies whether reviewers will receive notifications. Required.
        Args:
            value: Value to set for the notifyReviewers property.
        """
        self._notify_reviewers = value
    
    @property
    def reminders_enabled(self,) -> Optional[bool]:
        """
        Gets the remindersEnabled property value. Specifies whether reviewers will receive reminder emails. Required.
        Returns: Optional[bool]
        """
        return self._reminders_enabled
    
    @reminders_enabled.setter
    def reminders_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the remindersEnabled property value. Specifies whether reviewers will receive reminder emails. Required.
        Args:
            value: Value to set for the remindersEnabled property.
        """
        self._reminders_enabled = value
    
    @property
    def request_duration_in_days(self,) -> Optional[int]:
        """
        Gets the requestDurationInDays property value. Specifies the duration the request is active before it automatically expires if no decision is applied.
        Returns: Optional[int]
        """
        return self._request_duration_in_days
    
    @request_duration_in_days.setter
    def request_duration_in_days(self,value: Optional[int] = None) -> None:
        """
        Sets the requestDurationInDays property value. Specifies the duration the request is active before it automatically expires if no decision is applied.
        Args:
            value: Value to set for the requestDurationInDays property.
        """
        self._request_duration_in_days = value
    
    @property
    def reviewers(self,) -> Optional[List[access_review_reviewer_scope.AccessReviewReviewerScope]]:
        """
        Gets the reviewers property value. The list of reviewers for the admin consent. Required.
        Returns: Optional[List[access_review_reviewer_scope.AccessReviewReviewerScope]]
        """
        return self._reviewers
    
    @reviewers.setter
    def reviewers(self,value: Optional[List[access_review_reviewer_scope.AccessReviewReviewerScope]] = None) -> None:
        """
        Sets the reviewers property value. The list of reviewers for the admin consent. Required.
        Args:
            value: Value to set for the reviewers property.
        """
        self._reviewers = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("isEnabled", self.is_enabled)
        writer.write_bool_value("notifyReviewers", self.notify_reviewers)
        writer.write_bool_value("remindersEnabled", self.reminders_enabled)
        writer.write_int_value("requestDurationInDays", self.request_duration_in_days)
        writer.write_collection_of_object_values("reviewers", self.reviewers)
        writer.write_int_value("version", self.version)
    
    @property
    def version(self,) -> Optional[int]:
        """
        Gets the version property value. Specifies the version of this policy. When the policy is updated, this version is updated. Read-only.
        Returns: Optional[int]
        """
        return self._version
    
    @version.setter
    def version(self,value: Optional[int] = None) -> None:
        """
        Sets the version property value. Specifies the version of this policy. When the policy is updated, this version is updated. Read-only.
        Args:
            value: Value to set for the version property.
        """
        self._version = value
    

