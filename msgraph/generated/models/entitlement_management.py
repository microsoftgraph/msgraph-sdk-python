from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import access_package, access_package_assignment, access_package_assignment_policy, access_package_assignment_request, access_package_catalog, approval, connected_organization, entitlement_management_settings, entity

from . import entity

@dataclass
class EntitlementManagement(entity.Entity):
    # Approval stages for decisions associated with access package assignment requests.
    access_package_assignment_approvals: Optional[List[approval.Approval]] = None
    # Access packages define the collection of resource roles and the policies for which subjects can request or be assigned access to those resources.
    access_packages: Optional[List[access_package.AccessPackage]] = None
    # Access package assignment policies govern which subjects can request or be assigned an access package via an access package assignment.
    assignment_policies: Optional[List[access_package_assignment_policy.AccessPackageAssignmentPolicy]] = None
    # Access package assignment requests created by or on behalf of a subject.
    assignment_requests: Optional[List[access_package_assignment_request.AccessPackageAssignmentRequest]] = None
    # The assignment of an access package to a subject for a period of time.
    assignments: Optional[List[access_package_assignment.AccessPackageAssignment]] = None
    # A container for access packages.
    catalogs: Optional[List[access_package_catalog.AccessPackageCatalog]] = None
    # References to a directory or domain of another organization whose users can request access.
    connected_organizations: Optional[List[connected_organization.ConnectedOrganization]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The settings that control the behavior of Azure AD entitlement management.
    settings: Optional[entitlement_management_settings.EntitlementManagementSettings] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EntitlementManagement:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EntitlementManagement
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return EntitlementManagement()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import access_package, access_package_assignment, access_package_assignment_policy, access_package_assignment_request, access_package_catalog, approval, connected_organization, entitlement_management_settings, entity

        from . import access_package, access_package_assignment, access_package_assignment_policy, access_package_assignment_request, access_package_catalog, approval, connected_organization, entitlement_management_settings, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "accessPackageAssignmentApprovals": lambda n : setattr(self, 'access_package_assignment_approvals', n.get_collection_of_object_values(approval.Approval)),
            "accessPackages": lambda n : setattr(self, 'access_packages', n.get_collection_of_object_values(access_package.AccessPackage)),
            "assignmentPolicies": lambda n : setattr(self, 'assignment_policies', n.get_collection_of_object_values(access_package_assignment_policy.AccessPackageAssignmentPolicy)),
            "assignmentRequests": lambda n : setattr(self, 'assignment_requests', n.get_collection_of_object_values(access_package_assignment_request.AccessPackageAssignmentRequest)),
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(access_package_assignment.AccessPackageAssignment)),
            "catalogs": lambda n : setattr(self, 'catalogs', n.get_collection_of_object_values(access_package_catalog.AccessPackageCatalog)),
            "connectedOrganizations": lambda n : setattr(self, 'connected_organizations', n.get_collection_of_object_values(connected_organization.ConnectedOrganization)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("accessPackageAssignmentApprovals", self.access_package_assignment_approvals)
        writer.write_collection_of_object_values("accessPackages", self.access_packages)
        writer.write_collection_of_object_values("assignmentPolicies", self.assignment_policies)
        writer.write_collection_of_object_values("assignmentRequests", self.assignment_requests)
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_collection_of_object_values("catalogs", self.catalogs)
        writer.write_collection_of_object_values("connectedOrganizations", self.connected_organizations)
        writer.write_object_value("settings", self.settings)
    

