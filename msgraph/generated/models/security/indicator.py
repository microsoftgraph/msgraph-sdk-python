from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .article_indicator import ArticleIndicator
    from .artifact import Artifact
    from .indicator_source import IndicatorSource
    from .intelligence_profile_indicator import IntelligenceProfileIndicator

from ..entity import Entity

@dataclass
class Indicator(Entity):
    # The artifact property
    artifact: Optional[Artifact] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The source property
    source: Optional[IndicatorSource] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Indicator:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Indicator
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.articleIndicator".casefold():
            from .article_indicator import ArticleIndicator

            return ArticleIndicator()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.intelligenceProfileIndicator".casefold():
            from .intelligence_profile_indicator import IntelligenceProfileIndicator

            return IntelligenceProfileIndicator()
        return Indicator()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .article_indicator import ArticleIndicator
        from .artifact import Artifact
        from .indicator_source import IndicatorSource
        from .intelligence_profile_indicator import IntelligenceProfileIndicator

        from ..entity import Entity
        from .article_indicator import ArticleIndicator
        from .artifact import Artifact
        from .indicator_source import IndicatorSource
        from .intelligence_profile_indicator import IntelligenceProfileIndicator

        fields: Dict[str, Callable[[Any], None]] = {
            "artifact": lambda n : setattr(self, 'artifact', n.get_object_value(Artifact)),
            "source": lambda n : setattr(self, 'source', n.get_enum_value(IndicatorSource)),
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
        writer.write_object_value("artifact", self.artifact)
        writer.write_enum_value("source", self.source)
    

