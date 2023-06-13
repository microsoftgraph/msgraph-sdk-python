from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import microsoft_store_for_business_license_type, mobile_app

from . import mobile_app

@dataclass
class MicrosoftStoreForBusinessApp(mobile_app.MobileApp):
    odata_type = "#microsoft.graph.microsoftStoreForBusinessApp"
    # The licenseType property
    license_type: Optional[microsoft_store_for_business_license_type.MicrosoftStoreForBusinessLicenseType] = None
    # The app package identifier
    package_identity_name: Optional[str] = None
    # The app product key
    product_key: Optional[str] = None
    # The total number of Microsoft Store for Business licenses.
    total_license_count: Optional[int] = None
    # The number of Microsoft Store for Business licenses in use.
    used_license_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MicrosoftStoreForBusinessApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MicrosoftStoreForBusinessApp
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MicrosoftStoreForBusinessApp()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import microsoft_store_for_business_license_type, mobile_app

        fields: Dict[str, Callable[[Any], None]] = {
            "licenseType": lambda n : setattr(self, 'license_type', n.get_enum_value(microsoft_store_for_business_license_type.MicrosoftStoreForBusinessLicenseType)),
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
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("licenseType", self.license_type)
        writer.write_str_value("packageIdentityName", self.package_identity_name)
        writer.write_str_value("productKey", self.product_key)
        writer.write_int_value("totalLicenseCount", self.total_license_count)
        writer.write_int_value("usedLicenseCount", self.used_license_count)
    

