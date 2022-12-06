from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class LocalizedNotificationMessage(entity.Entity):
    """
    The text content of a Notification Message Template for the specified locale.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new localizedNotificationMessage and sets the default values.
        """
        super().__init__()
        # Flag to indicate whether or not this is the default locale for language fallback. This flag can only be set. To unset, set this property to true on another Localized Notification Message.
        self._is_default: Optional[bool] = None
        # DateTime the object was last modified.
        self._last_modified_date_time: Optional[datetime] = None
        # The Locale for which this message is destined.
        self._locale: Optional[str] = None
        # The Message Template content.
        self._message_template: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The Message Template Subject.
        self._subject: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> LocalizedNotificationMessage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: LocalizedNotificationMessage
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return LocalizedNotificationMessage()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "is_default": lambda n : setattr(self, 'is_default', n.get_bool_value()),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "locale": lambda n : setattr(self, 'locale', n.get_str_value()),
            "message_template": lambda n : setattr(self, 'message_template', n.get_str_value()),
            "subject": lambda n : setattr(self, 'subject', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_default(self,) -> Optional[bool]:
        """
        Gets the isDefault property value. Flag to indicate whether or not this is the default locale for language fallback. This flag can only be set. To unset, set this property to true on another Localized Notification Message.
        Returns: Optional[bool]
        """
        return self._is_default
    
    @is_default.setter
    def is_default(self,value: Optional[bool] = None) -> None:
        """
        Sets the isDefault property value. Flag to indicate whether or not this is the default locale for language fallback. This flag can only be set. To unset, set this property to true on another Localized Notification Message.
        Args:
            value: Value to set for the isDefault property.
        """
        self._is_default = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. DateTime the object was last modified.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. DateTime the object was last modified.
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    @property
    def locale(self,) -> Optional[str]:
        """
        Gets the locale property value. The Locale for which this message is destined.
        Returns: Optional[str]
        """
        return self._locale
    
    @locale.setter
    def locale(self,value: Optional[str] = None) -> None:
        """
        Sets the locale property value. The Locale for which this message is destined.
        Args:
            value: Value to set for the locale property.
        """
        self._locale = value
    
    @property
    def message_template(self,) -> Optional[str]:
        """
        Gets the messageTemplate property value. The Message Template content.
        Returns: Optional[str]
        """
        return self._message_template
    
    @message_template.setter
    def message_template(self,value: Optional[str] = None) -> None:
        """
        Sets the messageTemplate property value. The Message Template content.
        Args:
            value: Value to set for the messageTemplate property.
        """
        self._message_template = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("isDefault", self.is_default)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("locale", self.locale)
        writer.write_str_value("messageTemplate", self.message_template)
        writer.write_str_value("subject", self.subject)
    
    @property
    def subject(self,) -> Optional[str]:
        """
        Gets the subject property value. The Message Template Subject.
        Returns: Optional[str]
        """
        return self._subject
    
    @subject.setter
    def subject(self,value: Optional[str] = None) -> None:
        """
        Sets the subject property value. The Message Template Subject.
        Args:
            value: Value to set for the subject property.
        """
        self._subject = value
    

