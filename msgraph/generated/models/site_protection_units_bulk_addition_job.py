from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .protection_units_bulk_job_base import ProtectionUnitsBulkJobBase

from .protection_units_bulk_job_base import ProtectionUnitsBulkJobBase

@dataclass
class SiteProtectionUnitsBulkAdditionJob(ProtectionUnitsBulkJobBase, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.siteProtectionUnitsBulkAdditionJob"
    # The list of SharePoint site IDs to add to the SharePoint protection policy.
    site_ids: Optional[list[str]] = None
    # The list of SharePoint site URLs to add to the SharePoint protection policy.
    site_web_urls: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SiteProtectionUnitsBulkAdditionJob:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SiteProtectionUnitsBulkAdditionJob
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SiteProtectionUnitsBulkAdditionJob()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .protection_units_bulk_job_base import ProtectionUnitsBulkJobBase

        from .protection_units_bulk_job_base import ProtectionUnitsBulkJobBase

        fields: dict[str, Callable[[Any], None]] = {
            "siteIds": lambda n : setattr(self, 'site_ids', n.get_collection_of_primitive_values(str)),
            "siteWebUrls": lambda n : setattr(self, 'site_web_urls', n.get_collection_of_primitive_values(str)),
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
        writer.write_collection_of_primitive_values("siteIds", self.site_ids)
        writer.write_collection_of_primitive_values("siteWebUrls", self.site_web_urls)
    

