from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

mail_tips_type = lazy_import('msgraph.generated.models.mail_tips_type')

class GetMailTipsPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the getMailTips method.
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new getMailTipsPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The EmailAddresses property
        self._email_addresses: Optional[List[str]] = None
        # The MailTipsOptions property
        self._mail_tips_options: Optional[mail_tips_type.MailTipsType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GetMailTipsPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: GetMailTipsPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return GetMailTipsPostRequestBody()
    
    @property
    def email_addresses(self,) -> Optional[List[str]]:
        """
        Gets the emailAddresses property value. The EmailAddresses property
        Returns: Optional[List[str]]
        """
        return self._email_addresses
    
    @email_addresses.setter
    def email_addresses(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the emailAddresses property value. The EmailAddresses property
        Args:
            value: Value to set for the EmailAddresses property.
        """
        self._email_addresses = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "email_addresses": lambda n : setattr(self, 'email_addresses', n.get_collection_of_primitive_values(str)),
            "mail_tips_options": lambda n : setattr(self, 'mail_tips_options', n.get_enum_value(mail_tips_type.MailTipsType)),
        }
        return fields
    
    @property
    def mail_tips_options(self,) -> Optional[mail_tips_type.MailTipsType]:
        """
        Gets the mailTipsOptions property value. The MailTipsOptions property
        Returns: Optional[mail_tips_type.MailTipsType]
        """
        return self._mail_tips_options
    
    @mail_tips_options.setter
    def mail_tips_options(self,value: Optional[mail_tips_type.MailTipsType] = None) -> None:
        """
        Sets the mailTipsOptions property value. The MailTipsOptions property
        Args:
            value: Value to set for the MailTipsOptions property.
        """
        self._mail_tips_options = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_primitive_values("EmailAddresses", self.email_addresses)
        writer.write_enum_value("MailTipsOptions", self.mail_tips_options)
        writer.write_additional_data_value(self.additional_data)
    

