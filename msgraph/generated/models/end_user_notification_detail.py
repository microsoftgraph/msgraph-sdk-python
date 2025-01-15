from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .email_identity import EmailIdentity
    from .entity import Entity

from .entity import Entity

@dataclass
class EndUserNotificationDetail(Entity, Parsable):
    # Email HTML content.
    email_content: Optional[str] = None
    # Indicates whether this language is default.
    is_default_langauge: Optional[bool] = None
    # Notification language.
    language: Optional[str] = None
    # Notification locale.
    locale: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The sentFrom property
    sent_from: Optional[EmailIdentity] = None
    # Mail subject.
    subject: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EndUserNotificationDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EndUserNotificationDetail
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EndUserNotificationDetail()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .email_identity import EmailIdentity
        from .entity import Entity

        from .email_identity import EmailIdentity
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "emailContent": lambda n : setattr(self, 'email_content', n.get_str_value()),
            "isDefaultLangauge": lambda n : setattr(self, 'is_default_langauge', n.get_bool_value()),
            "language": lambda n : setattr(self, 'language', n.get_str_value()),
            "locale": lambda n : setattr(self, 'locale', n.get_str_value()),
            "sentFrom": lambda n : setattr(self, 'sent_from', n.get_object_value(EmailIdentity)),
            "subject": lambda n : setattr(self, 'subject', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("emailContent", self.email_content)
        writer.write_bool_value("isDefaultLangauge", self.is_default_langauge)
        writer.write_str_value("language", self.language)
        writer.write_str_value("locale", self.locale)
        writer.write_object_value("sentFrom", self.sent_from)
        writer.write_str_value("subject", self.subject)
    

