from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .insights_settings import InsightsSettings
    from .profile_card_property import ProfileCardProperty
    from .pronouns_settings import PronounsSettings

from .entity import Entity

@dataclass
class PeopleAdminSettings(Entity, Parsable):
    # Represents administrator settings that manage the support for item insights in an organization.
    item_insights: Optional[InsightsSettings] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Contains a collection of the properties an administrator has defined as visible on the Microsoft 365 profile card.
    profile_card_properties: Optional[list[ProfileCardProperty]] = None
    # Represents administrator settings that manage the support of pronouns in an organization.
    pronouns: Optional[PronounsSettings] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PeopleAdminSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PeopleAdminSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PeopleAdminSettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .insights_settings import InsightsSettings
        from .profile_card_property import ProfileCardProperty
        from .pronouns_settings import PronounsSettings

        from .entity import Entity
        from .insights_settings import InsightsSettings
        from .profile_card_property import ProfileCardProperty
        from .pronouns_settings import PronounsSettings

        fields: dict[str, Callable[[Any], None]] = {
            "itemInsights": lambda n : setattr(self, 'item_insights', n.get_object_value(InsightsSettings)),
            "profileCardProperties": lambda n : setattr(self, 'profile_card_properties', n.get_collection_of_object_values(ProfileCardProperty)),
            "pronouns": lambda n : setattr(self, 'pronouns', n.get_object_value(PronounsSettings)),
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
        writer.write_object_value("itemInsights", self.item_insights)
        writer.write_collection_of_object_values("profileCardProperties", self.profile_card_properties)
        writer.write_object_value("pronouns", self.pronouns)
    

