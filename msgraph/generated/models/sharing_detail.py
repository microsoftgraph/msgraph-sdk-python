from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import insight_identity, resource_reference

class SharingDetail(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new sharingDetail and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # The user who shared the document.
        self._shared_by: Optional[insight_identity.InsightIdentity] = None
        # The date and time the file was last shared. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
        self._shared_date_time: Optional[datetime] = None
        # The sharingReference property
        self._sharing_reference: Optional[resource_reference.ResourceReference] = None
        # The subject with which the document was shared.
        self._sharing_subject: Optional[str] = None
        # Determines the way the document was shared, can be by a 'Link', 'Attachment', 'Group', 'Site'.
        self._sharing_type: Optional[str] = None
    
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
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SharingDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SharingDetail
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SharingDetail()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import insight_identity, resource_reference

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "sharedBy": lambda n : setattr(self, 'shared_by', n.get_object_value(insight_identity.InsightIdentity)),
            "sharedDateTime": lambda n : setattr(self, 'shared_date_time', n.get_datetime_value()),
            "sharingReference": lambda n : setattr(self, 'sharing_reference', n.get_object_value(resource_reference.ResourceReference)),
            "sharingSubject": lambda n : setattr(self, 'sharing_subject', n.get_str_value()),
            "sharingType": lambda n : setattr(self, 'sharing_type', n.get_str_value()),
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
            value: Value to set for the odata_type property.
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("sharedBy", self.shared_by)
        writer.write_datetime_value("sharedDateTime", self.shared_date_time)
        writer.write_str_value("sharingSubject", self.sharing_subject)
        writer.write_str_value("sharingType", self.sharing_type)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def shared_by(self,) -> Optional[insight_identity.InsightIdentity]:
        """
        Gets the sharedBy property value. The user who shared the document.
        Returns: Optional[insight_identity.InsightIdentity]
        """
        return self._shared_by
    
    @shared_by.setter
    def shared_by(self,value: Optional[insight_identity.InsightIdentity] = None) -> None:
        """
        Sets the sharedBy property value. The user who shared the document.
        Args:
            value: Value to set for the shared_by property.
        """
        self._shared_by = value
    
    @property
    def shared_date_time(self,) -> Optional[datetime]:
        """
        Gets the sharedDateTime property value. The date and time the file was last shared. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
        Returns: Optional[datetime]
        """
        return self._shared_date_time
    
    @shared_date_time.setter
    def shared_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the sharedDateTime property value. The date and time the file was last shared. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
        Args:
            value: Value to set for the shared_date_time property.
        """
        self._shared_date_time = value
    
    @property
    def sharing_reference(self,) -> Optional[resource_reference.ResourceReference]:
        """
        Gets the sharingReference property value. The sharingReference property
        Returns: Optional[resource_reference.ResourceReference]
        """
        return self._sharing_reference
    
    @sharing_reference.setter
    def sharing_reference(self,value: Optional[resource_reference.ResourceReference] = None) -> None:
        """
        Sets the sharingReference property value. The sharingReference property
        Args:
            value: Value to set for the sharing_reference property.
        """
        self._sharing_reference = value
    
    @property
    def sharing_subject(self,) -> Optional[str]:
        """
        Gets the sharingSubject property value. The subject with which the document was shared.
        Returns: Optional[str]
        """
        return self._sharing_subject
    
    @sharing_subject.setter
    def sharing_subject(self,value: Optional[str] = None) -> None:
        """
        Sets the sharingSubject property value. The subject with which the document was shared.
        Args:
            value: Value to set for the sharing_subject property.
        """
        self._sharing_subject = value
    
    @property
    def sharing_type(self,) -> Optional[str]:
        """
        Gets the sharingType property value. Determines the way the document was shared, can be by a 'Link', 'Attachment', 'Group', 'Site'.
        Returns: Optional[str]
        """
        return self._sharing_type
    
    @sharing_type.setter
    def sharing_type(self,value: Optional[str] = None) -> None:
        """
        Sets the sharingType property value. Determines the way the document was shared, can be by a 'Link', 'Attachment', 'Group', 'Site'.
        Args:
            value: Value to set for the sharing_type property.
        """
        self._sharing_type = value
    

