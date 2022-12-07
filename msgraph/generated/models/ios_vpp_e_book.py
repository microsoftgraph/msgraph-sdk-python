from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

managed_e_book = lazy_import('msgraph.generated.models.managed_e_book')

class IosVppEBook(managed_e_book.ManagedEBook):
    @property
    def apple_id(self,) -> Optional[str]:
        """
        Gets the appleId property value. The Apple ID associated with Vpp token.
        Returns: Optional[str]
        """
        return self._apple_id
    
    @apple_id.setter
    def apple_id(self,value: Optional[str] = None) -> None:
        """
        Sets the appleId property value. The Apple ID associated with Vpp token.
        Args:
            value: Value to set for the appleId property.
        """
        self._apple_id = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new IosVppEBook and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.iosVppEBook"
        # The Apple ID associated with Vpp token.
        self._apple_id: Optional[str] = None
        # Genres.
        self._genres: Optional[List[str]] = None
        # Language.
        self._language: Optional[str] = None
        # Seller.
        self._seller: Optional[str] = None
        # Total license count.
        self._total_license_count: Optional[int] = None
        # Used license count.
        self._used_license_count: Optional[int] = None
        # The Vpp token's organization name.
        self._vpp_organization_name: Optional[str] = None
        # The Vpp token ID.
        self._vpp_token_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IosVppEBook:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IosVppEBook
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IosVppEBook()
    
    @property
    def genres(self,) -> Optional[List[str]]:
        """
        Gets the genres property value. Genres.
        Returns: Optional[List[str]]
        """
        return self._genres
    
    @genres.setter
    def genres(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the genres property value. Genres.
        Args:
            value: Value to set for the genres property.
        """
        self._genres = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "apple_id": lambda n : setattr(self, 'apple_id', n.get_str_value()),
            "genres": lambda n : setattr(self, 'genres', n.get_collection_of_primitive_values(str)),
            "language": lambda n : setattr(self, 'language', n.get_str_value()),
            "seller": lambda n : setattr(self, 'seller', n.get_str_value()),
            "total_license_count": lambda n : setattr(self, 'total_license_count', n.get_int_value()),
            "used_license_count": lambda n : setattr(self, 'used_license_count', n.get_int_value()),
            "vpp_organization_name": lambda n : setattr(self, 'vpp_organization_name', n.get_str_value()),
            "vpp_token_id": lambda n : setattr(self, 'vpp_token_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def language(self,) -> Optional[str]:
        """
        Gets the language property value. Language.
        Returns: Optional[str]
        """
        return self._language
    
    @language.setter
    def language(self,value: Optional[str] = None) -> None:
        """
        Sets the language property value. Language.
        Args:
            value: Value to set for the language property.
        """
        self._language = value
    
    @property
    def seller(self,) -> Optional[str]:
        """
        Gets the seller property value. Seller.
        Returns: Optional[str]
        """
        return self._seller
    
    @seller.setter
    def seller(self,value: Optional[str] = None) -> None:
        """
        Sets the seller property value. Seller.
        Args:
            value: Value to set for the seller property.
        """
        self._seller = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("appleId", self.apple_id)
        writer.write_collection_of_primitive_values("genres", self.genres)
        writer.write_str_value("language", self.language)
        writer.write_str_value("seller", self.seller)
        writer.write_int_value("totalLicenseCount", self.total_license_count)
        writer.write_int_value("usedLicenseCount", self.used_license_count)
        writer.write_str_value("vppOrganizationName", self.vpp_organization_name)
        writer.write_str_value("vppTokenId", self.vpp_token_id)
    
    @property
    def total_license_count(self,) -> Optional[int]:
        """
        Gets the totalLicenseCount property value. Total license count.
        Returns: Optional[int]
        """
        return self._total_license_count
    
    @total_license_count.setter
    def total_license_count(self,value: Optional[int] = None) -> None:
        """
        Sets the totalLicenseCount property value. Total license count.
        Args:
            value: Value to set for the totalLicenseCount property.
        """
        self._total_license_count = value
    
    @property
    def used_license_count(self,) -> Optional[int]:
        """
        Gets the usedLicenseCount property value. Used license count.
        Returns: Optional[int]
        """
        return self._used_license_count
    
    @used_license_count.setter
    def used_license_count(self,value: Optional[int] = None) -> None:
        """
        Sets the usedLicenseCount property value. Used license count.
        Args:
            value: Value to set for the usedLicenseCount property.
        """
        self._used_license_count = value
    
    @property
    def vpp_organization_name(self,) -> Optional[str]:
        """
        Gets the vppOrganizationName property value. The Vpp token's organization name.
        Returns: Optional[str]
        """
        return self._vpp_organization_name
    
    @vpp_organization_name.setter
    def vpp_organization_name(self,value: Optional[str] = None) -> None:
        """
        Sets the vppOrganizationName property value. The Vpp token's organization name.
        Args:
            value: Value to set for the vppOrganizationName property.
        """
        self._vpp_organization_name = value
    
    @property
    def vpp_token_id(self,) -> Optional[str]:
        """
        Gets the vppTokenId property value. The Vpp token ID.
        Returns: Optional[str]
        """
        return self._vpp_token_id
    
    @vpp_token_id.setter
    def vpp_token_id(self,value: Optional[str] = None) -> None:
        """
        Sets the vppTokenId property value. The Vpp token ID.
        Args:
            value: Value to set for the vppTokenId property.
        """
        self._vpp_token_id = value
    

