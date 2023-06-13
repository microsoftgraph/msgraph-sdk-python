from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import access_package, access_package_assignment_approval_settings, access_package_assignment_requestor_settings, access_package_assignment_review_settings, access_package_automatic_request_settings, access_package_catalog, access_package_question, allowed_target_scope, entity, expiration_pattern, subject_set

from . import entity

@dataclass
class AccessPackageAssignmentPolicy(entity.Entity):
    # Access package containing this policy. Read-only.
    access_package: Optional[access_package.AccessPackage] = None
    # Principals that can be assigned the access package through this policy. The possible values are: notSpecified, specificDirectoryUsers, specificConnectedOrganizationUsers, specificDirectoryServicePrincipals, allMemberUsers, allDirectoryUsers, allDirectoryServicePrincipals, allConfiguredConnectedOrganizationUsers, allExternalUsers, unknownFutureValue.
    allowed_target_scope: Optional[allowed_target_scope.AllowedTargetScope] = None
    # This property is only present for an auto assignment policy; if absent, this is a request-based policy.
    automatic_request_settings: Optional[access_package_automatic_request_settings.AccessPackageAutomaticRequestSettings] = None
    # Catalog of the access package containing this policy. Read-only.
    catalog: Optional[access_package_catalog.AccessPackageCatalog] = None
    # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    created_date_time: Optional[datetime] = None
    # The description of the policy.
    description: Optional[str] = None
    # The display name of the policy.
    display_name: Optional[str] = None
    # The expiration date for assignments created in this policy.
    expiration: Optional[expiration_pattern.ExpirationPattern] = None
    # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    modified_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Questions that are posed to the  requestor.
    questions: Optional[List[access_package_question.AccessPackageQuestion]] = None
    # Specifies the settings for approval of requests for an access package assignment through this policy. For example, if approval is required for new requests.
    request_approval_settings: Optional[access_package_assignment_approval_settings.AccessPackageAssignmentApprovalSettings] = None
    # Provides additional settings to select who can create a request for an access package assignment through this policy, and what they can include in their request.
    requestor_settings: Optional[access_package_assignment_requestor_settings.AccessPackageAssignmentRequestorSettings] = None
    # Settings for access reviews of assignments through this policy.
    review_settings: Optional[access_package_assignment_review_settings.AccessPackageAssignmentReviewSettings] = None
    # The principals that can be assigned access from an access package through this policy.
    specific_allowed_targets: Optional[List[subject_set.SubjectSet]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessPackageAssignmentPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageAssignmentPolicy
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AccessPackageAssignmentPolicy()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import access_package, access_package_assignment_approval_settings, access_package_assignment_requestor_settings, access_package_assignment_review_settings, access_package_automatic_request_settings, access_package_catalog, access_package_question, allowed_target_scope, entity, expiration_pattern, subject_set

        fields: Dict[str, Callable[[Any], None]] = {
            "accessPackage": lambda n : setattr(self, 'access_package', n.get_object_value(access_package.AccessPackage)),
            "allowedTargetScope": lambda n : setattr(self, 'allowed_target_scope', n.get_enum_value(allowed_target_scope.AllowedTargetScope)),
            "automaticRequestSettings": lambda n : setattr(self, 'automatic_request_settings', n.get_object_value(access_package_automatic_request_settings.AccessPackageAutomaticRequestSettings)),
            "catalog": lambda n : setattr(self, 'catalog', n.get_object_value(access_package_catalog.AccessPackageCatalog)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "expiration": lambda n : setattr(self, 'expiration', n.get_object_value(expiration_pattern.ExpirationPattern)),
            "modifiedDateTime": lambda n : setattr(self, 'modified_date_time', n.get_datetime_value()),
            "questions": lambda n : setattr(self, 'questions', n.get_collection_of_object_values(access_package_question.AccessPackageQuestion)),
            "requestorSettings": lambda n : setattr(self, 'requestor_settings', n.get_object_value(access_package_assignment_requestor_settings.AccessPackageAssignmentRequestorSettings)),
            "requestApprovalSettings": lambda n : setattr(self, 'request_approval_settings', n.get_object_value(access_package_assignment_approval_settings.AccessPackageAssignmentApprovalSettings)),
            "reviewSettings": lambda n : setattr(self, 'review_settings', n.get_object_value(access_package_assignment_review_settings.AccessPackageAssignmentReviewSettings)),
            "specificAllowedTargets": lambda n : setattr(self, 'specific_allowed_targets', n.get_collection_of_object_values(subject_set.SubjectSet)),
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
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("accessPackage", self.access_package)
        writer.write_enum_value("allowedTargetScope", self.allowed_target_scope)
        writer.write_object_value("automaticRequestSettings", self.automatic_request_settings)
        writer.write_object_value("catalog", self.catalog)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("expiration", self.expiration)
        writer.write_datetime_value("modifiedDateTime", self.modified_date_time)
        writer.write_collection_of_object_values("questions", self.questions)
        writer.write_object_value("requestorSettings", self.requestor_settings)
        writer.write_object_value("requestApprovalSettings", self.request_approval_settings)
        writer.write_object_value("reviewSettings", self.review_settings)
        writer.write_collection_of_object_values("specificAllowedTargets", self.specific_allowed_targets)
    

