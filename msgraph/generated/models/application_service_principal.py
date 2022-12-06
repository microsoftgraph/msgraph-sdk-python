from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

application = lazy_import('msgraph.generated.models.application')
service_principal = lazy_import('msgraph.generated.models.service_principal')

class ApplicationServicePrincipal(AdditionalDataHolder, Parsable):
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
    def application(self,) -> Optional[application.Application]:
        """
        Gets the application property value. The application property
        Returns: Optional[application.Application]
        """
        return self._application
    
    @application.setter
    def application(self,value: Optional[application.Application] = None) -> None:
        """
        Sets the application property value. The application property
        Args:
            value: Value to set for the application property.
        """
        self._application = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new applicationServicePrincipal and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The application property
        self._application: Optional[application.Application] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The servicePrincipal property
        self._service_principal: Optional[service_principal.ServicePrincipal] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ApplicationServicePrincipal:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ApplicationServicePrincipal
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ApplicationServicePrincipal()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "application": lambda n : setattr(self, 'application', n.get_object_value(application.Application)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "service_principal": lambda n : setattr(self, 'service_principal', n.get_object_value(service_principal.ServicePrincipal)),
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("application", self.application)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("servicePrincipal", self.service_principal)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def service_principal(self,) -> Optional[service_principal.ServicePrincipal]:
        """
        Gets the servicePrincipal property value. The servicePrincipal property
        Returns: Optional[service_principal.ServicePrincipal]
        """
        return self._service_principal
    
    @service_principal.setter
    def service_principal(self,value: Optional[service_principal.ServicePrincipal] = None) -> None:
        """
        Sets the servicePrincipal property value. The servicePrincipal property
        Args:
            value: Value to set for the servicePrincipal property.
        """
        self._service_principal = value
    

