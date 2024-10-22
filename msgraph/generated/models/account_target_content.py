from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .account_target_content_type import AccountTargetContentType
    from .address_book_account_target_content import AddressBookAccountTargetContent
    from .include_all_account_target_content import IncludeAllAccountTargetContent

@dataclass
class AccountTargetContent(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The OdataType property
    odata_type: Optional[str] = None
    # The type of account target content. Possible values are: unknown, includeAll, addressBook, unknownFutureValue.
    type: Optional[AccountTargetContentType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AccountTargetContent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccountTargetContent
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.addressBookAccountTargetContent".casefold():
            from .address_book_account_target_content import AddressBookAccountTargetContent

            return AddressBookAccountTargetContent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.includeAllAccountTargetContent".casefold():
            from .include_all_account_target_content import IncludeAllAccountTargetContent

            return IncludeAllAccountTargetContent()
        return AccountTargetContent()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .account_target_content_type import AccountTargetContentType
        from .address_book_account_target_content import AddressBookAccountTargetContent
        from .include_all_account_target_content import IncludeAllAccountTargetContent

        from .account_target_content_type import AccountTargetContentType
        from .address_book_account_target_content import AddressBookAccountTargetContent
        from .include_all_account_target_content import IncludeAllAccountTargetContent

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(AccountTargetContentType)),
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
        from .account_target_content_type import AccountTargetContentType
        from .address_book_account_target_content import AddressBookAccountTargetContent
        from .include_all_account_target_content import IncludeAllAccountTargetContent

        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

