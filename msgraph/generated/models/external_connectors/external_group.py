from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, Union

from . import identity
from .. import entity

class ExternalGroup(entity.Entity):
    """
    Provides operations to manage the collection of externalConnection entities.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new externalGroup and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.externalConnectors.externalGroup"
        # The description of the external group. Optional.
        self._description: Optional[str] = None
        # The friendly name of the external group. Optional.
        self._display_name: Optional[str] = None
        # A member added to an externalGroup. You can add Azure Active Directory users, Azure Active Directory groups, or an externalGroup as members.
        self._members: Optional[List[identity.Identity]] = None

    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ExternalGroup:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ExternalGroup
        """
        if not parse_node:
            raise Exception("parse_node cannot be undefined")
        return ExternalGroup()

    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The description of the external group. Optional.
        Returns: Optional[str]
        """
        return self._description

    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The description of the external group. Optional.
        Args:
            value: Value to set for the description property.
        """
        self._description = value

    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The friendly name of the external group. Optional.
        Returns: Optional[str]
        """
        return self._display_name

    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The friendly name of the external group. Optional.
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
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "members": lambda n : setattr(self, 'members', n.get_collection_of_object_values(identity.Identity)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields

    @property
    def members(self,) -> Optional[List[identity.Identity]]:
        """
        Gets the members property value. A member added to an externalGroup. You can add Azure Active Directory users, Azure Active Directory groups, or an externalGroup as members.
        Returns: Optional[List[identity.Identity]]
        """
        return self._members

    @members.setter
    def members(self,value: Optional[List[identity.Identity]] = None) -> None:
        """
        Sets the members property value. A member added to an externalGroup. You can add Azure Active Directory users, Azure Active Directory groups, or an externalGroup as members.
        Args:
            value: Value to set for the members property.
        """
        self._members = value

    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("members", self.members)


