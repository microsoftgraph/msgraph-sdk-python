from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .formatted_content import FormattedContent
    from .intelligence_profile_country_or_region_of_origin import IntelligenceProfileCountryOrRegionOfOrigin
    from .intelligence_profile_indicator import IntelligenceProfileIndicator
    from .intelligence_profile_kind import IntelligenceProfileKind

from ..entity import Entity

@dataclass
class IntelligenceProfile(Entity, Parsable):
    # A list of commonly-known aliases for the threat intelligence included in the intelligenceProfile.
    aliases: Optional[list[str]] = None
    # The country/region of origin for the given actor or threat associated with this intelligenceProfile.
    countries_or_regions_of_origin: Optional[list[IntelligenceProfileCountryOrRegionOfOrigin]] = None
    # The description property
    description: Optional[FormattedContent] = None
    # The date and time when this intelligenceProfile was first active. The timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    first_active_date_time: Optional[datetime.datetime] = None
    # Includes an assemblage of high-fidelity network indicators of compromise.
    indicators: Optional[list[IntelligenceProfileIndicator]] = None
    # The kind property
    kind: Optional[IntelligenceProfileKind] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The summary property
    summary: Optional[FormattedContent] = None
    # Known targets related to this intelligenceProfile.
    targets: Optional[list[str]] = None
    # The title of this intelligenceProfile.
    title: Optional[str] = None
    # Formatted information featuring a description of the distinctive tactics, techniques, and procedures (TTP) of the group, followed by a list of all known custom, commodity, and publicly available implants used by the group.
    tradecraft: Optional[FormattedContent] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IntelligenceProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IntelligenceProfile
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return IntelligenceProfile()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .formatted_content import FormattedContent
        from .intelligence_profile_country_or_region_of_origin import IntelligenceProfileCountryOrRegionOfOrigin
        from .intelligence_profile_indicator import IntelligenceProfileIndicator
        from .intelligence_profile_kind import IntelligenceProfileKind

        from ..entity import Entity
        from .formatted_content import FormattedContent
        from .intelligence_profile_country_or_region_of_origin import IntelligenceProfileCountryOrRegionOfOrigin
        from .intelligence_profile_indicator import IntelligenceProfileIndicator
        from .intelligence_profile_kind import IntelligenceProfileKind

        fields: dict[str, Callable[[Any], None]] = {
            "aliases": lambda n : setattr(self, 'aliases', n.get_collection_of_primitive_values(str)),
            "countriesOrRegionsOfOrigin": lambda n : setattr(self, 'countries_or_regions_of_origin', n.get_collection_of_object_values(IntelligenceProfileCountryOrRegionOfOrigin)),
            "description": lambda n : setattr(self, 'description', n.get_object_value(FormattedContent)),
            "firstActiveDateTime": lambda n : setattr(self, 'first_active_date_time', n.get_datetime_value()),
            "indicators": lambda n : setattr(self, 'indicators', n.get_collection_of_object_values(IntelligenceProfileIndicator)),
            "kind": lambda n : setattr(self, 'kind', n.get_enum_value(IntelligenceProfileKind)),
            "summary": lambda n : setattr(self, 'summary', n.get_object_value(FormattedContent)),
            "targets": lambda n : setattr(self, 'targets', n.get_collection_of_primitive_values(str)),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
            "tradecraft": lambda n : setattr(self, 'tradecraft', n.get_object_value(FormattedContent)),
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
        writer.write_collection_of_primitive_values("aliases", self.aliases)
        writer.write_collection_of_object_values("countriesOrRegionsOfOrigin", self.countries_or_regions_of_origin)
        writer.write_object_value("description", self.description)
        writer.write_datetime_value("firstActiveDateTime", self.first_active_date_time)
        writer.write_collection_of_object_values("indicators", self.indicators)
        writer.write_enum_value("kind", self.kind)
        writer.write_object_value("summary", self.summary)
        writer.write_collection_of_primitive_values("targets", self.targets)
        writer.write_str_value("title", self.title)
        writer.write_object_value("tradecraft", self.tradecraft)
    

