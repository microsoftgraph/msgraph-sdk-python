from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class FileEncryptionInfo(AdditionalDataHolder, BackedModel, Parsable):
    """
    Contains properties for file encryption information for the content version of a line of business app.
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The key used to encrypt the file content.
    encryption_key: Optional[bytes] = None
    # The file digest prior to encryption. ProfileVersion1 requires a non-null FileDigest.
    file_digest: Optional[bytes] = None
    # The file digest algorithm. ProfileVersion1 currently only supports SHA256 for the FileDigestAlgorithm.
    file_digest_algorithm: Optional[str] = None
    # The initialization vector (IV) used for the encryption algorithm. Must be 16 bytes.
    initialization_vector: Optional[bytes] = None
    # The hash of the concatenation of the IV and encrypted file content. Must be 32 bytes.
    mac: Optional[bytes] = None
    # The key used to compute the message authentication code of the concatenation of the IV and encrypted file content. Must be 32 bytes.
    mac_key: Optional[bytes] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The profile identifier. Maps to the strategy used to encrypt the file. Currently, only ProfileVersion1 is supported.
    profile_identifier: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FileEncryptionInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FileEncryptionInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FileEncryptionInfo()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "encryptionKey": lambda n : setattr(self, 'encryption_key', n.get_bytes_value()),
            "fileDigest": lambda n : setattr(self, 'file_digest', n.get_bytes_value()),
            "fileDigestAlgorithm": lambda n : setattr(self, 'file_digest_algorithm', n.get_str_value()),
            "initializationVector": lambda n : setattr(self, 'initialization_vector', n.get_bytes_value()),
            "mac": lambda n : setattr(self, 'mac', n.get_bytes_value()),
            "macKey": lambda n : setattr(self, 'mac_key', n.get_bytes_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "profileIdentifier": lambda n : setattr(self, 'profile_identifier', n.get_str_value()),
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
        writer.write_bytes_value("encryptionKey", self.encryption_key)
        writer.write_bytes_value("fileDigest", self.file_digest)
        writer.write_str_value("fileDigestAlgorithm", self.file_digest_algorithm)
        writer.write_bytes_value("initializationVector", self.initialization_vector)
        writer.write_bytes_value("mac", self.mac)
        writer.write_bytes_value("macKey", self.mac_key)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("profileIdentifier", self.profile_identifier)
        writer.write_additional_data_value(self.additional_data)
    

