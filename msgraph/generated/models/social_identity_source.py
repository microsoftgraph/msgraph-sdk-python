from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .identity_source import IdentitySource
    from .social_identity_source_type import SocialIdentitySourceType

from .identity_source import IdentitySource

@dataclass
class SocialIdentitySource(IdentitySource):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.socialIdentitySource"
    # The displayName property
    display_name: Optional[str] = None
    # The socialIdentitySourceType property
    social_identity_source_type: Optional[SocialIdentitySourceType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SocialIdentitySource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SocialIdentitySource
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SocialIdentitySource()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .identity_source import IdentitySource
        from .social_identity_source_type import SocialIdentitySourceType

        from .identity_source import IdentitySource
        from .social_identity_source_type import SocialIdentitySourceType

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "socialIdentitySourceType": lambda n : setattr(self, 'social_identity_source_type', n.get_enum_value(SocialIdentitySourceType)),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("socialIdentitySourceType", self.social_identity_source_type)
    

