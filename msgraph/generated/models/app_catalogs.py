from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, teams_app

from . import entity

@dataclass
class AppCatalogs(entity.Entity):
    # The OdataType property
    odata_type: Optional[str] = None
    # The teamsApps property
    teams_apps: Optional[List[teams_app.TeamsApp]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AppCatalogs:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AppCatalogs
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AppCatalogs()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, teams_app

        fields: Dict[str, Callable[[Any], None]] = {
            "teamsApps": lambda n : setattr(self, 'teams_apps', n.get_collection_of_object_values(teams_app.TeamsApp)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("teamsApps", self.teams_apps)
    

