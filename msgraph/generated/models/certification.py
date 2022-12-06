from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class Certification(AdditionalDataHolder, Parsable):
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
    
    @property
    def certification_details_url(self,) -> Optional[str]:
        """
        Gets the certificationDetailsUrl property value. URL that shows certification details for the application.
        Returns: Optional[str]
        """
        return self._certification_details_url
    
    @certification_details_url.setter
    def certification_details_url(self,value: Optional[str] = None) -> None:
        """
        Sets the certificationDetailsUrl property value. URL that shows certification details for the application.
        Args:
            value: Value to set for the certificationDetailsUrl property.
        """
        self._certification_details_url = value
    
    @property
    def certification_expiration_date_time(self,) -> Optional[datetime]:
        """
        Gets the certificationExpirationDateTime property value. The timestamp when the current certification for the application will expire.
        Returns: Optional[datetime]
        """
        return self._certification_expiration_date_time
    
    @certification_expiration_date_time.setter
    def certification_expiration_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the certificationExpirationDateTime property value. The timestamp when the current certification for the application will expire.
        Args:
            value: Value to set for the certificationExpirationDateTime property.
        """
        self._certification_expiration_date_time = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new certification and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # URL that shows certification details for the application.
        self._certification_details_url: Optional[str] = None
        # The timestamp when the current certification for the application will expire.
        self._certification_expiration_date_time: Optional[datetime] = None
        # Indicates whether the application is certified by Microsoft.
        self._is_certified_by_microsoft: Optional[bool] = None
        # Indicates whether the application has been self-attested by the application developer or the publisher.
        self._is_publisher_attested: Optional[bool] = None
        # The timestamp when the certification for the application was most recently added or updated.
        self._last_certification_date_time: Optional[datetime] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Certification:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Certification
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Certification()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "certification_details_url": lambda n : setattr(self, 'certification_details_url', n.get_str_value()),
            "certification_expiration_date_time": lambda n : setattr(self, 'certification_expiration_date_time', n.get_datetime_value()),
            "is_certified_by_microsoft": lambda n : setattr(self, 'is_certified_by_microsoft', n.get_bool_value()),
            "is_publisher_attested": lambda n : setattr(self, 'is_publisher_attested', n.get_bool_value()),
            "last_certification_date_time": lambda n : setattr(self, 'last_certification_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def is_certified_by_microsoft(self,) -> Optional[bool]:
        """
        Gets the isCertifiedByMicrosoft property value. Indicates whether the application is certified by Microsoft.
        Returns: Optional[bool]
        """
        return self._is_certified_by_microsoft
    
    @is_certified_by_microsoft.setter
    def is_certified_by_microsoft(self,value: Optional[bool] = None) -> None:
        """
        Sets the isCertifiedByMicrosoft property value. Indicates whether the application is certified by Microsoft.
        Args:
            value: Value to set for the isCertifiedByMicrosoft property.
        """
        self._is_certified_by_microsoft = value
    
    @property
    def is_publisher_attested(self,) -> Optional[bool]:
        """
        Gets the isPublisherAttested property value. Indicates whether the application has been self-attested by the application developer or the publisher.
        Returns: Optional[bool]
        """
        return self._is_publisher_attested
    
    @is_publisher_attested.setter
    def is_publisher_attested(self,value: Optional[bool] = None) -> None:
        """
        Sets the isPublisherAttested property value. Indicates whether the application has been self-attested by the application developer or the publisher.
        Args:
            value: Value to set for the isPublisherAttested property.
        """
        self._is_publisher_attested = value
    
    @property
    def last_certification_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastCertificationDateTime property value. The timestamp when the certification for the application was most recently added or updated.
        Returns: Optional[datetime]
        """
        return self._last_certification_date_time
    
    @last_certification_date_time.setter
    def last_certification_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastCertificationDateTime property value. The timestamp when the certification for the application was most recently added or updated.
        Args:
            value: Value to set for the lastCertificationDateTime property.
        """
        self._last_certification_date_time = value
    
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_datetime_value("certificationExpirationDateTime", self.certification_expiration_date_time)
        writer.write_bool_value("isPublisherAttested", self.is_publisher_attested)
        writer.write_datetime_value("lastCertificationDateTime", self.last_certification_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

