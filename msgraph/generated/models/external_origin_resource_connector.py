from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .connection_info import ConnectionInfo
    from .connector_type import ConnectorType
    from .entity import Entity

from .entity import Entity

@dataclass
class ExternalOriginResourceConnector(Entity, Parsable):
    # The connectionInfo property
    connection_info: Optional[ConnectionInfo] = None
    # The connectorType property
    connector_type: Optional[ConnectorType] = None
    # The identifier of the user or application that created the connector.
    created_by: Optional[str] = None
    # The date and time when the connector was created.
    created_date_time: Optional[datetime.datetime] = None
    # A description of the connector.
    description: Optional[str] = None
    # The display name of the connector.
    display_name: Optional[str] = None
    # The identifier of the user or application that last modified the connector.
    modified_by: Optional[str] = None
    # The date and time when the connector was last modified.
    modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ExternalOriginResourceConnector:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ExternalOriginResourceConnector
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ExternalOriginResourceConnector()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .connection_info import ConnectionInfo
        from .connector_type import ConnectorType
        from .entity import Entity

        from .connection_info import ConnectionInfo
        from .connector_type import ConnectorType
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "connectionInfo": lambda n : setattr(self, 'connection_info', n.get_object_value(ConnectionInfo)),
            "connectorType": lambda n : setattr(self, 'connector_type', n.get_enum_value(ConnectorType)),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "modifiedBy": lambda n : setattr(self, 'modified_by', n.get_str_value()),
            "modifiedDateTime": lambda n : setattr(self, 'modified_date_time', n.get_datetime_value()),
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
        writer.write_object_value("connectionInfo", self.connection_info)
        writer.write_enum_value("connectorType", self.connector_type)
        writer.write_str_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("modifiedBy", self.modified_by)
        writer.write_datetime_value("modifiedDateTime", self.modified_date_time)
    

