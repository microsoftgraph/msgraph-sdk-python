from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, teams_app

from . import entity

class AppCatalogs(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new AppCatalogs and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The teamsApps property
        self._teams_apps: Optional[List[teams_app.TeamsApp]] = None
    
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
    
    @property
    def teams_apps(self,) -> Optional[List[teams_app.TeamsApp]]:
        """
        Gets the teamsApps property value. The teamsApps property
        Returns: Optional[List[teams_app.TeamsApp]]
        """
        return self._teams_apps
    
    @teams_apps.setter
    def teams_apps(self,value: Optional[List[teams_app.TeamsApp]] = None) -> None:
        """
        Sets the teamsApps property value. The teamsApps property
        Args:
            value: Value to set for the teams_apps property.
        """
        self._teams_apps = value
    

