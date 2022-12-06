from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

change_notification_encrypted_content = lazy_import('msgraph.generated.models.change_notification_encrypted_content')
change_type = lazy_import('msgraph.generated.models.change_type')
lifecycle_event_type = lazy_import('msgraph.generated.models.lifecycle_event_type')
resource_data = lazy_import('msgraph.generated.models.resource_data')

class ChangeNotification(AdditionalDataHolder, Parsable):
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
    def change_type(self,) -> Optional[change_type.ChangeType]:
        """
        Gets the changeType property value. The changeType property
        Returns: Optional[change_type.ChangeType]
        """
        return self._change_type
    
    @change_type.setter
    def change_type(self,value: Optional[change_type.ChangeType] = None) -> None:
        """
        Sets the changeType property value. The changeType property
        Args:
            value: Value to set for the changeType property.
        """
        self._change_type = value
    
    @property
    def client_state(self,) -> Optional[str]:
        """
        Gets the clientState property value. Value of the clientState property sent in the subscription request (if any). The maximum length is 255 characters. The client can check whether the change notification came from the service by comparing the values of the clientState property. The value of the clientState property sent with the subscription is compared with the value of the clientState property received with each change notification. Optional.
        Returns: Optional[str]
        """
        return self._client_state
    
    @client_state.setter
    def client_state(self,value: Optional[str] = None) -> None:
        """
        Sets the clientState property value. Value of the clientState property sent in the subscription request (if any). The maximum length is 255 characters. The client can check whether the change notification came from the service by comparing the values of the clientState property. The value of the clientState property sent with the subscription is compared with the value of the clientState property received with each change notification. Optional.
        Args:
            value: Value to set for the clientState property.
        """
        self._client_state = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new changeNotification and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The changeType property
        self._change_type: Optional[change_type.ChangeType] = None
        # Value of the clientState property sent in the subscription request (if any). The maximum length is 255 characters. The client can check whether the change notification came from the service by comparing the values of the clientState property. The value of the clientState property sent with the subscription is compared with the value of the clientState property received with each change notification. Optional.
        self._client_state: Optional[str] = None
        # (Preview) Encrypted content attached with the change notification. Only provided if encryptionCertificate and includeResourceData were defined during the subscription request and if the resource supports it. Optional.
        self._encrypted_content: Optional[change_notification_encrypted_content.ChangeNotificationEncryptedContent] = None
        # Unique ID for the notification. Optional.
        self._id: Optional[str] = None
        # The type of lifecycle notification if the current notification is a lifecycle notification. Optional. Supported values are missed, subscriptionRemoved, reauthorizationRequired. Optional.
        self._lifecycle_event: Optional[lifecycle_event_type.LifecycleEventType] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The URI of the resource that emitted the change notification relative to https://graph.microsoft.com. Required.
        self._resource: Optional[str] = None
        # The content of this property depends on the type of resource being subscribed to. Optional.
        self._resource_data: Optional[resource_data.ResourceData] = None
        # The expiration time for the subscription. Required.
        self._subscription_expiration_date_time: Optional[datetime] = None
        # The unique identifier of the subscription that generated the notification.Required.
        self._subscription_id: Optional[str] = None
        # The unique identifier of the tenant from which the change notification originated. Required.
        self._tenant_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ChangeNotification:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ChangeNotification
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ChangeNotification()
    
    @property
    def encrypted_content(self,) -> Optional[change_notification_encrypted_content.ChangeNotificationEncryptedContent]:
        """
        Gets the encryptedContent property value. (Preview) Encrypted content attached with the change notification. Only provided if encryptionCertificate and includeResourceData were defined during the subscription request and if the resource supports it. Optional.
        Returns: Optional[change_notification_encrypted_content.ChangeNotificationEncryptedContent]
        """
        return self._encrypted_content
    
    @encrypted_content.setter
    def encrypted_content(self,value: Optional[change_notification_encrypted_content.ChangeNotificationEncryptedContent] = None) -> None:
        """
        Sets the encryptedContent property value. (Preview) Encrypted content attached with the change notification. Only provided if encryptionCertificate and includeResourceData were defined during the subscription request and if the resource supports it. Optional.
        Args:
            value: Value to set for the encryptedContent property.
        """
        self._encrypted_content = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "change_type": lambda n : setattr(self, 'change_type', n.get_enum_value(change_type.ChangeType)),
            "client_state": lambda n : setattr(self, 'client_state', n.get_str_value()),
            "encrypted_content": lambda n : setattr(self, 'encrypted_content', n.get_object_value(change_notification_encrypted_content.ChangeNotificationEncryptedContent)),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "lifecycle_event": lambda n : setattr(self, 'lifecycle_event', n.get_enum_value(lifecycle_event_type.LifecycleEventType)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "resource": lambda n : setattr(self, 'resource', n.get_str_value()),
            "resource_data": lambda n : setattr(self, 'resource_data', n.get_object_value(resource_data.ResourceData)),
            "subscription_expiration_date_time": lambda n : setattr(self, 'subscription_expiration_date_time', n.get_datetime_value()),
            "subscription_id": lambda n : setattr(self, 'subscription_id', n.get_str_value()),
            "tenant_id": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
        }
        return fields
    
    @property
    def id(self,) -> Optional[str]:
        """
        Gets the id property value. Unique ID for the notification. Optional.
        Returns: Optional[str]
        """
        return self._id
    
    @id.setter
    def id(self,value: Optional[str] = None) -> None:
        """
        Sets the id property value. Unique ID for the notification. Optional.
        Args:
            value: Value to set for the id property.
        """
        self._id = value
    
    @property
    def lifecycle_event(self,) -> Optional[lifecycle_event_type.LifecycleEventType]:
        """
        Gets the lifecycleEvent property value. The type of lifecycle notification if the current notification is a lifecycle notification. Optional. Supported values are missed, subscriptionRemoved, reauthorizationRequired. Optional.
        Returns: Optional[lifecycle_event_type.LifecycleEventType]
        """
        return self._lifecycle_event
    
    @lifecycle_event.setter
    def lifecycle_event(self,value: Optional[lifecycle_event_type.LifecycleEventType] = None) -> None:
        """
        Sets the lifecycleEvent property value. The type of lifecycle notification if the current notification is a lifecycle notification. Optional. Supported values are missed, subscriptionRemoved, reauthorizationRequired. Optional.
        Args:
            value: Value to set for the lifecycleEvent property.
        """
        self._lifecycle_event = value
    
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
    def resource(self,) -> Optional[str]:
        """
        Gets the resource property value. The URI of the resource that emitted the change notification relative to https://graph.microsoft.com. Required.
        Returns: Optional[str]
        """
        return self._resource
    
    @resource.setter
    def resource(self,value: Optional[str] = None) -> None:
        """
        Sets the resource property value. The URI of the resource that emitted the change notification relative to https://graph.microsoft.com. Required.
        Args:
            value: Value to set for the resource property.
        """
        self._resource = value
    
    @property
    def resource_data(self,) -> Optional[resource_data.ResourceData]:
        """
        Gets the resourceData property value. The content of this property depends on the type of resource being subscribed to. Optional.
        Returns: Optional[resource_data.ResourceData]
        """
        return self._resource_data
    
    @resource_data.setter
    def resource_data(self,value: Optional[resource_data.ResourceData] = None) -> None:
        """
        Sets the resourceData property value. The content of this property depends on the type of resource being subscribed to. Optional.
        Args:
            value: Value to set for the resourceData property.
        """
        self._resource_data = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_enum_value("changeType", self.change_type)
        writer.write_str_value("clientState", self.client_state)
        writer.write_object_value("encryptedContent", self.encrypted_content)
        writer.write_str_value("id", self.id)
        writer.write_enum_value("lifecycleEvent", self.lifecycle_event)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("resource", self.resource)
        writer.write_object_value("resourceData", self.resource_data)
        writer.write_datetime_value("subscriptionExpirationDateTime", self.subscription_expiration_date_time)
        writer.write_str_value("subscriptionId", self.subscription_id)
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def subscription_expiration_date_time(self,) -> Optional[datetime]:
        """
        Gets the subscriptionExpirationDateTime property value. The expiration time for the subscription. Required.
        Returns: Optional[datetime]
        """
        return self._subscription_expiration_date_time
    
    @subscription_expiration_date_time.setter
    def subscription_expiration_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the subscriptionExpirationDateTime property value. The expiration time for the subscription. Required.
        Args:
            value: Value to set for the subscriptionExpirationDateTime property.
        """
        self._subscription_expiration_date_time = value
    
    @property
    def subscription_id(self,) -> Optional[str]:
        """
        Gets the subscriptionId property value. The unique identifier of the subscription that generated the notification.Required.
        Returns: Optional[str]
        """
        return self._subscription_id
    
    @subscription_id.setter
    def subscription_id(self,value: Optional[str] = None) -> None:
        """
        Sets the subscriptionId property value. The unique identifier of the subscription that generated the notification.Required.
        Args:
            value: Value to set for the subscriptionId property.
        """
        self._subscription_id = value
    
    @property
    def tenant_id(self,) -> Optional[str]:
        """
        Gets the tenantId property value. The unique identifier of the tenant from which the change notification originated. Required.
        Returns: Optional[str]
        """
        return self._tenant_id
    
    @tenant_id.setter
    def tenant_id(self,value: Optional[str] = None) -> None:
        """
        Sets the tenantId property value. The unique identifier of the tenant from which the change notification originated. Required.
        Args:
            value: Value to set for the tenantId property.
        """
        self._tenant_id = value
    

