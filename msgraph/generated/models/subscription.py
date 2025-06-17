from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class Subscription(Entity, Parsable):
    # Optional. Identifier of the application used to create the subscription. Read-only.
    application_id: Optional[str] = None
    # Required. Indicates the type of change in the subscribed resource that raises a change notification. The supported values are: created, updated, deleted. Multiple values can be combined using a comma-separated list. Note:  Drive root item and list change notifications support only the updated changeType. User and group change notifications support updated and deleted changeType. Use updated to receive notifications when user or group is created, updated, or soft deleted. Use deleted to receive notifications when user or group is permanently deleted.
    change_type: Optional[str] = None
    # Optional. Specifies the value of the clientState property sent by the service in each change notification. The maximum length is 128 characters. The client can check that the change notification came from the service by comparing the value of the clientState property sent with the subscription with the value of the clientState property received with each change notification.
    client_state: Optional[str] = None
    # Optional. Identifier of the user or service principal that created the subscription. If the app used delegated permissions to create the subscription, this field contains the ID of the signed-in user the app called on behalf of. If the app used application permissions, this field contains the ID of the service principal corresponding to the app. Read-only.
    creator_id: Optional[str] = None
    # Optional. A base64-encoded representation of a certificate with a public key used to encrypt resource data in change notifications. Optional but required when includeResourceData is true.
    encryption_certificate: Optional[str] = None
    # Optional. A custom app-provided identifier to help identify the certificate needed to decrypt resource data.
    encryption_certificate_id: Optional[str] = None
    # Required. Specifies the date and time when the webhook subscription expires. The time is in UTC, and can be an amount of time from subscription creation that varies for the resource subscribed to. Any value under 45 minutes after the time of the request is automatically set to 45 minutes after the request time. For the maximum supported subscription length of time, see Subscription lifetime.
    expiration_date_time: Optional[datetime.datetime] = None
    # Optional. When set to true, change notifications include resource data (such as content of a chat message).
    include_resource_data: Optional[bool] = None
    # Optional. Specifies the latest version of Transport Layer Security (TLS) that the notification endpoint, specified by notificationUrl, supports. The possible values are: v10, v11, v12, v13. For subscribers whose notification endpoint supports a version lower than the currently recommended version (TLS 1.2), specifying this property by a set timeline allows them to temporarily use their deprecated version of TLS before completing their upgrade to TLS 1.2. For these subscribers, not setting this property per the timeline would result in subscription operations failing. For subscribers whose notification endpoint already supports TLS 1.2, setting this property is optional. In such cases, Microsoft Graph defaults the property to v1_2.
    latest_supported_tls_version: Optional[str] = None
    # Required for Teams resources if  the expirationDateTime value is more than 1 hour from now; optional otherwise. The URL of the endpoint that receives lifecycle notifications, including subscriptionRemoved, reauthorizationRequired, and missed notifications. This URL must make use of the HTTPS protocol. For more information, see Reduce missing subscriptions and change notifications.
    lifecycle_notification_url: Optional[str] = None
    # Optional. OData query options for specifying value for the targeting resource. Clients receive notifications when resource reaches the state matching the query options provided here. With this new property in the subscription creation payload along with all existing properties, Webhooks deliver notifications whenever a resource reaches the desired state mentioned in the notificationQueryOptions property. For example, when the print job is completed or when a print job resource isFetchable property value becomes true etc.  Supported only for Universal Print Service. For more information, see Subscribe to change notifications from cloud printing APIs using Microsoft Graph.
    notification_query_options: Optional[str] = None
    # Required. The URL of the endpoint that receives the change notifications. This URL must make use of the HTTPS protocol. Any query string parameter included in the notificationUrl property is included in the HTTP POST request when Microsoft Graph sends the change notifications.
    notification_url: Optional[str] = None
    # Optional. The app ID that the subscription service can use to generate the validation token. The value allows the client to validate the authenticity of the notification received.
    notification_url_app_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Required. Specifies the resource that is monitored for changes. Don't include the base URL (https://graph.microsoft.com/v1.0/). See the possible resource path values for each supported resource.
    resource: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Subscription:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Subscription
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Subscription()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "applicationId": lambda n : setattr(self, 'application_id', n.get_str_value()),
            "changeType": lambda n : setattr(self, 'change_type', n.get_str_value()),
            "clientState": lambda n : setattr(self, 'client_state', n.get_str_value()),
            "creatorId": lambda n : setattr(self, 'creator_id', n.get_str_value()),
            "encryptionCertificate": lambda n : setattr(self, 'encryption_certificate', n.get_str_value()),
            "encryptionCertificateId": lambda n : setattr(self, 'encryption_certificate_id', n.get_str_value()),
            "expirationDateTime": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "includeResourceData": lambda n : setattr(self, 'include_resource_data', n.get_bool_value()),
            "latestSupportedTlsVersion": lambda n : setattr(self, 'latest_supported_tls_version', n.get_str_value()),
            "lifecycleNotificationUrl": lambda n : setattr(self, 'lifecycle_notification_url', n.get_str_value()),
            "notificationQueryOptions": lambda n : setattr(self, 'notification_query_options', n.get_str_value()),
            "notificationUrl": lambda n : setattr(self, 'notification_url', n.get_str_value()),
            "notificationUrlAppId": lambda n : setattr(self, 'notification_url_app_id', n.get_str_value()),
            "resource": lambda n : setattr(self, 'resource', n.get_str_value()),
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
    

