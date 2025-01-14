from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .teams_app_definition import TeamsAppDefinition
    from .teams_app_distribution_method import TeamsAppDistributionMethod

from .entity import Entity

@dataclass
class TeamsApp(Entity, Parsable):
    # The details for each version of the app.
    app_definitions: Optional[list[TeamsAppDefinition]] = None
    # The name of the catalog app provided by the app developer in the Microsoft Teams zip app package.
    display_name: Optional[str] = None
    # The method of distribution for the app. Read-only.
    distribution_method: Optional[TeamsAppDistributionMethod] = None
    # The ID of the catalog provided by the app developer in the Microsoft Teams zip app package.
    external_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TeamsApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TeamsApp
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TeamsApp()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .teams_app_definition import TeamsAppDefinition
        from .teams_app_distribution_method import TeamsAppDistributionMethod

        from .entity import Entity
        from .teams_app_definition import TeamsAppDefinition
        from .teams_app_distribution_method import TeamsAppDistributionMethod

        fields: dict[str, Callable[[Any], None]] = {
            "appDefinitions": lambda n : setattr(self, 'app_definitions', n.get_collection_of_object_values(TeamsAppDefinition)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "distributionMethod": lambda n : setattr(self, 'distribution_method', n.get_enum_value(TeamsAppDistributionMethod)),
            "externalId": lambda n : setattr(self, 'external_id', n.get_str_value()),
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
        writer.write_collection_of_object_values("appDefinitions", self.app_definitions)
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("distributionMethod", self.distribution_method)
        writer.write_str_value("externalId", self.external_id)
    

