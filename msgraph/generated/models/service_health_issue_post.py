from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

item_body = lazy_import('msgraph.generated.models.item_body')
post_type = lazy_import('msgraph.generated.models.post_type')

class ServiceHealthIssuePost(AdditionalDataHolder, Parsable):
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
        Instantiates a new serviceHealthIssuePost and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The published time of the post.
        self._created_date_time: Optional[datetime] = None
        # The content of the service issue post. The supported value for the contentType property is html.
        self._description: Optional[item_body.ItemBody] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The post type of the service issue historical post. Possible values are: regular, quick, strategic, unknownFutureValue.
        self._post_type: Optional[post_type.PostType] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The published time of the post.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The published time of the post.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ServiceHealthIssuePost:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ServiceHealthIssuePost
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ServiceHealthIssuePost()
    
    @property
    def description(self,) -> Optional[item_body.ItemBody]:
        """
        Gets the description property value. The content of the service issue post. The supported value for the contentType property is html.
        Returns: Optional[item_body.ItemBody]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[item_body.ItemBody] = None) -> None:
        """
        Sets the description property value. The content of the service issue post. The supported value for the contentType property is html.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_object_value(item_body.ItemBody)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "post_type": lambda n : setattr(self, 'post_type', n.get_enum_value(post_type.PostType)),
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
    
    @property
    def post_type(self,) -> Optional[post_type.PostType]:
        """
        Gets the postType property value. The post type of the service issue historical post. Possible values are: regular, quick, strategic, unknownFutureValue.
        Returns: Optional[post_type.PostType]
        """
        return self._post_type
    
    @post_type.setter
    def post_type(self,value: Optional[post_type.PostType] = None) -> None:
        """
        Sets the postType property value. The post type of the service issue historical post. Possible values are: regular, quick, strategic, unknownFutureValue.
        Args:
            value: Value to set for the postType property.
        """
        self._post_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("description", self.description)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("postType", self.post_type)
        writer.write_additional_data_value(self.additional_data)
    

