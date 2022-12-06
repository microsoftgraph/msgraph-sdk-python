from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

access_package = lazy_import('msgraph.generated.models.access_package')
access_package_catalog_state = lazy_import('msgraph.generated.models.access_package_catalog_state')
access_package_catalog_type = lazy_import('msgraph.generated.models.access_package_catalog_type')
entity = lazy_import('msgraph.generated.models.entity')

class AccessPackageCatalog(entity.Entity):
    @property
    def access_packages(self,) -> Optional[List[access_package.AccessPackage]]:
        """
        Gets the accessPackages property value. The access packages in this catalog. Read-only. Nullable.
        Returns: Optional[List[access_package.AccessPackage]]
        """
        return self._access_packages
    
    @access_packages.setter
    def access_packages(self,value: Optional[List[access_package.AccessPackage]] = None) -> None:
        """
        Sets the accessPackages property value. The access packages in this catalog. Read-only. Nullable.
        Args:
            value: Value to set for the accessPackages property.
        """
        self._access_packages = value
    
    @property
    def catalog_type(self,) -> Optional[access_package_catalog_type.AccessPackageCatalogType]:
        """
        Gets the catalogType property value. Whether the catalog is created by a user or entitlement management. The possible values are: userManaged, serviceDefault, serviceManaged, unknownFutureValue.
        Returns: Optional[access_package_catalog_type.AccessPackageCatalogType]
        """
        return self._catalog_type
    
    @catalog_type.setter
    def catalog_type(self,value: Optional[access_package_catalog_type.AccessPackageCatalogType] = None) -> None:
        """
        Sets the catalogType property value. Whether the catalog is created by a user or entitlement management. The possible values are: userManaged, serviceDefault, serviceManaged, unknownFutureValue.
        Args:
            value: Value to set for the catalogType property.
        """
        self._catalog_type = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new accessPackageCatalog and sets the default values.
        """
        super().__init__()
        # The access packages in this catalog. Read-only. Nullable.
        self._access_packages: Optional[List[access_package.AccessPackage]] = None
        # Whether the catalog is created by a user or entitlement management. The possible values are: userManaged, serviceDefault, serviceManaged, unknownFutureValue.
        self._catalog_type: Optional[access_package_catalog_type.AccessPackageCatalogType] = None
        # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
        self._created_date_time: Optional[datetime] = None
        # The description of the access package catalog.
        self._description: Optional[str] = None
        # The display name of the access package catalog.
        self._display_name: Optional[str] = None
        # Whether the access packages in this catalog can be requested by users outside of the tenant.
        self._is_externally_visible: Optional[bool] = None
        # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
        self._modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Has the value published if the access packages are available for management. The possible values are: unpublished, published, unknownFutureValue.
        self._state: Optional[access_package_catalog_state.AccessPackageCatalogState] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessPackageCatalog:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageCatalog
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AccessPackageCatalog()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The description of the access package catalog.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The description of the access package catalog.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name of the access package catalog.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name of the access package catalog.
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
            "access_packages": lambda n : setattr(self, 'access_packages', n.get_collection_of_object_values(access_package.AccessPackage)),
            "catalog_type": lambda n : setattr(self, 'catalog_type', n.get_enum_value(access_package_catalog_type.AccessPackageCatalogType)),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "is_externally_visible": lambda n : setattr(self, 'is_externally_visible', n.get_bool_value()),
            "modified_date_time": lambda n : setattr(self, 'modified_date_time', n.get_datetime_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(access_package_catalog_state.AccessPackageCatalogState)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_externally_visible(self,) -> Optional[bool]:
        """
        Gets the isExternallyVisible property value. Whether the access packages in this catalog can be requested by users outside of the tenant.
        Returns: Optional[bool]
        """
        return self._is_externally_visible
    
    @is_externally_visible.setter
    def is_externally_visible(self,value: Optional[bool] = None) -> None:
        """
        Sets the isExternallyVisible property value. Whether the access packages in this catalog can be requested by users outside of the tenant.
        Args:
            value: Value to set for the isExternallyVisible property.
        """
        self._is_externally_visible = value
    
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
        writer.write_collection_of_object_values("accessPackages", self.access_packages)
        writer.write_enum_value("catalogType", self.catalog_type)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("isExternallyVisible", self.is_externally_visible)
        writer.write_datetime_value("modifiedDateTime", self.modified_date_time)
        writer.write_enum_value("state", self.state)
    
    @property
    def state(self,) -> Optional[access_package_catalog_state.AccessPackageCatalogState]:
        """
        Gets the state property value. Has the value published if the access packages are available for management. The possible values are: unpublished, published, unknownFutureValue.
        Returns: Optional[access_package_catalog_state.AccessPackageCatalogState]
        """
        return self._state
    
    @state.setter
    def state(self,value: Optional[access_package_catalog_state.AccessPackageCatalogState] = None) -> None:
        """
        Sets the state property value. Has the value published if the access packages are available for management. The possible values are: unpublished, published, unknownFutureValue.
        Args:
            value: Value to set for the state property.
        """
        self._state = value
    

