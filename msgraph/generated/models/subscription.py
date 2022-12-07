from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class Subscription(entity.Entity):
    """
    Provides operations to manage the collection of agreement entities.
    """
    @property
    def application_id(self,) -> Optional[str]:
        """
        Gets the applicationId property value. Optional. Identifier of the application used to create the subscription. Read-only.
        Returns: Optional[str]
        """
        return self._application_id
    
    @application_id.setter
    def application_id(self,value: Optional[str] = None) -> None:
        """
        Sets the applicationId property value. Optional. Identifier of the application used to create the subscription. Read-only.
        Args:
            value: Value to set for the applicationId property.
        """
        self._application_id = value
    
    @property
    def change_type(self,) -> Optional[str]:
        """
        Gets the changeType property value. Required. Indicates the type of change in the subscribed resource that will raise a change notification. The supported values are: created, updated, deleted. Multiple values can be combined using a comma-separated list. Note:  Drive root item and list change notifications support only the updated changeType. User and group change notifications support updated and deleted changeType.
        Returns: Optional[str]
        """
        return self._change_type
    
    @change_type.setter
    def change_type(self,value: Optional[str] = None) -> None:
        """
        Sets the changeType property value. Required. Indicates the type of change in the subscribed resource that will raise a change notification. The supported values are: created, updated, deleted. Multiple values can be combined using a comma-separated list. Note:  Drive root item and list change notifications support only the updated changeType. User and group change notifications support updated and deleted changeType.
        Args:
            value: Value to set for the changeType property.
        """
        self._change_type = value
    
    @property
    def client_state(self,) -> Optional[str]:
        """
        Gets the clientState property value. Optional. Specifies the value of the clientState property sent by the service in each change notification. The maximum length is 128 characters. The client can check that the change notification came from the service by comparing the value of the clientState property sent with the subscription with the value of the clientState property received with each change notification.
        Returns: Optional[str]
        """
        return self._client_state
    
    @client_state.setter
    def client_state(self,value: Optional[str] = None) -> None:
        """
        Sets the clientState property value. Optional. Specifies the value of the clientState property sent by the service in each change notification. The maximum length is 128 characters. The client can check that the change notification came from the service by comparing the value of the clientState property sent with the subscription with the value of the clientState property received with each change notification.
        Args:
            value: Value to set for the clientState property.
        """
        self._client_state = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new subscription and sets the default values.
        """
        super().__init__()
        # Optional. Identifier of the application used to create the subscription. Read-only.
        self._application_id: Optional[str] = None
        # Required. Indicates the type of change in the subscribed resource that will raise a change notification. The supported values are: created, updated, deleted. Multiple values can be combined using a comma-separated list. Note:  Drive root item and list change notifications support only the updated changeType. User and group change notifications support updated and deleted changeType.
        self._change_type: Optional[str] = None
        # Optional. Specifies the value of the clientState property sent by the service in each change notification. The maximum length is 128 characters. The client can check that the change notification came from the service by comparing the value of the clientState property sent with the subscription with the value of the clientState property received with each change notification.
        self._client_state: Optional[str] = None
        # Optional. Identifier of the user or service principal that created the subscription. If the app used delegated permissions to create the subscription, this field contains the id of the signed-in user the app called on behalf of. If the app used application permissions, this field contains the id of the service principal corresponding to the app. Read-only.
        self._creator_id: Optional[str] = None
        # Optional. A base64-encoded representation of a certificate with a public key used to encrypt resource data in change notifications. Optional but required when includeResourceData is true.
        self._encryption_certificate: Optional[str] = None
        # Optional. A custom app-provided identifier to help identify the certificate needed to decrypt resource data.
        self._encryption_certificate_id: Optional[str] = None
        # Required. Specifies the date and time when the webhook subscription expires. The time is in UTC, and can be an amount of time from subscription creation that varies for the resource subscribed to. For the maximum supported subscription length of time, see the table below.
        self._expiration_date_time: Optional[datetime] = None
        # Optional. When set to true, change notifications include resource data (such as content of a chat message).
        self._include_resource_data: Optional[bool] = None
        # Optional. Specifies the latest version of Transport Layer Security (TLS) that the notification endpoint, specified by notificationUrl, supports. The possible values are: v1_0, v1_1, v1_2, v1_3. For subscribers whose notification endpoint supports a version lower than the currently recommended version (TLS 1.2), specifying this property by a set timeline allows them to temporarily use their deprecated version of TLS before completing their upgrade to TLS 1.2. For these subscribers, not setting this property per the timeline would result in subscription operations failing. For subscribers whose notification endpoint already supports TLS 1.2, setting this property is optional. In such cases, Microsoft Graph defaults the property to v1_2.
        self._latest_supported_tls_version: Optional[str] = None
        # Optional. The URL of the endpoint that receives lifecycle notifications, including subscriptionRemoved and missed notifications. This URL must make use of the HTTPS protocol.
        self._lifecycle_notification_url: Optional[str] = None
        # Optional. OData query options for specifying value for the targeting resource. Clients receive notifications when resource reaches the state matching the query options provided here. With this new property in the subscription creation payload along with all existing properties, Webhooks will deliver notifications whenever a resource reaches the desired state mentioned in the notificationQueryOptions property. For example, when the print job is completed or when a print job resource isFetchable property value becomes true etc.
        self._notification_query_options: Optional[str] = None
        # Required. The URL of the endpoint that will receive the change notifications. This URL must make use of the HTTPS protocol.
        self._notification_url: Optional[str] = None
        # Optional. The app ID that the subscription service can use to generate the validation token. This allows the client to validate the authenticity of the notification received.
        self._notification_url_app_id: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Required. Specifies the resource that will be monitored for changes. Do not include the base URL (https://graph.microsoft.com/v1.0/). See the possible resource path values for each supported resource.
        self._resource: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Subscription:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Subscription
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Subscription()
    
    @property
    def creator_id(self,) -> Optional[str]:
        """
        Gets the creatorId property value. Optional. Identifier of the user or service principal that created the subscription. If the app used delegated permissions to create the subscription, this field contains the id of the signed-in user the app called on behalf of. If the app used application permissions, this field contains the id of the service principal corresponding to the app. Read-only.
        Returns: Optional[str]
        """
        return self._creator_id
    
    @creator_id.setter
    def creator_id(self,value: Optional[str] = None) -> None:
        """
        Sets the creatorId property value. Optional. Identifier of the user or service principal that created the subscription. If the app used delegated permissions to create the subscription, this field contains the id of the signed-in user the app called on behalf of. If the app used application permissions, this field contains the id of the service principal corresponding to the app. Read-only.
        Args:
            value: Value to set for the creatorId property.
        """
        self._creator_id = value
    
    @property
    def encryption_certificate(self,) -> Optional[str]:
        """
        Gets the encryptionCertificate property value. Optional. A base64-encoded representation of a certificate with a public key used to encrypt resource data in change notifications. Optional but required when includeResourceData is true.
        Returns: Optional[str]
        """
        return self._encryption_certificate
    
    @encryption_certificate.setter
    def encryption_certificate(self,value: Optional[str] = None) -> None:
        """
        Sets the encryptionCertificate property value. Optional. A base64-encoded representation of a certificate with a public key used to encrypt resource data in change notifications. Optional but required when includeResourceData is true.
        Args:
            value: Value to set for the encryptionCertificate property.
        """
        self._encryption_certificate = value
    
    @property
    def encryption_certificate_id(self,) -> Optional[str]:
        """
        Gets the encryptionCertificateId property value. Optional. A custom app-provided identifier to help identify the certificate needed to decrypt resource data.
        Returns: Optional[str]
        """
        return self._encryption_certificate_id
    
    @encryption_certificate_id.setter
    def encryption_certificate_id(self,value: Optional[str] = None) -> None:
        """
        Sets the encryptionCertificateId property value. Optional. A custom app-provided identifier to help identify the certificate needed to decrypt resource data.
        Args:
            value: Value to set for the encryptionCertificateId property.
        """
        self._encryption_certificate_id = value
    
    @property
    def expiration_date_time(self,) -> Optional[datetime]:
        """
        Gets the expirationDateTime property value. Required. Specifies the date and time when the webhook subscription expires. The time is in UTC, and can be an amount of time from subscription creation that varies for the resource subscribed to. For the maximum supported subscription length of time, see the table below.
        Returns: Optional[datetime]
        """
        return self._expiration_date_time
    
    @expiration_date_time.setter
    def expiration_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the expirationDateTime property value. Required. Specifies the date and time when the webhook subscription expires. The time is in UTC, and can be an amount of time from subscription creation that varies for the resource subscribed to. For the maximum supported subscription length of time, see the table below.
        Args:
            value: Value to set for the expirationDateTime property.
        """
        self._expiration_date_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "application_id": lambda n : setattr(self, 'application_id', n.get_str_value()),
            "change_type": lambda n : setattr(self, 'change_type', n.get_str_value()),
            "client_state": lambda n : setattr(self, 'client_state', n.get_str_value()),
            "creator_id": lambda n : setattr(self, 'creator_id', n.get_str_value()),
            "encryption_certificate": lambda n : setattr(self, 'encryption_certificate', n.get_str_value()),
            "encryption_certificate_id": lambda n : setattr(self, 'encryption_certificate_id', n.get_str_value()),
            "expiration_date_time": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "include_resource_data": lambda n : setattr(self, 'include_resource_data', n.get_bool_value()),
            "latest_supported_tls_version": lambda n : setattr(self, 'latest_supported_tls_version', n.get_str_value()),
            "lifecycle_notification_url": lambda n : setattr(self, 'lifecycle_notification_url', n.get_str_value()),
            "notification_query_options": lambda n : setattr(self, 'notification_query_options', n.get_str_value()),
            "notification_url": lambda n : setattr(self, 'notification_url', n.get_str_value()),
            "notification_url_app_id": lambda n : setattr(self, 'notification_url_app_id', n.get_str_value()),
            "resource": lambda n : setattr(self, 'resource', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def include_resource_data(self,) -> Optional[bool]:
        """
        Gets the includeResourceData property value. Optional. When set to true, change notifications include resource data (such as content of a chat message).
        Returns: Optional[bool]
        """
        return self._include_resource_data
    
    @include_resource_data.setter
    def include_resource_data(self,value: Optional[bool] = None) -> None:
        """
        Sets the includeResourceData property value. Optional. When set to true, change notifications include resource data (such as content of a chat message).
        Args:
            value: Value to set for the includeResourceData property.
        """
        self._include_resource_data = value
    
    @property
    def latest_supported_tls_version(self,) -> Optional[str]:
        """
        Gets the latestSupportedTlsVersion property value. Optional. Specifies the latest version of Transport Layer Security (TLS) that the notification endpoint, specified by notificationUrl, supports. The possible values are: v1_0, v1_1, v1_2, v1_3. For subscribers whose notification endpoint supports a version lower than the currently recommended version (TLS 1.2), specifying this property by a set timeline allows them to temporarily use their deprecated version of TLS before completing their upgrade to TLS 1.2. For these subscribers, not setting this property per the timeline would result in subscription operations failing. For subscribers whose notification endpoint already supports TLS 1.2, setting this property is optional. In such cases, Microsoft Graph defaults the property to v1_2.
        Returns: Optional[str]
        """
        return self._latest_supported_tls_version
    
    @latest_supported_tls_version.setter
    def latest_supported_tls_version(self,value: Optional[str] = None) -> None:
        """
        Sets the latestSupportedTlsVersion property value. Optional. Specifies the latest version of Transport Layer Security (TLS) that the notification endpoint, specified by notificationUrl, supports. The possible values are: v1_0, v1_1, v1_2, v1_3. For subscribers whose notification endpoint supports a version lower than the currently recommended version (TLS 1.2), specifying this property by a set timeline allows them to temporarily use their deprecated version of TLS before completing their upgrade to TLS 1.2. For these subscribers, not setting this property per the timeline would result in subscription operations failing. For subscribers whose notification endpoint already supports TLS 1.2, setting this property is optional. In such cases, Microsoft Graph defaults the property to v1_2.
        Args:
            value: Value to set for the latestSupportedTlsVersion property.
        """
        self._latest_supported_tls_version = value
    
    @property
    def lifecycle_notification_url(self,) -> Optional[str]:
        """
        Gets the lifecycleNotificationUrl property value. Optional. The URL of the endpoint that receives lifecycle notifications, including subscriptionRemoved and missed notifications. This URL must make use of the HTTPS protocol.
        Returns: Optional[str]
        """
        return self._lifecycle_notification_url
    
    @lifecycle_notification_url.setter
    def lifecycle_notification_url(self,value: Optional[str] = None) -> None:
        """
        Sets the lifecycleNotificationUrl property value. Optional. The URL of the endpoint that receives lifecycle notifications, including subscriptionRemoved and missed notifications. This URL must make use of the HTTPS protocol.
        Args:
            value: Value to set for the lifecycleNotificationUrl property.
        """
        self._lifecycle_notification_url = value
    
    @property
    def notification_query_options(self,) -> Optional[str]:
        """
        Gets the notificationQueryOptions property value. Optional. OData query options for specifying value for the targeting resource. Clients receive notifications when resource reaches the state matching the query options provided here. With this new property in the subscription creation payload along with all existing properties, Webhooks will deliver notifications whenever a resource reaches the desired state mentioned in the notificationQueryOptions property. For example, when the print job is completed or when a print job resource isFetchable property value becomes true etc.
        Returns: Optional[str]
        """
        return self._notification_query_options
    
    @notification_query_options.setter
    def notification_query_options(self,value: Optional[str] = None) -> None:
        """
        Sets the notificationQueryOptions property value. Optional. OData query options for specifying value for the targeting resource. Clients receive notifications when resource reaches the state matching the query options provided here. With this new property in the subscription creation payload along with all existing properties, Webhooks will deliver notifications whenever a resource reaches the desired state mentioned in the notificationQueryOptions property. For example, when the print job is completed or when a print job resource isFetchable property value becomes true etc.
        Args:
            value: Value to set for the notificationQueryOptions property.
        """
        self._notification_query_options = value
    
    @property
    def notification_url(self,) -> Optional[str]:
        """
        Gets the notificationUrl property value. Required. The URL of the endpoint that will receive the change notifications. This URL must make use of the HTTPS protocol.
        Returns: Optional[str]
        """
        return self._notification_url
    
    @notification_url.setter
    def notification_url(self,value: Optional[str] = None) -> None:
        """
        Sets the notificationUrl property value. Required. The URL of the endpoint that will receive the change notifications. This URL must make use of the HTTPS protocol.
        Args:
            value: Value to set for the notificationUrl property.
        """
        self._notification_url = value
    
    @property
    def notification_url_app_id(self,) -> Optional[str]:
        """
        Gets the notificationUrlAppId property value. Optional. The app ID that the subscription service can use to generate the validation token. This allows the client to validate the authenticity of the notification received.
        Returns: Optional[str]
        """
        return self._notification_url_app_id
    
    @notification_url_app_id.setter
    def notification_url_app_id(self,value: Optional[str] = None) -> None:
        """
        Sets the notificationUrlAppId property value. Optional. The app ID that the subscription service can use to generate the validation token. This allows the client to validate the authenticity of the notification received.
        Args:
            value: Value to set for the notificationUrlAppId property.
        """
        self._notification_url_app_id = value
    
    @property
    def resource(self,) -> Optional[str]:
        """
        Gets the resource property value. Required. Specifies the resource that will be monitored for changes. Do not include the base URL (https://graph.microsoft.com/v1.0/). See the possible resource path values for each supported resource.
        Returns: Optional[str]
        """
        return self._resource
    
    @resource.setter
    def resource(self,value: Optional[str] = None) -> None:
        """
        Sets the resource property value. Required. Specifies the resource that will be monitored for changes. Do not include the base URL (https://graph.microsoft.com/v1.0/). See the possible resource path values for each supported resource.
        Args:
            value: Value to set for the resource property.
        """
        self._resource = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("applicationId", self.application_id)
        writer.write_str_value("changeType", self.change_type)
        writer.write_str_value("clientState", self.client_state)
        writer.write_str_value("creatorId", self.creator_id)
        writer.write_str_value("encryptionCertificate", self.encryption_certificate)
        writer.write_str_value("encryptionCertificateId", self.encryption_certificate_id)
        writer.write_datetime_value("expirationDateTime", self.expiration_date_time)
        writer.write_bool_value("includeResourceData", self.include_resource_data)
        writer.write_str_value("latestSupportedTlsVersion", self.latest_supported_tls_version)
        writer.write_str_value("lifecycleNotificationUrl", self.lifecycle_notification_url)
        writer.write_str_value("notificationQueryOptions", self.notification_query_options)
        writer.write_str_value("notificationUrl", self.notification_url)
        writer.write_str_value("notificationUrlAppId", self.notification_url_app_id)
        writer.write_str_value("resource", self.resource)
    

