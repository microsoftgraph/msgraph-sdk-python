from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

identity = lazy_import('msgraph.generated.models.identity')

class IdentitySet(AdditionalDataHolder, Parsable):
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
    def application(self,) -> Optional[identity.Identity]:
        """
        Gets the application property value. Optional. The application associated with this action.
        Returns: Optional[identity.Identity]
        """
        return self._application
    
    @application.setter
    def application(self,value: Optional[identity.Identity] = None) -> None:
        """
        Sets the application property value. Optional. The application associated with this action.
        Args:
            value: Value to set for the application property.
        """
        self._application = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new identitySet and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Optional. The application associated with this action.
        self._application: Optional[identity.Identity] = None
        # Optional. The device associated with this action.
        self._device: Optional[identity.Identity] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Optional. The user associated with this action.
        self._user: Optional[identity.Identity] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IdentitySet:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IdentitySet
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IdentitySet()
    
    @property
    def device(self,) -> Optional[identity.Identity]:
        """
        Gets the device property value. Optional. The device associated with this action.
        Returns: Optional[identity.Identity]
        """
        return self._device
    
    @device.setter
    def device(self,value: Optional[identity.Identity] = None) -> None:
        """
        Sets the device property value. Optional. The device associated with this action.
        Args:
            value: Value to set for the device property.
        """
        self._device = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "application": lambda n : setattr(self, 'application', n.get_object_value(identity.Identity)),
            "device": lambda n : setattr(self, 'device', n.get_object_value(identity.Identity)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "user": lambda n : setattr(self, 'user', n.get_object_value(identity.Identity)),
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
        writer.write_object_value("device", self.device)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("user", self.user)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def user(self,) -> Optional[identity.Identity]:
        """
        Gets the user property value. Optional. The user associated with this action.
        Returns: Optional[identity.Identity]
        """
        return self._user
    
    @user.setter
    def user(self,value: Optional[identity.Identity] = None) -> None:
        """
        Sets the user property value. Optional. The user associated with this action.
        Args:
            value: Value to set for the user property.
        """
        self._user = value
    

