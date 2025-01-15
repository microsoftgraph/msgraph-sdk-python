from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ......models.clonable_team_parts import ClonableTeamParts
    from ......models.team_visibility_type import TeamVisibilityType

@dataclass
class ClonePostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The classification property
    classification: Optional[str] = None
    # The description property
    description: Optional[str] = None
    # The displayName property
    display_name: Optional[str] = None
    # The mailNickname property
    mail_nickname: Optional[str] = None
    # The partsToClone property
    parts_to_clone: Optional[ClonableTeamParts] = None
    # The visibility property
    visibility: Optional[TeamVisibilityType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ClonePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ClonePostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ClonePostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ......models.clonable_team_parts import ClonableTeamParts
        from ......models.team_visibility_type import TeamVisibilityType

        from ......models.clonable_team_parts import ClonableTeamParts
        from ......models.team_visibility_type import TeamVisibilityType

        fields: dict[str, Callable[[Any], None]] = {
            "classification": lambda n : setattr(self, 'classification', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "mailNickname": lambda n : setattr(self, 'mail_nickname', n.get_str_value()),
            "partsToClone": lambda n : setattr(self, 'parts_to_clone', n.get_collection_of_enum_values(ClonableTeamParts)),
            "visibility": lambda n : setattr(self, 'visibility', n.get_enum_value(TeamVisibilityType)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("classification", self.classification)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("mailNickname", self.mail_nickname)
        writer.write_enum_value("partsToClone", self.parts_to_clone)
        writer.write_enum_value("visibility", self.visibility)
        writer.write_additional_data_value(self.additional_data)
    

