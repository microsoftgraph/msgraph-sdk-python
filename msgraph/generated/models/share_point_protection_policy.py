from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .protection_policy_base import ProtectionPolicyBase
    from .site_protection_rule import SiteProtectionRule
    from .site_protection_unit import SiteProtectionUnit
    from .site_protection_units_bulk_addition_job import SiteProtectionUnitsBulkAdditionJob

from .protection_policy_base import ProtectionPolicyBase

@dataclass
class SharePointProtectionPolicy(ProtectionPolicyBase, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.sharePointProtectionPolicy"
    # The rules associated with the SharePoint Protection policy.
    site_inclusion_rules: Optional[list[SiteProtectionRule]] = None
    # The protection units (sites) that are protected under the site protection policy.
    site_protection_units: Optional[list[SiteProtectionUnit]] = None
    # The siteProtectionUnitsBulkAdditionJobs property
    site_protection_units_bulk_addition_jobs: Optional[list[SiteProtectionUnitsBulkAdditionJob]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SharePointProtectionPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SharePointProtectionPolicy
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SharePointProtectionPolicy()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .protection_policy_base import ProtectionPolicyBase
        from .site_protection_rule import SiteProtectionRule
        from .site_protection_unit import SiteProtectionUnit
        from .site_protection_units_bulk_addition_job import SiteProtectionUnitsBulkAdditionJob

        from .protection_policy_base import ProtectionPolicyBase
        from .site_protection_rule import SiteProtectionRule
        from .site_protection_unit import SiteProtectionUnit
        from .site_protection_units_bulk_addition_job import SiteProtectionUnitsBulkAdditionJob

        fields: dict[str, Callable[[Any], None]] = {
            "siteInclusionRules": lambda n : setattr(self, 'site_inclusion_rules', n.get_collection_of_object_values(SiteProtectionRule)),
            "siteProtectionUnits": lambda n : setattr(self, 'site_protection_units', n.get_collection_of_object_values(SiteProtectionUnit)),
            "siteProtectionUnitsBulkAdditionJobs": lambda n : setattr(self, 'site_protection_units_bulk_addition_jobs', n.get_collection_of_object_values(SiteProtectionUnitsBulkAdditionJob)),
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
        writer.write_collection_of_object_values("siteInclusionRules", self.site_inclusion_rules)
        writer.write_collection_of_object_values("siteProtectionUnits", self.site_protection_units)
        writer.write_collection_of_object_values("siteProtectionUnitsBulkAdditionJobs", self.site_protection_units_bulk_addition_jobs)
    

