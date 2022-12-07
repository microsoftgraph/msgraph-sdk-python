from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class SecurityVendorInformation(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new securityVendorInformation and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # Specific provider (product/service - not vendor company); for example, WindowsDefenderATP.
        self._provider: Optional[str] = None
        # Version of the provider or subprovider, if it exists, that generated the alert. Required
        self._provider_version: Optional[str] = None
        # Specific subprovider (under aggregating provider); for example, WindowsDefenderATP.SmartScreen.
        self._sub_provider: Optional[str] = None
        # Name of the alert vendor (for example, Microsoft, Dell, FireEye). Required
        self._vendor: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SecurityVendorInformation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SecurityVendorInformation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SecurityVendorInformation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "provider": lambda n : setattr(self, 'provider', n.get_str_value()),
            "provider_version": lambda n : setattr(self, 'provider_version', n.get_str_value()),
            "sub_provider": lambda n : setattr(self, 'sub_provider', n.get_str_value()),
            "vendor": lambda n : setattr(self, 'vendor', n.get_str_value()),
        }
        return fields
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def provider(self,) -> Optional[str]:
        """
        Gets the provider property value. Specific provider (product/service - not vendor company); for example, WindowsDefenderATP.
        Returns: Optional[str]
        """
        return self._provider
    
    @provider.setter
    def provider(self,value: Optional[str] = None) -> None:
        """
        Sets the provider property value. Specific provider (product/service - not vendor company); for example, WindowsDefenderATP.
        Args:
            value: Value to set for the provider property.
        """
        self._provider = value
    
    @property
    def provider_version(self,) -> Optional[str]:
        """
        Gets the providerVersion property value. Version of the provider or subprovider, if it exists, that generated the alert. Required
        Returns: Optional[str]
        """
        return self._provider_version
    
    @provider_version.setter
    def provider_version(self,value: Optional[str] = None) -> None:
        """
        Sets the providerVersion property value. Version of the provider or subprovider, if it exists, that generated the alert. Required
        Args:
            value: Value to set for the providerVersion property.
        """
        self._provider_version = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("provider", self.provider)
        writer.write_str_value("providerVersion", self.provider_version)
        writer.write_str_value("subProvider", self.sub_provider)
        writer.write_str_value("vendor", self.vendor)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def sub_provider(self,) -> Optional[str]:
        """
        Gets the subProvider property value. Specific subprovider (under aggregating provider); for example, WindowsDefenderATP.SmartScreen.
        Returns: Optional[str]
        """
        return self._sub_provider
    
    @sub_provider.setter
    def sub_provider(self,value: Optional[str] = None) -> None:
        """
        Sets the subProvider property value. Specific subprovider (under aggregating provider); for example, WindowsDefenderATP.SmartScreen.
        Args:
            value: Value to set for the subProvider property.
        """
        self._sub_provider = value
    
    @property
    def vendor(self,) -> Optional[str]:
        """
        Gets the vendor property value. Name of the alert vendor (for example, Microsoft, Dell, FireEye). Required
        Returns: Optional[str]
        """
        return self._vendor
    
    @vendor.setter
    def vendor(self,value: Optional[str] = None) -> None:
        """
        Sets the vendor property value. Name of the alert vendor (for example, Microsoft, Dell, FireEye). Required
        Args:
            value: Value to set for the vendor property.
        """
        self._vendor = value
    

