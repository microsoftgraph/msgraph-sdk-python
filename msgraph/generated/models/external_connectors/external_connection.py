from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .activity_settings import ActivitySettings
    from .configuration import Configuration
    from .connection_operation import ConnectionOperation
    from .connection_state import ConnectionState
    from .external_group import ExternalGroup
    from .external_item import ExternalItem
    from .schema import Schema
    from .search_settings import SearchSettings

from ..entity import Entity

@dataclass
class ExternalConnection(Entity, Parsable):
    # Collects configurable settings related to activities involving connector content.
    activity_settings: Optional[ActivitySettings] = None
    # Specifies additional application IDs that are allowed to manage the connection and to index content in the connection. Optional.
    configuration: Optional[Configuration] = None
    # The Teams app ID. Optional.
    connector_id: Optional[str] = None
    # Description of the connection displayed in the Microsoft 365 admin center. Optional.
    description: Optional[str] = None
    # The groups property
    groups: Optional[list[ExternalGroup]] = None
    # The items property
    items: Optional[list[ExternalItem]] = None
    # The display name of the connection to be displayed in the Microsoft 365 admin center. Maximum length of 128 characters. Required.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The operations property
    operations: Optional[list[ConnectionOperation]] = None
    # The schema property
    schema: Optional[Schema] = None
    # The settings configuring the search experience for content in this connection, such as the display templates for search results.
    search_settings: Optional[SearchSettings] = None
    # Indicates the current state of the connection. The possible values are: draft, ready, obsolete, limitExceeded, unknownFutureValue.
    state: Optional[ConnectionState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ExternalConnection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ExternalConnection
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ExternalConnection()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .activity_settings import ActivitySettings
        from .configuration import Configuration
        from .connection_operation import ConnectionOperation
        from .connection_state import ConnectionState
        from .external_group import ExternalGroup
        from .external_item import ExternalItem
        from .schema import Schema
        from .search_settings import SearchSettings

        from ..entity import Entity
        from .activity_settings import ActivitySettings
        from .configuration import Configuration
        from .connection_operation import ConnectionOperation
        from .connection_state import ConnectionState
        from .external_group import ExternalGroup
        from .external_item import ExternalItem
        from .schema import Schema
        from .search_settings import SearchSettings

        fields: dict[str, Callable[[Any], None]] = {
            "activitySettings": lambda n : setattr(self, 'activity_settings', n.get_object_value(ActivitySettings)),
            "configuration": lambda n : setattr(self, 'configuration', n.get_object_value(Configuration)),
            "connectorId": lambda n : setattr(self, 'connector_id', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "groups": lambda n : setattr(self, 'groups', n.get_collection_of_object_values(ExternalGroup)),
            "items": lambda n : setattr(self, 'items', n.get_collection_of_object_values(ExternalItem)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "operations": lambda n : setattr(self, 'operations', n.get_collection_of_object_values(ConnectionOperation)),
            "schema": lambda n : setattr(self, 'schema', n.get_object_value(Schema)),
            "searchSettings": lambda n : setattr(self, 'search_settings', n.get_object_value(SearchSettings)),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(ConnectionState)),
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
        writer.write_object_value("activitySettings", self.activity_settings)
        writer.write_object_value("configuration", self.configuration)
        writer.write_str_value("connectorId", self.connector_id)
        writer.write_str_value("description", self.description)
        writer.write_collection_of_object_values("groups", self.groups)
        writer.write_collection_of_object_values("items", self.items)
        writer.write_str_value("name", self.name)
        writer.write_collection_of_object_values("operations", self.operations)
        writer.write_object_value("schema", self.schema)
        writer.write_object_value("searchSettings", self.search_settings)
    

