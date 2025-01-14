from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_management_exchange_connector_status import DeviceManagementExchangeConnectorStatus
    from .device_management_exchange_connector_type import DeviceManagementExchangeConnectorType
    from .entity import Entity

from .entity import Entity

@dataclass
class DeviceManagementExchangeConnector(Entity, Parsable):
    """
    Entity which represents a connection to an Exchange environment.
    """
    # The name of the server hosting the Exchange Connector.
    connector_server_name: Optional[str] = None
    # An alias assigned to the Exchange server
    exchange_alias: Optional[str] = None
    # The type of Exchange Connector.
    exchange_connector_type: Optional[DeviceManagementExchangeConnectorType] = None
    # Exchange Organization to the Exchange server
    exchange_organization: Optional[str] = None
    # Last sync time for the Exchange Connector
    last_sync_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Email address used to configure the Service To Service Exchange Connector.
    primary_smtp_address: Optional[str] = None
    # The name of the Exchange server.
    server_name: Optional[str] = None
    # The current status of the Exchange Connector.
    status: Optional[DeviceManagementExchangeConnectorStatus] = None
    # The version of the ExchangeConnectorAgent
    version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceManagementExchangeConnector:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementExchangeConnector
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceManagementExchangeConnector()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_management_exchange_connector_status import DeviceManagementExchangeConnectorStatus
        from .device_management_exchange_connector_type import DeviceManagementExchangeConnectorType
        from .entity import Entity

        from .device_management_exchange_connector_status import DeviceManagementExchangeConnectorStatus
        from .device_management_exchange_connector_type import DeviceManagementExchangeConnectorType
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "connectorServerName": lambda n : setattr(self, 'connector_server_name', n.get_str_value()),
            "exchangeAlias": lambda n : setattr(self, 'exchange_alias', n.get_str_value()),
            "exchangeConnectorType": lambda n : setattr(self, 'exchange_connector_type', n.get_enum_value(DeviceManagementExchangeConnectorType)),
            "exchangeOrganization": lambda n : setattr(self, 'exchange_organization', n.get_str_value()),
            "lastSyncDateTime": lambda n : setattr(self, 'last_sync_date_time', n.get_datetime_value()),
            "primarySmtpAddress": lambda n : setattr(self, 'primary_smtp_address', n.get_str_value()),
            "serverName": lambda n : setattr(self, 'server_name', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(DeviceManagementExchangeConnectorStatus)),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
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
        writer.write_str_value("connectorServerName", self.connector_server_name)
        writer.write_str_value("exchangeAlias", self.exchange_alias)
        writer.write_enum_value("exchangeConnectorType", self.exchange_connector_type)
        writer.write_str_value("exchangeOrganization", self.exchange_organization)
        writer.write_datetime_value("lastSyncDateTime", self.last_sync_date_time)
        writer.write_str_value("primarySmtpAddress", self.primary_smtp_address)
        writer.write_str_value("serverName", self.server_name)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("version", self.version)
    

