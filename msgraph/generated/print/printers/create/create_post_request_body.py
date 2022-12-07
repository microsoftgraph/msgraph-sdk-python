from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

print_certificate_signing_request = lazy_import('msgraph.generated.models.print_certificate_signing_request')

class CreatePostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the create method.
    """
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
    def certificate_signing_request(self,) -> Optional[print_certificate_signing_request.PrintCertificateSigningRequest]:
        """
        Gets the certificateSigningRequest property value. The certificateSigningRequest property
        Returns: Optional[print_certificate_signing_request.PrintCertificateSigningRequest]
        """
        return self._certificate_signing_request
    
    @certificate_signing_request.setter
    def certificate_signing_request(self,value: Optional[print_certificate_signing_request.PrintCertificateSigningRequest] = None) -> None:
        """
        Sets the certificateSigningRequest property value. The certificateSigningRequest property
        Args:
            value: Value to set for the certificateSigningRequest property.
        """
        self._certificate_signing_request = value
    
    @property
    def connector_id(self,) -> Optional[str]:
        """
        Gets the connectorId property value. The connectorId property
        Returns: Optional[str]
        """
        return self._connector_id
    
    @connector_id.setter
    def connector_id(self,value: Optional[str] = None) -> None:
        """
        Sets the connectorId property value. The connectorId property
        Args:
            value: Value to set for the connectorId property.
        """
        self._connector_id = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new createPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The certificateSigningRequest property
        self._certificate_signing_request: Optional[print_certificate_signing_request.PrintCertificateSigningRequest] = None
        # The connectorId property
        self._connector_id: Optional[str] = None
        # The displayName property
        self._display_name: Optional[str] = None
        # The hasPhysicalDevice property
        self._has_physical_device: Optional[bool] = None
        # The manufacturer property
        self._manufacturer: Optional[str] = None
        # The model property
        self._model: Optional[str] = None
        # The physicalDeviceId property
        self._physical_device_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CreatePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CreatePostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CreatePostRequestBody()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The displayName property
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The displayName property
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "certificate_signing_request": lambda n : setattr(self, 'certificate_signing_request', n.get_object_value(print_certificate_signing_request.PrintCertificateSigningRequest)),
            "connector_id": lambda n : setattr(self, 'connector_id', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "has_physical_device": lambda n : setattr(self, 'has_physical_device', n.get_bool_value()),
            "manufacturer": lambda n : setattr(self, 'manufacturer', n.get_str_value()),
            "model": lambda n : setattr(self, 'model', n.get_str_value()),
            "physical_device_id": lambda n : setattr(self, 'physical_device_id', n.get_str_value()),
        }
        return fields
    
    @property
    def has_physical_device(self,) -> Optional[bool]:
        """
        Gets the hasPhysicalDevice property value. The hasPhysicalDevice property
        Returns: Optional[bool]
        """
        return self._has_physical_device
    
    @has_physical_device.setter
    def has_physical_device(self,value: Optional[bool] = None) -> None:
        """
        Sets the hasPhysicalDevice property value. The hasPhysicalDevice property
        Args:
            value: Value to set for the hasPhysicalDevice property.
        """
        self._has_physical_device = value
    
    @property
    def manufacturer(self,) -> Optional[str]:
        """
        Gets the manufacturer property value. The manufacturer property
        Returns: Optional[str]
        """
        return self._manufacturer
    
    @manufacturer.setter
    def manufacturer(self,value: Optional[str] = None) -> None:
        """
        Sets the manufacturer property value. The manufacturer property
        Args:
            value: Value to set for the manufacturer property.
        """
        self._manufacturer = value
    
    @property
    def model(self,) -> Optional[str]:
        """
        Gets the model property value. The model property
        Returns: Optional[str]
        """
        return self._model
    
    @model.setter
    def model(self,value: Optional[str] = None) -> None:
        """
        Sets the model property value. The model property
        Args:
            value: Value to set for the model property.
        """
        self._model = value
    
    @property
    def physical_device_id(self,) -> Optional[str]:
        """
        Gets the physicalDeviceId property value. The physicalDeviceId property
        Returns: Optional[str]
        """
        return self._physical_device_id
    
    @physical_device_id.setter
    def physical_device_id(self,value: Optional[str] = None) -> None:
        """
        Sets the physicalDeviceId property value. The physicalDeviceId property
        Args:
            value: Value to set for the physicalDeviceId property.
        """
        self._physical_device_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("certificateSigningRequest", self.certificate_signing_request)
        writer.write_str_value("connectorId", self.connector_id)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("hasPhysicalDevice", self.has_physical_device)
        writer.write_str_value("manufacturer", self.manufacturer)
        writer.write_str_value("model", self.model)
        writer.write_str_value("physicalDeviceId", self.physical_device_id)
        writer.write_additional_data_value(self.additional_data)
    

