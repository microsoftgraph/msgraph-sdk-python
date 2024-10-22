from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .app_log_decryption_algorithm import AppLogDecryptionAlgorithm

@dataclass
class AppLogCollectionDownloadDetails(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The appLogDecryptionAlgorithm property
    app_log_decryption_algorithm: Optional[AppLogDecryptionAlgorithm] = None
    # Decryption key that used to decrypt the log.
    decryption_key: Optional[str] = None
    # Download SAS (Shared Access Signature) Url for completed app log request.
    download_url: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AppLogCollectionDownloadDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AppLogCollectionDownloadDetails
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AppLogCollectionDownloadDetails()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .app_log_decryption_algorithm import AppLogDecryptionAlgorithm

        from .app_log_decryption_algorithm import AppLogDecryptionAlgorithm

        fields: Dict[str, Callable[[Any], None]] = {
            "appLogDecryptionAlgorithm": lambda n : setattr(self, 'app_log_decryption_algorithm', n.get_enum_value(AppLogDecryptionAlgorithm)),
            "decryptionKey": lambda n : setattr(self, 'decryption_key', n.get_str_value()),
            "downloadUrl": lambda n : setattr(self, 'download_url', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        from .app_log_decryption_algorithm import AppLogDecryptionAlgorithm

        writer.write_enum_value("appLogDecryptionAlgorithm", self.app_log_decryption_algorithm)
        writer.write_str_value("decryptionKey", self.decryption_key)
        writer.write_str_value("downloadUrl", self.download_url)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

