from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_package import AccessPackage
    from .access_package_assignment_approval_settings import AccessPackageAssignmentApprovalSettings
    from .access_package_assignment_requestor_settings import AccessPackageAssignmentRequestorSettings
    from .access_package_assignment_review_settings import AccessPackageAssignmentReviewSettings
    from .access_package_automatic_request_settings import AccessPackageAutomaticRequestSettings
    from .access_package_catalog import AccessPackageCatalog
    from .access_package_notification_settings import AccessPackageNotificationSettings
    from .access_package_question import AccessPackageQuestion
    from .allowed_target_scope import AllowedTargetScope
    from .custom_extension_stage_setting import CustomExtensionStageSetting
    from .entity import Entity
    from .expiration_pattern import ExpirationPattern
    from .subject_set import SubjectSet

from .entity import Entity

@dataclass
class AccessPackageAssignmentPolicy(Entity, Parsable):
    # Access package containing this policy. Read-only.  Supports $expand.
    access_package: Optional[AccessPackage] = None
    # Principals that can be assigned the access package through this policy. The possible values are: notSpecified, specificDirectoryUsers, specificConnectedOrganizationUsers, specificDirectoryServicePrincipals, allMemberUsers, allDirectoryUsers, allDirectoryServicePrincipals, allConfiguredConnectedOrganizationUsers, allExternalUsers, unknownFutureValue.
    allowed_target_scope: Optional[AllowedTargetScope] = None
    # This property is only present for an auto assignment policy; if absent, this is a request-based policy.
    automatic_request_settings: Optional[AccessPackageAutomaticRequestSettings] = None
    # Catalog of the access package containing this policy. Read-only.
    catalog: Optional[AccessPackageCatalog] = None
    # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    created_date_time: Optional[datetime.datetime] = None
    # The collection of stages when to execute one or more custom access package workflow extensions. Supports $expand.
    custom_extension_stage_settings: Optional[list[CustomExtensionStageSetting]] = None
    # The description of the policy.
    description: Optional[str] = None
    # The display name of the policy.
    display_name: Optional[str] = None
    # The expiration date for assignments created in this policy.
    expiration: Optional[ExpirationPattern] = None
    # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    modified_date_time: Optional[datetime.datetime] = None
    # The notificationSettings property
    notification_settings: Optional[AccessPackageNotificationSettings] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Questions that are posed to the  requestor.
    questions: Optional[list[AccessPackageQuestion]] = None
    # Specifies the settings for approval of requests for an access package assignment through this policy. For example, if approval is required for new requests.
    request_approval_settings: Optional[AccessPackageAssignmentApprovalSettings] = None
    # Provides additional settings to select who can create a request for an access package assignment through this policy, and what they can include in their request.
    requestor_settings: Optional[AccessPackageAssignmentRequestorSettings] = None
    # Settings for access reviews of assignments through this policy.
    review_settings: Optional[AccessPackageAssignmentReviewSettings] = None
    # The principals that can be assigned access from an access package through this policy.
    specific_allowed_targets: Optional[list[SubjectSet]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AccessPackageAssignmentPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageAssignmentPolicy
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AccessPackageAssignmentPolicy()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .access_package import AccessPackage
        from .access_package_assignment_approval_settings import AccessPackageAssignmentApprovalSettings
        from .access_package_assignment_requestor_settings import AccessPackageAssignmentRequestorSettings
        from .access_package_assignment_review_settings import AccessPackageAssignmentReviewSettings
        from .access_package_automatic_request_settings import AccessPackageAutomaticRequestSettings
        from .access_package_catalog import AccessPackageCatalog
        from .access_package_notification_settings import AccessPackageNotificationSettings
        from .access_package_question import AccessPackageQuestion
        from .allowed_target_scope import AllowedTargetScope
        from .custom_extension_stage_setting import CustomExtensionStageSetting
        from .entity import Entity
        from .expiration_pattern import ExpirationPattern
        from .subject_set import SubjectSet

        from .access_package import AccessPackage
        from .access_package_assignment_approval_settings import AccessPackageAssignmentApprovalSettings
        from .access_package_assignment_requestor_settings import AccessPackageAssignmentRequestorSettings
        from .access_package_assignment_review_settings import AccessPackageAssignmentReviewSettings
        from .access_package_automatic_request_settings import AccessPackageAutomaticRequestSettings
        from .access_package_catalog import AccessPackageCatalog
        from .access_package_notification_settings import AccessPackageNotificationSettings
        from .access_package_question import AccessPackageQuestion
        from .allowed_target_scope import AllowedTargetScope
        from .custom_extension_stage_setting import CustomExtensionStageSetting
        from .entity import Entity
        from .expiration_pattern import ExpirationPattern
        from .subject_set import SubjectSet

        fields: dict[str, Callable[[Any], None]] = {
            "accessPackage": lambda n : setattr(self, 'access_package', n.get_object_value(AccessPackage)),
            "allowedTargetScope": lambda n : setattr(self, 'allowed_target_scope', n.get_enum_value(AllowedTargetScope)),
            "automaticRequestSettings": lambda n : setattr(self, 'automatic_request_settings', n.get_object_value(AccessPackageAutomaticRequestSettings)),
            "catalog": lambda n : setattr(self, 'catalog', n.get_object_value(AccessPackageCatalog)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "customExtensionStageSettings": lambda n : setattr(self, 'custom_extension_stage_settings', n.get_collection_of_object_values(CustomExtensionStageSetting)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "expiration": lambda n : setattr(self, 'expiration', n.get_object_value(ExpirationPattern)),
            "modifiedDateTime": lambda n : setattr(self, 'modified_date_time', n.get_datetime_value()),
            "notificationSettings": lambda n : setattr(self, 'notification_settings', n.get_object_value(AccessPackageNotificationSettings)),
            "questions": lambda n : setattr(self, 'questions', n.get_collection_of_object_values(AccessPackageQuestion)),
            "requestApprovalSettings": lambda n : setattr(self, 'request_approval_settings', n.get_object_value(AccessPackageAssignmentApprovalSettings)),
            "requestorSettings": lambda n : setattr(self, 'requestor_settings', n.get_object_value(AccessPackageAssignmentRequestorSettings)),
            "reviewSettings": lambda n : setattr(self, 'review_settings', n.get_object_value(AccessPackageAssignmentReviewSettings)),
            "specificAllowedTargets": lambda n : setattr(self, 'specific_allowed_targets', n.get_collection_of_object_values(SubjectSet)),
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
        writer.write_object_value("accessPackage", self.access_package)
        writer.write_enum_value("allowedTargetScope", self.allowed_target_scope)
        writer.write_object_value("automaticRequestSettings", self.automatic_request_settings)
        writer.write_object_value("catalog", self.catalog)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_collection_of_object_values("customExtensionStageSettings", self.custom_extension_stage_settings)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("expiration", self.expiration)
        writer.write_datetime_value("modifiedDateTime", self.modified_date_time)
        writer.write_object_value("notificationSettings", self.notification_settings)
        writer.write_collection_of_object_values("questions", self.questions)
        writer.write_object_value("requestApprovalSettings", self.request_approval_settings)
        writer.write_object_value("requestorSettings", self.requestor_settings)
        writer.write_object_value("reviewSettings", self.review_settings)
        writer.write_collection_of_object_values("specificAllowedTargets", self.specific_allowed_targets)
    

