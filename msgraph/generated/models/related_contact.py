from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

contact_relationship = lazy_import('msgraph.generated.models.contact_relationship')

class RelatedContact(AdditionalDataHolder, Parsable):
    @property
    def access_consent(self,) -> Optional[bool]:
        """
        Gets the accessConsent property value. Indicates whether the user has been consented to access student data.
        Returns: Optional[bool]
        """
        return self._access_consent
    
    @access_consent.setter
    def access_consent(self,value: Optional[bool] = None) -> None:
        """
        Sets the accessConsent property value. Indicates whether the user has been consented to access student data.
        Args:
            value: Value to set for the accessConsent property.
        """
        self._access_consent = value
    
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
        Instantiates a new relatedContact and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Indicates whether the user has been consented to access student data.
        self._access_consent: Optional[bool] = None
        # Name of the contact. Required.
        self._display_name: Optional[str] = None
        # Primary email address of the contact. Required.
        self._email_address: Optional[str] = None
        # Mobile phone number of the contact.
        self._mobile_phone: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The relationship property
        self._relationship: Optional[contact_relationship.ContactRelationship] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RelatedContact:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RelatedContact
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RelatedContact()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Name of the contact. Required.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Name of the contact. Required.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def email_address(self,) -> Optional[str]:
        """
        Gets the emailAddress property value. Primary email address of the contact. Required.
        Returns: Optional[str]
        """
        return self._email_address
    
    @email_address.setter
    def email_address(self,value: Optional[str] = None) -> None:
        """
        Sets the emailAddress property value. Primary email address of the contact. Required.
        Args:
            value: Value to set for the emailAddress property.
        """
        self._email_address = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "access_consent": lambda n : setattr(self, 'access_consent', n.get_bool_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "email_address": lambda n : setattr(self, 'email_address', n.get_str_value()),
            "mobile_phone": lambda n : setattr(self, 'mobile_phone', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "relationship": lambda n : setattr(self, 'relationship', n.get_enum_value(contact_relationship.ContactRelationship)),
        }
        return fields
    
    @property
    def mobile_phone(self,) -> Optional[str]:
        """
        Gets the mobilePhone property value. Mobile phone number of the contact.
        Returns: Optional[str]
        """
        return self._mobile_phone
    
    @mobile_phone.setter
    def mobile_phone(self,value: Optional[str] = None) -> None:
        """
        Sets the mobilePhone property value. Mobile phone number of the contact.
        Args:
            value: Value to set for the mobilePhone property.
        """
        self._mobile_phone = value
    
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
    def relationship(self,) -> Optional[contact_relationship.ContactRelationship]:
        """
        Gets the relationship property value. The relationship property
        Returns: Optional[contact_relationship.ContactRelationship]
        """
        return self._relationship
    
    @relationship.setter
    def relationship(self,value: Optional[contact_relationship.ContactRelationship] = None) -> None:
        """
        Sets the relationship property value. The relationship property
        Args:
            value: Value to set for the relationship property.
        """
        self._relationship = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_bool_value("accessConsent", self.access_consent)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("emailAddress", self.email_address)
        writer.write_str_value("mobilePhone", self.mobile_phone)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("relationship", self.relationship)
        writer.write_additional_data_value(self.additional_data)
    

