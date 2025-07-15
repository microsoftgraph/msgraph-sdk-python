from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .aad_risk_detection_audit_record import AadRiskDetectionAuditRecord
    from .aed_audit_record import AedAuditRecord
    from .aip_file_deleted import AipFileDeleted
    from .aip_heart_beat import AipHeartBeat
    from .aip_protection_action_log_request import AipProtectionActionLogRequest
    from .aip_scanner_discover_event import AipScannerDiscoverEvent
    from .aip_sensitivity_label_action_log_request import AipSensitivityLabelActionLogRequest
    from .air_admin_action_investigation_data import AirAdminActionInvestigationData
    from .air_investigation_data import AirInvestigationData
    from .air_manual_investigation_data import AirManualInvestigationData
    from .ai_app_interaction_audit_record import AiAppInteractionAuditRecord
    from .attack_sim_admin_audit_record import AttackSimAdminAuditRecord
    from .audit_search_audit_record import AuditSearchAuditRecord
    from .azure_active_directory_account_logon_audit_record import AzureActiveDirectoryAccountLogonAuditRecord
    from .azure_active_directory_audit_record import AzureActiveDirectoryAuditRecord
    from .azure_active_directory_base_audit_record import AzureActiveDirectoryBaseAuditRecord
    from .azure_active_directory_sts_logon_audit_record import AzureActiveDirectoryStsLogonAuditRecord
    from .campaign_audit_record import CampaignAuditRecord
    from .case_audit_record import CaseAuditRecord
    from .case_investigation import CaseInvestigation
    from .cdp_cold_crawl_status_record import CdpColdCrawlStatusRecord
    from .cdp_content_explorer_aggregate_record import CdpContentExplorerAggregateRecord
    from .cdp_dlp_sensitive_audit_record import CdpDlpSensitiveAuditRecord
    from .cdp_dlp_sensitive_endpoint_audit_record import CdpDlpSensitiveEndpointAuditRecord
    from .cdp_log_record import CdpLogRecord
    from .cdp_ocr_billing_record import CdpOcrBillingRecord
    from .cdp_resource_scope_change_event_record import CdpResourceScopeChangeEventRecord
    from .cerner_s_m_s_link_record import CernerSMSLinkRecord
    from .cerner_s_m_s_settings_update_record import CernerSMSSettingsUpdateRecord
    from .cerner_s_m_s_unlink_record import CernerSMSUnlinkRecord
    from .compliance_connector_audit_record import ComplianceConnectorAuditRecord
    from .compliance_dlp_applications_audit_record import ComplianceDlpApplicationsAuditRecord
    from .compliance_dlp_applications_classification_audit_record import ComplianceDlpApplicationsClassificationAuditRecord
    from .compliance_dlp_base_audit_record import ComplianceDlpBaseAuditRecord
    from .compliance_dlp_classification_base_audit_record import ComplianceDlpClassificationBaseAuditRecord
    from .compliance_dlp_classification_base_cdp_record import ComplianceDlpClassificationBaseCdpRecord
    from .compliance_dlp_endpoint_audit_record import ComplianceDlpEndpointAuditRecord
    from .compliance_dlp_endpoint_discovery_audit_record import ComplianceDlpEndpointDiscoveryAuditRecord
    from .compliance_dlp_exchange_audit_record import ComplianceDlpExchangeAuditRecord
    from .compliance_dlp_exchange_classification_audit_record import ComplianceDlpExchangeClassificationAuditRecord
    from .compliance_dlp_exchange_classification_cdp_record import ComplianceDlpExchangeClassificationCdpRecord
    from .compliance_dlp_exchange_discovery_audit_record import ComplianceDlpExchangeDiscoveryAuditRecord
    from .compliance_dlp_share_point_audit_record import ComplianceDlpSharePointAuditRecord
    from .compliance_dlp_share_point_classification_audit_record import ComplianceDlpSharePointClassificationAuditRecord
    from .compliance_dlp_share_point_classification_extended_audit_record import ComplianceDlpSharePointClassificationExtendedAuditRecord
    from .compliance_d_l_m_exchange_audit_record import ComplianceDLMExchangeAuditRecord
    from .compliance_d_l_m_share_point_audit_record import ComplianceDLMSharePointAuditRecord
    from .compliance_manager_action_record import ComplianceManagerActionRecord
    from .compliance_supervision_base_audit_record import ComplianceSupervisionBaseAuditRecord
    from .compliance_supervision_exchange_audit_record import ComplianceSupervisionExchangeAuditRecord
    from .consumption_resource_audit_record import ConsumptionResourceAuditRecord
    from .copilot_interaction_audit_record import CopilotInteractionAuditRecord
    from .core_reporting_settings_audit_record import CoreReportingSettingsAuditRecord
    from .cortana_briefing_audit_record import CortanaBriefingAuditRecord
    from .cps_common_policy_audit_record import CpsCommonPolicyAuditRecord
    from .cps_policy_config_audit_record import CpsPolicyConfigAuditRecord
    from .crm_base_audit_record import CrmBaseAuditRecord
    from .crm_entity_operation_audit_record import CrmEntityOperationAuditRecord
    from .customer_key_service_encryption_audit_record import CustomerKeyServiceEncryptionAuditRecord
    from .data_center_security_base_audit_record import DataCenterSecurityBaseAuditRecord
    from .data_center_security_cmdlet_audit_record import DataCenterSecurityCmdletAuditRecord
    from .data_governance_audit_record import DataGovernanceAuditRecord
    from .data_insights_rest_api_audit_record import DataInsightsRestApiAuditRecord
    from .data_lake_export_operation_audit_record import DataLakeExportOperationAuditRecord
    from .data_share_operation_audit_record import DataShareOperationAuditRecord
    from .default_audit_data import DefaultAuditData
    from .defender_security_alert_base_record import DefenderSecurityAlertBaseRecord
    from .delete_certificate_record import DeleteCertificateRecord
    from .disable_consent_record import DisableConsentRecord
    from .discovery_audit_record import DiscoveryAuditRecord
    from .dlp_endpoint_audit_record import DlpEndpointAuditRecord
    from .dlp_sensitive_information_type_cmdlet_record import DlpSensitiveInformationTypeCmdletRecord
    from .dlp_sensitive_information_type_rule_package_cmdlet_record import DlpSensitiveInformationTypeRulePackageCmdletRecord
    from .download_certificate_record import DownloadCertificateRecord
    from .dynamics365_business_central_audit_record import Dynamics365BusinessCentralAuditRecord
    from .enable_consent_record import EnableConsentRecord
    from .epic_s_m_s_link_record import EpicSMSLinkRecord
    from .epic_s_m_s_settings_update_record import EpicSMSSettingsUpdateRecord
    from .epic_s_m_s_unlink_record import EpicSMSUnlinkRecord
    from .exchange_admin_audit_record import ExchangeAdminAuditRecord
    from .exchange_aggregated_mailbox_audit_record import ExchangeAggregatedMailboxAuditRecord
    from .exchange_aggregated_operation_record import ExchangeAggregatedOperationRecord
    from .exchange_mailbox_audit_base_record import ExchangeMailboxAuditBaseRecord
    from .exchange_mailbox_audit_group_record import ExchangeMailboxAuditGroupRecord
    from .exchange_mailbox_audit_record import ExchangeMailboxAuditRecord
    from .fhir_base_url_add_record import FhirBaseUrlAddRecord
    from .fhir_base_url_approve_record import FhirBaseUrlApproveRecord
    from .fhir_base_url_delete_record import FhirBaseUrlDeleteRecord
    from .fhir_base_url_update_record import FhirBaseUrlUpdateRecord
    from .healthcare_signal_record import HealthcareSignalRecord
    from .hosted_rpa_audit_record import HostedRpaAuditRecord
    from .hr_signal_audit_record import HrSignalAuditRecord
    from .hygiene_event_record import HygieneEventRecord
    from .information_barrier_policy_application_audit_record import InformationBarrierPolicyApplicationAuditRecord
    from .information_worker_protection_audit_record import InformationWorkerProtectionAuditRecord
    from .insider_risk_scoped_users_record import InsiderRiskScopedUsersRecord
    from .insider_risk_scoped_user_insights_record import InsiderRiskScopedUserInsightsRecord
    from .irm_security_alert_record import IrmSecurityAlertRecord
    from .irm_user_defined_detection_record import IrmUserDefinedDetectionRecord
    from .kaizala_audit_record import KaizalaAuditRecord
    from .label_analytics_aggregate_audit_record import LabelAnalyticsAggregateAuditRecord
    from .label_content_explorer_audit_record import LabelContentExplorerAuditRecord
    from .large_content_metadata_audit_record import LargeContentMetadataAuditRecord
    from .m365_compliance_connector_audit_record import M365ComplianceConnectorAuditRecord
    from .m365_d_a_a_d_audit_record import M365DAADAuditRecord
    from .mail_submission_data import MailSubmissionData
    from .managed_services_audit_record import ManagedServicesAuditRecord
    from .managed_tenants_audit_record import ManagedTenantsAuditRecord
    from .mapg_alerts_audit_record import MapgAlertsAuditRecord
    from .mapg_onboard_audit_record import MapgOnboardAuditRecord
    from .mapg_policy_audit_record import MapgPolicyAuditRecord
    from .mcas_alerts_audit_record import McasAlertsAuditRecord
    from .mdatp_audit_record import MdatpAuditRecord
    from .mda_data_security_signal_record import MdaDataSecuritySignalRecord
    from .mdc_events_record import MdcEventsRecord
    from .mdi_audit_record import MdiAuditRecord
    from .mesh_worlds_audit_record import MeshWorldsAuditRecord
    from .microsoft365_backup_backup_item_audit_record import Microsoft365BackupBackupItemAuditRecord
    from .microsoft365_backup_backup_policy_audit_record import Microsoft365BackupBackupPolicyAuditRecord
    from .microsoft365_backup_restore_item_audit_record import Microsoft365BackupRestoreItemAuditRecord
    from .microsoft365_backup_restore_task_audit_record import Microsoft365BackupRestoreTaskAuditRecord
    from .microsoft_defender_experts_base_audit_record import MicrosoftDefenderExpertsBaseAuditRecord
    from .microsoft_defender_experts_x_d_r_audit_record import MicrosoftDefenderExpertsXDRAuditRecord
    from .microsoft_flow_audit_record import MicrosoftFlowAuditRecord
    from .microsoft_forms_audit_record import MicrosoftFormsAuditRecord
    from .microsoft_graph_data_connect_consent import MicrosoftGraphDataConnectConsent
    from .microsoft_graph_data_connect_operation import MicrosoftGraphDataConnectOperation
    from .microsoft_purview_data_map_operation_record import MicrosoftPurviewDataMapOperationRecord
    from .microsoft_purview_metadata_policy_operation_record import MicrosoftPurviewMetadataPolicyOperationRecord
    from .microsoft_purview_policy_operation_record import MicrosoftPurviewPolicyOperationRecord
    from .microsoft_purview_privacy_audit_event import MicrosoftPurviewPrivacyAuditEvent
    from .microsoft_stream_audit_record import MicrosoftStreamAuditRecord
    from .microsoft_teams_admin_audit_record import MicrosoftTeamsAdminAuditRecord
    from .microsoft_teams_analytics_audit_record import MicrosoftTeamsAnalyticsAuditRecord
    from .microsoft_teams_audit_record import MicrosoftTeamsAuditRecord
    from .microsoft_teams_device_audit_record import MicrosoftTeamsDeviceAuditRecord
    from .microsoft_teams_retention_label_action_audit_record import MicrosoftTeamsRetentionLabelActionAuditRecord
    from .microsoft_teams_sensitivity_label_action_audit_record import MicrosoftTeamsSensitivityLabelActionAuditRecord
    from .microsoft_teams_shifts_audit_record import MicrosoftTeamsShiftsAuditRecord
    from .mip_auto_label_exchange_item_audit_record import MipAutoLabelExchangeItemAuditRecord
    from .mip_auto_label_item_audit_record import MipAutoLabelItemAuditRecord
    from .mip_auto_label_policy_audit_record import MipAutoLabelPolicyAuditRecord
    from .mip_auto_label_progress_feedback_audit_record import MipAutoLabelProgressFeedbackAuditRecord
    from .mip_auto_label_share_point_item_audit_record import MipAutoLabelSharePointItemAuditRecord
    from .mip_auto_label_share_point_policy_location_audit_record import MipAutoLabelSharePointPolicyLocationAuditRecord
    from .mip_auto_label_simulation_share_point_completion_record import MipAutoLabelSimulationSharePointCompletionRecord
    from .mip_auto_label_simulation_share_point_progress_record import MipAutoLabelSimulationSharePointProgressRecord
    from .mip_auto_label_simulation_statistics_record import MipAutoLabelSimulationStatisticsRecord
    from .mip_auto_label_simulation_status_record import MipAutoLabelSimulationStatusRecord
    from .mip_exact_data_match_audit_record import MipExactDataMatchAuditRecord
    from .mip_label_analytics_audit_record import MipLabelAnalyticsAuditRecord
    from .mip_label_audit_record import MipLabelAuditRecord
    from .msde_general_settings_audit_record import MsdeGeneralSettingsAuditRecord
    from .msde_indicators_settings_audit_record import MsdeIndicatorsSettingsAuditRecord
    from .msde_response_actions_audit_record import MsdeResponseActionsAuditRecord
    from .msde_roles_settings_audit_record import MsdeRolesSettingsAuditRecord
    from .mstic_nation_state_notification_record import MsticNationStateNotificationRecord
    from .multi_stage_disposition_audit_record import MultiStageDispositionAuditRecord
    from .my_analytics_settings_audit_record import MyAnalyticsSettingsAuditRecord
    from .m_s365_d_custom_detection_audit_record import MS365DCustomDetectionAuditRecord
    from .m_s365_d_incident_audit_record import MS365DIncidentAuditRecord
    from .m_s365_d_suppression_rule_audit_record import MS365DSuppressionRuleAuditRecord
    from .office_native_audit_record import OfficeNativeAuditRecord
    from .ome_portal_audit_record import OmePortalAuditRecord
    from .one_drive_audit_record import OneDriveAuditRecord
    from .on_premises_file_share_scanner_dlp_audit_record import OnPremisesFileShareScannerDlpAuditRecord
    from .on_premises_scanner_dlp_audit_record import OnPremisesScannerDlpAuditRecord
    from .on_premises_share_point_scanner_dlp_audit_record import OnPremisesSharePointScannerDlpAuditRecord
    from .owa_get_access_token_for_resource_audit_record import OwaGetAccessTokenForResourceAuditRecord
    from .people_admin_settings_audit_record import PeopleAdminSettingsAuditRecord
    from .physical_badging_signal_audit_record import PhysicalBadgingSignalAuditRecord
    from .planner_copy_plan_audit_record import PlannerCopyPlanAuditRecord
    from .planner_plan_audit_record import PlannerPlanAuditRecord
    from .planner_plan_list_audit_record import PlannerPlanListAuditRecord
    from .planner_roster_audit_record import PlannerRosterAuditRecord
    from .planner_roster_sensitivity_label_audit_record import PlannerRosterSensitivityLabelAuditRecord
    from .planner_task_audit_record import PlannerTaskAuditRecord
    from .planner_task_list_audit_record import PlannerTaskListAuditRecord
    from .planner_tenant_settings_audit_record import PlannerTenantSettingsAuditRecord
    from .power_apps_audit_app_record import PowerAppsAuditAppRecord
    from .power_apps_audit_plan_record import PowerAppsAuditPlanRecord
    from .power_apps_audit_resource_record import PowerAppsAuditResourceRecord
    from .power_bi_audit_record import PowerBiAuditRecord
    from .power_bi_dlp_audit_record import PowerBiDlpAuditRecord
    from .power_pages_site_audit_record import PowerPagesSiteAuditRecord
    from .power_platform_administrator_activity_record import PowerPlatformAdministratorActivityRecord
    from .power_platform_admin_dlp_audit_record import PowerPlatformAdminDlpAuditRecord
    from .power_platform_admin_environment_audit_record import PowerPlatformAdminEnvironmentAuditRecord
    from .power_platform_lockbox_resource_access_request_audit_record import PowerPlatformLockboxResourceAccessRequestAuditRecord
    from .power_platform_lockbox_resource_command_audit_record import PowerPlatformLockboxResourceCommandAuditRecord
    from .power_platform_service_activity_audit_record import PowerPlatformServiceActivityAuditRecord
    from .privacy_data_match_audit_record import PrivacyDataMatchAuditRecord
    from .privacy_data_minimization_record import PrivacyDataMinimizationRecord
    from .privacy_digest_email_record import PrivacyDigestEmailRecord
    from .privacy_open_access_audit_record import PrivacyOpenAccessAuditRecord
    from .privacy_portal_audit_record import PrivacyPortalAuditRecord
    from .privacy_remediation_action_record import PrivacyRemediationActionRecord
    from .privacy_remediation_record import PrivacyRemediationRecord
    from .privacy_tenant_audit_history_record import PrivacyTenantAuditHistoryRecord
    from .project_audit_record import ProjectAuditRecord
    from .project_for_the_web_assigned_to_me_settings_audit_record import ProjectForTheWebAssignedToMeSettingsAuditRecord
    from .project_for_the_web_project_audit_record import ProjectForTheWebProjectAuditRecord
    from .project_for_the_web_project_settings_audit_record import ProjectForTheWebProjectSettingsAuditRecord
    from .project_for_the_web_roadmap_audit_record import ProjectForTheWebRoadmapAuditRecord
    from .project_for_the_web_roadmap_item_audit_record import ProjectForTheWebRoadmapItemAuditRecord
    from .project_for_the_web_roadmap_settings_audit_record import ProjectForTheWebRoadmapSettingsAuditRecord
    from .project_for_the_web_task_audit_record import ProjectForTheWebTaskAuditRecord
    from .public_folder_audit_record import PublicFolderAuditRecord
    from .purview_insider_risk_alerts_record import PurviewInsiderRiskAlertsRecord
    from .purview_insider_risk_cases_record import PurviewInsiderRiskCasesRecord
    from .quarantine_audit_record import QuarantineAuditRecord
    from .records_management_audit_record import RecordsManagementAuditRecord
    from .retention_policy_audit_record import RetentionPolicyAuditRecord
    from .score_evidence import ScoreEvidence
    from .score_platform_generic_audit_record import ScorePlatformGenericAuditRecord
    from .script_run_audit_record import ScriptRunAuditRecord
    from .search_audit_record import SearchAuditRecord
    from .security_compliance_alert_record import SecurityComplianceAlertRecord
    from .security_compliance_center_e_o_p_cmdlet_audit_record import SecurityComplianceCenterEOPCmdletAuditRecord
    from .security_compliance_insights_audit_record import SecurityComplianceInsightsAuditRecord
    from .security_compliance_r_b_a_c_audit_record import SecurityComplianceRBACAuditRecord
    from .security_compliance_user_change_audit_record import SecurityComplianceUserChangeAuditRecord
    from .share_point_app_permission_operation_audit_record import SharePointAppPermissionOperationAuditRecord
    from .share_point_audit_record import SharePointAuditRecord
    from .share_point_comment_operation_audit_record import SharePointCommentOperationAuditRecord
    from .share_point_content_type_operation_audit_record import SharePointContentTypeOperationAuditRecord
    from .share_point_e_signature_audit_record import SharePointESignatureAuditRecord
    from .share_point_field_operation_audit_record import SharePointFieldOperationAuditRecord
    from .share_point_file_operation_audit_record import SharePointFileOperationAuditRecord
    from .share_point_list_operation_audit_record import SharePointListOperationAuditRecord
    from .share_point_sharing_operation_audit_record import SharePointSharingOperationAuditRecord
    from .skype_for_business_base_audit_record import SkypeForBusinessBaseAuditRecord
    from .skype_for_business_cmdlets_audit_record import SkypeForBusinessCmdletsAuditRecord
    from .skype_for_business_p_s_t_n_usage_audit_record import SkypeForBusinessPSTNUsageAuditRecord
    from .skype_for_business_users_blocked_audit_record import SkypeForBusinessUsersBlockedAuditRecord
    from .sms_create_phone_number_record import SmsCreatePhoneNumberRecord
    from .sms_delete_phone_number_record import SmsDeletePhoneNumberRecord
    from .supervisory_review_day_x_insights_audit_record import SupervisoryReviewDayXInsightsAuditRecord
    from .synthetic_probe_audit_record import SyntheticProbeAuditRecord
    from .teams_easy_approvals_audit_record import TeamsEasyApprovalsAuditRecord
    from .teams_healthcare_audit_record import TeamsHealthcareAuditRecord
    from .teams_updates_audit_record import TeamsUpdatesAuditRecord
    from .tenant_allow_block_list_audit_record import TenantAllowBlockListAuditRecord
    from .threat_finder_audit_record import ThreatFinderAuditRecord
    from .threat_intelligence_atp_content_data import ThreatIntelligenceAtpContentData
    from .threat_intelligence_mail_data import ThreatIntelligenceMailData
    from .threat_intelligence_url_click_data import ThreatIntelligenceUrlClickData
    from .todo_audit_record import TodoAuditRecord
    from .uam_operation_audit_record import UamOperationAuditRecord
    from .unified_group_audit_record import UnifiedGroupAuditRecord
    from .unified_simulation_matched_item_audit_record import UnifiedSimulationMatchedItemAuditRecord
    from .unified_simulation_summary_audit_record import UnifiedSimulationSummaryAuditRecord
    from .upload_certificate_record import UploadCertificateRecord
    from .urbac_assignment_audit_record import UrbacAssignmentAuditRecord
    from .urbac_enable_state_audit_record import UrbacEnableStateAuditRecord
    from .urbac_role_audit_record import UrbacRoleAuditRecord
    from .user_training_audit_record import UserTrainingAuditRecord
    from .vfam_base_policy_audit_record import VfamBasePolicyAuditRecord
    from .vfam_create_policy_audit_record import VfamCreatePolicyAuditRecord
    from .vfam_delete_policy_audit_record import VfamDeletePolicyAuditRecord
    from .vfam_update_policy_audit_record import VfamUpdatePolicyAuditRecord
    from .viva_goals_audit_record import VivaGoalsAuditRecord
    from .viva_learning_admin_audit_record import VivaLearningAdminAuditRecord
    from .viva_learning_audit_record import VivaLearningAuditRecord
    from .viva_pulse_admin_audit_record import VivaPulseAdminAuditRecord
    from .viva_pulse_organizer_audit_record import VivaPulseOrganizerAuditRecord
    from .viva_pulse_report_audit_record import VivaPulseReportAuditRecord
    from .viva_pulse_response_audit_record import VivaPulseResponseAuditRecord
    from .wdatp_alerts_audit_record import WdatpAlertsAuditRecord
    from .windows365_customer_lockbox_audit_record import Windows365CustomerLockboxAuditRecord
    from .workplace_analytics_audit_record import WorkplaceAnalyticsAuditRecord
    from .yammer_audit_record import YammerAuditRecord

