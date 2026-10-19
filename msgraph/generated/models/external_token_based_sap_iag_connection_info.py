from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .connection_info import ConnectionInfo

from .connection_info import ConnectionInfo

@dataclass
class ExternalTokenBasedSapIagConnectionInfo(ConnectionInfo, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.externalTokenBasedSapIagConnectionInfo"
    # The URL endpoint used to obtain access tokens for authentication with the SAP IAG system.
    access_token_url: Optional[str] = None
    # The client identifier used for authentication with the SAP IAG system.
    client_id: Optional[str] = None
    # The name of the Azure Key Vault that stores the client secret for authentication.
    key_vault_name: Optional[str] = None
    # The Azure resource group that contains the Key Vault.
    resource_group: Optional[str] = None
    # The name of the secret in Azure Key Vault that contains the client secret.
    secret_name: Optional[str] = None
    # The Azure subscription ID that contains the Key Vault.
    subscription_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ExternalTokenBasedSapIagConnectionInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ExternalTokenBasedSapIagConnectionInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ExternalTokenBasedSapIagConnectionInfo()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .connection_info import ConnectionInfo

        from .connection_info import ConnectionInfo

        fields: dict[str, Callable[[Any], None]] = {
            "accessTokenUrl": lambda n : setattr(self, 'access_token_url', n.get_str_value()),
            "clientId": lambda n : setattr(self, 'client_id', n.get_str_value()),
            "keyVaultName": lambda n : setattr(self, 'key_vault_name', n.get_str_value()),
            "resourceGroup": lambda n : setattr(self, 'resource_group', n.get_str_value()),
            "secretName": lambda n : setattr(self, 'secret_name', n.get_str_value()),
            "subscriptionId": lambda n : setattr(self, 'subscription_id', n.get_str_value()),
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
        writer.write_str_value("accessTokenUrl", self.access_token_url)
        writer.write_str_value("clientId", self.client_id)
        writer.write_str_value("keyVaultName", self.key_vault_name)
        writer.write_str_value("resourceGroup", self.resource_group)
        writer.write_str_value("secretName", self.secret_name)
        writer.write_str_value("subscriptionId", self.subscription_id)
    

