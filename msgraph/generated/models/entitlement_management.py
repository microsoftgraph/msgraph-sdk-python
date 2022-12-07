from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

access_package = lazy_import('msgraph.generated.models.access_package')
access_package_assignment = lazy_import('msgraph.generated.models.access_package_assignment')
access_package_assignment_policy = lazy_import('msgraph.generated.models.access_package_assignment_policy')
access_package_assignment_request = lazy_import('msgraph.generated.models.access_package_assignment_request')
access_package_catalog = lazy_import('msgraph.generated.models.access_package_catalog')
approval = lazy_import('msgraph.generated.models.approval')
connected_organization = lazy_import('msgraph.generated.models.connected_organization')
entitlement_management_settings = lazy_import('msgraph.generated.models.entitlement_management_settings')
entity = lazy_import('msgraph.generated.models.entity')

class EntitlementManagement(entity.Entity):
    @property
    def access_package_assignment_approvals(self,) -> Optional[List[approval.Approval]]:
        """
        Gets the accessPackageAssignmentApprovals property value. Approval stages for decisions associated with access package assignment requests.
        Returns: Optional[List[approval.Approval]]
        """
        return self._access_package_assignment_approvals
    
    @access_package_assignment_approvals.setter
    def access_package_assignment_approvals(self,value: Optional[List[approval.Approval]] = None) -> None:
        """
        Sets the accessPackageAssignmentApprovals property value. Approval stages for decisions associated with access package assignment requests.
        Args:
            value: Value to set for the accessPackageAssignmentApprovals property.
        """
        self._access_package_assignment_approvals = value
    
    @property
    def access_packages(self,) -> Optional[List[access_package.AccessPackage]]:
        """
        Gets the accessPackages property value. Access packages define the collection of resource roles and the policies for which subjects can request or be assigned access to those resources.
        Returns: Optional[List[access_package.AccessPackage]]
        """
        return self._access_packages
    
    @access_packages.setter
    def access_packages(self,value: Optional[List[access_package.AccessPackage]] = None) -> None:
        """
        Sets the accessPackages property value. Access packages define the collection of resource roles and the policies for which subjects can request or be assigned access to those resources.
        Args:
            value: Value to set for the accessPackages property.
        """
        self._access_packages = value
    
    @property
    def assignment_policies(self,) -> Optional[List[access_package_assignment_policy.AccessPackageAssignmentPolicy]]:
        """
        Gets the assignmentPolicies property value. Access package assignment policies govern which subjects can request or be assigned an access package via an access package assignment.
        Returns: Optional[List[access_package_assignment_policy.AccessPackageAssignmentPolicy]]
        """
        return self._assignment_policies
    
    @assignment_policies.setter
    def assignment_policies(self,value: Optional[List[access_package_assignment_policy.AccessPackageAssignmentPolicy]] = None) -> None:
        """
        Sets the assignmentPolicies property value. Access package assignment policies govern which subjects can request or be assigned an access package via an access package assignment.
        Args:
            value: Value to set for the assignmentPolicies property.
        """
        self._assignment_policies = value
    
    @property
    def assignment_requests(self,) -> Optional[List[access_package_assignment_request.AccessPackageAssignmentRequest]]:
        """
        Gets the assignmentRequests property value. Access package assignment requests created by or on behalf of a subject.
        Returns: Optional[List[access_package_assignment_request.AccessPackageAssignmentRequest]]
        """
        return self._assignment_requests
    
    @assignment_requests.setter
    def assignment_requests(self,value: Optional[List[access_package_assignment_request.AccessPackageAssignmentRequest]] = None) -> None:
        """
        Sets the assignmentRequests property value. Access package assignment requests created by or on behalf of a subject.
        Args:
            value: Value to set for the assignmentRequests property.
        """
        self._assignment_requests = value
    
    @property
    def assignments(self,) -> Optional[List[access_package_assignment.AccessPackageAssignment]]:
        """
        Gets the assignments property value. The assignment of an access package to a subject for a period of time.
        Returns: Optional[List[access_package_assignment.AccessPackageAssignment]]
        """
        return self._assignments
    
    @assignments.setter
    def assignments(self,value: Optional[List[access_package_assignment.AccessPackageAssignment]] = None) -> None:
        """
        Sets the assignments property value. The assignment of an access package to a subject for a period of time.
        Args:
            value: Value to set for the assignments property.
        """
        self._assignments = value
    
    @property
    def catalogs(self,) -> Optional[List[access_package_catalog.AccessPackageCatalog]]:
        """
        Gets the catalogs property value. A container for access packages.
        Returns: Optional[List[access_package_catalog.AccessPackageCatalog]]
        """
        return self._catalogs
    
    @catalogs.setter
    def catalogs(self,value: Optional[List[access_package_catalog.AccessPackageCatalog]] = None) -> None:
        """
        Sets the catalogs property value. A container for access packages.
        Args:
            value: Value to set for the catalogs property.
        """
        self._catalogs = value
    
    @property
    def connected_organizations(self,) -> Optional[List[connected_organization.ConnectedOrganization]]:
        """
        Gets the connectedOrganizations property value. References to a directory or domain of another organization whose users can request access.
        Returns: Optional[List[connected_organization.ConnectedOrganization]]
        """
        return self._connected_organizations
    
    @connected_organizations.setter
    def connected_organizations(self,value: Optional[List[connected_organization.ConnectedOrganization]] = None) -> None:
        """
        Sets the connectedOrganizations property value. References to a directory or domain of another organization whose users can request access.
        Args:
            value: Value to set for the connectedOrganizations property.
        """
        self._connected_organizations = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new EntitlementManagement and sets the default values.
        """
        super().__init__()
        # Approval stages for decisions associated with access package assignment requests.
        self._access_package_assignment_approvals: Optional[List[approval.Approval]] = None
        # Access packages define the collection of resource roles and the policies for which subjects can request or be assigned access to those resources.
        self._access_packages: Optional[List[access_package.AccessPackage]] = None
        # Access package assignment policies govern which subjects can request or be assigned an access package via an access package assignment.
        self._assignment_policies: Optional[List[access_package_assignment_policy.AccessPackageAssignmentPolicy]] = None
        # Access package assignment requests created by or on behalf of a subject.
        self._assignment_requests: Optional[List[access_package_assignment_request.AccessPackageAssignmentRequest]] = None
        # The assignment of an access package to a subject for a period of time.
        self._assignments: Optional[List[access_package_assignment.AccessPackageAssignment]] = None
        # A container for access packages.
        self._catalogs: Optional[List[access_package_catalog.AccessPackageCatalog]] = None
        # References to a directory or domain of another organization whose users can request access.
        self._connected_organizations: Optional[List[connected_organization.ConnectedOrganization]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The settings that control the behavior of Azure AD entitlement management.
        self._settings: Optional[entitlement_management_settings.EntitlementManagementSettings] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EntitlementManagement:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EntitlementManagement
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EntitlementManagement()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "access_package_assignment_approvals": lambda n : setattr(self, 'access_package_assignment_approvals', n.get_collection_of_object_values(approval.Approval)),
            "access_packages": lambda n : setattr(self, 'access_packages', n.get_collection_of_object_values(access_package.AccessPackage)),
            "assignment_policies": lambda n : setattr(self, 'assignment_policies', n.get_collection_of_object_values(access_package_assignment_policy.AccessPackageAssignmentPolicy)),
            "assignment_requests": lambda n : setattr(self, 'assignment_requests', n.get_collection_of_object_values(access_package_assignment_request.AccessPackageAssignmentRequest)),
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(access_package_assignment.AccessPackageAssignment)),
            "catalogs": lambda n : setattr(self, 'catalogs', n.get_collection_of_object_values(access_package_catalog.AccessPackageCatalog)),
            "connected_organizations": lambda n : setattr(self, 'connected_organizations', n.get_collection_of_object_values(connected_organization.ConnectedOrganization)),
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(entitlement_management_settings.EntitlementManagementSettings)),
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
        writer.write_collection_of_object_values("accessPackageAssignmentApprovals", self.access_package_assignment_approvals)
        writer.write_collection_of_object_values("accessPackages", self.access_packages)
        writer.write_collection_of_object_values("assignmentPolicies", self.assignment_policies)
        writer.write_collection_of_object_values("assignmentRequests", self.assignment_requests)
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_collection_of_object_values("catalogs", self.catalogs)
        writer.write_collection_of_object_values("connectedOrganizations", self.connected_organizations)
        writer.write_object_value("settings", self.settings)
    
    @property
    def settings(self,) -> Optional[entitlement_management_settings.EntitlementManagementSettings]:
        """
        Gets the settings property value. The settings that control the behavior of Azure AD entitlement management.
        Returns: Optional[entitlement_management_settings.EntitlementManagementSettings]
        """
        return self._settings
    
    @settings.setter
    def settings(self,value: Optional[entitlement_management_settings.EntitlementManagementSettings] = None) -> None:
        """
        Sets the settings property value. The settings that control the behavior of Azure AD entitlement management.
        Args:
            value: Value to set for the settings property.
        """
        self._settings = value
    

