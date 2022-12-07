from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class InformationalUrl(AdditionalDataHolder, Parsable):
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
        Instantiates a new informationalUrl and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # CDN URL to the application's logo, Read-only.
        self._logo_url: Optional[str] = None
        # Link to the application's marketing page. For example, https://www.contoso.com/app/marketing
        self._marketing_url: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Link to the application's privacy statement. For example, https://www.contoso.com/app/privacy
        self._privacy_statement_url: Optional[str] = None
        # Link to the application's support page. For example, https://www.contoso.com/app/support
        self._support_url: Optional[str] = None
        # Link to the application's terms of service statement. For example, https://www.contoso.com/app/termsofservice
        self._terms_of_service_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> InformationalUrl:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: InformationalUrl
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return InformationalUrl()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "logo_url": lambda n : setattr(self, 'logo_url', n.get_str_value()),
            "marketing_url": lambda n : setattr(self, 'marketing_url', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "privacy_statement_url": lambda n : setattr(self, 'privacy_statement_url', n.get_str_value()),
            "support_url": lambda n : setattr(self, 'support_url', n.get_str_value()),
            "terms_of_service_url": lambda n : setattr(self, 'terms_of_service_url', n.get_str_value()),
        }
        return fields
    
    @property
    def logo_url(self,) -> Optional[str]:
        """
        Gets the logoUrl property value. CDN URL to the application's logo, Read-only.
        Returns: Optional[str]
        """
        return self._logo_url
    
    @logo_url.setter
    def logo_url(self,value: Optional[str] = None) -> None:
        """
        Sets the logoUrl property value. CDN URL to the application's logo, Read-only.
        Args:
            value: Value to set for the logoUrl property.
        """
        self._logo_url = value
    
    @property
    def marketing_url(self,) -> Optional[str]:
        """
        Gets the marketingUrl property value. Link to the application's marketing page. For example, https://www.contoso.com/app/marketing
        Returns: Optional[str]
        """
        return self._marketing_url
    
    @marketing_url.setter
    def marketing_url(self,value: Optional[str] = None) -> None:
        """
        Sets the marketingUrl property value. Link to the application's marketing page. For example, https://www.contoso.com/app/marketing
        Args:
            value: Value to set for the marketingUrl property.
        """
        self._marketing_url = value
    
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
    def privacy_statement_url(self,) -> Optional[str]:
        """
        Gets the privacyStatementUrl property value. Link to the application's privacy statement. For example, https://www.contoso.com/app/privacy
        Returns: Optional[str]
        """
        return self._privacy_statement_url
    
    @privacy_statement_url.setter
    def privacy_statement_url(self,value: Optional[str] = None) -> None:
        """
        Sets the privacyStatementUrl property value. Link to the application's privacy statement. For example, https://www.contoso.com/app/privacy
        Args:
            value: Value to set for the privacyStatementUrl property.
        """
        self._privacy_statement_url = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("logoUrl", self.logo_url)
        writer.write_str_value("marketingUrl", self.marketing_url)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("privacyStatementUrl", self.privacy_statement_url)
        writer.write_str_value("supportUrl", self.support_url)
        writer.write_str_value("termsOfServiceUrl", self.terms_of_service_url)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def support_url(self,) -> Optional[str]:
        """
        Gets the supportUrl property value. Link to the application's support page. For example, https://www.contoso.com/app/support
        Returns: Optional[str]
        """
        return self._support_url
    
    @support_url.setter
    def support_url(self,value: Optional[str] = None) -> None:
        """
        Sets the supportUrl property value. Link to the application's support page. For example, https://www.contoso.com/app/support
        Args:
            value: Value to set for the supportUrl property.
        """
        self._support_url = value
    
    @property
    def terms_of_service_url(self,) -> Optional[str]:
        """
        Gets the termsOfServiceUrl property value. Link to the application's terms of service statement. For example, https://www.contoso.com/app/termsofservice
        Returns: Optional[str]
        """
        return self._terms_of_service_url
    
    @terms_of_service_url.setter
    def terms_of_service_url(self,value: Optional[str] = None) -> None:
        """
        Sets the termsOfServiceUrl property value. Link to the application's terms of service statement. For example, https://www.contoso.com/app/termsofservice
        Args:
            value: Value to set for the termsOfServiceUrl property.
        """
        self._terms_of_service_url = value
    

