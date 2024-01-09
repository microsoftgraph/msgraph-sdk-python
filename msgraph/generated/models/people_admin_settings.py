from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .profile_card_property import ProfileCardProperty
    from .pronouns_settings import PronounsSettings

from .entity import Entity

@dataclass
class PeopleAdminSettings(Entity):
    # The OdataType property
    odata_type: Optional[str] = None
    # Contains a collection of the properties an administrator has defined as visible on the Microsoft 365 profile card.
    profile_card_properties: Optional[List[ProfileCardProperty]] = None
    # Represents administrator settings that manage the support of pronouns in an organization.
    pronouns: Optional[PronounsSettings] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PeopleAdminSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PeopleAdminSettings
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return PeopleAdminSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .profile_card_property import ProfileCardProperty
        from .pronouns_settings import PronounsSettings

        from .entity import Entity
        from .profile_card_property import ProfileCardProperty
        from .pronouns_settings import PronounsSettings

        fields: Dict[str, Callable[[Any], None]] = {
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("profileCardProperties", self.profile_card_properties)
        writer.write_object_value("pronouns", self.pronouns)
    

