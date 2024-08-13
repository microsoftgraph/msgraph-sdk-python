from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class ServicePrincipalLockConfiguration(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Enables locking all sensitive properties. The sensitive properties are keyCredentials, passwordCredentials, and tokenEncryptionKeyId.
    all_properties: Optional[bool] = None
    # Locks the keyCredentials and passwordCredentials properties for modification where credential usage type is Sign.
    credentials_with_usage_sign: Optional[bool] = None
    # Locks the keyCredentials and passwordCredentials properties for modification where credential usage type is Verify. This locks OAuth service principals.
    credentials_with_usage_verify: Optional[bool] = None
    # Enables or disables service principal lock configuration. To allow the sensitive properties to be updated, update this property to false to disable the lock on the service principal.
    is_enabled: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Locks the tokenEncryptionKeyId property for modification on the service principal.
    token_encryption_key_id: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ServicePrincipalLockConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ServicePrincipalLockConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ServicePrincipalLockConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "allProperties": lambda n : setattr(self, 'all_properties', n.get_bool_value()),
            "credentialsWithUsageSign": lambda n : setattr(self, 'credentials_with_usage_sign', n.get_bool_value()),
            "credentialsWithUsageVerify": lambda n : setattr(self, 'credentials_with_usage_verify', n.get_bool_value()),
            "isEnabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "tokenEncryptionKeyId": lambda n : setattr(self, 'token_encryption_key_id', n.get_bool_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_bool_value("allProperties", self.all_properties)
        writer.write_bool_value("credentialsWithUsageSign", self.credentials_with_usage_sign)
        writer.write_bool_value("credentialsWithUsageVerify", self.credentials_with_usage_verify)
        writer.write_bool_value("isEnabled", self.is_enabled)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("tokenEncryptionKeyId", self.token_encryption_key_id)
        writer.write_additional_data_value(self.additional_data)
    

