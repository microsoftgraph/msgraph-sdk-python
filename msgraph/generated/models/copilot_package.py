from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .copilot_package_detail import CopilotPackageDetail
    from .entity import Entity
    from .package_status import PackageStatus
    from .package_type import PackageType

from .entity import Entity

@dataclass
class CopilotPackage(Entity, Parsable):
    # The appId property
    app_id: Optional[str] = None
    # The assetId property
    asset_id: Optional[str] = None
    # The availableTo property
    available_to: Optional[PackageStatus] = None
    # The createdDateTime property
    created_date_time: Optional[datetime.datetime] = None
    # The deployedTo property
    deployed_to: Optional[PackageStatus] = None
    # The displayName property
    display_name: Optional[str] = None
    # The elementTypes property
    element_types: Optional[list[str]] = None
    # The isBlocked property
    is_blocked: Optional[bool] = None
    # The lastModifiedDateTime property
    last_modified_date_time: Optional[datetime.datetime] = None
    # The manifestId property
    manifest_id: Optional[str] = None
    # The manifestVersion property
    manifest_version: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The ownerId property
    owner_id: Optional[str] = None
    # The platform property
    platform: Optional[str] = None
    # The publisher property
    publisher: Optional[str] = None
    # The shortDescription property
    short_description: Optional[str] = None
    # The supportedHosts property
    supported_hosts: Optional[list[str]] = None
    # The type property
    type: Optional[PackageType] = None
    # The version property
    version: Optional[str] = None
    # The zipFile property
    zip_file: Optional[bytes] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CopilotPackage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CopilotPackage
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.copilotPackageDetail".casefold():
            from .copilot_package_detail import CopilotPackageDetail

            return CopilotPackageDetail()
        return CopilotPackage()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .copilot_package_detail import CopilotPackageDetail
        from .entity import Entity
        from .package_status import PackageStatus
        from .package_type import PackageType

        from .copilot_package_detail import CopilotPackageDetail
        from .entity import Entity
        from .package_status import PackageStatus
        from .package_type import PackageType

        fields: dict[str, Callable[[Any], None]] = {
            "appId": lambda n : setattr(self, 'app_id', n.get_str_value()),
            "assetId": lambda n : setattr(self, 'asset_id', n.get_str_value()),
            "availableTo": lambda n : setattr(self, 'available_to', n.get_enum_value(PackageStatus)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "deployedTo": lambda n : setattr(self, 'deployed_to', n.get_enum_value(PackageStatus)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "elementTypes": lambda n : setattr(self, 'element_types', n.get_collection_of_primitive_values(str)),
            "isBlocked": lambda n : setattr(self, 'is_blocked', n.get_bool_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "manifestId": lambda n : setattr(self, 'manifest_id', n.get_str_value()),
            "manifestVersion": lambda n : setattr(self, 'manifest_version', n.get_str_value()),
            "ownerId": lambda n : setattr(self, 'owner_id', n.get_str_value()),
            "platform": lambda n : setattr(self, 'platform', n.get_str_value()),
            "publisher": lambda n : setattr(self, 'publisher', n.get_str_value()),
            "shortDescription": lambda n : setattr(self, 'short_description', n.get_str_value()),
            "supportedHosts": lambda n : setattr(self, 'supported_hosts', n.get_collection_of_primitive_values(str)),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(PackageType)),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
            "zipFile": lambda n : setattr(self, 'zip_file', n.get_bytes_value()),
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
        writer.write_str_value("appId", self.app_id)
        writer.write_str_value("assetId", self.asset_id)
        writer.write_enum_value("availableTo", self.available_to)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_enum_value("deployedTo", self.deployed_to)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_primitive_values("elementTypes", self.element_types)
        writer.write_bool_value("isBlocked", self.is_blocked)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("manifestId", self.manifest_id)
        writer.write_str_value("manifestVersion", self.manifest_version)
        writer.write_str_value("ownerId", self.owner_id)
        writer.write_str_value("platform", self.platform)
        writer.write_str_value("publisher", self.publisher)
        writer.write_str_value("shortDescription", self.short_description)
        writer.write_collection_of_primitive_values("supportedHosts", self.supported_hosts)
        writer.write_enum_value("type", self.type)
        writer.write_str_value("version", self.version)
        writer.write_bytes_value("zipFile", self.zip_file)
    

