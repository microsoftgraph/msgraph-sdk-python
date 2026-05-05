from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .artifact_restore_status import ArtifactRestoreStatus
    from .entity import Entity
    from .granular_drive_restore_artifact import GranularDriveRestoreArtifact
    from .granular_site_restore_artifact import GranularSiteRestoreArtifact

from .entity import Entity

@dataclass
class GranularRestoreArtifactBase(Entity, Parsable):
    # The browseSessionId property
    browse_session_id: Optional[str] = None
    # The completionDateTime property
    completion_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The restorePointDateTime property
    restore_point_date_time: Optional[datetime.datetime] = None
    # The restoredItemKey property
    restored_item_key: Optional[str] = None
    # The restoredItemPath property
    restored_item_path: Optional[str] = None
    # The restoredItemWebUrl property
    restored_item_web_url: Optional[str] = None
    # The startDateTime property
    start_date_time: Optional[datetime.datetime] = None
    # The status property
    status: Optional[ArtifactRestoreStatus] = None
    # The webUrl property
    web_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> GranularRestoreArtifactBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GranularRestoreArtifactBase
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.granularDriveRestoreArtifact".casefold():
            from .granular_drive_restore_artifact import GranularDriveRestoreArtifact

            return GranularDriveRestoreArtifact()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.granularSiteRestoreArtifact".casefold():
            from .granular_site_restore_artifact import GranularSiteRestoreArtifact

            return GranularSiteRestoreArtifact()
        return GranularRestoreArtifactBase()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .artifact_restore_status import ArtifactRestoreStatus
        from .entity import Entity
        from .granular_drive_restore_artifact import GranularDriveRestoreArtifact
        from .granular_site_restore_artifact import GranularSiteRestoreArtifact

        from .artifact_restore_status import ArtifactRestoreStatus
        from .entity import Entity
        from .granular_drive_restore_artifact import GranularDriveRestoreArtifact
        from .granular_site_restore_artifact import GranularSiteRestoreArtifact

        fields: dict[str, Callable[[Any], None]] = {
            "browseSessionId": lambda n : setattr(self, 'browse_session_id', n.get_str_value()),
            "completionDateTime": lambda n : setattr(self, 'completion_date_time', n.get_datetime_value()),
            "restorePointDateTime": lambda n : setattr(self, 'restore_point_date_time', n.get_datetime_value()),
            "restoredItemKey": lambda n : setattr(self, 'restored_item_key', n.get_str_value()),
            "restoredItemPath": lambda n : setattr(self, 'restored_item_path', n.get_str_value()),
            "restoredItemWebUrl": lambda n : setattr(self, 'restored_item_web_url', n.get_str_value()),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(ArtifactRestoreStatus)),
            "webUrl": lambda n : setattr(self, 'web_url', n.get_str_value()),
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
        writer.write_str_value("browseSessionId", self.browse_session_id)
        writer.write_datetime_value("completionDateTime", self.completion_date_time)
        writer.write_datetime_value("restorePointDateTime", self.restore_point_date_time)
        writer.write_str_value("restoredItemKey", self.restored_item_key)
        writer.write_str_value("restoredItemPath", self.restored_item_path)
        writer.write_str_value("restoredItemWebUrl", self.restored_item_web_url)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("webUrl", self.web_url)
    