@dataclass
class AuditData(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AuditData:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AuditData
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.aadRiskDetectionAuditRecord".casefold():
            from .aad_risk_detection_audit_record import AadRiskDetectionAuditRecord

            return AadRiskDetectionAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.aedAuditRecord".casefold():
            from .aed_audit_record import AedAuditRecord

            return AedAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.aiAppInteractionAuditRecord".casefold():
            from .ai_app_interaction_audit_record import AiAppInteractionAuditRecord

            return AiAppInteractionAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.aipFileDeleted".casefold():
            from .aip_file_deleted import AipFileDeleted

            return AipFileDeleted()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.aipHeartBeat".casefold():
            from .aip_heart_beat import AipHeartBeat

            return AipHeartBeat()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.aipProtectionActionLogRequest".casefold():
            from .aip_protection_action_log_request import AipProtectionActionLogRequest

            return AipProtectionActionLogRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.aipScannerDiscoverEvent".casefold():
            from .aip_scanner_discover_event import AipScannerDiscoverEvent

            return AipScannerDiscoverEvent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.aipSensitivityLabelActionLogRequest".casefold():
            from .aip_sensitivity_label_action_log_request import AipSensitivityLabelActionLogRequest

            return AipSensitivityLabelActionLogRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.airAdminActionInvestigationData".casefold():
            from .air_admin_action_investigation_data import AirAdminActionInvestigationData

            return AirAdminActionInvestigationData()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.airInvestigationData".casefold():
            from .air_investigation_data import AirInvestigationData

            return AirInvestigationData()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.airManualInvestigationData".casefold():
            from .air_manual_investigation_data import AirManualInvestigationData

            return AirManualInvestigationData()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.attackSimAdminAuditRecord".casefold():
            from .attack_sim_admin_audit_record import AttackSimAdminAuditRecord

            return AttackSimAdminAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.auditSearchAuditRecord".casefold():
            from .audit_search_audit_record import AuditSearchAuditRecord

            return AuditSearchAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.azureActiveDirectoryAccountLogonAuditRecord".casefold():
            from .azure_active_directory_account_logon_audit_record import AzureActiveDirectoryAccountLogonAuditRecord

            return AzureActiveDirectoryAccountLogonAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.azureActiveDirectoryAuditRecord".casefold():
            from .azure_active_directory_audit_record import AzureActiveDirectoryAuditRecord

            return AzureActiveDirectoryAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.azureActiveDirectoryBaseAuditRecord".casefold():
            from .azure_active_directory_base_audit_record import AzureActiveDirectoryBaseAuditRecord

            return AzureActiveDirectoryBaseAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.azureActiveDirectoryStsLogonAuditRecord".casefold():
            from .azure_active_directory_sts_logon_audit_record import AzureActiveDirectoryStsLogonAuditRecord

            return AzureActiveDirectoryStsLogonAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.campaignAuditRecord".casefold():
            from .campaign_audit_record import CampaignAuditRecord

            return CampaignAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.caseAuditRecord".casefold():
            from .case_audit_record import CaseAuditRecord

            return CaseAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.caseInvestigation".casefold():
            from .case_investigation import CaseInvestigation

            return CaseInvestigation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.cdpColdCrawlStatusRecord".casefold():
            from .cdp_cold_crawl_status_record import CdpColdCrawlStatusRecord

            return CdpColdCrawlStatusRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.cdpContentExplorerAggregateRecord".casefold():
            from .cdp_content_explorer_aggregate_record import CdpContentExplorerAggregateRecord

            return CdpContentExplorerAggregateRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.cdpDlpSensitiveAuditRecord".casefold():
            from .cdp_dlp_sensitive_audit_record import CdpDlpSensitiveAuditRecord

            return CdpDlpSensitiveAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.cdpDlpSensitiveEndpointAuditRecord".casefold():
            from .cdp_dlp_sensitive_endpoint_audit_record import CdpDlpSensitiveEndpointAuditRecord

            return CdpDlpSensitiveEndpointAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.cdpLogRecord".casefold():
            from .cdp_log_record import CdpLogRecord

            return CdpLogRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.cdpOcrBillingRecord".casefold():
            from .cdp_ocr_billing_record import CdpOcrBillingRecord

            return CdpOcrBillingRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.cdpResourceScopeChangeEventRecord".casefold():
            from .cdp_resource_scope_change_event_record import CdpResourceScopeChangeEventRecord

            return CdpResourceScopeChangeEventRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.cernerSMSLinkRecord".casefold():
            from .cerner_s_m_s_link_record import CernerSMSLinkRecord

            return CernerSMSLinkRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.cernerSMSSettingsUpdateRecord".casefold():
            from .cerner_s_m_s_settings_update_record import CernerSMSSettingsUpdateRecord

            return CernerSMSSettingsUpdateRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.cernerSMSUnlinkRecord".casefold():
            from .cerner_s_m_s_unlink_record import CernerSMSUnlinkRecord

            return CernerSMSUnlinkRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.complianceConnectorAuditRecord".casefold():
            from .compliance_connector_audit_record import ComplianceConnectorAuditRecord

            return ComplianceConnectorAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.complianceDLMExchangeAuditRecord".casefold():
            from .compliance_d_l_m_exchange_audit_record import ComplianceDLMExchangeAuditRecord

            return ComplianceDLMExchangeAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.complianceDLMSharePointAuditRecord".casefold():
            from .compliance_d_l_m_share_point_audit_record import ComplianceDLMSharePointAuditRecord

            return ComplianceDLMSharePointAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.complianceDlpApplicationsAuditRecord".casefold():
            from .compliance_dlp_applications_audit_record import ComplianceDlpApplicationsAuditRecord

            return ComplianceDlpApplicationsAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.complianceDlpApplicationsClassificationAuditRecord".casefold():
            from .compliance_dlp_applications_classification_audit_record import ComplianceDlpApplicationsClassificationAuditRecord

            return ComplianceDlpApplicationsClassificationAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.complianceDlpBaseAuditRecord".casefold():
            from .compliance_dlp_base_audit_record import ComplianceDlpBaseAuditRecord

            return ComplianceDlpBaseAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.complianceDlpClassificationBaseAuditRecord".casefold():
            from .compliance_dlp_classification_base_audit_record import ComplianceDlpClassificationBaseAuditRecord

            return ComplianceDlpClassificationBaseAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.complianceDlpClassificationBaseCdpRecord".casefold():
            from .compliance_dlp_classification_base_cdp_record import ComplianceDlpClassificationBaseCdpRecord

            return ComplianceDlpClassificationBaseCdpRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.complianceDlpEndpointAuditRecord".casefold():
            from .compliance_dlp_endpoint_audit_record import ComplianceDlpEndpointAuditRecord

            return ComplianceDlpEndpointAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.complianceDlpEndpointDiscoveryAuditRecord".casefold():
            from .compliance_dlp_endpoint_discovery_audit_record import ComplianceDlpEndpointDiscoveryAuditRecord

            return ComplianceDlpEndpointDiscoveryAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.complianceDlpExchangeAuditRecord".casefold():
            from .compliance_dlp_exchange_audit_record import ComplianceDlpExchangeAuditRecord

            return ComplianceDlpExchangeAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.complianceDlpExchangeClassificationAuditRecord".casefold():
            from .compliance_dlp_exchange_classification_audit_record import ComplianceDlpExchangeClassificationAuditRecord

            return ComplianceDlpExchangeClassificationAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.complianceDlpExchangeClassificationCdpRecord".casefold():
            from .compliance_dlp_exchange_classification_cdp_record import ComplianceDlpExchangeClassificationCdpRecord

            return ComplianceDlpExchangeClassificationCdpRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.complianceDlpExchangeDiscoveryAuditRecord".casefold():
            from .compliance_dlp_exchange_discovery_audit_record import ComplianceDlpExchangeDiscoveryAuditRecord

            return ComplianceDlpExchangeDiscoveryAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.complianceDlpSharePointAuditRecord".casefold():
            from .compliance_dlp_share_point_audit_record import ComplianceDlpSharePointAuditRecord

            return ComplianceDlpSharePointAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.complianceDlpSharePointClassificationAuditRecord".casefold():
            from .compliance_dlp_share_point_classification_audit_record import ComplianceDlpSharePointClassificationAuditRecord

            return ComplianceDlpSharePointClassificationAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.complianceDlpSharePointClassificationExtendedAuditRecord".casefold():
            from .compliance_dlp_share_point_classification_extended_audit_record import ComplianceDlpSharePointClassificationExtendedAuditRecord

            return ComplianceDlpSharePointClassificationExtendedAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.complianceManagerActionRecord".casefold():
            from .compliance_manager_action_record import ComplianceManagerActionRecord

            return ComplianceManagerActionRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.complianceSupervisionBaseAuditRecord".casefold():
            from .compliance_supervision_base_audit_record import ComplianceSupervisionBaseAuditRecord

            return ComplianceSupervisionBaseAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.complianceSupervisionExchangeAuditRecord".casefold():
            from .compliance_supervision_exchange_audit_record import ComplianceSupervisionExchangeAuditRecord

            return ComplianceSupervisionExchangeAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.consumptionResourceAuditRecord".casefold():
            from .consumption_resource_audit_record import ConsumptionResourceAuditRecord

            return ConsumptionResourceAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.copilotInteractionAuditRecord".casefold():
            from .copilot_interaction_audit_record import CopilotInteractionAuditRecord

            return CopilotInteractionAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.coreReportingSettingsAuditRecord".casefold():
            from .core_reporting_settings_audit_record import CoreReportingSettingsAuditRecord

            return CoreReportingSettingsAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.cortanaBriefingAuditRecord".casefold():
            from .cortana_briefing_audit_record import CortanaBriefingAuditRecord

            return CortanaBriefingAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.cpsCommonPolicyAuditRecord".casefold():
            from .cps_common_policy_audit_record import CpsCommonPolicyAuditRecord

            return CpsCommonPolicyAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.cpsPolicyConfigAuditRecord".casefold():
            from .cps_policy_config_audit_record import CpsPolicyConfigAuditRecord

            return CpsPolicyConfigAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.crmBaseAuditRecord".casefold():
            from .crm_base_audit_record import CrmBaseAuditRecord

            return CrmBaseAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.crmEntityOperationAuditRecord".casefold():
            from .crm_entity_operation_audit_record import CrmEntityOperationAuditRecord

            return CrmEntityOperationAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.customerKeyServiceEncryptionAuditRecord".casefold():
            from .customer_key_service_encryption_audit_record import CustomerKeyServiceEncryptionAuditRecord

            return CustomerKeyServiceEncryptionAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.dataCenterSecurityBaseAuditRecord".casefold():
            from .data_center_security_base_audit_record import DataCenterSecurityBaseAuditRecord

            return DataCenterSecurityBaseAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.dataCenterSecurityCmdletAuditRecord".casefold():
            from .data_center_security_cmdlet_audit_record import DataCenterSecurityCmdletAuditRecord

            return DataCenterSecurityCmdletAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.dataGovernanceAuditRecord".casefold():
            from .data_governance_audit_record import DataGovernanceAuditRecord

            return DataGovernanceAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.dataInsightsRestApiAuditRecord".casefold():
            from .data_insights_rest_api_audit_record import DataInsightsRestApiAuditRecord

            return DataInsightsRestApiAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.dataLakeExportOperationAuditRecord".casefold():
            from .data_lake_export_operation_audit_record import DataLakeExportOperationAuditRecord

            return DataLakeExportOperationAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.dataShareOperationAuditRecord".casefold():
            from .data_share_operation_audit_record import DataShareOperationAuditRecord

            return DataShareOperationAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.defaultAuditData".casefold():
            from .default_audit_data import DefaultAuditData

            return DefaultAuditData()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.defenderSecurityAlertBaseRecord".casefold():
            from .defender_security_alert_base_record import DefenderSecurityAlertBaseRecord

            return DefenderSecurityAlertBaseRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.deleteCertificateRecord".casefold():
            from .delete_certificate_record import DeleteCertificateRecord

            return DeleteCertificateRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.disableConsentRecord".casefold():
            from .disable_consent_record import DisableConsentRecord

            return DisableConsentRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.discoveryAuditRecord".casefold():
            from .discovery_audit_record import DiscoveryAuditRecord

            return DiscoveryAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.dlpEndpointAuditRecord".casefold():
            from .dlp_endpoint_audit_record import DlpEndpointAuditRecord

            return DlpEndpointAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.dlpSensitiveInformationTypeCmdletRecord".casefold():
            from .dlp_sensitive_information_type_cmdlet_record import DlpSensitiveInformationTypeCmdletRecord

            return DlpSensitiveInformationTypeCmdletRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.dlpSensitiveInformationTypeRulePackageCmdletRecord".casefold():
            from .dlp_sensitive_information_type_rule_package_cmdlet_record import DlpSensitiveInformationTypeRulePackageCmdletRecord

            return DlpSensitiveInformationTypeRulePackageCmdletRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.downloadCertificateRecord".casefold():
            from .download_certificate_record import DownloadCertificateRecord

            return DownloadCertificateRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.dynamics365BusinessCentralAuditRecord".casefold():
            from .dynamics365_business_central_audit_record import Dynamics365BusinessCentralAuditRecord

            return Dynamics365BusinessCentralAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.enableConsentRecord".casefold():
            from .enable_consent_record import EnableConsentRecord

            return EnableConsentRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.epicSMSLinkRecord".casefold():
            from .epic_s_m_s_link_record import EpicSMSLinkRecord

            return EpicSMSLinkRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.epicSMSSettingsUpdateRecord".casefold():
            from .epic_s_m_s_settings_update_record import EpicSMSSettingsUpdateRecord

            return EpicSMSSettingsUpdateRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.epicSMSUnlinkRecord".casefold():
            from .epic_s_m_s_unlink_record import EpicSMSUnlinkRecord

            return EpicSMSUnlinkRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.exchangeAdminAuditRecord".casefold():
            from .exchange_admin_audit_record import ExchangeAdminAuditRecord

            return ExchangeAdminAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.exchangeAggregatedMailboxAuditRecord".casefold():
            from .exchange_aggregated_mailbox_audit_record import ExchangeAggregatedMailboxAuditRecord

            return ExchangeAggregatedMailboxAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.exchangeAggregatedOperationRecord".casefold():
            from .exchange_aggregated_operation_record import ExchangeAggregatedOperationRecord

            return ExchangeAggregatedOperationRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.exchangeMailboxAuditBaseRecord".casefold():
            from .exchange_mailbox_audit_base_record import ExchangeMailboxAuditBaseRecord

            return ExchangeMailboxAuditBaseRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.exchangeMailboxAuditGroupRecord".casefold():
            from .exchange_mailbox_audit_group_record import ExchangeMailboxAuditGroupRecord

            return ExchangeMailboxAuditGroupRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.exchangeMailboxAuditRecord".casefold():
            from .exchange_mailbox_audit_record import ExchangeMailboxAuditRecord

            return ExchangeMailboxAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.fhirBaseUrlAddRecord".casefold():
            from .fhir_base_url_add_record import FhirBaseUrlAddRecord

            return FhirBaseUrlAddRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.fhirBaseUrlApproveRecord".casefold():
            from .fhir_base_url_approve_record import FhirBaseUrlApproveRecord

            return FhirBaseUrlApproveRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.fhirBaseUrlDeleteRecord".casefold():
            from .fhir_base_url_delete_record import FhirBaseUrlDeleteRecord

            return FhirBaseUrlDeleteRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.fhirBaseUrlUpdateRecord".casefold():
            from .fhir_base_url_update_record import FhirBaseUrlUpdateRecord

            return FhirBaseUrlUpdateRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.healthcareSignalRecord".casefold():
            from .healthcare_signal_record import HealthcareSignalRecord

            return HealthcareSignalRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.hostedRpaAuditRecord".casefold():
            from .hosted_rpa_audit_record import HostedRpaAuditRecord

            return HostedRpaAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.hrSignalAuditRecord".casefold():
            from .hr_signal_audit_record import HrSignalAuditRecord

            return HrSignalAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.hygieneEventRecord".casefold():
            from .hygiene_event_record import HygieneEventRecord

            return HygieneEventRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.informationBarrierPolicyApplicationAuditRecord".casefold():
            from .information_barrier_policy_application_audit_record import InformationBarrierPolicyApplicationAuditRecord

            return InformationBarrierPolicyApplicationAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.informationWorkerProtectionAuditRecord".casefold():
            from .information_worker_protection_audit_record import InformationWorkerProtectionAuditRecord

            return InformationWorkerProtectionAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.insiderRiskScopedUserInsightsRecord".casefold():
            from .insider_risk_scoped_user_insights_record import InsiderRiskScopedUserInsightsRecord

            return InsiderRiskScopedUserInsightsRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.insiderRiskScopedUsersRecord".casefold():
            from .insider_risk_scoped_users_record import InsiderRiskScopedUsersRecord

            return InsiderRiskScopedUsersRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.irmSecurityAlertRecord".casefold():
            from .irm_security_alert_record import IrmSecurityAlertRecord

            return IrmSecurityAlertRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.irmUserDefinedDetectionRecord".casefold():
            from .irm_user_defined_detection_record import IrmUserDefinedDetectionRecord

            return IrmUserDefinedDetectionRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.kaizalaAuditRecord".casefold():
            from .kaizala_audit_record import KaizalaAuditRecord

            return KaizalaAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.labelAnalyticsAggregateAuditRecord".casefold():
            from .label_analytics_aggregate_audit_record import LabelAnalyticsAggregateAuditRecord

            return LabelAnalyticsAggregateAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.labelContentExplorerAuditRecord".casefold():
            from .label_content_explorer_audit_record import LabelContentExplorerAuditRecord

            return LabelContentExplorerAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.largeContentMetadataAuditRecord".casefold():
            from .large_content_metadata_audit_record import LargeContentMetadataAuditRecord

            return LargeContentMetadataAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.m365ComplianceConnectorAuditRecord".casefold():
            from .m365_compliance_connector_audit_record import M365ComplianceConnectorAuditRecord

            return M365ComplianceConnectorAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.m365DAADAuditRecord".casefold():
            from .m365_d_a_a_d_audit_record import M365DAADAuditRecord

            return M365DAADAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.mailSubmissionData".casefold():
            from .mail_submission_data import MailSubmissionData

            return MailSubmissionData()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.managedServicesAuditRecord".casefold():
            from .managed_services_audit_record import ManagedServicesAuditRecord

            return ManagedServicesAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.managedTenantsAuditRecord".casefold():
            from .managed_tenants_audit_record import ManagedTenantsAuditRecord

            return ManagedTenantsAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.mapgAlertsAuditRecord".casefold():
            from .mapg_alerts_audit_record import MapgAlertsAuditRecord

            return MapgAlertsAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.mapgOnboardAuditRecord".casefold():
            from .mapg_onboard_audit_record import MapgOnboardAuditRecord

            return MapgOnboardAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.mapgPolicyAuditRecord".casefold():
            from .mapg_policy_audit_record import MapgPolicyAuditRecord

            return MapgPolicyAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.mcasAlertsAuditRecord".casefold():
            from .mcas_alerts_audit_record import McasAlertsAuditRecord

            return McasAlertsAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.mdaDataSecuritySignalRecord".casefold():
            from .mda_data_security_signal_record import MdaDataSecuritySignalRecord

            return MdaDataSecuritySignalRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.mdatpAuditRecord".casefold():
            from .mdatp_audit_record import MdatpAuditRecord

            return MdatpAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.mdcEventsRecord".casefold():
            from .mdc_events_record import MdcEventsRecord

            return MdcEventsRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.mdiAuditRecord".casefold():
            from .mdi_audit_record import MdiAuditRecord

            return MdiAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.meshWorldsAuditRecord".casefold():
            from .mesh_worlds_audit_record import MeshWorldsAuditRecord

            return MeshWorldsAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.microsoft365BackupBackupItemAuditRecord".casefold():
            from .microsoft365_backup_backup_item_audit_record import Microsoft365BackupBackupItemAuditRecord

            return Microsoft365BackupBackupItemAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.microsoft365BackupBackupPolicyAuditRecord".casefold():
            from .microsoft365_backup_backup_policy_audit_record import Microsoft365BackupBackupPolicyAuditRecord

            return Microsoft365BackupBackupPolicyAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.microsoft365BackupRestoreItemAuditRecord".casefold():
            from .microsoft365_backup_restore_item_audit_record import Microsoft365BackupRestoreItemAuditRecord

            return Microsoft365BackupRestoreItemAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.microsoft365BackupRestoreTaskAuditRecord".casefold():
            from .microsoft365_backup_restore_task_audit_record import Microsoft365BackupRestoreTaskAuditRecord

            return Microsoft365BackupRestoreTaskAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.microsoftDefenderExpertsBaseAuditRecord".casefold():
            from .microsoft_defender_experts_base_audit_record import MicrosoftDefenderExpertsBaseAuditRecord

            return MicrosoftDefenderExpertsBaseAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.microsoftDefenderExpertsXDRAuditRecord".casefold():
            from .microsoft_defender_experts_x_d_r_audit_record import MicrosoftDefenderExpertsXDRAuditRecord

            return MicrosoftDefenderExpertsXDRAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.microsoftFlowAuditRecord".casefold():
            from .microsoft_flow_audit_record import MicrosoftFlowAuditRecord

            return MicrosoftFlowAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.microsoftFormsAuditRecord".casefold():
            from .microsoft_forms_audit_record import MicrosoftFormsAuditRecord

            return MicrosoftFormsAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.microsoftGraphDataConnectConsent".casefold():
            from .microsoft_graph_data_connect_consent import MicrosoftGraphDataConnectConsent

            return MicrosoftGraphDataConnectConsent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.microsoftGraphDataConnectOperation".casefold():
            from .microsoft_graph_data_connect_operation import MicrosoftGraphDataConnectOperation

            return MicrosoftGraphDataConnectOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.microsoftPurviewDataMapOperationRecord".casefold():
            from .microsoft_purview_data_map_operation_record import MicrosoftPurviewDataMapOperationRecord

            return MicrosoftPurviewDataMapOperationRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.microsoftPurviewMetadataPolicyOperationRecord".casefold():
            from .microsoft_purview_metadata_policy_operation_record import MicrosoftPurviewMetadataPolicyOperationRecord

            return MicrosoftPurviewMetadataPolicyOperationRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.microsoftPurviewPolicyOperationRecord".casefold():
            from .microsoft_purview_policy_operation_record import MicrosoftPurviewPolicyOperationRecord

            return MicrosoftPurviewPolicyOperationRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.microsoftPurviewPrivacyAuditEvent".casefold():
            from .microsoft_purview_privacy_audit_event import MicrosoftPurviewPrivacyAuditEvent

            return MicrosoftPurviewPrivacyAuditEvent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.microsoftStreamAuditRecord".casefold():
            from .microsoft_stream_audit_record import MicrosoftStreamAuditRecord

            return MicrosoftStreamAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.microsoftTeamsAdminAuditRecord".casefold():
            from .microsoft_teams_admin_audit_record import MicrosoftTeamsAdminAuditRecord

            return MicrosoftTeamsAdminAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.microsoftTeamsAnalyticsAuditRecord".casefold():
            from .microsoft_teams_analytics_audit_record import MicrosoftTeamsAnalyticsAuditRecord

            return MicrosoftTeamsAnalyticsAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.microsoftTeamsAuditRecord".casefold():
            from .microsoft_teams_audit_record import MicrosoftTeamsAuditRecord

            return MicrosoftTeamsAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.microsoftTeamsDeviceAuditRecord".casefold():
            from .microsoft_teams_device_audit_record import MicrosoftTeamsDeviceAuditRecord

            return MicrosoftTeamsDeviceAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.microsoftTeamsRetentionLabelActionAuditRecord".casefold():
            from .microsoft_teams_retention_label_action_audit_record import MicrosoftTeamsRetentionLabelActionAuditRecord

            return MicrosoftTeamsRetentionLabelActionAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.microsoftTeamsSensitivityLabelActionAuditRecord".casefold():
            from .microsoft_teams_sensitivity_label_action_audit_record import MicrosoftTeamsSensitivityLabelActionAuditRecord

            return MicrosoftTeamsSensitivityLabelActionAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.microsoftTeamsShiftsAuditRecord".casefold():
            from .microsoft_teams_shifts_audit_record import MicrosoftTeamsShiftsAuditRecord

            return MicrosoftTeamsShiftsAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.mipAutoLabelExchangeItemAuditRecord".casefold():
            from .mip_auto_label_exchange_item_audit_record import MipAutoLabelExchangeItemAuditRecord

            return MipAutoLabelExchangeItemAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.mipAutoLabelItemAuditRecord".casefold():
            from .mip_auto_label_item_audit_record import MipAutoLabelItemAuditRecord

            return MipAutoLabelItemAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.mipAutoLabelPolicyAuditRecord".casefold():
            from .mip_auto_label_policy_audit_record import MipAutoLabelPolicyAuditRecord

            return MipAutoLabelPolicyAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.mipAutoLabelProgressFeedbackAuditRecord".casefold():
            from .mip_auto_label_progress_feedback_audit_record import MipAutoLabelProgressFeedbackAuditRecord

            return MipAutoLabelProgressFeedbackAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.mipAutoLabelSharePointItemAuditRecord".casefold():
            from .mip_auto_label_share_point_item_audit_record import MipAutoLabelSharePointItemAuditRecord

            return MipAutoLabelSharePointItemAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.mipAutoLabelSharePointPolicyLocationAuditRecord".casefold():
            from .mip_auto_label_share_point_policy_location_audit_record import MipAutoLabelSharePointPolicyLocationAuditRecord

            return MipAutoLabelSharePointPolicyLocationAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.mipAutoLabelSimulationSharePointCompletionRecord".casefold():
            from .mip_auto_label_simulation_share_point_completion_record import MipAutoLabelSimulationSharePointCompletionRecord

            return MipAutoLabelSimulationSharePointCompletionRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.mipAutoLabelSimulationSharePointProgressRecord".casefold():
            from .mip_auto_label_simulation_share_point_progress_record import MipAutoLabelSimulationSharePointProgressRecord

            return MipAutoLabelSimulationSharePointProgressRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.mipAutoLabelSimulationStatisticsRecord".casefold():
            from .mip_auto_label_simulation_statistics_record import MipAutoLabelSimulationStatisticsRecord

            return MipAutoLabelSimulationStatisticsRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.mipAutoLabelSimulationStatusRecord".casefold():
            from .mip_auto_label_simulation_status_record import MipAutoLabelSimulationStatusRecord

            return MipAutoLabelSimulationStatusRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.mipExactDataMatchAuditRecord".casefold():
            from .mip_exact_data_match_audit_record import MipExactDataMatchAuditRecord

            return MipExactDataMatchAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.mipLabelAnalyticsAuditRecord".casefold():
            from .mip_label_analytics_audit_record import MipLabelAnalyticsAuditRecord

            return MipLabelAnalyticsAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.mipLabelAuditRecord".casefold():
            from .mip_label_audit_record import MipLabelAuditRecord

            return MipLabelAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.mS365DCustomDetectionAuditRecord".casefold():
            from .m_s365_d_custom_detection_audit_record import MS365DCustomDetectionAuditRecord

            return MS365DCustomDetectionAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.mS365DIncidentAuditRecord".casefold():
            from .m_s365_d_incident_audit_record import MS365DIncidentAuditRecord

            return MS365DIncidentAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.mS365DSuppressionRuleAuditRecord".casefold():
            from .m_s365_d_suppression_rule_audit_record import MS365DSuppressionRuleAuditRecord

            return MS365DSuppressionRuleAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.msdeGeneralSettingsAuditRecord".casefold():
            from .msde_general_settings_audit_record import MsdeGeneralSettingsAuditRecord

            return MsdeGeneralSettingsAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.msdeIndicatorsSettingsAuditRecord".casefold():
            from .msde_indicators_settings_audit_record import MsdeIndicatorsSettingsAuditRecord

            return MsdeIndicatorsSettingsAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.msdeResponseActionsAuditRecord".casefold():
            from .msde_response_actions_audit_record import MsdeResponseActionsAuditRecord

            return MsdeResponseActionsAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.msdeRolesSettingsAuditRecord".casefold():
            from .msde_roles_settings_audit_record import MsdeRolesSettingsAuditRecord

            return MsdeRolesSettingsAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.msticNationStateNotificationRecord".casefold():
            from .mstic_nation_state_notification_record import MsticNationStateNotificationRecord

            return MsticNationStateNotificationRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.multiStageDispositionAuditRecord".casefold():
            from .multi_stage_disposition_audit_record import MultiStageDispositionAuditRecord

            return MultiStageDispositionAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.myAnalyticsSettingsAuditRecord".casefold():
            from .my_analytics_settings_audit_record import MyAnalyticsSettingsAuditRecord

            return MyAnalyticsSettingsAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.officeNativeAuditRecord".casefold():
            from .office_native_audit_record import OfficeNativeAuditRecord

            return OfficeNativeAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.omePortalAuditRecord".casefold():
            from .ome_portal_audit_record import OmePortalAuditRecord

            return OmePortalAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.oneDriveAuditRecord".casefold():
            from .one_drive_audit_record import OneDriveAuditRecord

            return OneDriveAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.onPremisesFileShareScannerDlpAuditRecord".casefold():
            from .on_premises_file_share_scanner_dlp_audit_record import OnPremisesFileShareScannerDlpAuditRecord

            return OnPremisesFileShareScannerDlpAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.onPremisesScannerDlpAuditRecord".casefold():
            from .on_premises_scanner_dlp_audit_record import OnPremisesScannerDlpAuditRecord

            return OnPremisesScannerDlpAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.onPremisesSharePointScannerDlpAuditRecord".casefold():
            from .on_premises_share_point_scanner_dlp_audit_record import OnPremisesSharePointScannerDlpAuditRecord

            return OnPremisesSharePointScannerDlpAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.owaGetAccessTokenForResourceAuditRecord".casefold():
            from .owa_get_access_token_for_resource_audit_record import OwaGetAccessTokenForResourceAuditRecord

            return OwaGetAccessTokenForResourceAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.peopleAdminSettingsAuditRecord".casefold():
            from .people_admin_settings_audit_record import PeopleAdminSettingsAuditRecord

            return PeopleAdminSettingsAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.physicalBadgingSignalAuditRecord".casefold():
            from .physical_badging_signal_audit_record import PhysicalBadgingSignalAuditRecord

            return PhysicalBadgingSignalAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.plannerCopyPlanAuditRecord".casefold():
            from .planner_copy_plan_audit_record import PlannerCopyPlanAuditRecord

            return PlannerCopyPlanAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.plannerPlanAuditRecord".casefold():
            from .planner_plan_audit_record import PlannerPlanAuditRecord

            return PlannerPlanAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.plannerPlanListAuditRecord".casefold():
            from .planner_plan_list_audit_record import PlannerPlanListAuditRecord

            return PlannerPlanListAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.plannerRosterAuditRecord".casefold():
            from .planner_roster_audit_record import PlannerRosterAuditRecord

            return PlannerRosterAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.plannerRosterSensitivityLabelAuditRecord".casefold():
            from .planner_roster_sensitivity_label_audit_record import PlannerRosterSensitivityLabelAuditRecord

            return PlannerRosterSensitivityLabelAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.plannerTaskAuditRecord".casefold():
            from .planner_task_audit_record import PlannerTaskAuditRecord

            return PlannerTaskAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.plannerTaskListAuditRecord".casefold():
            from .planner_task_list_audit_record import PlannerTaskListAuditRecord

            return PlannerTaskListAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.plannerTenantSettingsAuditRecord".casefold():
            from .planner_tenant_settings_audit_record import PlannerTenantSettingsAuditRecord

            return PlannerTenantSettingsAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.powerAppsAuditAppRecord".casefold():
            from .power_apps_audit_app_record import PowerAppsAuditAppRecord

            return PowerAppsAuditAppRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.powerAppsAuditPlanRecord".casefold():
            from .power_apps_audit_plan_record import PowerAppsAuditPlanRecord

            return PowerAppsAuditPlanRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.powerAppsAuditResourceRecord".casefold():
            from .power_apps_audit_resource_record import PowerAppsAuditResourceRecord

            return PowerAppsAuditResourceRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.powerBiAuditRecord".casefold():
            from .power_bi_audit_record import PowerBiAuditRecord

            return PowerBiAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.powerBiDlpAuditRecord".casefold():
            from .power_bi_dlp_audit_record import PowerBiDlpAuditRecord

            return PowerBiDlpAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.powerPagesSiteAuditRecord".casefold():
            from .power_pages_site_audit_record import PowerPagesSiteAuditRecord

            return PowerPagesSiteAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.powerPlatformAdminDlpAuditRecord".casefold():
            from .power_platform_admin_dlp_audit_record import PowerPlatformAdminDlpAuditRecord

            return PowerPlatformAdminDlpAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.powerPlatformAdminEnvironmentAuditRecord".casefold():
            from .power_platform_admin_environment_audit_record import PowerPlatformAdminEnvironmentAuditRecord

            return PowerPlatformAdminEnvironmentAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.powerPlatformAdministratorActivityRecord".casefold():
            from .power_platform_administrator_activity_record import PowerPlatformAdministratorActivityRecord

            return PowerPlatformAdministratorActivityRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.powerPlatformLockboxResourceAccessRequestAuditRecord".casefold():
            from .power_platform_lockbox_resource_access_request_audit_record import PowerPlatformLockboxResourceAccessRequestAuditRecord

            return PowerPlatformLockboxResourceAccessRequestAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.powerPlatformLockboxResourceCommandAuditRecord".casefold():
            from .power_platform_lockbox_resource_command_audit_record import PowerPlatformLockboxResourceCommandAuditRecord

            return PowerPlatformLockboxResourceCommandAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.powerPlatformServiceActivityAuditRecord".casefold():
            from .power_platform_service_activity_audit_record import PowerPlatformServiceActivityAuditRecord

            return PowerPlatformServiceActivityAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.privacyDataMatchAuditRecord".casefold():
            from .privacy_data_match_audit_record import PrivacyDataMatchAuditRecord

            return PrivacyDataMatchAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.privacyDataMinimizationRecord".casefold():
            from .privacy_data_minimization_record import PrivacyDataMinimizationRecord

            return PrivacyDataMinimizationRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.privacyDigestEmailRecord".casefold():
            from .privacy_digest_email_record import PrivacyDigestEmailRecord

            return PrivacyDigestEmailRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.privacyOpenAccessAuditRecord".casefold():
            from .privacy_open_access_audit_record import PrivacyOpenAccessAuditRecord

            return PrivacyOpenAccessAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.privacyPortalAuditRecord".casefold():
            from .privacy_portal_audit_record import PrivacyPortalAuditRecord

            return PrivacyPortalAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.privacyRemediationActionRecord".casefold():
            from .privacy_remediation_action_record import PrivacyRemediationActionRecord

            return PrivacyRemediationActionRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.privacyRemediationRecord".casefold():
            from .privacy_remediation_record import PrivacyRemediationRecord

            return PrivacyRemediationRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.privacyTenantAuditHistoryRecord".casefold():
            from .privacy_tenant_audit_history_record import PrivacyTenantAuditHistoryRecord

            return PrivacyTenantAuditHistoryRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.projectAuditRecord".casefold():
            from .project_audit_record import ProjectAuditRecord

            return ProjectAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.projectForTheWebAssignedToMeSettingsAuditRecord".casefold():
            from .project_for_the_web_assigned_to_me_settings_audit_record import ProjectForTheWebAssignedToMeSettingsAuditRecord

            return ProjectForTheWebAssignedToMeSettingsAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.projectForTheWebProjectAuditRecord".casefold():
            from .project_for_the_web_project_audit_record import ProjectForTheWebProjectAuditRecord

            return ProjectForTheWebProjectAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.projectForTheWebProjectSettingsAuditRecord".casefold():
            from .project_for_the_web_project_settings_audit_record import ProjectForTheWebProjectSettingsAuditRecord

            return ProjectForTheWebProjectSettingsAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.projectForTheWebRoadmapAuditRecord".casefold():
            from .project_for_the_web_roadmap_audit_record import ProjectForTheWebRoadmapAuditRecord

            return ProjectForTheWebRoadmapAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.projectForTheWebRoadmapItemAuditRecord".casefold():
            from .project_for_the_web_roadmap_item_audit_record import ProjectForTheWebRoadmapItemAuditRecord

            return ProjectForTheWebRoadmapItemAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.projectForTheWebRoadmapSettingsAuditRecord".casefold():
            from .project_for_the_web_roadmap_settings_audit_record import ProjectForTheWebRoadmapSettingsAuditRecord

            return ProjectForTheWebRoadmapSettingsAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.projectForTheWebTaskAuditRecord".casefold():
            from .project_for_the_web_task_audit_record import ProjectForTheWebTaskAuditRecord

            return ProjectForTheWebTaskAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.publicFolderAuditRecord".casefold():
            from .public_folder_audit_record import PublicFolderAuditRecord

            return PublicFolderAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.purviewInsiderRiskAlertsRecord".casefold():
            from .purview_insider_risk_alerts_record import PurviewInsiderRiskAlertsRecord

            return PurviewInsiderRiskAlertsRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.purviewInsiderRiskCasesRecord".casefold():
            from .purview_insider_risk_cases_record import PurviewInsiderRiskCasesRecord

            return PurviewInsiderRiskCasesRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.quarantineAuditRecord".casefold():
            from .quarantine_audit_record import QuarantineAuditRecord

            return QuarantineAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.recordsManagementAuditRecord".casefold():
            from .records_management_audit_record import RecordsManagementAuditRecord

            return RecordsManagementAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.retentionPolicyAuditRecord".casefold():
            from .retention_policy_audit_record import RetentionPolicyAuditRecord

            return RetentionPolicyAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.scoreEvidence".casefold():
            from .score_evidence import ScoreEvidence

            return ScoreEvidence()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.scorePlatformGenericAuditRecord".casefold():
            from .score_platform_generic_audit_record import ScorePlatformGenericAuditRecord

            return ScorePlatformGenericAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.scriptRunAuditRecord".casefold():
            from .script_run_audit_record import ScriptRunAuditRecord

            return ScriptRunAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.searchAuditRecord".casefold():
            from .search_audit_record import SearchAuditRecord

            return SearchAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.securityComplianceAlertRecord".casefold():
            from .security_compliance_alert_record import SecurityComplianceAlertRecord

            return SecurityComplianceAlertRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.securityComplianceCenterEOPCmdletAuditRecord".casefold():
            from .security_compliance_center_e_o_p_cmdlet_audit_record import SecurityComplianceCenterEOPCmdletAuditRecord

            return SecurityComplianceCenterEOPCmdletAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.securityComplianceInsightsAuditRecord".casefold():
            from .security_compliance_insights_audit_record import SecurityComplianceInsightsAuditRecord

            return SecurityComplianceInsightsAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.securityComplianceRBACAuditRecord".casefold():
            from .security_compliance_r_b_a_c_audit_record import SecurityComplianceRBACAuditRecord

            return SecurityComplianceRBACAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.securityComplianceUserChangeAuditRecord".casefold():
            from .security_compliance_user_change_audit_record import SecurityComplianceUserChangeAuditRecord

            return SecurityComplianceUserChangeAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.sharePointAppPermissionOperationAuditRecord".casefold():
            from .share_point_app_permission_operation_audit_record import SharePointAppPermissionOperationAuditRecord

            return SharePointAppPermissionOperationAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.sharePointAuditRecord".casefold():
            from .share_point_audit_record import SharePointAuditRecord

            return SharePointAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.sharePointCommentOperationAuditRecord".casefold():
            from .share_point_comment_operation_audit_record import SharePointCommentOperationAuditRecord

            return SharePointCommentOperationAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.sharePointContentTypeOperationAuditRecord".casefold():
            from .share_point_content_type_operation_audit_record import SharePointContentTypeOperationAuditRecord

            return SharePointContentTypeOperationAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.sharePointESignatureAuditRecord".casefold():
            from .share_point_e_signature_audit_record import SharePointESignatureAuditRecord

            return SharePointESignatureAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.sharePointFieldOperationAuditRecord".casefold():
            from .share_point_field_operation_audit_record import SharePointFieldOperationAuditRecord

            return SharePointFieldOperationAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.sharePointFileOperationAuditRecord".casefold():
            from .share_point_file_operation_audit_record import SharePointFileOperationAuditRecord

            return SharePointFileOperationAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.sharePointListOperationAuditRecord".casefold():
            from .share_point_list_operation_audit_record import SharePointListOperationAuditRecord

            return SharePointListOperationAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.sharePointSharingOperationAuditRecord".casefold():
            from .share_point_sharing_operation_audit_record import SharePointSharingOperationAuditRecord

            return SharePointSharingOperationAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.skypeForBusinessBaseAuditRecord".casefold():
            from .skype_for_business_base_audit_record import SkypeForBusinessBaseAuditRecord

            return SkypeForBusinessBaseAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.skypeForBusinessCmdletsAuditRecord".casefold():
            from .skype_for_business_cmdlets_audit_record import SkypeForBusinessCmdletsAuditRecord

            return SkypeForBusinessCmdletsAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.skypeForBusinessPSTNUsageAuditRecord".casefold():
            from .skype_for_business_p_s_t_n_usage_audit_record import SkypeForBusinessPSTNUsageAuditRecord

            return SkypeForBusinessPSTNUsageAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.skypeForBusinessUsersBlockedAuditRecord".casefold():
            from .skype_for_business_users_blocked_audit_record import SkypeForBusinessUsersBlockedAuditRecord

            return SkypeForBusinessUsersBlockedAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.smsCreatePhoneNumberRecord".casefold():
            from .sms_create_phone_number_record import SmsCreatePhoneNumberRecord

            return SmsCreatePhoneNumberRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.smsDeletePhoneNumberRecord".casefold():
            from .sms_delete_phone_number_record import SmsDeletePhoneNumberRecord

            return SmsDeletePhoneNumberRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.supervisoryReviewDayXInsightsAuditRecord".casefold():
            from .supervisory_review_day_x_insights_audit_record import SupervisoryReviewDayXInsightsAuditRecord

            return SupervisoryReviewDayXInsightsAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.syntheticProbeAuditRecord".casefold():
            from .synthetic_probe_audit_record import SyntheticProbeAuditRecord

            return SyntheticProbeAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.teamsEasyApprovalsAuditRecord".casefold():
            from .teams_easy_approvals_audit_record import TeamsEasyApprovalsAuditRecord

            return TeamsEasyApprovalsAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.teamsHealthcareAuditRecord".casefold():
            from .teams_healthcare_audit_record import TeamsHealthcareAuditRecord

            return TeamsHealthcareAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.teamsUpdatesAuditRecord".casefold():
            from .teams_updates_audit_record import TeamsUpdatesAuditRecord

            return TeamsUpdatesAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.tenantAllowBlockListAuditRecord".casefold():
            from .tenant_allow_block_list_audit_record import TenantAllowBlockListAuditRecord

            return TenantAllowBlockListAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.threatFinderAuditRecord".casefold():
            from .threat_finder_audit_record import ThreatFinderAuditRecord

            return ThreatFinderAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.threatIntelligenceAtpContentData".casefold():
            from .threat_intelligence_atp_content_data import ThreatIntelligenceAtpContentData

            return ThreatIntelligenceAtpContentData()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.threatIntelligenceMailData".casefold():
            from .threat_intelligence_mail_data import ThreatIntelligenceMailData

            return ThreatIntelligenceMailData()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.threatIntelligenceUrlClickData".casefold():
            from .threat_intelligence_url_click_data import ThreatIntelligenceUrlClickData

            return ThreatIntelligenceUrlClickData()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.todoAuditRecord".casefold():
            from .todo_audit_record import TodoAuditRecord

            return TodoAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.uamOperationAuditRecord".casefold():
            from .uam_operation_audit_record import UamOperationAuditRecord

            return UamOperationAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.unifiedGroupAuditRecord".casefold():
            from .unified_group_audit_record import UnifiedGroupAuditRecord

            return UnifiedGroupAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.unifiedSimulationMatchedItemAuditRecord".casefold():
            from .unified_simulation_matched_item_audit_record import UnifiedSimulationMatchedItemAuditRecord

            return UnifiedSimulationMatchedItemAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.unifiedSimulationSummaryAuditRecord".casefold():
            from .unified_simulation_summary_audit_record import UnifiedSimulationSummaryAuditRecord

            return UnifiedSimulationSummaryAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.uploadCertificateRecord".casefold():
            from .upload_certificate_record import UploadCertificateRecord

            return UploadCertificateRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.urbacAssignmentAuditRecord".casefold():
            from .urbac_assignment_audit_record import UrbacAssignmentAuditRecord

            return UrbacAssignmentAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.urbacEnableStateAuditRecord".casefold():
            from .urbac_enable_state_audit_record import UrbacEnableStateAuditRecord

            return UrbacEnableStateAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.urbacRoleAuditRecord".casefold():
            from .urbac_role_audit_record import UrbacRoleAuditRecord

            return UrbacRoleAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.userTrainingAuditRecord".casefold():
            from .user_training_audit_record import UserTrainingAuditRecord

            return UserTrainingAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.vfamBasePolicyAuditRecord".casefold():
            from .vfam_base_policy_audit_record import VfamBasePolicyAuditRecord

            return VfamBasePolicyAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.vfamCreatePolicyAuditRecord".casefold():
            from .vfam_create_policy_audit_record import VfamCreatePolicyAuditRecord

            return VfamCreatePolicyAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.vfamDeletePolicyAuditRecord".casefold():
            from .vfam_delete_policy_audit_record import VfamDeletePolicyAuditRecord

            return VfamDeletePolicyAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.vfamUpdatePolicyAuditRecord".casefold():
            from .vfam_update_policy_audit_record import VfamUpdatePolicyAuditRecord

            return VfamUpdatePolicyAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.vivaGoalsAuditRecord".casefold():
            from .viva_goals_audit_record import VivaGoalsAuditRecord

            return VivaGoalsAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.vivaLearningAdminAuditRecord".casefold():
            from .viva_learning_admin_audit_record import VivaLearningAdminAuditRecord

            return VivaLearningAdminAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.vivaLearningAuditRecord".casefold():
            from .viva_learning_audit_record import VivaLearningAuditRecord

            return VivaLearningAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.vivaPulseAdminAuditRecord".casefold():
            from .viva_pulse_admin_audit_record import VivaPulseAdminAuditRecord

            return VivaPulseAdminAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.vivaPulseOrganizerAuditRecord".casefold():
            from .viva_pulse_organizer_audit_record import VivaPulseOrganizerAuditRecord

            return VivaPulseOrganizerAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.vivaPulseReportAuditRecord".casefold():
            from .viva_pulse_report_audit_record import VivaPulseReportAuditRecord

            return VivaPulseReportAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.vivaPulseResponseAuditRecord".casefold():
            from .viva_pulse_response_audit_record import VivaPulseResponseAuditRecord

            return VivaPulseResponseAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.wdatpAlertsAuditRecord".casefold():
            from .wdatp_alerts_audit_record import WdatpAlertsAuditRecord

            return WdatpAlertsAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.windows365CustomerLockboxAuditRecord".casefold():
            from .windows365_customer_lockbox_audit_record import Windows365CustomerLockboxAuditRecord

            return Windows365CustomerLockboxAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.workplaceAnalyticsAuditRecord".casefold():
            from .workplace_analytics_audit_record import WorkplaceAnalyticsAuditRecord

            return WorkplaceAnalyticsAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.yammerAuditRecord".casefold():
            from .yammer_audit_record import YammerAuditRecord

            return YammerAuditRecord()
        return AuditData()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .aad_risk_detection_audit_record import AadRiskDetectionAuditRecord
        from .aed_audit_record import AedAuditRecord
        from .aip_file_deleted import AipFileDeleted
        from .aip_heart_beat import AipHeartBeat
        from .aip_protection_action_log_request import AipProtectionActionLogRequest
        from .aip_scanner_discover_event import AipScannerDiscoverEvent
        from .aip_sensitivity_label_action_log_request import AipSensitivityLabelActionLogRequest
        from .air_admin_action_investigation_data import AirAdminActionInvestigationData
        from .air_investigation_data import AirInvestigationData
        from .air_manual_investigation_data import AirManualInvestigationData
        from .ai_app_interaction_audit_record import AiAppInteractionAuditRecord
        from .attack_sim_admin_audit_record import AttackSimAdminAuditRecord
        from .audit_search_audit_record import AuditSearchAuditRecord
        from .azure_active_directory_account_logon_audit_record import AzureActiveDirectoryAccountLogonAuditRecord
        from .azure_active_directory_audit_record import AzureActiveDirectoryAuditRecord
        from .azure_active_directory_base_audit_record import AzureActiveDirectoryBaseAuditRecord
        from .azure_active_directory_sts_logon_audit_record import AzureActiveDirectoryStsLogonAuditRecord
        from .campaign_audit_record import CampaignAuditRecord
        from .case_audit_record import CaseAuditRecord
        from .case_investigation import CaseInvestigation
        from .cdp_cold_crawl_status_record import CdpColdCrawlStatusRecord
        from .cdp_content_explorer_aggregate_record import CdpContentExplorerAggregateRecord
        from .cdp_dlp_sensitive_audit_record import CdpDlpSensitiveAuditRecord
        from .cdp_dlp_sensitive_endpoint_audit_record import CdpDlpSensitiveEndpointAuditRecord
        from .cdp_log_record import CdpLogRecord
        from .cdp_ocr_billing_record import CdpOcrBillingRecord
        from .cdp_resource_scope_change_event_record import CdpResourceScopeChangeEventRecord
        from .cerner_s_m_s_link_record import CernerSMSLinkRecord
        from .cerner_s_m_s_settings_update_record import CernerSMSSettingsUpdateRecord
        from .cerner_s_m_s_unlink_record import CernerSMSUnlinkRecord
        from .compliance_connector_audit_record import ComplianceConnectorAuditRecord
        from .compliance_dlp_applications_audit_record import ComplianceDlpApplicationsAuditRecord
        from .compliance_dlp_applications_classification_audit_record import ComplianceDlpApplicationsClassificationAuditRecord
        from .compliance_dlp_base_audit_record import ComplianceDlpBaseAuditRecord
        from .compliance_dlp_classification_base_audit_record import ComplianceDlpClassificationBaseAuditRecord
        from .compliance_dlp_classification_base_cdp_record import ComplianceDlpClassificationBaseCdpRecord
        from .compliance_dlp_endpoint_audit_record import ComplianceDlpEndpointAuditRecord
        from .compliance_dlp_endpoint_discovery_audit_record import ComplianceDlpEndpointDiscoveryAuditRecord
        from .compliance_dlp_exchange_audit_record import ComplianceDlpExchangeAuditRecord
        from .compliance_dlp_exchange_classification_audit_record import ComplianceDlpExchangeClassificationAuditRecord
        from .compliance_dlp_exchange_classification_cdp_record import ComplianceDlpExchangeClassificationCdpRecord
        from .compliance_dlp_exchange_discovery_audit_record import ComplianceDlpExchangeDiscoveryAuditRecord
        from .compliance_dlp_share_point_audit_record import ComplianceDlpSharePointAuditRecord
        from .compliance_dlp_share_point_classification_audit_record import ComplianceDlpSharePointClassificationAuditRecord
        from .compliance_dlp_share_point_classification_extended_audit_record import ComplianceDlpSharePointClassificationExtendedAuditRecord
        from .compliance_d_l_m_exchange_audit_record import ComplianceDLMExchangeAuditRecord
        from .compliance_d_l_m_share_point_audit_record import ComplianceDLMSharePointAuditRecord
        from .compliance_manager_action_record import ComplianceManagerActionRecord
        from .compliance_supervision_base_audit_record import ComplianceSupervisionBaseAuditRecord
        from .compliance_supervision_exchange_audit_record import ComplianceSupervisionExchangeAuditRecord
        from .consumption_resource_audit_record import ConsumptionResourceAuditRecord
        from .copilot_interaction_audit_record import CopilotInteractionAuditRecord
        from .core_reporting_settings_audit_record import CoreReportingSettingsAuditRecord
        from .cortana_briefing_audit_record import CortanaBriefingAuditRecord
        from .cps_common_policy_audit_record import CpsCommonPolicyAuditRecord
        from .cps_policy_config_audit_record import CpsPolicyConfigAuditRecord
        from .crm_base_audit_record import CrmBaseAuditRecord
        from .crm_entity_operation_audit_record import CrmEntityOperationAuditRecord
        from .customer_key_service_encryption_audit_record import CustomerKeyServiceEncryptionAuditRecord
        from .data_center_security_base_audit_record import DataCenterSecurityBaseAuditRecord
        from .data_center_security_cmdlet_audit_record import DataCenterSecurityCmdletAuditRecord
        from .data_governance_audit_record import DataGovernanceAuditRecord
        from .data_insights_rest_api_audit_record import DataInsightsRestApiAuditRecord
        from .data_lake_export_operation_audit_record import DataLakeExportOperationAuditRecord
        from .data_share_operation_audit_record import DataShareOperationAuditRecord
        from .default_audit_data import DefaultAuditData
        from .defender_security_alert_base_record import DefenderSecurityAlertBaseRecord
        from .delete_certificate_record import DeleteCertificateRecord
        from .disable_consent_record import DisableConsentRecord
        from .discovery_audit_record import DiscoveryAuditRecord
        from .dlp_endpoint_audit_record import DlpEndpointAuditRecord
        from .dlp_sensitive_information_type_cmdlet_record import DlpSensitiveInformationTypeCmdletRecord
        from .dlp_sensitive_information_type_rule_package_cmdlet_record import DlpSensitiveInformationTypeRulePackageCmdletRecord
        from .download_certificate_record import DownloadCertificateRecord
        from .dynamics365_business_central_audit_record import Dynamics365BusinessCentralAuditRecord
        from .enable_consent_record import EnableConsentRecord
        from .epic_s_m_s_link_record import EpicSMSLinkRecord
        from .epic_s_m_s_settings_update_record import EpicSMSSettingsUpdateRecord
        from .epic_s_m_s_unlink_record import EpicSMSUnlinkRecord
        from .exchange_admin_audit_record import ExchangeAdminAuditRecord
        from .exchange_aggregated_mailbox_audit_record import ExchangeAggregatedMailboxAuditRecord
        from .exchange_aggregated_operation_record import ExchangeAggregatedOperationRecord
        from .exchange_mailbox_audit_base_record import ExchangeMailboxAuditBaseRecord
        from .exchange_mailbox_audit_group_record import ExchangeMailboxAuditGroupRecord
        from .exchange_mailbox_audit_record import ExchangeMailboxAuditRecord
        from .fhir_base_url_add_record import FhirBaseUrlAddRecord
        from .fhir_base_url_approve_record import FhirBaseUrlApproveRecord
        from .fhir_base_url_delete_record import FhirBaseUrlDeleteRecord
        from .fhir_base_url_update_record import FhirBaseUrlUpdateRecord
        from .healthcare_signal_record import HealthcareSignalRecord
        from .hosted_rpa_audit_record import HostedRpaAuditRecord
        from .hr_signal_audit_record import HrSignalAuditRecord
        from .hygiene_event_record import HygieneEventRecord
        from .information_barrier_policy_application_audit_record import InformationBarrierPolicyApplicationAuditRecord
        from .information_worker_protection_audit_record import InformationWorkerProtectionAuditRecord
        from .insider_risk_scoped_users_record import InsiderRiskScopedUsersRecord
        from .insider_risk_scoped_user_insights_record import InsiderRiskScopedUserInsightsRecord
        from .irm_security_alert_record import IrmSecurityAlertRecord
        from .irm_user_defined_detection_record import IrmUserDefinedDetectionRecord
        from .kaizala_audit_record import KaizalaAuditRecord
        from .label_analytics_aggregate_audit_record import LabelAnalyticsAggregateAuditRecord
        from .label_content_explorer_audit_record import LabelContentExplorerAuditRecord
        from .large_content_metadata_audit_record import LargeContentMetadataAuditRecord
        from .m365_compliance_connector_audit_record import M365ComplianceConnectorAuditRecord
        from .m365_d_a_a_d_audit_record import M365DAADAuditRecord
        from .mail_submission_data import MailSubmissionData
        from .managed_services_audit_record import ManagedServicesAuditRecord
        from .managed_tenants_audit_record import ManagedTenantsAuditRecord
        from .mapg_alerts_audit_record import MapgAlertsAuditRecord
        from .mapg_onboard_audit_record import MapgOnboardAuditRecord
        from .mapg_policy_audit_record import MapgPolicyAuditRecord
        from .mcas_alerts_audit_record import McasAlertsAuditRecord
        from .mdatp_audit_record import MdatpAuditRecord
        from .mda_data_security_signal_record import MdaDataSecuritySignalRecord
        from .mdc_events_record import MdcEventsRecord
        from .mdi_audit_record import MdiAuditRecord
        from .mesh_worlds_audit_record import MeshWorldsAuditRecord
        from .microsoft365_backup_backup_item_audit_record import Microsoft365BackupBackupItemAuditRecord
        from .microsoft365_backup_backup_policy_audit_record import Microsoft365BackupBackupPolicyAuditRecord
        from .microsoft365_backup_restore_item_audit_record import Microsoft365BackupRestoreItemAuditRecord
        from .microsoft365_backup_restore_task_audit_record import Microsoft365BackupRestoreTaskAuditRecord
        from .microsoft_defender_experts_base_audit_record import MicrosoftDefenderExpertsBaseAuditRecord
        from .microsoft_defender_experts_x_d_r_audit_record import MicrosoftDefenderExpertsXDRAuditRecord
        from .microsoft_flow_audit_record import MicrosoftFlowAuditRecord
        from .microsoft_forms_audit_record import MicrosoftFormsAuditRecord
        from .microsoft_graph_data_connect_consent import MicrosoftGraphDataConnectConsent
        from .microsoft_graph_data_connect_operation import MicrosoftGraphDataConnectOperation
        from .microsoft_purview_data_map_operation_record import MicrosoftPurviewDataMapOperationRecord
        from .microsoft_purview_metadata_policy_operation_record import MicrosoftPurviewMetadataPolicyOperationRecord
        from .microsoft_purview_policy_operation_record import MicrosoftPurviewPolicyOperationRecord
        from .microsoft_purview_privacy_audit_event import MicrosoftPurviewPrivacyAuditEvent
        from .microsoft_stream_audit_record import MicrosoftStreamAuditRecord
        from .microsoft_teams_admin_audit_record import MicrosoftTeamsAdminAuditRecord
        from .microsoft_teams_analytics_audit_record import MicrosoftTeamsAnalyticsAuditRecord
        from .microsoft_teams_audit_record import MicrosoftTeamsAuditRecord
        from .microsoft_teams_device_audit_record import MicrosoftTeamsDeviceAuditRecord
        from .microsoft_teams_retention_label_action_audit_record import MicrosoftTeamsRetentionLabelActionAuditRecord
        from .microsoft_teams_sensitivity_label_action_audit_record import MicrosoftTeamsSensitivityLabelActionAuditRecord
        from .microsoft_teams_shifts_audit_record import MicrosoftTeamsShiftsAuditRecord
        from .mip_auto_label_exchange_item_audit_record import MipAutoLabelExchangeItemAuditRecord
        from .mip_auto_label_item_audit_record import MipAutoLabelItemAuditRecord
        from .mip_auto_label_policy_audit_record import MipAutoLabelPolicyAuditRecord
        from .mip_auto_label_progress_feedback_audit_record import MipAutoLabelProgressFeedbackAuditRecord
        from .mip_auto_label_share_point_item_audit_record import MipAutoLabelSharePointItemAuditRecord
        from .mip_auto_label_share_point_policy_location_audit_record import MipAutoLabelSharePointPolicyLocationAuditRecord
        from .mip_auto_label_simulation_share_point_completion_record import MipAutoLabelSimulationSharePointCompletionRecord
        from .mip_auto_label_simulation_share_point_progress_record import MipAutoLabelSimulationSharePointProgressRecord
        from .mip_auto_label_simulation_statistics_record import MipAutoLabelSimulationStatisticsRecord
        from .mip_auto_label_simulation_status_record import MipAutoLabelSimulationStatusRecord
        from .mip_exact_data_match_audit_record import MipExactDataMatchAuditRecord
        from .mip_label_analytics_audit_record import MipLabelAnalyticsAuditRecord
        from .mip_label_audit_record import MipLabelAuditRecord
        from .msde_general_settings_audit_record import MsdeGeneralSettingsAuditRecord
        from .msde_indicators_settings_audit_record import MsdeIndicatorsSettingsAuditRecord
        from .msde_response_actions_audit_record import MsdeResponseActionsAuditRecord
        from .msde_roles_settings_audit_record import MsdeRolesSettingsAuditRecord
        from .mstic_nation_state_notification_record import MsticNationStateNotificationRecord
        from .multi_stage_disposition_audit_record import MultiStageDispositionAuditRecord
        from .my_analytics_settings_audit_record import MyAnalyticsSettingsAuditRecord
        from .m_s365_d_custom_detection_audit_record import MS365DCustomDetectionAuditRecord
        from .m_s365_d_incident_audit_record import MS365DIncidentAuditRecord
        from .m_s365_d_suppression_rule_audit_record import MS365DSuppressionRuleAuditRecord
        from .office_native_audit_record import OfficeNativeAuditRecord
        from .ome_portal_audit_record import OmePortalAuditRecord
        from .one_drive_audit_record import OneDriveAuditRecord
        from .on_premises_file_share_scanner_dlp_audit_record import OnPremisesFileShareScannerDlpAuditRecord
        from .on_premises_scanner_dlp_audit_record import OnPremisesScannerDlpAuditRecord
        from .on_premises_share_point_scanner_dlp_audit_record import OnPremisesSharePointScannerDlpAuditRecord
        from .owa_get_access_token_for_resource_audit_record import OwaGetAccessTokenForResourceAuditRecord
        from .people_admin_settings_audit_record import PeopleAdminSettingsAuditRecord
        from .physical_badging_signal_audit_record import PhysicalBadgingSignalAuditRecord
        from .planner_copy_plan_audit_record import PlannerCopyPlanAuditRecord
        from .planner_plan_audit_record import PlannerPlanAuditRecord
        from .planner_plan_list_audit_record import PlannerPlanListAuditRecord
        from .planner_roster_audit_record import PlannerRosterAuditRecord
        from .planner_roster_sensitivity_label_audit_record import PlannerRosterSensitivityLabelAuditRecord
        from .planner_task_audit_record import PlannerTaskAuditRecord
        from .planner_task_list_audit_record import PlannerTaskListAuditRecord
        from .planner_tenant_settings_audit_record import PlannerTenantSettingsAuditRecord
        from .power_apps_audit_app_record import PowerAppsAuditAppRecord
        from .power_apps_audit_plan_record import PowerAppsAuditPlanRecord
        from .power_apps_audit_resource_record import PowerAppsAuditResourceRecord
        from .power_bi_audit_record import PowerBiAuditRecord
        from .power_bi_dlp_audit_record import PowerBiDlpAuditRecord
        from .power_pages_site_audit_record import PowerPagesSiteAuditRecord
        from .power_platform_administrator_activity_record import PowerPlatformAdministratorActivityRecord
        from .power_platform_admin_dlp_audit_record import PowerPlatformAdminDlpAuditRecord
        from .power_platform_admin_environment_audit_record import PowerPlatformAdminEnvironmentAuditRecord
        from .power_platform_lockbox_resource_access_request_audit_record import PowerPlatformLockboxResourceAccessRequestAuditRecord
        from .power_platform_lockbox_resource_command_audit_record import PowerPlatformLockboxResourceCommandAuditRecord
        from .power_platform_service_activity_audit_record import PowerPlatformServiceActivityAuditRecord
        from .privacy_data_match_audit_record import PrivacyDataMatchAuditRecord
        from .privacy_data_minimization_record import PrivacyDataMinimizationRecord
        from .privacy_digest_email_record import PrivacyDigestEmailRecord
        from .privacy_open_access_audit_record import PrivacyOpenAccessAuditRecord
        from .privacy_portal_audit_record import PrivacyPortalAuditRecord
        from .privacy_remediation_action_record import PrivacyRemediationActionRecord
        from .privacy_remediation_record import PrivacyRemediationRecord
        from .privacy_tenant_audit_history_record import PrivacyTenantAuditHistoryRecord
        from .project_audit_record import ProjectAuditRecord
        from .project_for_the_web_assigned_to_me_settings_audit_record import ProjectForTheWebAssignedToMeSettingsAuditRecord
        from .project_for_the_web_project_audit_record import ProjectForTheWebProjectAuditRecord
        from .project_for_the_web_project_settings_audit_record import ProjectForTheWebProjectSettingsAuditRecord
        from .project_for_the_web_roadmap_audit_record import ProjectForTheWebRoadmapAuditRecord
        from .project_for_the_web_roadmap_item_audit_record import ProjectForTheWebRoadmapItemAuditRecord
        from .project_for_the_web_roadmap_settings_audit_record import ProjectForTheWebRoadmapSettingsAuditRecord
        from .project_for_the_web_task_audit_record import ProjectForTheWebTaskAuditRecord
        from .public_folder_audit_record import PublicFolderAuditRecord
        from .purview_insider_risk_alerts_record import PurviewInsiderRiskAlertsRecord
        from .purview_insider_risk_cases_record import PurviewInsiderRiskCasesRecord
        from .quarantine_audit_record import QuarantineAuditRecord
        from .records_management_audit_record import RecordsManagementAuditRecord
        from .retention_policy_audit_record import RetentionPolicyAuditRecord
        from .score_evidence import ScoreEvidence
        from .score_platform_generic_audit_record import ScorePlatformGenericAuditRecord
        from .script_run_audit_record import ScriptRunAuditRecord
        from .search_audit_record import SearchAuditRecord
        from .security_compliance_alert_record import SecurityComplianceAlertRecord
        from .security_compliance_center_e_o_p_cmdlet_audit_record import SecurityComplianceCenterEOPCmdletAuditRecord
        from .security_compliance_insights_audit_record import SecurityComplianceInsightsAuditRecord
        from .security_compliance_r_b_a_c_audit_record import SecurityComplianceRBACAuditRecord
        from .security_compliance_user_change_audit_record import SecurityComplianceUserChangeAuditRecord
        from .share_point_app_permission_operation_audit_record import SharePointAppPermissionOperationAuditRecord
        from .share_point_audit_record import SharePointAuditRecord
        from .share_point_comment_operation_audit_record import SharePointCommentOperationAuditRecord
        from .share_point_content_type_operation_audit_record import SharePointContentTypeOperationAuditRecord
        from .share_point_e_signature_audit_record import SharePointESignatureAuditRecord
        from .share_point_field_operation_audit_record import SharePointFieldOperationAuditRecord
        from .share_point_file_operation_audit_record import SharePointFileOperationAuditRecord
        from .share_point_list_operation_audit_record import SharePointListOperationAuditRecord
        from .share_point_sharing_operation_audit_record import SharePointSharingOperationAuditRecord
        from .skype_for_business_base_audit_record import SkypeForBusinessBaseAuditRecord
        from .skype_for_business_cmdlets_audit_record import SkypeForBusinessCmdletsAuditRecord
        from .skype_for_business_p_s_t_n_usage_audit_record import SkypeForBusinessPSTNUsageAuditRecord
        from .skype_for_business_users_blocked_audit_record import SkypeForBusinessUsersBlockedAuditRecord
        from .sms_create_phone_number_record import SmsCreatePhoneNumberRecord
        from .sms_delete_phone_number_record import SmsDeletePhoneNumberRecord
        from .supervisory_review_day_x_insights_audit_record import SupervisoryReviewDayXInsightsAuditRecord
        from .synthetic_probe_audit_record import SyntheticProbeAuditRecord
        from .teams_easy_approvals_audit_record import TeamsEasyApprovalsAuditRecord
        from .teams_healthcare_audit_record import TeamsHealthcareAuditRecord
        from .teams_updates_audit_record import TeamsUpdatesAuditRecord
        from .tenant_allow_block_list_audit_record import TenantAllowBlockListAuditRecord
        from .threat_finder_audit_record import ThreatFinderAuditRecord
        from .threat_intelligence_atp_content_data import ThreatIntelligenceAtpContentData
        from .threat_intelligence_mail_data import ThreatIntelligenceMailData
        from .threat_intelligence_url_click_data import ThreatIntelligenceUrlClickData
        from .todo_audit_record import TodoAuditRecord
        from .uam_operation_audit_record import UamOperationAuditRecord
        from .unified_group_audit_record import UnifiedGroupAuditRecord
        from .unified_simulation_matched_item_audit_record import UnifiedSimulationMatchedItemAuditRecord
        from .unified_simulation_summary_audit_record import UnifiedSimulationSummaryAuditRecord
        from .upload_certificate_record import UploadCertificateRecord
        from .urbac_assignment_audit_record import UrbacAssignmentAuditRecord
        from .urbac_enable_state_audit_record import UrbacEnableStateAuditRecord
        from .urbac_role_audit_record import UrbacRoleAuditRecord
        from .user_training_audit_record import UserTrainingAuditRecord
        from .vfam_base_policy_audit_record import VfamBasePolicyAuditRecord
        from .vfam_create_policy_audit_record import VfamCreatePolicyAuditRecord
        from .vfam_delete_policy_audit_record import VfamDeletePolicyAuditRecord
        from .vfam_update_policy_audit_record import VfamUpdatePolicyAuditRecord
        from .viva_goals_audit_record import VivaGoalsAuditRecord
        from .viva_learning_admin_audit_record import VivaLearningAdminAuditRecord
        from .viva_learning_audit_record import VivaLearningAuditRecord
        from .viva_pulse_admin_audit_record import VivaPulseAdminAuditRecord
        from .viva_pulse_organizer_audit_record import VivaPulseOrganizerAuditRecord
        from .viva_pulse_report_audit_record import VivaPulseReportAuditRecord
        from .viva_pulse_response_audit_record import VivaPulseResponseAuditRecord
        from .wdatp_alerts_audit_record import WdatpAlertsAuditRecord
        from .windows365_customer_lockbox_audit_record import Windows365CustomerLockboxAuditRecord
        from .workplace_analytics_audit_record import WorkplaceAnalyticsAuditRecord
        from .yammer_audit_record import YammerAuditRecord

        from .aad_risk_detection_audit_record import AadRiskDetectionAuditRecord
        from .aed_audit_record import AedAuditRecord
        from .aip_file_deleted import AipFileDeleted
        from .aip_heart_beat import AipHeartBeat
        from .aip_protection_action_log_request import AipProtectionActionLogRequest
        from .aip_scanner_discover_event import AipScannerDiscoverEvent
        from .aip_sensitivity_label_action_log_request import AipSensitivityLabelActionLogRequest
        from .air_admin_action_investigation_data import AirAdminActionInvestigationData
        from .air_investigation_data import AirInvestigationData
        from .air_manual_investigation_data import AirManualInvestigationData
        from .ai_app_interaction_audit_record import AiAppInteractionAuditRecord
        from .attack_sim_admin_audit_record import AttackSimAdminAuditRecord
        from .audit_search_audit_record import AuditSearchAuditRecord
        from .azure_active_directory_account_logon_audit_record import AzureActiveDirectoryAccountLogonAuditRecord
        from .azure_active_directory_audit_record import AzureActiveDirectoryAuditRecord
        from .azure_active_directory_base_audit_record import AzureActiveDirectoryBaseAuditRecord
        from .azure_active_directory_sts_logon_audit_record import AzureActiveDirectoryStsLogonAuditRecord
        from .campaign_audit_record import CampaignAuditRecord
        from .case_audit_record import CaseAuditRecord
        from .case_investigation import CaseInvestigation
        from .cdp_cold_crawl_status_record import CdpColdCrawlStatusRecord
        from .cdp_content_explorer_aggregate_record import CdpContentExplorerAggregateRecord
        from .cdp_dlp_sensitive_audit_record import CdpDlpSensitiveAuditRecord
        from .cdp_dlp_sensitive_endpoint_audit_record import CdpDlpSensitiveEndpointAuditRecord
        from .cdp_log_record import CdpLogRecord
        from .cdp_ocr_billing_record import CdpOcrBillingRecord
        from .cdp_resource_scope_change_event_record import CdpResourceScopeChangeEventRecord
        from .cerner_s_m_s_link_record import CernerSMSLinkRecord
        from .cerner_s_m_s_settings_update_record import CernerSMSSettingsUpdateRecord
        from .cerner_s_m_s_unlink_record import CernerSMSUnlinkRecord
        from .compliance_connector_audit_record import ComplianceConnectorAuditRecord
        from .compliance_dlp_applications_audit_record import ComplianceDlpApplicationsAuditRecord
        from .compliance_dlp_applications_classification_audit_record import ComplianceDlpApplicationsClassificationAuditRecord
        from .compliance_dlp_base_audit_record import ComplianceDlpBaseAuditRecord
        from .compliance_dlp_classification_base_audit_record import ComplianceDlpClassificationBaseAuditRecord
        from .compliance_dlp_classification_base_cdp_record import ComplianceDlpClassificationBaseCdpRecord
        from .compliance_dlp_endpoint_audit_record import ComplianceDlpEndpointAuditRecord
        from .compliance_dlp_endpoint_discovery_audit_record import ComplianceDlpEndpointDiscoveryAuditRecord
        from .compliance_dlp_exchange_audit_record import ComplianceDlpExchangeAuditRecord
        from .compliance_dlp_exchange_classification_audit_record import ComplianceDlpExchangeClassificationAuditRecord
        from .compliance_dlp_exchange_classification_cdp_record import ComplianceDlpExchangeClassificationCdpRecord
        from .compliance_dlp_exchange_discovery_audit_record import ComplianceDlpExchangeDiscoveryAuditRecord
        from .compliance_dlp_share_point_audit_record import ComplianceDlpSharePointAuditRecord
        from .compliance_dlp_share_point_classification_audit_record import ComplianceDlpSharePointClassificationAuditRecord
        from .compliance_dlp_share_point_classification_extended_audit_record import ComplianceDlpSharePointClassificationExtendedAuditRecord
        from .compliance_d_l_m_exchange_audit_record import ComplianceDLMExchangeAuditRecord
        from .compliance_d_l_m_share_point_audit_record import ComplianceDLMSharePointAuditRecord
        from .compliance_manager_action_record import ComplianceManagerActionRecord
        from .compliance_supervision_base_audit_record import ComplianceSupervisionBaseAuditRecord
        from .compliance_supervision_exchange_audit_record import ComplianceSupervisionExchangeAuditRecord
        from .consumption_resource_audit_record import ConsumptionResourceAuditRecord
        from .copilot_interaction_audit_record import CopilotInteractionAuditRecord
        from .core_reporting_settings_audit_record import CoreReportingSettingsAuditRecord
        from .cortana_briefing_audit_record import CortanaBriefingAuditRecord
        from .cps_common_policy_audit_record import CpsCommonPolicyAuditRecord
        from .cps_policy_config_audit_record import CpsPolicyConfigAuditRecord
        from .crm_base_audit_record import CrmBaseAuditRecord
        from .crm_entity_operation_audit_record import CrmEntityOperationAuditRecord
        from .customer_key_service_encryption_audit_record import CustomerKeyServiceEncryptionAuditRecord
        from .data_center_security_base_audit_record import DataCenterSecurityBaseAuditRecord
        from .data_center_security_cmdlet_audit_record import DataCenterSecurityCmdletAuditRecord
        from .data_governance_audit_record import DataGovernanceAuditRecord
        from .data_insights_rest_api_audit_record import DataInsightsRestApiAuditRecord
        from .data_lake_export_operation_audit_record import DataLakeExportOperationAuditRecord
        from .data_share_operation_audit_record import DataShareOperationAuditRecord
        from .default_audit_data import DefaultAuditData
        from .defender_security_alert_base_record import DefenderSecurityAlertBaseRecord
        from .delete_certificate_record import DeleteCertificateRecord
        from .disable_consent_record import DisableConsentRecord
        from .discovery_audit_record import DiscoveryAuditRecord
        from .dlp_endpoint_audit_record import DlpEndpointAuditRecord
        from .dlp_sensitive_information_type_cmdlet_record import DlpSensitiveInformationTypeCmdletRecord
        from .dlp_sensitive_information_type_rule_package_cmdlet_record import DlpSensitiveInformationTypeRulePackageCmdletRecord
        from .download_certificate_record import DownloadCertificateRecord
        from .dynamics365_business_central_audit_record import Dynamics365BusinessCentralAuditRecord
        from .enable_consent_record import EnableConsentRecord
        from .epic_s_m_s_link_record import EpicSMSLinkRecord
        from .epic_s_m_s_settings_update_record import EpicSMSSettingsUpdateRecord
        from .epic_s_m_s_unlink_record import EpicSMSUnlinkRecord
        from .exchange_admin_audit_record import ExchangeAdminAuditRecord
        from .exchange_aggregated_mailbox_audit_record import ExchangeAggregatedMailboxAuditRecord
        from .exchange_aggregated_operation_record import ExchangeAggregatedOperationRecord
        from .exchange_mailbox_audit_base_record import ExchangeMailboxAuditBaseRecord
        from .exchange_mailbox_audit_group_record import ExchangeMailboxAuditGroupRecord
        from .exchange_mailbox_audit_record import ExchangeMailboxAuditRecord
        from .fhir_base_url_add_record import FhirBaseUrlAddRecord
        from .fhir_base_url_approve_record import FhirBaseUrlApproveRecord
        from .fhir_base_url_delete_record import FhirBaseUrlDeleteRecord
        from .fhir_base_url_update_record import FhirBaseUrlUpdateRecord
        from .healthcare_signal_record import HealthcareSignalRecord
        from .hosted_rpa_audit_record import HostedRpaAuditRecord
        from .hr_signal_audit_record import HrSignalAuditRecord
        from .hygiene_event_record import HygieneEventRecord
        from .information_barrier_policy_application_audit_record import InformationBarrierPolicyApplicationAuditRecord
        from .information_worker_protection_audit_record import InformationWorkerProtectionAuditRecord
        from .insider_risk_scoped_users_record import InsiderRiskScopedUsersRecord
        from .insider_risk_scoped_user_insights_record import InsiderRiskScopedUserInsightsRecord
        from .irm_security_alert_record import IrmSecurityAlertRecord
        from .irm_user_defined_detection_record import IrmUserDefinedDetectionRecord
        from .kaizala_audit_record import KaizalaAuditRecord
        from .label_analytics_aggregate_audit_record import LabelAnalyticsAggregateAuditRecord
        from .label_content_explorer_audit_record import LabelContentExplorerAuditRecord
        from .large_content_metadata_audit_record import LargeContentMetadataAuditRecord
        from .m365_compliance_connector_audit_record import M365ComplianceConnectorAuditRecord
        from .m365_d_a_a_d_audit_record import M365DAADAuditRecord
        from .mail_submission_data import MailSubmissionData
        from .managed_services_audit_record import ManagedServicesAuditRecord
        from .managed_tenants_audit_record import ManagedTenantsAuditRecord
        from .mapg_alerts_audit_record import MapgAlertsAuditRecord
        from .mapg_onboard_audit_record import MapgOnboardAuditRecord
        from .mapg_policy_audit_record import MapgPolicyAuditRecord
        from .mcas_alerts_audit_record import McasAlertsAuditRecord
        from .mdatp_audit_record import MdatpAuditRecord
        from .mda_data_security_signal_record import MdaDataSecuritySignalRecord
        from .mdc_events_record import MdcEventsRecord
        from .mdi_audit_record import MdiAuditRecord
        from .mesh_worlds_audit_record import MeshWorldsAuditRecord
        from .microsoft365_backup_backup_item_audit_record import Microsoft365BackupBackupItemAuditRecord
        from .microsoft365_backup_backup_policy_audit_record import Microsoft365BackupBackupPolicyAuditRecord
        from .microsoft365_backup_restore_item_audit_record import Microsoft365BackupRestoreItemAuditRecord
        from .microsoft365_backup_restore_task_audit_record import Microsoft365BackupRestoreTaskAuditRecord
        from .microsoft_defender_experts_base_audit_record import MicrosoftDefenderExpertsBaseAuditRecord
        from .microsoft_defender_experts_x_d_r_audit_record import MicrosoftDefenderExpertsXDRAuditRecord
        from .microsoft_flow_audit_record import MicrosoftFlowAuditRecord
        from .microsoft_forms_audit_record import MicrosoftFormsAuditRecord
        from .microsoft_graph_data_connect_consent import MicrosoftGraphDataConnectConsent
        from .microsoft_graph_data_connect_operation import MicrosoftGraphDataConnectOperation
        from .microsoft_purview_data_map_operation_record import MicrosoftPurviewDataMapOperationRecord
        from .microsoft_purview_metadata_policy_operation_record import MicrosoftPurviewMetadataPolicyOperationRecord
        from .microsoft_purview_policy_operation_record import MicrosoftPurviewPolicyOperationRecord
        from .microsoft_purview_privacy_audit_event import MicrosoftPurviewPrivacyAuditEvent
        from .microsoft_stream_audit_record import MicrosoftStreamAuditRecord
        from .microsoft_teams_admin_audit_record import MicrosoftTeamsAdminAuditRecord
        from .microsoft_teams_analytics_audit_record import MicrosoftTeamsAnalyticsAuditRecord
        from .microsoft_teams_audit_record import MicrosoftTeamsAuditRecord
        from .microsoft_teams_device_audit_record import MicrosoftTeamsDeviceAuditRecord
        from .microsoft_teams_retention_label_action_audit_record import MicrosoftTeamsRetentionLabelActionAuditRecord
        from .microsoft_teams_sensitivity_label_action_audit_record import MicrosoftTeamsSensitivityLabelActionAuditRecord
        from .microsoft_teams_shifts_audit_record import MicrosoftTeamsShiftsAuditRecord
        from .mip_auto_label_exchange_item_audit_record import MipAutoLabelExchangeItemAuditRecord
        from .mip_auto_label_item_audit_record import MipAutoLabelItemAuditRecord
        from .mip_auto_label_policy_audit_record import MipAutoLabelPolicyAuditRecord
        from .mip_auto_label_progress_feedback_audit_record import MipAutoLabelProgressFeedbackAuditRecord
        from .mip_auto_label_share_point_item_audit_record import MipAutoLabelSharePointItemAuditRecord
        from .mip_auto_label_share_point_policy_location_audit_record import MipAutoLabelSharePointPolicyLocationAuditRecord
        from .mip_auto_label_simulation_share_point_completion_record import MipAutoLabelSimulationSharePointCompletionRecord
        from .mip_auto_label_simulation_share_point_progress_record import MipAutoLabelSimulationSharePointProgressRecord
        from .mip_auto_label_simulation_statistics_record import MipAutoLabelSimulationStatisticsRecord
        from .mip_auto_label_simulation_status_record import MipAutoLabelSimulationStatusRecord
        from .mip_exact_data_match_audit_record import MipExactDataMatchAuditRecord
        from .mip_label_analytics_audit_record import MipLabelAnalyticsAuditRecord
        from .mip_label_audit_record import MipLabelAuditRecord
        from .msde_general_settings_audit_record import MsdeGeneralSettingsAuditRecord
        from .msde_indicators_settings_audit_record import MsdeIndicatorsSettingsAuditRecord
        from .msde_response_actions_audit_record import MsdeResponseActionsAuditRecord
        from .msde_roles_settings_audit_record import MsdeRolesSettingsAuditRecord
        from .mstic_nation_state_notification_record import MsticNationStateNotificationRecord
        from .multi_stage_disposition_audit_record import MultiStageDispositionAuditRecord
        from .my_analytics_settings_audit_record import MyAnalyticsSettingsAuditRecord
        from .m_s365_d_custom_detection_audit_record import MS365DCustomDetectionAuditRecord
        from .m_s365_d_incident_audit_record import MS365DIncidentAuditRecord
        from .m_s365_d_suppression_rule_audit_record import MS365DSuppressionRuleAuditRecord
        from .office_native_audit_record import OfficeNativeAuditRecord
        from .ome_portal_audit_record import OmePortalAuditRecord
        from .one_drive_audit_record import OneDriveAuditRecord
        from .on_premises_file_share_scanner_dlp_audit_record import OnPremisesFileShareScannerDlpAuditRecord
        from .on_premises_scanner_dlp_audit_record import OnPremisesScannerDlpAuditRecord
        from .on_premises_share_point_scanner_dlp_audit_record import OnPremisesSharePointScannerDlpAuditRecord
        from .owa_get_access_token_for_resource_audit_record import OwaGetAccessTokenForResourceAuditRecord
        from .people_admin_settings_audit_record import PeopleAdminSettingsAuditRecord
        from .physical_badging_signal_audit_record import PhysicalBadgingSignalAuditRecord
        from .planner_copy_plan_audit_record import PlannerCopyPlanAuditRecord
        from .planner_plan_audit_record import PlannerPlanAuditRecord
        from .planner_plan_list_audit_record import PlannerPlanListAuditRecord
        from .planner_roster_audit_record import PlannerRosterAuditRecord
        from .planner_roster_sensitivity_label_audit_record import PlannerRosterSensitivityLabelAuditRecord
        from .planner_task_audit_record import PlannerTaskAuditRecord
        from .planner_task_list_audit_record import PlannerTaskListAuditRecord
        from .planner_tenant_settings_audit_record import PlannerTenantSettingsAuditRecord
        from .power_apps_audit_app_record import PowerAppsAuditAppRecord
        from .power_apps_audit_plan_record import PowerAppsAuditPlanRecord
        from .power_apps_audit_resource_record import PowerAppsAuditResourceRecord
        from .power_bi_audit_record import PowerBiAuditRecord
        from .power_bi_dlp_audit_record import PowerBiDlpAuditRecord
        from .power_pages_site_audit_record import PowerPagesSiteAuditRecord
        from .power_platform_administrator_activity_record import PowerPlatformAdministratorActivityRecord
        from .power_platform_admin_dlp_audit_record import PowerPlatformAdminDlpAuditRecord
        from .power_platform_admin_environment_audit_record import PowerPlatformAdminEnvironmentAuditRecord
        from .power_platform_lockbox_resource_access_request_audit_record import PowerPlatformLockboxResourceAccessRequestAuditRecord
        from .power_platform_lockbox_resource_command_audit_record import PowerPlatformLockboxResourceCommandAuditRecord
        from .power_platform_service_activity_audit_record import PowerPlatformServiceActivityAuditRecord
        from .privacy_data_match_audit_record import PrivacyDataMatchAuditRecord
        from .privacy_data_minimization_record import PrivacyDataMinimizationRecord
        from .privacy_digest_email_record import PrivacyDigestEmailRecord
        from .privacy_open_access_audit_record import PrivacyOpenAccessAuditRecord
        from .privacy_portal_audit_record import PrivacyPortalAuditRecord
        from .privacy_remediation_action_record import PrivacyRemediationActionRecord
        from .privacy_remediation_record import PrivacyRemediationRecord
        from .privacy_tenant_audit_history_record import PrivacyTenantAuditHistoryRecord
        from .project_audit_record import ProjectAuditRecord
        from .project_for_the_web_assigned_to_me_settings_audit_record import ProjectForTheWebAssignedToMeSettingsAuditRecord
        from .project_for_the_web_project_audit_record import ProjectForTheWebProjectAuditRecord
        from .project_for_the_web_project_settings_audit_record import ProjectForTheWebProjectSettingsAuditRecord
        from .project_for_the_web_roadmap_audit_record import ProjectForTheWebRoadmapAuditRecord
        from .project_for_the_web_roadmap_item_audit_record import ProjectForTheWebRoadmapItemAuditRecord
        from .project_for_the_web_roadmap_settings_audit_record import ProjectForTheWebRoadmapSettingsAuditRecord
        from .project_for_the_web_task_audit_record import ProjectForTheWebTaskAuditRecord
        from .public_folder_audit_record import PublicFolderAuditRecord
        from .purview_insider_risk_alerts_record import PurviewInsiderRiskAlertsRecord
        from .purview_insider_risk_cases_record import PurviewInsiderRiskCasesRecord
        from .quarantine_audit_record import QuarantineAuditRecord
        from .records_management_audit_record import RecordsManagementAuditRecord
        from .retention_policy_audit_record import RetentionPolicyAuditRecord
        from .score_evidence import ScoreEvidence
        from .score_platform_generic_audit_record import ScorePlatformGenericAuditRecord
        from .script_run_audit_record import ScriptRunAuditRecord
        from .search_audit_record import SearchAuditRecord
        from .security_compliance_alert_record import SecurityComplianceAlertRecord
        from .security_compliance_center_e_o_p_cmdlet_audit_record import SecurityComplianceCenterEOPCmdletAuditRecord
        from .security_compliance_insights_audit_record import SecurityComplianceInsightsAuditRecord
        from .security_compliance_r_b_a_c_audit_record import SecurityComplianceRBACAuditRecord
        from .security_compliance_user_change_audit_record import SecurityComplianceUserChangeAuditRecord
        from .share_point_app_permission_operation_audit_record import SharePointAppPermissionOperationAuditRecord
        from .share_point_audit_record import SharePointAuditRecord
        from .share_point_comment_operation_audit_record import SharePointCommentOperationAuditRecord
        from .share_point_content_type_operation_audit_record import SharePointContentTypeOperationAuditRecord
        from .share_point_e_signature_audit_record import SharePointESignatureAuditRecord
        from .share_point_field_operation_audit_record import SharePointFieldOperationAuditRecord
        from .share_point_file_operation_audit_record import SharePointFileOperationAuditRecord
        from .share_point_list_operation_audit_record import SharePointListOperationAuditRecord
        from .share_point_sharing_operation_audit_record import SharePointSharingOperationAuditRecord
        from .skype_for_business_base_audit_record import SkypeForBusinessBaseAuditRecord
        from .skype_for_business_cmdlets_audit_record import SkypeForBusinessCmdletsAuditRecord
        from .skype_for_business_p_s_t_n_usage_audit_record import SkypeForBusinessPSTNUsageAuditRecord
        from .skype_for_business_users_blocked_audit_record import SkypeForBusinessUsersBlockedAuditRecord
        from .sms_create_phone_number_record import SmsCreatePhoneNumberRecord
        from .sms_delete_phone_number_record import SmsDeletePhoneNumberRecord
        from .supervisory_review_day_x_insights_audit_record import SupervisoryReviewDayXInsightsAuditRecord
        from .synthetic_probe_audit_record import SyntheticProbeAuditRecord
        from .teams_easy_approvals_audit_record import TeamsEasyApprovalsAuditRecord
        from .teams_healthcare_audit_record import TeamsHealthcareAuditRecord
        from .teams_updates_audit_record import TeamsUpdatesAuditRecord
        from .tenant_allow_block_list_audit_record import TenantAllowBlockListAuditRecord
        from .threat_finder_audit_record import ThreatFinderAuditRecord
        from .threat_intelligence_atp_content_data import ThreatIntelligenceAtpContentData
        from .threat_intelligence_mail_data import ThreatIntelligenceMailData
        from .threat_intelligence_url_click_data import ThreatIntelligenceUrlClickData
        from .todo_audit_record import TodoAuditRecord
        from .uam_operation_audit_record import UamOperationAuditRecord
        from .unified_group_audit_record import UnifiedGroupAuditRecord
        from .unified_simulation_matched_item_audit_record import UnifiedSimulationMatchedItemAuditRecord
        from .unified_simulation_summary_audit_record import UnifiedSimulationSummaryAuditRecord
        from .upload_certificate_record import UploadCertificateRecord
        from .urbac_assignment_audit_record import UrbacAssignmentAuditRecord
        from .urbac_enable_state_audit_record import UrbacEnableStateAuditRecord
        from .urbac_role_audit_record import UrbacRoleAuditRecord
        from .user_training_audit_record import UserTrainingAuditRecord
        from .vfam_base_policy_audit_record import VfamBasePolicyAuditRecord
        from .vfam_create_policy_audit_record import VfamCreatePolicyAuditRecord
        from .vfam_delete_policy_audit_record import VfamDeletePolicyAuditRecord
        from .vfam_update_policy_audit_record import VfamUpdatePolicyAuditRecord
        from .viva_goals_audit_record import VivaGoalsAuditRecord
        from .viva_learning_admin_audit_record import VivaLearningAdminAuditRecord
        from .viva_learning_audit_record import VivaLearningAuditRecord
        from .viva_pulse_admin_audit_record import VivaPulseAdminAuditRecord
        from .viva_pulse_organizer_audit_record import VivaPulseOrganizerAuditRecord
        from .viva_pulse_report_audit_record import VivaPulseReportAuditRecord
        from .viva_pulse_response_audit_record import VivaPulseResponseAuditRecord
        from .wdatp_alerts_audit_record import WdatpAlertsAuditRecord
        from .windows365_customer_lockbox_audit_record import Windows365CustomerLockboxAuditRecord
        from .workplace_analytics_audit_record import WorkplaceAnalyticsAuditRecord
        from .yammer_audit_record import YammerAuditRecord

        fields: dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

