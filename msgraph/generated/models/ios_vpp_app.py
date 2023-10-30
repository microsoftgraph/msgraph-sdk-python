from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .ios_device_type import IosDeviceType
    from .mobile_app import MobileApp
    from .vpp_licensing_type import VppLicensingType
    from .vpp_token_account_type import VppTokenAccountType

from .mobile_app import MobileApp

@dataclass
class IosVppApp(MobileApp):
    """
    Contains properties and inherited properties for iOS Volume-Purchased Program (VPP) Apps.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.iosVppApp"
    # The store URL.
    app_store_url: Optional[str] = None
    # The applicable iOS Device Type.
    applicable_device_type: Optional[IosDeviceType] = None
    # The Identity Name.
    bundle_id: Optional[str] = None
    # The supported License Type.
    licensing_type: Optional[VppLicensingType] = None
    # The VPP application release date and time.
    release_date_time: Optional[datetime.datetime] = None
    # The total number of VPP licenses.
    total_license_count: Optional[int] = None
    # The number of VPP licenses in use.
    used_license_count: Optional[int] = None
    # Possible types of an Apple Volume Purchase Program token.
    vpp_token_account_type: Optional[VppTokenAccountType] = None
    # The Apple Id associated with the given Apple Volume Purchase Program Token.
    vpp_token_apple_id: Optional[str] = None
    # The organization associated with the Apple Volume Purchase Program Token
    vpp_token_organization_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IosVppApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IosVppApp
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return IosVppApp()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .ios_device_type import IosDeviceType
        from .mobile_app import MobileApp
        from .vpp_licensing_type import VppLicensingType
        from .vpp_token_account_type import VppTokenAccountType

        from .ios_device_type import IosDeviceType
        from .mobile_app import MobileApp
        from .vpp_licensing_type import VppLicensingType
        from .vpp_token_account_type import VppTokenAccountType

        fields: Dict[str, Callable[[Any], None]] = {
            "app_store_url": lambda n : setattr(self, 'app_store_url', n.get_str_value()),
            "applicable_device_type": lambda n : setattr(self, 'applicable_device_type', n.get_object_value(IosDeviceType)),
            "bundle_id": lambda n : setattr(self, 'bundle_id', n.get_str_value()),
            "licensing_type": lambda n : setattr(self, 'licensing_type', n.get_object_value(VppLicensingType)),
            "release_date_time": lambda n : setattr(self, 'release_date_time', n.get_datetime_value()),
            "total_license_count": lambda n : setattr(self, 'total_license_count', n.get_int_value()),
            "used_license_count": lambda n : setattr(self, 'used_license_count', n.get_int_value()),
            "vpp_token_account_type": lambda n : setattr(self, 'vpp_token_account_type', n.get_enum_value(VppTokenAccountType)),
            "vpp_token_apple_id": lambda n : setattr(self, 'vpp_token_apple_id', n.get_str_value()),
            "vpp_token_organization_name": lambda n : setattr(self, 'vpp_token_organization_name', n.get_str_value()),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("app_store_url", self.app_store_url)
        writer.write_object_value("applicable_device_type", self.applicable_device_type)
        writer.write_str_value("bundle_id", self.bundle_id)
        writer.write_object_value("licensing_type", self.licensing_type)
        writer.write_datetime_value("release_date_time", self.release_date_time)
        writer.write_int_value("total_license_count", self.total_license_count)
        writer.write_int_value("used_license_count", self.used_license_count)
        writer.write_enum_value("vpp_token_account_type", self.vpp_token_account_type)
        writer.write_str_value("vpp_token_apple_id", self.vpp_token_apple_id)
        writer.write_str_value("vpp_token_organization_name", self.vpp_token_organization_name)
    

