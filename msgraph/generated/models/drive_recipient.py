from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class DriveRecipient(AdditionalDataHolder, Parsable):
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
    def alias(self,) -> Optional[str]:
        """
        Gets the alias property value. The alias of the domain object, for cases where an email address is unavailable (e.g. security groups).
        Returns: Optional[str]
        """
        return self._alias
    
    @alias.setter
    def alias(self,value: Optional[str] = None) -> None:
        """
        Sets the alias property value. The alias of the domain object, for cases where an email address is unavailable (e.g. security groups).
        Args:
            value: Value to set for the alias property.
        """
        self._alias = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new driveRecipient and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The alias of the domain object, for cases where an email address is unavailable (e.g. security groups).
        self._alias: Optional[str] = None
        # The email address for the recipient, if the recipient has an associated email address.
        self._email: Optional[str] = None
        # The unique identifier for the recipient in the directory.
        self._object_id: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DriveRecipient:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DriveRecipient
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DriveRecipient()
    
    @property
    def email(self,) -> Optional[str]:
        """
        Gets the email property value. The email address for the recipient, if the recipient has an associated email address.
        Returns: Optional[str]
        """
        return self._email
    
    @email.setter
    def email(self,value: Optional[str] = None) -> None:
        """
        Sets the email property value. The email address for the recipient, if the recipient has an associated email address.
        Args:
            value: Value to set for the email property.
        """
        self._email = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "alias": lambda n : setattr(self, 'alias', n.get_str_value()),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "object_id": lambda n : setattr(self, 'object_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def object_id(self,) -> Optional[str]:
        """
        Gets the objectId property value. The unique identifier for the recipient in the directory.
        Returns: Optional[str]
        """
        return self._object_id
    
    @object_id.setter
    def object_id(self,value: Optional[str] = None) -> None:
        """
        Sets the objectId property value. The unique identifier for the recipient in the directory.
        Args:
            value: Value to set for the objectId property.
        """
        self._object_id = value
    
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
        writer.write_str_value("alias", self.alias)
        writer.write_str_value("email", self.email)
        writer.write_str_value("objectId", self.object_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

