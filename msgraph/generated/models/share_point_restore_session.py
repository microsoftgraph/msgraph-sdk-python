from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .restore_session_base import RestoreSessionBase
    from .site_restore_artifact import SiteRestoreArtifact
    from .site_restore_artifacts_bulk_addition_request import SiteRestoreArtifactsBulkAdditionRequest

from .restore_session_base import RestoreSessionBase

@dataclass
class SharePointRestoreSession(RestoreSessionBase, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.sharePointRestoreSession"
    # A collection of restore points and destination details that can be used to restore SharePoint sites.
    site_restore_artifacts: Optional[list[SiteRestoreArtifact]] = None
    # A collection of SharePoint site URLs and destination details that can be used to restore SharePoint sites.
    site_restore_artifacts_bulk_addition_requests: Optional[list[SiteRestoreArtifactsBulkAdditionRequest]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SharePointRestoreSession:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SharePointRestoreSession
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SharePointRestoreSession()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .restore_session_base import RestoreSessionBase
        from .site_restore_artifact import SiteRestoreArtifact
        from .site_restore_artifacts_bulk_addition_request import SiteRestoreArtifactsBulkAdditionRequest

        from .restore_session_base import RestoreSessionBase
        from .site_restore_artifact import SiteRestoreArtifact
        from .site_restore_artifacts_bulk_addition_request import SiteRestoreArtifactsBulkAdditionRequest

        fields: dict[str, Callable[[Any], None]] = {
            "siteRestoreArtifacts": lambda n : setattr(self, 'site_restore_artifacts', n.get_collection_of_object_values(SiteRestoreArtifact)),
            "siteRestoreArtifactsBulkAdditionRequests": lambda n : setattr(self, 'site_restore_artifacts_bulk_addition_requests', n.get_collection_of_object_values(SiteRestoreArtifactsBulkAdditionRequest)),
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
        writer.write_collection_of_object_values("siteRestoreArtifacts", self.site_restore_artifacts)
        writer.write_collection_of_object_values("siteRestoreArtifactsBulkAdditionRequests", self.site_restore_artifacts_bulk_addition_requests)
    

