from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
configuration = lazy_import('msgraph.generated.models.external_connectors.configuration')
connection_operation = lazy_import('msgraph.generated.models.external_connectors.connection_operation')
connection_state = lazy_import('msgraph.generated.models.external_connectors.connection_state')
external_group = lazy_import('msgraph.generated.models.external_connectors.external_group')
external_item = lazy_import('msgraph.generated.models.external_connectors.external_item')
schema = lazy_import('msgraph.generated.models.external_connectors.schema')

class ExternalConnection(entity.Entity):
    """
    Provides operations to manage the collection of externalConnection entities.
    """
    @property
    def configuration(self,) -> Optional[configuration.Configuration]:
        """
        Gets the configuration property value. Specifies additional application IDs that are allowed to manage the connection and to index content in the connection. Optional.
        Returns: Optional[configuration.Configuration]
        """
        return self._configuration
    
    @configuration.setter
    def configuration(self,value: Optional[configuration.Configuration] = None) -> None:
        """
        Sets the configuration property value. Specifies additional application IDs that are allowed to manage the connection and to index content in the connection. Optional.
        Args:
            value: Value to set for the configuration property.
        """
        self._configuration = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new externalConnection and sets the default values.
        """
        super().__init__()
        # Specifies additional application IDs that are allowed to manage the connection and to index content in the connection. Optional.
        self._configuration: Optional[configuration.Configuration] = None
        # Description of the connection displayed in the Microsoft 365 admin center. Optional.
        self._description: Optional[str] = None
        # The groups property
        self._groups: Optional[List[external_group.ExternalGroup]] = None
        # The items property
        self._items: Optional[List[external_item.ExternalItem]] = None
        # The display name of the connection to be displayed in the Microsoft 365 admin center. Maximum length of 128 characters. Required.
        self._name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The operations property
        self._operations: Optional[List[connection_operation.ConnectionOperation]] = None
        # The schema property
        self._schema: Optional[schema.Schema] = None
        # Indicates the current state of the connection. Possible values are: draft, ready, obsolete, limitExceeded, unknownFutureValue.
        self._state: Optional[connection_state.ConnectionState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ExternalConnection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ExternalConnection
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ExternalConnection()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Description of the connection displayed in the Microsoft 365 admin center. Optional.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Description of the connection displayed in the Microsoft 365 admin center. Optional.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "configuration": lambda n : setattr(self, 'configuration', n.get_object_value(configuration.Configuration)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "groups": lambda n : setattr(self, 'groups', n.get_collection_of_object_values(external_group.ExternalGroup)),
            "items": lambda n : setattr(self, 'items', n.get_collection_of_object_values(external_item.ExternalItem)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "operations": lambda n : setattr(self, 'operations', n.get_collection_of_object_values(connection_operation.ConnectionOperation)),
            "schema": lambda n : setattr(self, 'schema', n.get_object_value(schema.Schema)),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(connection_state.ConnectionState)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def groups(self,) -> Optional[List[external_group.ExternalGroup]]:
        """
        Gets the groups property value. The groups property
        Returns: Optional[List[external_group.ExternalGroup]]
        """
        return self._groups
    
    @groups.setter
    def groups(self,value: Optional[List[external_group.ExternalGroup]] = None) -> None:
        """
        Sets the groups property value. The groups property
        Args:
            value: Value to set for the groups property.
        """
        self._groups = value
    
    @property
    def items(self,) -> Optional[List[external_item.ExternalItem]]:
        """
        Gets the items property value. The items property
        Returns: Optional[List[external_item.ExternalItem]]
        """
        return self._items
    
    @items.setter
    def items(self,value: Optional[List[external_item.ExternalItem]] = None) -> None:
        """
        Sets the items property value. The items property
        Args:
            value: Value to set for the items property.
        """
        self._items = value
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. The display name of the connection to be displayed in the Microsoft 365 admin center. Maximum length of 128 characters. Required.
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. The display name of the connection to be displayed in the Microsoft 365 admin center. Maximum length of 128 characters. Required.
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
    @property
    def operations(self,) -> Optional[List[connection_operation.ConnectionOperation]]:
        """
        Gets the operations property value. The operations property
        Returns: Optional[List[connection_operation.ConnectionOperation]]
        """
        return self._operations
    
    @operations.setter
    def operations(self,value: Optional[List[connection_operation.ConnectionOperation]] = None) -> None:
        """
        Sets the operations property value. The operations property
        Args:
            value: Value to set for the operations property.
        """
        self._operations = value
    
    @property
    def schema(self,) -> Optional[schema.Schema]:
        """
        Gets the schema property value. The schema property
        Returns: Optional[schema.Schema]
        """
        return self._schema
    
    @schema.setter
    def schema(self,value: Optional[schema.Schema] = None) -> None:
        """
        Sets the schema property value. The schema property
        Args:
            value: Value to set for the schema property.
        """
        self._schema = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("configuration", self.configuration)
        writer.write_str_value("description", self.description)
        writer.write_collection_of_object_values("groups", self.groups)
        writer.write_collection_of_object_values("items", self.items)
        writer.write_str_value("name", self.name)
        writer.write_collection_of_object_values("operations", self.operations)
        writer.write_object_value("schema", self.schema)
    
    @property
    def state(self,) -> Optional[connection_state.ConnectionState]:
        """
        Gets the state property value. Indicates the current state of the connection. Possible values are: draft, ready, obsolete, limitExceeded, unknownFutureValue.
        Returns: Optional[connection_state.ConnectionState]
        """
        return self._state
    
    @state.setter
    def state(self,value: Optional[connection_state.ConnectionState] = None) -> None:
        """
        Sets the state property value. Indicates the current state of the connection. Possible values are: draft, ready, obsolete, limitExceeded, unknownFutureValue.
        Args:
            value: Value to set for the state property.
        """
        self._state = value
    

