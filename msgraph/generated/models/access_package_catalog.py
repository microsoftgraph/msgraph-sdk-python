from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import access_package, access_package_catalog_state, access_package_catalog_type, entity

from . import entity

@dataclass
class AccessPackageCatalog(entity.Entity):
    # The access packages in this catalog. Read-only. Nullable.
    access_packages: Optional[List[access_package.AccessPackage]] = None
    # Whether the catalog is created by a user or entitlement management. The possible values are: userManaged, serviceDefault, serviceManaged, unknownFutureValue.
    catalog_type: Optional[access_package_catalog_type.AccessPackageCatalogType] = None
    # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
    created_date_time: Optional[datetime] = None
    # The description of the access package catalog.
    description: Optional[str] = None
    # The display name of the access package catalog.
    display_name: Optional[str] = None
    # Whether the access packages in this catalog can be requested by users outside of the tenant.
    is_externally_visible: Optional[bool] = None
    # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
    modified_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Has the value published if the access packages are available for management. The possible values are: unpublished, published, unknownFutureValue.
    state: Optional[access_package_catalog_state.AccessPackageCatalogState] = None
    
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
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import access_package, access_package_catalog_state, access_package_catalog_type, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "accessPackages": lambda n : setattr(self, 'access_packages', n.get_collection_of_object_values(access_package.AccessPackage)),
            "catalogType": lambda n : setattr(self, 'catalog_type', n.get_enum_value(access_package_catalog_type.AccessPackageCatalogType)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "isExternallyVisible": lambda n : setattr(self, 'is_externally_visible', n.get_bool_value()),
            "modifiedDateTime": lambda n : setattr(self, 'modified_date_time', n.get_datetime_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(access_package_catalog_state.AccessPackageCatalogState)),
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
        writer.write_collection_of_object_values("accessPackages", self.access_packages)
        writer.write_enum_value("catalogType", self.catalog_type)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("isExternallyVisible", self.is_externally_visible)
        writer.write_datetime_value("modifiedDateTime", self.modified_date_time)
        writer.write_enum_value("state", self.state)
    

