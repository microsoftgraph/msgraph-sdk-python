from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
team = lazy_import('msgraph.generated.models.team')

class TeamInfo(entity.Entity):
    """
    Provides operations to manage the collection of agreement entities.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new teamInfo and sets the default values.
        """
        super().__init__()
        # The name of the team.
        self._display_name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The team property
        self._team: Optional[team.Team] = None
        # The ID of the Azure Active Directory tenant.
        self._tenant_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamInfo
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TeamInfo()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The name of the team.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The name of the team.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "team": lambda n : setattr(self, 'team', n.get_object_value(team.Team)),
            "tenant_id": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("team", self.team)
        writer.write_str_value("tenantId", self.tenant_id)
    
    @property
    def team(self,) -> Optional[team.Team]:
        """
        Gets the team property value. The team property
        Returns: Optional[team.Team]
        """
        return self._team
    
    @team.setter
    def team(self,value: Optional[team.Team] = None) -> None:
        """
        Sets the team property value. The team property
        Args:
            value: Value to set for the team property.
        """
        self._team = value
    
    @property
    def tenant_id(self,) -> Optional[str]:
        """
        Gets the tenantId property value. The ID of the Azure Active Directory tenant.
        Returns: Optional[str]
        """
        return self._tenant_id
    
    @tenant_id.setter
    def tenant_id(self,value: Optional[str] = None) -> None:
        """
        Sets the tenantId property value. The ID of the Azure Active Directory tenant.
        Args:
            value: Value to set for the tenantId property.
        """
        self._tenant_id = value
    

