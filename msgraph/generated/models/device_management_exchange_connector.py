from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_management_exchange_connector_status = lazy_import('msgraph.generated.models.device_management_exchange_connector_status')
device_management_exchange_connector_type = lazy_import('msgraph.generated.models.device_management_exchange_connector_type')
entity = lazy_import('msgraph.generated.models.entity')

class DeviceManagementExchangeConnector(entity.Entity):
    """
    Entity which represents a connection to an Exchange environment.
    """
    @property
    def connector_server_name(self,) -> Optional[str]:
        """
        Gets the connectorServerName property value. The name of the server hosting the Exchange Connector.
        Returns: Optional[str]
        """
        return self._connector_server_name
    
    @connector_server_name.setter
    def connector_server_name(self,value: Optional[str] = None) -> None:
        """
        Sets the connectorServerName property value. The name of the server hosting the Exchange Connector.
        Args:
            value: Value to set for the connectorServerName property.
        """
        self._connector_server_name = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new deviceManagementExchangeConnector and sets the default values.
        """
        super().__init__()
        # The name of the server hosting the Exchange Connector.
        self._connector_server_name: Optional[str] = None
        # An alias assigned to the Exchange server
        self._exchange_alias: Optional[str] = None
        # The type of Exchange Connector.
        self._exchange_connector_type: Optional[device_management_exchange_connector_type.DeviceManagementExchangeConnectorType] = None
        # Exchange Organization to the Exchange server
        self._exchange_organization: Optional[str] = None
        # Last sync time for the Exchange Connector
        self._last_sync_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Email address used to configure the Service To Service Exchange Connector.
        self._primary_smtp_address: Optional[str] = None
        # The name of the Exchange server.
        self._server_name: Optional[str] = None
        # The current status of the Exchange Connector.
        self._status: Optional[device_management_exchange_connector_status.DeviceManagementExchangeConnectorStatus] = None
        # The version of the ExchangeConnectorAgent
        self._version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementExchangeConnector:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementExchangeConnector
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementExchangeConnector()
    
    @property
    def exchange_alias(self,) -> Optional[str]:
        """
        Gets the exchangeAlias property value. An alias assigned to the Exchange server
        Returns: Optional[str]
        """
        return self._exchange_alias
    
    @exchange_alias.setter
    def exchange_alias(self,value: Optional[str] = None) -> None:
        """
        Sets the exchangeAlias property value. An alias assigned to the Exchange server
        Args:
            value: Value to set for the exchangeAlias property.
        """
        self._exchange_alias = value
    
    @property
    def exchange_connector_type(self,) -> Optional[device_management_exchange_connector_type.DeviceManagementExchangeConnectorType]:
        """
        Gets the exchangeConnectorType property value. The type of Exchange Connector.
        Returns: Optional[device_management_exchange_connector_type.DeviceManagementExchangeConnectorType]
        """
        return self._exchange_connector_type
    
    @exchange_connector_type.setter
    def exchange_connector_type(self,value: Optional[device_management_exchange_connector_type.DeviceManagementExchangeConnectorType] = None) -> None:
        """
        Sets the exchangeConnectorType property value. The type of Exchange Connector.
        Args:
            value: Value to set for the exchangeConnectorType property.
        """
        self._exchange_connector_type = value
    
    @property
    def exchange_organization(self,) -> Optional[str]:
        """
        Gets the exchangeOrganization property value. Exchange Organization to the Exchange server
        Returns: Optional[str]
        """
        return self._exchange_organization
    
    @exchange_organization.setter
    def exchange_organization(self,value: Optional[str] = None) -> None:
        """
        Sets the exchangeOrganization property value. Exchange Organization to the Exchange server
        Args:
            value: Value to set for the exchangeOrganization property.
        """
        self._exchange_organization = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "connector_server_name": lambda n : setattr(self, 'connector_server_name', n.get_str_value()),
            "exchange_alias": lambda n : setattr(self, 'exchange_alias', n.get_str_value()),
            "exchange_connector_type": lambda n : setattr(self, 'exchange_connector_type', n.get_enum_value(device_management_exchange_connector_type.DeviceManagementExchangeConnectorType)),
            "exchange_organization": lambda n : setattr(self, 'exchange_organization', n.get_str_value()),
            "last_sync_date_time": lambda n : setattr(self, 'last_sync_date_time', n.get_datetime_value()),
            "primary_smtp_address": lambda n : setattr(self, 'primary_smtp_address', n.get_str_value()),
            "server_name": lambda n : setattr(self, 'server_name', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(device_management_exchange_connector_status.DeviceManagementExchangeConnectorStatus)),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_sync_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastSyncDateTime property value. Last sync time for the Exchange Connector
        Returns: Optional[datetime]
        """
        return self._last_sync_date_time
    
    @last_sync_date_time.setter
    def last_sync_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastSyncDateTime property value. Last sync time for the Exchange Connector
        Args:
            value: Value to set for the lastSyncDateTime property.
        """
        self._last_sync_date_time = value
    
    @property
    def primary_smtp_address(self,) -> Optional[str]:
        """
        Gets the primarySmtpAddress property value. Email address used to configure the Service To Service Exchange Connector.
        Returns: Optional[str]
        """
        return self._primary_smtp_address
    
    @primary_smtp_address.setter
    def primary_smtp_address(self,value: Optional[str] = None) -> None:
        """
        Sets the primarySmtpAddress property value. Email address used to configure the Service To Service Exchange Connector.
        Args:
            value: Value to set for the primarySmtpAddress property.
        """
        self._primary_smtp_address = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
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
    
    @property
    def server_name(self,) -> Optional[str]:
        """
        Gets the serverName property value. The name of the Exchange server.
        Returns: Optional[str]
        """
        return self._server_name
    
    @server_name.setter
    def server_name(self,value: Optional[str] = None) -> None:
        """
        Sets the serverName property value. The name of the Exchange server.
        Args:
            value: Value to set for the serverName property.
        """
        self._server_name = value
    
    @property
    def status(self,) -> Optional[device_management_exchange_connector_status.DeviceManagementExchangeConnectorStatus]:
        """
        Gets the status property value. The current status of the Exchange Connector.
        Returns: Optional[device_management_exchange_connector_status.DeviceManagementExchangeConnectorStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[device_management_exchange_connector_status.DeviceManagementExchangeConnectorStatus] = None) -> None:
        """
        Sets the status property value. The current status of the Exchange Connector.
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    
    @property
    def version(self,) -> Optional[str]:
        """
        Gets the version property value. The version of the ExchangeConnectorAgent
        Returns: Optional[str]
        """
        return self._version
    
    @version.setter
    def version(self,value: Optional[str] = None) -> None:
        """
        Sets the version property value. The version of the ExchangeConnectorAgent
        Args:
            value: Value to set for the version property.
        """
        self._version = value
    

