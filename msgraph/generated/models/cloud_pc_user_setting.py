from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_pc_restore_point_setting import CloudPcRestorePointSetting
    from .cloud_pc_user_setting_assignment import CloudPcUserSettingAssignment
    from .entity import Entity

from .entity import Entity

@dataclass
class CloudPcUserSetting(Entity):
    # The assignments property
    assignments: Optional[List[CloudPcUserSettingAssignment]] = None
    # The createdDateTime property
    created_date_time: Optional[datetime.datetime] = None
    # The displayName property
    display_name: Optional[str] = None
    # The lastModifiedDateTime property
    last_modified_date_time: Optional[datetime.datetime] = None
    # The localAdminEnabled property
    local_admin_enabled: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The resetEnabled property
    reset_enabled: Optional[bool] = None
    # The restorePointSetting property
    restore_point_setting: Optional[CloudPcRestorePointSetting] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CloudPcUserSetting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcUserSetting
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return CloudPcUserSetting()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_pc_restore_point_setting import CloudPcRestorePointSetting
        from .cloud_pc_user_setting_assignment import CloudPcUserSettingAssignment
        from .entity import Entity

        from .cloud_pc_restore_point_setting import CloudPcRestorePointSetting
        from .cloud_pc_user_setting_assignment import CloudPcUserSettingAssignment
        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(CloudPcUserSettingAssignment)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "localAdminEnabled": lambda n : setattr(self, 'local_admin_enabled', n.get_bool_value()),
            "resetEnabled": lambda n : setattr(self, 'reset_enabled', n.get_bool_value()),
            "restorePointSetting": lambda n : setattr(self, 'restore_point_setting', n.get_object_value(CloudPcRestorePointSetting)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_bool_value("localAdminEnabled", self.local_admin_enabled)
        writer.write_bool_value("resetEnabled", self.reset_enabled)
        writer.write_object_value("restorePointSetting", self.restore_point_setting)
    

