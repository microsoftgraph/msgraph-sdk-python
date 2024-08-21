from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .i_pv4_cidr_range import IPv4CidrRange
    from .i_pv4_range import IPv4Range
    from .i_pv6_cidr_range import IPv6CidrRange
    from .i_pv6_range import IPv6Range

@dataclass
class IpRange(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IpRange:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IpRange
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iPv4CidrRange".casefold():
            from .i_pv4_cidr_range import IPv4CidrRange

            return IPv4CidrRange()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iPv4Range".casefold():
            from .i_pv4_range import IPv4Range

            return IPv4Range()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iPv6CidrRange".casefold():
            from .i_pv6_cidr_range import IPv6CidrRange

            return IPv6CidrRange()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iPv6Range".casefold():
            from .i_pv6_range import IPv6Range

            return IPv6Range()
        return IpRange()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .i_pv4_cidr_range import IPv4CidrRange
        from .i_pv4_range import IPv4Range
        from .i_pv6_cidr_range import IPv6CidrRange
        from .i_pv6_range import IPv6Range

        from .i_pv4_cidr_range import IPv4CidrRange
        from .i_pv4_range import IPv4Range
        from .i_pv6_cidr_range import IPv6CidrRange
        from .i_pv6_range import IPv6Range

        fields: Dict[str, Callable[[Any], None]] = {
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

