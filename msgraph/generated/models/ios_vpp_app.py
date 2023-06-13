from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import ios_device_type, mobile_app, vpp_licensing_type, vpp_token_account_type

from . import mobile_app

@dataclass
class IosVppApp(mobile_app.MobileApp):
    odata_type = "#microsoft.graph.iosVppApp"
    # The store URL.
    app_store_url: Optional[str] = None
    # The applicable iOS Device Type.
    applicable_device_type: Optional[ios_device_type.IosDeviceType] = None
    # The Identity Name.
    bundle_id: Optional[str] = None
    # The supported License Type.
    licensing_type: Optional[vpp_licensing_type.VppLicensingType] = None
    # The VPP application release date and time.
    release_date_time: Optional[datetime] = None
    # The total number of VPP licenses.
    total_license_count: Optional[int] = None
    # The number of VPP licenses in use.
    used_license_count: Optional[int] = None
    # Possible types of an Apple Volume Purchase Program token.
    vpp_token_account_type: Optional[vpp_token_account_type.VppTokenAccountType] = None
    # The Apple Id associated with the given Apple Volume Purchase Program Token.
    vpp_token_apple_id: Optional[str] = None
    # The organization associated with the Apple Volume Purchase Program Token
    vpp_token_organization_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IosVppApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IosVppApp
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IosVppApp()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import ios_device_type, mobile_app, vpp_licensing_type, vpp_token_account_type

        fields: Dict[str, Callable[[Any], None]] = {
            "applicableDeviceType": lambda n : setattr(self, 'applicable_device_type', n.get_object_value(ios_device_type.IosDeviceType)),
            "appStoreUrl": lambda n : setattr(self, 'app_store_url', n.get_str_value()),
            "bundleId": lambda n : setattr(self, 'bundle_id', n.get_str_value()),
            "licensingType": lambda n : setattr(self, 'licensing_type', n.get_object_value(vpp_licensing_type.VppLicensingType)),
            "releaseDateTime": lambda n : setattr(self, 'release_date_time', n.get_datetime_value()),
            "totalLicenseCount": lambda n : setattr(self, 'total_license_count', n.get_int_value()),
            "usedLicenseCount": lambda n : setattr(self, 'used_license_count', n.get_int_value()),
            "vppTokenAccountType": lambda n : setattr(self, 'vpp_token_account_type', n.get_enum_value(vpp_token_account_type.VppTokenAccountType)),
            "vppTokenAppleId": lambda n : setattr(self, 'vpp_token_apple_id', n.get_str_value()),
            "vppTokenOrganizationName": lambda n : setattr(self, 'vpp_token_organization_name', n.get_str_value()),
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
        writer.write_object_value("applicableDeviceType", self.applicable_device_type)
        writer.write_str_value("appStoreUrl", self.app_store_url)
        writer.write_str_value("bundleId", self.bundle_id)
        writer.write_object_value("licensingType", self.licensing_type)
        writer.write_datetime_value("releaseDateTime", self.release_date_time)
        writer.write_int_value("totalLicenseCount", self.total_license_count)
        writer.write_int_value("usedLicenseCount", self.used_license_count)
        writer.write_enum_value("vppTokenAccountType", self.vpp_token_account_type)
        writer.write_str_value("vppTokenAppleId", self.vpp_token_apple_id)
        writer.write_str_value("vppTokenOrganizationName", self.vpp_token_organization_name)
    

