from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .managed_e_book import ManagedEBook

from .managed_e_book import ManagedEBook

@dataclass
class IosVppEBook(ManagedEBook, Parsable):
    """
    A class containing the properties for iOS Vpp eBook.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.iosVppEBook"
    # The Apple ID associated with Vpp token.
    apple_id: Optional[str] = None
    # Genres.
    genres: Optional[list[str]] = None
    # Language.
    language: Optional[str] = None
    # Seller.
    seller: Optional[str] = None
    # Total license count.
    total_license_count: Optional[int] = None
    # Used license count.
    used_license_count: Optional[int] = None
    # The Vpp token's organization name.
    vpp_organization_name: Optional[str] = None
    # The Vpp token ID.
    vpp_token_id: Optional[UUID] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IosVppEBook:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IosVppEBook
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return IosVppEBook()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .managed_e_book import ManagedEBook

        from .managed_e_book import ManagedEBook

        fields: dict[str, Callable[[Any], None]] = {
            "appleId": lambda n : setattr(self, 'apple_id', n.get_str_value()),
            "genres": lambda n : setattr(self, 'genres', n.get_collection_of_primitive_values(str)),
            "language": lambda n : setattr(self, 'language', n.get_str_value()),
            "seller": lambda n : setattr(self, 'seller', n.get_str_value()),
            "totalLicenseCount": lambda n : setattr(self, 'total_license_count', n.get_int_value()),
            "usedLicenseCount": lambda n : setattr(self, 'used_license_count', n.get_int_value()),
            "vppOrganizationName": lambda n : setattr(self, 'vpp_organization_name', n.get_str_value()),
            "vppTokenId": lambda n : setattr(self, 'vpp_token_id', n.get_uuid_value()),
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
        writer.write_str_value("appleId", self.apple_id)
        writer.write_collection_of_primitive_values("genres", self.genres)
        writer.write_str_value("language", self.language)
        writer.write_str_value("seller", self.seller)
        writer.write_int_value("totalLicenseCount", self.total_license_count)
        writer.write_int_value("usedLicenseCount", self.used_license_count)
        writer.write_str_value("vppOrganizationName", self.vpp_organization_name)
        writer.write_uuid_value("vppTokenId", self.vpp_token_id)
    

