from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..device_platform_type import DevicePlatformType
    from .answer_keyword import AnswerKeyword
    from .answer_state import AnswerState
    from .answer_variant import AnswerVariant
    from .search_answer import SearchAnswer

from .search_answer import SearchAnswer

@dataclass
class Bookmark(SearchAnswer):
    # The availabilityEndDateTime property
    availability_end_date_time: Optional[datetime.datetime] = None
    # The availabilityStartDateTime property
    availability_start_date_time: Optional[datetime.datetime] = None
    # The categories property
    categories: Optional[List[str]] = None
    # The groupIds property
    group_ids: Optional[List[str]] = None
    # The isSuggested property
    is_suggested: Optional[bool] = None
    # The keywords property
    keywords: Optional[AnswerKeyword] = None
    # The languageTags property
    language_tags: Optional[List[str]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The platforms property
    platforms: Optional[List[DevicePlatformType]] = None
    # The powerAppIds property
    power_app_ids: Optional[List[str]] = None
    # The state property
    state: Optional[AnswerState] = None
    # The targetedVariations property
    targeted_variations: Optional[List[AnswerVariant]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Bookmark:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Bookmark
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Bookmark()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..device_platform_type import DevicePlatformType
        from .answer_keyword import AnswerKeyword
        from .answer_state import AnswerState
        from .answer_variant import AnswerVariant
        from .search_answer import SearchAnswer

        from ..device_platform_type import DevicePlatformType
        from .answer_keyword import AnswerKeyword
        from .answer_state import AnswerState
        from .answer_variant import AnswerVariant
        from .search_answer import SearchAnswer

        fields: Dict[str, Callable[[Any], None]] = {
            "availabilityEndDateTime": lambda n : setattr(self, 'availability_end_date_time', n.get_datetime_value()),
            "availabilityStartDateTime": lambda n : setattr(self, 'availability_start_date_time', n.get_datetime_value()),
            "categories": lambda n : setattr(self, 'categories', n.get_collection_of_primitive_values(str)),
            "groupIds": lambda n : setattr(self, 'group_ids', n.get_collection_of_primitive_values(str)),
            "isSuggested": lambda n : setattr(self, 'is_suggested', n.get_bool_value()),
            "keywords": lambda n : setattr(self, 'keywords', n.get_object_value(AnswerKeyword)),
            "languageTags": lambda n : setattr(self, 'language_tags', n.get_collection_of_primitive_values(str)),
            "platforms": lambda n : setattr(self, 'platforms', n.get_collection_of_enum_values(DevicePlatformType)),
            "powerAppIds": lambda n : setattr(self, 'power_app_ids', n.get_collection_of_primitive_values(str)),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(AnswerState)),
            "targetedVariations": lambda n : setattr(self, 'targeted_variations', n.get_collection_of_object_values(AnswerVariant)),
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
        writer.write_datetime_value("availabilityEndDateTime", self.availability_end_date_time)
        writer.write_datetime_value("availabilityStartDateTime", self.availability_start_date_time)
        writer.write_collection_of_primitive_values("categories", self.categories)
        writer.write_collection_of_primitive_values("groupIds", self.group_ids)
        writer.write_bool_value("isSuggested", self.is_suggested)
        writer.write_object_value("keywords", self.keywords)
        writer.write_collection_of_primitive_values("languageTags", self.language_tags)
        writer.write_collection_of_enum_values("platforms", self.platforms)
        writer.write_collection_of_primitive_values("powerAppIds", self.power_app_ids)
        writer.write_enum_value("state", self.state)
        writer.write_collection_of_object_values("targetedVariations", self.targeted_variations)
    

