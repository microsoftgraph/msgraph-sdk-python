from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import activity_settings, configuration, connection_operation, connection_state, external_group, external_item, schema, search_settings
    from .. import entity

from .. import entity

@dataclass
class ExternalConnection(entity.Entity):
    # Collects configurable settings related to activities involving connector content.
    activity_settings: Optional[activity_settings.ActivitySettings] = None
    # Specifies additional application IDs that are allowed to manage the connection and to index content in the connection. Optional.
    configuration: Optional[configuration.Configuration] = None
    # Description of the connection displayed in the Microsoft 365 admin center. Optional.
    description: Optional[str] = None
    # The groups property
    groups: Optional[List[external_group.ExternalGroup]] = None
    # The items property
    items: Optional[List[external_item.ExternalItem]] = None
    # The display name of the connection to be displayed in the Microsoft 365 admin center. Maximum length of 128 characters. Required.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The operations property
    operations: Optional[List[connection_operation.ConnectionOperation]] = None
    # The schema property
    schema: Optional[schema.Schema] = None
    # The settings configuring the search experience for content in this connection, such as the display templates for search results.
    search_settings: Optional[search_settings.SearchSettings] = None
    # Indicates the current state of the connection. Possible values are: draft, ready, obsolete, limitExceeded, unknownFutureValue.
    state: Optional[connection_state.ConnectionState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ExternalConnection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ExternalConnection
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ExternalConnection()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import activity_settings, configuration, connection_operation, connection_state, external_group, external_item, schema, search_settings
        from .. import entity

        from . import activity_settings, configuration, connection_operation, connection_state, external_group, external_item, schema, search_settings
        from .. import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "activitySettings": lambda n : setattr(self, 'activity_settings', n.get_object_value(activity_settings.ActivitySettings)),
            "configuration": lambda n : setattr(self, 'configuration', n.get_object_value(configuration.Configuration)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "groups": lambda n : setattr(self, 'groups', n.get_collection_of_object_values(external_group.ExternalGroup)),
            "items": lambda n : setattr(self, 'items', n.get_collection_of_object_values(external_item.ExternalItem)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "operations": lambda n : setattr(self, 'operations', n.get_collection_of_object_values(connection_operation.ConnectionOperation)),
            "schema": lambda n : setattr(self, 'schema', n.get_object_value(schema.Schema)),
            "searchSettings": lambda n : setattr(self, 'search_settings', n.get_object_value(search_settings.SearchSettings)),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(connection_state.ConnectionState)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_object_value("activitySettings", self.activity_settings)
        writer.write_object_value("configuration", self.configuration)
        writer.write_str_value("description", self.description)
        writer.write_collection_of_object_values("groups", self.groups)
        writer.write_collection_of_object_values("items", self.items)
        writer.write_str_value("name", self.name)
        writer.write_collection_of_object_values("operations", self.operations)
        writer.write_object_value("schema", self.schema)
        writer.write_object_value("searchSettings", self.search_settings)
    

