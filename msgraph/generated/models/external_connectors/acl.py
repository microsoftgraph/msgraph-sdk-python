from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_type import AccessType
    from .acl_type import AclType

@dataclass
class Acl(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The accessType property
    access_type: Optional[AccessType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The type property
    type: Optional[AclType] = None
    # The unique identifer of the identity. For Microsoft Entra identities, value is set to the object identifier of the user, group or tenant for types user, group and everyone (and everyoneExceptGuests) respectively. For external groups value is set to the ID of the externalGroup
    value: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Acl:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Acl
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Acl()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .access_type import AccessType
        from .acl_type import AclType

        from .access_type import AccessType
        from .acl_type import AclType

        fields: Dict[str, Callable[[Any], None]] = {
            "accessType": lambda n : setattr(self, 'access_type', n.get_enum_value(AccessType)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(AclType)),
            "value": lambda n : setattr(self, 'value', n.get_str_value()),
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
        from .access_type import AccessType
        from .acl_type import AclType

        writer.write_enum_value("accessType", self.access_type)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("type", self.type)
        writer.write_str_value("value", self.value)
        writer.write_additional_data_value(self.additional_data)
    

