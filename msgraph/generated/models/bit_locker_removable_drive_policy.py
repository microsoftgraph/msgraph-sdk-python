from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import bit_locker_encryption_method

@dataclass
class BitLockerRemovableDrivePolicy(AdditionalDataHolder, Parsable):
    """
    BitLocker Removable Drive Policies.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # This policy setting determines whether BitLocker protection is required for removable data drives to be writable on a computer.
    block_cross_organization_write_access: Optional[bool] = None
    # Select the encryption method for removable  drives. Possible values are: aesCbc128, aesCbc256, xtsAes128, xtsAes256.
    encryption_method: Optional[bit_locker_encryption_method.BitLockerEncryptionMethod] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates whether to block write access to devices configured in another organization.  If requireEncryptionForWriteAccess is false, this value does not affect.
    require_encryption_for_write_access: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BitLockerRemovableDrivePolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: BitLockerRemovableDrivePolicy
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return BitLockerRemovableDrivePolicy()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import bit_locker_encryption_method

        fields: Dict[str, Callable[[Any], None]] = {
            "blockCrossOrganizationWriteAccess": lambda n : setattr(self, 'block_cross_organization_write_access', n.get_bool_value()),
            "encryptionMethod": lambda n : setattr(self, 'encryption_method', n.get_enum_value(bit_locker_encryption_method.BitLockerEncryptionMethod)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "requireEncryptionForWriteAccess": lambda n : setattr(self, 'require_encryption_for_write_access', n.get_bool_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_bool_value("blockCrossOrganizationWriteAccess", self.block_cross_organization_write_access)
        writer.write_enum_value("encryptionMethod", self.encryption_method)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("requireEncryptionForWriteAccess", self.require_encryption_for_write_access)
        writer.write_additional_data_value(self.additional_data)
    

