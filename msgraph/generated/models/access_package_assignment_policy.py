from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

access_package = lazy_import('msgraph.generated.models.access_package')
access_package_assignment_approval_settings = lazy_import('msgraph.generated.models.access_package_assignment_approval_settings')
access_package_assignment_requestor_settings = lazy_import('msgraph.generated.models.access_package_assignment_requestor_settings')
access_package_assignment_review_settings = lazy_import('msgraph.generated.models.access_package_assignment_review_settings')
access_package_automatic_request_settings = lazy_import('msgraph.generated.models.access_package_automatic_request_settings')
access_package_catalog = lazy_import('msgraph.generated.models.access_package_catalog')
allowed_target_scope = lazy_import('msgraph.generated.models.allowed_target_scope')
entity = lazy_import('msgraph.generated.models.entity')
expiration_pattern = lazy_import('msgraph.generated.models.expiration_pattern')
subject_set = lazy_import('msgraph.generated.models.subject_set')

class AccessPackageAssignmentPolicy(entity.Entity):
    """
    Provides operations to manage the collection of agreement entities.
    """
    @property
    def access_package(self,) -> Optional[access_package.AccessPackage]:
        """
        Gets the accessPackage property value. Access package containing this policy. Read-only.
        Returns: Optional[access_package.AccessPackage]
        """
        return self._access_package
    
    @access_package.setter
    def access_package(self,value: Optional[access_package.AccessPackage] = None) -> None:
        """
        Sets the accessPackage property value. Access package containing this policy. Read-only.
        Args:
            value: Value to set for the accessPackage property.
        """
        self._access_package = value
    
    @property
    def allowed_target_scope(self,) -> Optional[allowed_target_scope.AllowedTargetScope]:
        """
        Gets the allowedTargetScope property value. Principals that can be assigned the access package through this policy. The possible values are: notSpecified, specificDirectoryUsers, specificConnectedOrganizationUsers, specificDirectoryServicePrincipals, allMemberUsers, allDirectoryUsers, allDirectoryServicePrincipals, allConfiguredConnectedOrganizationUsers, allExternalUsers, unknownFutureValue.
        Returns: Optional[allowed_target_scope.AllowedTargetScope]
        """
        return self._allowed_target_scope
    
    @allowed_target_scope.setter
    def allowed_target_scope(self,value: Optional[allowed_target_scope.AllowedTargetScope] = None) -> None:
        """
        Sets the allowedTargetScope property value. Principals that can be assigned the access package through this policy. The possible values are: notSpecified, specificDirectoryUsers, specificConnectedOrganizationUsers, specificDirectoryServicePrincipals, allMemberUsers, allDirectoryUsers, allDirectoryServicePrincipals, allConfiguredConnectedOrganizationUsers, allExternalUsers, unknownFutureValue.
        Args:
            value: Value to set for the allowedTargetScope property.
        """
        self._allowed_target_scope = value
    
    @property
    def automatic_request_settings(self,) -> Optional[access_package_automatic_request_settings.AccessPackageAutomaticRequestSettings]:
        """
        Gets the automaticRequestSettings property value. This property is only present for an auto assignment policy; if absent, this is a request-based policy.
        Returns: Optional[access_package_automatic_request_settings.AccessPackageAutomaticRequestSettings]
        """
        return self._automatic_request_settings
    
    @automatic_request_settings.setter
    def automatic_request_settings(self,value: Optional[access_package_automatic_request_settings.AccessPackageAutomaticRequestSettings] = None) -> None:
        """
        Sets the automaticRequestSettings property value. This property is only present for an auto assignment policy; if absent, this is a request-based policy.
        Args:
            value: Value to set for the automaticRequestSettings property.
        """
        self._automatic_request_settings = value
    
    @property
    def catalog(self,) -> Optional[access_package_catalog.AccessPackageCatalog]:
        """
        Gets the catalog property value. Catalog of the access package containing this policy. Read-only.
        Returns: Optional[access_package_catalog.AccessPackageCatalog]
        """
        return self._catalog
    
    @catalog.setter
    def catalog(self,value: Optional[access_package_catalog.AccessPackageCatalog] = None) -> None:
        """
        Sets the catalog property value. Catalog of the access package containing this policy. Read-only.
        Args:
            value: Value to set for the catalog property.
        """
        self._catalog = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new accessPackageAssignmentPolicy and sets the default values.
        """
        super().__init__()
        # Access package containing this policy. Read-only.
        self._access_package: Optional[access_package.AccessPackage] = None
        # Principals that can be assigned the access package through this policy. The possible values are: notSpecified, specificDirectoryUsers, specificConnectedOrganizationUsers, specificDirectoryServicePrincipals, allMemberUsers, allDirectoryUsers, allDirectoryServicePrincipals, allConfiguredConnectedOrganizationUsers, allExternalUsers, unknownFutureValue.
        self._allowed_target_scope: Optional[allowed_target_scope.AllowedTargetScope] = None
        # This property is only present for an auto assignment policy; if absent, this is a request-based policy.
        self._automatic_request_settings: Optional[access_package_automatic_request_settings.AccessPackageAutomaticRequestSettings] = None
        # Catalog of the access package containing this policy. Read-only.
        self._catalog: Optional[access_package_catalog.AccessPackageCatalog] = None
        # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        self._created_date_time: Optional[datetime] = None
        # The description of the policy.
        self._description: Optional[str] = None
        # The display name of the policy.
        self._display_name: Optional[str] = None
        # The expiration date for assignments created in this policy.
        self._expiration: Optional[expiration_pattern.ExpirationPattern] = None
        # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        self._modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Specifies the settings for approval of requests for an access package assignment through this policy. For example, if approval is required for new requests.
        self._request_approval_settings: Optional[access_package_assignment_approval_settings.AccessPackageAssignmentApprovalSettings] = None
        # Provides additional settings to select who can create a request for an access package assignment through this policy, and what they can include in their request.
        self._requestor_settings: Optional[access_package_assignment_requestor_settings.AccessPackageAssignmentRequestorSettings] = None
        # Settings for access reviews of assignments through this policy.
        self._review_settings: Optional[access_package_assignment_review_settings.AccessPackageAssignmentReviewSettings] = None
        # The principals that can be assigned access from an access package through this policy.
        self._specific_allowed_targets: Optional[List[subject_set.SubjectSet]] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
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
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The description of the policy.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The description of the policy.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name of the policy.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name of the policy.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def expiration(self,) -> Optional[expiration_pattern.ExpirationPattern]:
        """
        Gets the expiration property value. The expiration date for assignments created in this policy.
        Returns: Optional[expiration_pattern.ExpirationPattern]
        """
        return self._expiration
    
    @expiration.setter
    def expiration(self,value: Optional[expiration_pattern.ExpirationPattern] = None) -> None:
        """
        Sets the expiration property value. The expiration date for assignments created in this policy.
        Args:
            value: Value to set for the expiration property.
        """
        self._expiration = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "access_package": lambda n : setattr(self, 'access_package', n.get_object_value(access_package.AccessPackage)),
            "allowed_target_scope": lambda n : setattr(self, 'allowed_target_scope', n.get_enum_value(allowed_target_scope.AllowedTargetScope)),
            "automatic_request_settings": lambda n : setattr(self, 'automatic_request_settings', n.get_object_value(access_package_automatic_request_settings.AccessPackageAutomaticRequestSettings)),
            "catalog": lambda n : setattr(self, 'catalog', n.get_object_value(access_package_catalog.AccessPackageCatalog)),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "expiration": lambda n : setattr(self, 'expiration', n.get_object_value(expiration_pattern.ExpirationPattern)),
            "modified_date_time": lambda n : setattr(self, 'modified_date_time', n.get_datetime_value()),
            "request_approval_settings": lambda n : setattr(self, 'request_approval_settings', n.get_object_value(access_package_assignment_approval_settings.AccessPackageAssignmentApprovalSettings)),
            "requestor_settings": lambda n : setattr(self, 'requestor_settings', n.get_object_value(access_package_assignment_requestor_settings.AccessPackageAssignmentRequestorSettings)),
            "review_settings": lambda n : setattr(self, 'review_settings', n.get_object_value(access_package_assignment_review_settings.AccessPackageAssignmentReviewSettings)),
            "specific_allowed_targets": lambda n : setattr(self, 'specific_allowed_targets', n.get_collection_of_object_values(subject_set.SubjectSet)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the modifiedDateTime property value. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._modified_date_time
    
    @modified_date_time.setter
    def modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the modifiedDateTime property value. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Args:
            value: Value to set for the modifiedDateTime property.
        """
        self._modified_date_time = value
    
    @property
    def request_approval_settings(self,) -> Optional[access_package_assignment_approval_settings.AccessPackageAssignmentApprovalSettings]:
        """
        Gets the requestApprovalSettings property value. Specifies the settings for approval of requests for an access package assignment through this policy. For example, if approval is required for new requests.
        Returns: Optional[access_package_assignment_approval_settings.AccessPackageAssignmentApprovalSettings]
        """
        return self._request_approval_settings
    
    @request_approval_settings.setter
    def request_approval_settings(self,value: Optional[access_package_assignment_approval_settings.AccessPackageAssignmentApprovalSettings] = None) -> None:
        """
        Sets the requestApprovalSettings property value. Specifies the settings for approval of requests for an access package assignment through this policy. For example, if approval is required for new requests.
        Args:
            value: Value to set for the requestApprovalSettings property.
        """
        self._request_approval_settings = value
    
    @property
    def requestor_settings(self,) -> Optional[access_package_assignment_requestor_settings.AccessPackageAssignmentRequestorSettings]:
        """
        Gets the requestorSettings property value. Provides additional settings to select who can create a request for an access package assignment through this policy, and what they can include in their request.
        Returns: Optional[access_package_assignment_requestor_settings.AccessPackageAssignmentRequestorSettings]
        """
        return self._requestor_settings
    
    @requestor_settings.setter
    def requestor_settings(self,value: Optional[access_package_assignment_requestor_settings.AccessPackageAssignmentRequestorSettings] = None) -> None:
        """
        Sets the requestorSettings property value. Provides additional settings to select who can create a request for an access package assignment through this policy, and what they can include in their request.
        Args:
            value: Value to set for the requestorSettings property.
        """
        self._requestor_settings = value
    
    @property
    def review_settings(self,) -> Optional[access_package_assignment_review_settings.AccessPackageAssignmentReviewSettings]:
        """
        Gets the reviewSettings property value. Settings for access reviews of assignments through this policy.
        Returns: Optional[access_package_assignment_review_settings.AccessPackageAssignmentReviewSettings]
        """
        return self._review_settings
    
    @review_settings.setter
    def review_settings(self,value: Optional[access_package_assignment_review_settings.AccessPackageAssignmentReviewSettings] = None) -> None:
        """
        Sets the reviewSettings property value. Settings for access reviews of assignments through this policy.
        Args:
            value: Value to set for the reviewSettings property.
        """
        self._review_settings = value
    
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
        writer.write_object_value("requestApprovalSettings", self.request_approval_settings)
        writer.write_object_value("requestorSettings", self.requestor_settings)
        writer.write_object_value("reviewSettings", self.review_settings)
        writer.write_collection_of_object_values("specificAllowedTargets", self.specific_allowed_targets)
    
    @property
    def specific_allowed_targets(self,) -> Optional[List[subject_set.SubjectSet]]:
        """
        Gets the specificAllowedTargets property value. The principals that can be assigned access from an access package through this policy.
        Returns: Optional[List[subject_set.SubjectSet]]
        """
        return self._specific_allowed_targets
    
    @specific_allowed_targets.setter
    def specific_allowed_targets(self,value: Optional[List[subject_set.SubjectSet]] = None) -> None:
        """
        Sets the specificAllowedTargets property value. The principals that can be assigned access from an access package through this policy.
        Args:
            value: Value to set for the specificAllowedTargets property.
        """
        self._specific_allowed_targets = value
    

