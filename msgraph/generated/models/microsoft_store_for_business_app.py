from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .microsoft_store_for_business_license_type import MicrosoftStoreForBusinessLicenseType
    from .mobile_app import MobileApp

from .mobile_app import MobileApp

@dataclass
class MicrosoftStoreForBusinessApp(MobileApp, Parsable):
    """
    Microsoft Store for Business Apps. This class does not support Create, Delete, or Update.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.microsoftStoreForBusinessApp"
    # The licenseType property
    license_type: Optional[MicrosoftStoreForBusinessLicenseType] = None
    # The app package identifier
    package_identity_name: Optional[str] = None
    # The app product key
    product_key: Optional[str] = None
    # The total number of Microsoft Store for Business licenses.
    total_license_count: Optional[int] = None
    # The number of Microsoft Store for Business licenses in use.
    used_license_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MicrosoftStoreForBusinessApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MicrosoftStoreForBusinessApp
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MicrosoftStoreForBusinessApp()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .microsoft_store_for_business_license_type import MicrosoftStoreForBusinessLicenseType
        from .mobile_app import MobileApp

        from .microsoft_store_for_business_license_type import MicrosoftStoreForBusinessLicenseType
        from .mobile_app import MobileApp

        fields: dict[str, Callable[[Any], None]] = {
            "licenseType": lambda n : setattr(self, 'license_type', n.get_enum_value(MicrosoftStoreForBusinessLicenseType)),
            "packageIdentityName": lambda n : setattr(self, 'package_identity_name', n.get_str_value()),
            "productKey": lambda n : setattr(self, 'product_key', n.get_str_value()),
            "totalLicenseCount": lambda n : setattr(self, 'total_license_count', n.get_int_value()),
            "usedLicenseCount": lambda n : setattr(self, 'used_license_count', n.get_int_value()),
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
        writer.write_enum_value("licenseType", self.license_type)
        writer.write_str_value("packageIdentityName", self.package_identity_name)
        writer.write_str_value("productKey", self.product_key)
        writer.write_int_value("totalLicenseCount", self.total_license_count)
        writer.write_int_value("usedLicenseCount", self.used_license_count)
    

