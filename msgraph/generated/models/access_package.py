from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

access_package_assignment_policy = lazy_import('msgraph.generated.models.access_package_assignment_policy')
access_package_catalog = lazy_import('msgraph.generated.models.access_package_catalog')
entity = lazy_import('msgraph.generated.models.entity')
group = lazy_import('msgraph.generated.models.group')

class AccessPackage(entity.Entity):
    """
    Provides operations to manage the collection of agreement entities.
    """
    @property
    def access_packages_incompatible_with(self,) -> Optional[List[AccessPackage]]:
        """
        Gets the accessPackagesIncompatibleWith property value. The access packages that are incompatible with this package. Read-only.
        Returns: Optional[List[AccessPackage]]
        """
        return self._access_packages_incompatible_with
    
    @access_packages_incompatible_with.setter
    def access_packages_incompatible_with(self,value: Optional[List[AccessPackage]] = None) -> None:
        """
        Sets the accessPackagesIncompatibleWith property value. The access packages that are incompatible with this package. Read-only.
        Args:
            value: Value to set for the accessPackagesIncompatibleWith property.
        """
        self._access_packages_incompatible_with = value
    
    @property
    def assignment_policies(self,) -> Optional[List[access_package_assignment_policy.AccessPackageAssignmentPolicy]]:
        """
        Gets the assignmentPolicies property value. The assignmentPolicies property
        Returns: Optional[List[access_package_assignment_policy.AccessPackageAssignmentPolicy]]
        """
        return self._assignment_policies
    
    @assignment_policies.setter
    def assignment_policies(self,value: Optional[List[access_package_assignment_policy.AccessPackageAssignmentPolicy]] = None) -> None:
        """
        Sets the assignmentPolicies property value. The assignmentPolicies property
        Args:
            value: Value to set for the assignmentPolicies property.
        """
        self._assignment_policies = value
    
    @property
    def catalog(self,) -> Optional[access_package_catalog.AccessPackageCatalog]:
        """
        Gets the catalog property value. The catalog property
        Returns: Optional[access_package_catalog.AccessPackageCatalog]
        """
        return self._catalog
    
    @catalog.setter
    def catalog(self,value: Optional[access_package_catalog.AccessPackageCatalog] = None) -> None:
        """
        Sets the catalog property value. The catalog property
        Args:
            value: Value to set for the catalog property.
        """
        self._catalog = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new accessPackage and sets the default values.
        """
        super().__init__()
        # The access packages that are incompatible with this package. Read-only.
        self._access_packages_incompatible_with: Optional[List[AccessPackage]] = None
        # The assignmentPolicies property
        self._assignment_policies: Optional[List[access_package_assignment_policy.AccessPackageAssignmentPolicy]] = None
        # The catalog property
        self._catalog: Optional[access_package_catalog.AccessPackageCatalog] = None
        # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
        self._created_date_time: Optional[datetime] = None
        # The description of the access package.
        self._description: Optional[str] = None
        # The display name of the access package. Supports $filter (eq, contains).
        self._display_name: Optional[str] = None
        # The access packages whose assigned users are ineligible to be assigned this access package.
        self._incompatible_access_packages: Optional[List[AccessPackage]] = None
        # The groups whose members are ineligible to be assigned this access package.
        self._incompatible_groups: Optional[List[group.Group]] = None
        # Whether the access package is hidden from the requestor.
        self._is_hidden: Optional[bool] = None
        # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
        self._modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessPackage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackage
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AccessPackage()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The description of the access package.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The description of the access package.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name of the access package. Supports $filter (eq, contains).
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name of the access package. Supports $filter (eq, contains).
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "access_packages_incompatible_with": lambda n : setattr(self, 'access_packages_incompatible_with', n.get_collection_of_object_values(AccessPackage)),
            "assignment_policies": lambda n : setattr(self, 'assignment_policies', n.get_collection_of_object_values(access_package_assignment_policy.AccessPackageAssignmentPolicy)),
            "catalog": lambda n : setattr(self, 'catalog', n.get_object_value(access_package_catalog.AccessPackageCatalog)),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "incompatible_access_packages": lambda n : setattr(self, 'incompatible_access_packages', n.get_collection_of_object_values(AccessPackage)),
            "incompatible_groups": lambda n : setattr(self, 'incompatible_groups', n.get_collection_of_object_values(group.Group)),
            "is_hidden": lambda n : setattr(self, 'is_hidden', n.get_bool_value()),
            "modified_date_time": lambda n : setattr(self, 'modified_date_time', n.get_datetime_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def incompatible_access_packages(self,) -> Optional[List[AccessPackage]]:
        """
        Gets the incompatibleAccessPackages property value. The access packages whose assigned users are ineligible to be assigned this access package.
        Returns: Optional[List[AccessPackage]]
        """
        return self._incompatible_access_packages
    
    @incompatible_access_packages.setter
    def incompatible_access_packages(self,value: Optional[List[AccessPackage]] = None) -> None:
        """
        Sets the incompatibleAccessPackages property value. The access packages whose assigned users are ineligible to be assigned this access package.
        Args:
            value: Value to set for the incompatibleAccessPackages property.
        """
        self._incompatible_access_packages = value
    
    @property
    def incompatible_groups(self,) -> Optional[List[group.Group]]:
        """
        Gets the incompatibleGroups property value. The groups whose members are ineligible to be assigned this access package.
        Returns: Optional[List[group.Group]]
        """
        return self._incompatible_groups
    
    @incompatible_groups.setter
    def incompatible_groups(self,value: Optional[List[group.Group]] = None) -> None:
        """
        Sets the incompatibleGroups property value. The groups whose members are ineligible to be assigned this access package.
        Args:
            value: Value to set for the incompatibleGroups property.
        """
        self._incompatible_groups = value
    
    @property
    def is_hidden(self,) -> Optional[bool]:
        """
        Gets the isHidden property value. Whether the access package is hidden from the requestor.
        Returns: Optional[bool]
        """
        return self._is_hidden
    
    @is_hidden.setter
    def is_hidden(self,value: Optional[bool] = None) -> None:
        """
        Sets the isHidden property value. Whether the access package is hidden from the requestor.
        Args:
            value: Value to set for the isHidden property.
        """
        self._is_hidden = value
    
    @property
    def modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the modifiedDateTime property value. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
        Returns: Optional[datetime]
        """
        return self._modified_date_time
    
    @modified_date_time.setter
    def modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the modifiedDateTime property value. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
        Args:
            value: Value to set for the modifiedDateTime property.
        """
        self._modified_date_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("accessPackagesIncompatibleWith", self.access_packages_incompatible_with)
        writer.write_collection_of_object_values("assignmentPolicies", self.assignment_policies)
        writer.write_object_value("catalog", self.catalog)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("incompatibleAccessPackages", self.incompatible_access_packages)
        writer.write_collection_of_object_values("incompatibleGroups", self.incompatible_groups)
        writer.write_bool_value("isHidden", self.is_hidden)
        writer.write_datetime_value("modifiedDateTime", self.modified_date_time)
    

