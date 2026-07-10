from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .a365_ai_execute_tool import A365AiExecuteTool
    from .a365_ai_inference_call import A365AiInferenceCall
    from .a365_ai_invoke_agent import A365AiInvokeAgent
    from .a365_ai_run_summary import A365AiRunSummary
    from .a365_span_outputs import A365SpanOutputs
    from .aad_risk_detection_audit_record import AadRiskDetectionAuditRecord
    from .aed_audit_record import AedAuditRecord
    from .agent_admin_activity_record import AgentAdminActivityRecord
    from .agent_setting_admin_activity import AgentSettingAdminActivity
    from .aip_discover import AipDiscover
    from .aip_file_deleted import AipFileDeleted
    from .aip_heart_beat import AipHeartBeat
    from .aip_protection_action_log_request import AipProtectionActionLogRequest
    from .aip_scanner_discover_event import AipScannerDiscoverEvent
    from .aip_sensitivity_label_action_log_request import AipSensitivityLabelActionLogRequest
    from .air_admin_action_investigation_data import AirAdminActionInvestigationData
    from .air_investigation_data import AirInvestigationData
    from .air_manual_investigation_data import AirManualInvestigationData
    from .ai_app_interaction_audit_record import AiAppInteractionAuditRecord
    from .ai_execute_tool_audit_record import AiExecuteToolAuditRecord
    from .ai_interactions_change_notification_audit_record import AiInteractionsChangeNotificationAuditRecord
    from .ai_interactions_export_audit_record import AiInteractionsExportAuditRecord
    from .ai_interactions_subscription_audit_record import AiInteractionsSubscriptionAuditRecord
    from .ai_invoke_agent_audit_record import AiInvokeAgentAuditRecord
    from .alert_submission_audit_record import AlertSubmissionAuditRecord
    from .alert_submission_result_detail_audit_record import AlertSubmissionResultDetailAuditRecord
    from .attack_sim_admin_audit_record import AttackSimAdminAuditRecord
    from .attack_sim_audit_record import AttackSimAuditRecord
    from .audit_config_audit_record import AuditConfigAuditRecord
    from .audit_record_type_dictionary import AuditRecordTypeDictionary
    from .audit_search_audit_record import AuditSearchAuditRecord
    from .azfw_application_rule_aggregation_event_record import AzfwApplicationRuleAggregationEventRecord
    from .azfw_dns_query_event_record import AzfwDnsQueryEventRecord
    from .azfw_network_rule_event_record import AzfwNetworkRuleEventRecord
    from .azure_active_directory_account_logon_audit_record import AzureActiveDirectoryAccountLogonAuditRecord
    from .azure_active_directory_audit_record import AzureActiveDirectoryAuditRecord
    from .azure_active_directory_sts_logon_audit_record import AzureActiveDirectoryStsLogonAuditRecord
    from .azure_a_i_search_audit_record import AzureAISearchAuditRecord
    from .a_i_span_outputs_audit_record import AISpanOutputsAuditRecord
    from .campaign_audit_record import CampaignAuditRecord
    from .ccrai_policy_violation_record import CcraiPolicyViolationRecord
    from .cdpdlmai_interaction_insights_record import CdpdlmaiInteractionInsightsRecord
    from .cdp_classifier_health_record import CdpClassifierHealthRecord
    from .cdp_cold_crawl_status_record import CdpColdCrawlStatusRecord
    from .cdp_consumption_resource_record import CdpConsumptionResourceRecord
    from .cdp_content_explorer_aggregate_record import CdpContentExplorerAggregateRecord
    from .cdp_dlp_sensitive_endpoint_audit_record import CdpDlpSensitiveEndpointAuditRecord
    from .cdp_log_record import CdpLogRecord
    from .cdp_ocr_billing_record import CdpOcrBillingRecord
    from .cdp_resource_scope_change_event_record import CdpResourceScopeChangeEventRecord
    from .cloud_update_device_config_audit_record import CloudUpdateDeviceConfigAuditRecord
    from .cloud_update_profile_config_audit_record import CloudUpdateProfileConfigAuditRecord
    from .cloud_update_tenant_config_audit_record import CloudUpdateTenantConfigAuditRecord
    from .compliance_connector_audit_record import ComplianceConnectorAuditRecord
    from .compliance_d_l_m_exchange_audit_record import ComplianceDLMExchangeAuditRecord
    from .compliance_d_l_m_share_point_audit_record import ComplianceDLMSharePointAuditRecord
    from .compliance_d_l_p_applications_audit_record import ComplianceDLPApplicationsAuditRecord
    from .compliance_d_l_p_applications_classification_audit_record import ComplianceDLPApplicationsClassificationAuditRecord
    from .compliance_d_l_p_endpoint_audit_record import ComplianceDLPEndpointAuditRecord
    from .compliance_d_l_p_endpoint_discovery_audit_record import ComplianceDLPEndpointDiscoveryAuditRecord
    from .compliance_d_l_p_enforcement_audit_record import ComplianceDLPEnforcementAuditRecord
    from .compliance_d_l_p_exchange_audit_record import ComplianceDLPExchangeAuditRecord
    from .compliance_d_l_p_exchange_classification_audit_record import ComplianceDLPExchangeClassificationAuditRecord
    from .compliance_d_l_p_exchange_classification_cdp_record import ComplianceDLPExchangeClassificationCdpRecord
    from .compliance_d_l_p_exchange_discovery_audit_record import ComplianceDLPExchangeDiscoveryAuditRecord
    from .compliance_d_l_p_share_point_audit_record import ComplianceDLPSharePointAuditRecord
    from .compliance_d_l_p_share_point_classification_audit_record import ComplianceDLPSharePointClassificationAuditRecord
    from .compliance_d_l_p_share_point_classification_cdp_record import ComplianceDLPSharePointClassificationCdpRecord
    from .compliance_d_l_p_share_point_classification_extended_audit_record import ComplianceDLPSharePointClassificationExtendedAuditRecord
    from .compliance_exchange_ocr_audit_record import ComplianceExchangeOcrAuditRecord
    from .compliance_manager_action_record import ComplianceManagerActionRecord
    from .compliance_policy_grading_share_point_audit_record import CompliancePolicyGradingSharePointAuditRecord
    from .compliance_settings_change_audit_record import ComplianceSettingsChangeAuditRecord
    from .compliance_sit_grading_share_point_audit_record import ComplianceSitGradingSharePointAuditRecord
    from .compliance_supervision_exchange_audit_record import ComplianceSupervisionExchangeAuditRecord
    from .connected_a_i_app_interaction_audit_record import ConnectedAIAppInteractionAuditRecord
    from .consumption_resource_audit_record import ConsumptionResourceAuditRecord
    from .content_store_metadata_record import ContentStoreMetadataRecord
    from .copilot_agent_management_audit_record import CopilotAgentManagementAuditRecord
    from .copilot_for_security_logging_audit_record import CopilotForSecurityLoggingAuditRecord
    from .copilot_for_security_trigger_audit_record import CopilotForSecurityTriggerAuditRecord
    from .copilot_interaction_audit_record import CopilotInteractionAuditRecord
    from .copilot_plugin_setting_audit_record import CopilotPluginSettingAuditRecord
    from .copilot_prompt_book_setting_audit_record import CopilotPromptBookSettingAuditRecord
    from .copilot_session_sharing_audit_record import CopilotSessionSharingAuditRecord
    from .copilot_setting_audit_record import CopilotSettingAuditRecord
    from .copilot_workspace_setting_audit_record import CopilotWorkspaceSettingAuditRecord
    from .core_reporting_settings_audit_record import CoreReportingSettingsAuditRecord
    from .cortana_briefing_audit_record import CortanaBriefingAuditRecord
    from .critical_asset_management_classification_record import CriticalAssetManagementClassificationRecord
    from .crm_entity_operation_audit_record import CrmEntityOperationAuditRecord
    from .cross_tenant_access_policy_audit_record import CrossTenantAccessPolicyAuditRecord
    from .customer_key_service_encryption_audit_record import CustomerKeyServiceEncryptionAuditRecord
    from .data_center_security_cmdlet_audit_record import DataCenterSecurityCmdletAuditRecord
    from .data_governance_audit_record import DataGovernanceAuditRecord
    from .data_insights_rest_api_audit_record import DataInsightsRestApiAuditRecord
    from .data_lake_export_operation_audit_record import DataLakeExportOperationAuditRecord
    from .data_security_investigation_audit_record import DataSecurityInvestigationAuditRecord
    from .data_share_operation_audit_record import DataShareOperationAuditRecord
    from .default_audit_data import DefaultAuditData
    from .defender_case_management_audit_record import DefenderCaseManagementAuditRecord
    from .defender_preview_features_record import DefenderPreviewFeaturesRecord
    from .defender_security_for_a_i_configuration_audit_record import DefenderSecurityForAIConfigurationAuditRecord
    from .deploy_feature_activity_record import DeployFeatureActivityRecord
    from .device_discovery_settings_authenticated_scans_record import DeviceDiscoverySettingsAuthenticatedScansRecord
    from .device_discovery_settings_exclusion_record import DeviceDiscoverySettingsExclusionRecord
    from .device_discovery_settings_record import DeviceDiscoverySettingsRecord
    from .discovery_audit_record import DiscoveryAuditRecord
    from .dlp_endpoint_audit_record import DlpEndpointAuditRecord
    from .dlp_import_result_audit_record import DlpImportResultAuditRecord
    from .dlp_sensitive_information_type_rule_package_cmdlet_record import DlpSensitiveInformationTypeRulePackageCmdletRecord
    from .dragon_copilot_access_record import DragonCopilotAccessRecord
    from .dragon_copilot_admin_record import DragonCopilotAdminRecord
    from .dragon_copilot_clinical_data_record import DragonCopilotClinicalDataRecord
    from .dragon_copilot_session_record import DragonCopilotSessionRecord
    from .dynamics365_business_central_audit_record import Dynamics365BusinessCentralAuditRecord
    from .ehr_connector_audit_base_record import EhrConnectorAuditBaseRecord
    from .eop_submission_feed_entity_audit_record import EopSubmissionFeedEntityAuditRecord
    from .exchange_admin_audit_record import ExchangeAdminAuditRecord
    from .exchange_aggregated_mailbox_audit_record import ExchangeAggregatedMailboxAuditRecord
    from .exchange_aggregated_operation_record import ExchangeAggregatedOperationRecord
    from .exchange_mailbox_audit_group_record import ExchangeMailboxAuditGroupRecord
    from .exchange_mailbox_audit_record import ExchangeMailboxAuditRecord
    from .fabric_audit_record import FabricAuditRecord
    from .fabric_policy_record import FabricPolicyRecord
    from .healthcare_signal_record import HealthcareSignalRecord
    from .hosted_rpa_audit_record import HostedRpaAuditRecord
    from .hr_signal_audit_record import HrSignalAuditRecord
    from .hygiene_event_record import HygieneEventRecord
    from .information_barrier_policy_application_audit_record import InformationBarrierPolicyApplicationAuditRecord
    from .information_worker_protection_audit_record import InformationWorkerProtectionAuditRecord
    from .insider_risk_scoped_users_record import InsiderRiskScopedUsersRecord
    from .insider_risk_scoped_user_insights_record import InsiderRiskScopedUserInsightsRecord
    from .integrated_apps_app_admin_activity_audit_record import IntegratedAppsAppAdminActivityAuditRecord
    from .integrated_apps_app_settings_admin_activity_audit_record import IntegratedAppsAppSettingsAdminActivityAuditRecord
    from .irm_activity_audit_trail_record import IrmActivityAuditTrailRecord
    from .irm_user_defined_detection_record import IrmUserDefinedDetectionRecord
    from .kaizala_audit_record import KaizalaAuditRecord
    from .label_analytics_aggregate_audit_record import LabelAnalyticsAggregateAuditRecord
    from .label_content_explorer_audit_record import LabelContentExplorerAuditRecord
    from .large_content_metadata_audit_record import LargeContentMetadataAuditRecord
    from .m365daad_audit_record import M365daadAuditRecord
    from .m365odsp_asset_metadata_record import M365odspAssetMetadataRecord
    from .m365_compliance_connector_audit_record import M365ComplianceConnectorAuditRecord
    from .m365_search_sections_record import M365SearchSectionsRecord
    from .mail_submission_data import MailSubmissionData
    from .managed_services_audit_record import ManagedServicesAuditRecord
    from .managed_tenants_audit_record import ManagedTenantsAuditRecord
    from .mapg_alerts_audit_record import MapgAlertsAuditRecord
    from .mapg_onboard_audit_record import MapgOnboardAuditRecord
    from .mapg_policy_audit_record import MapgPolicyAuditRecord
    from .mapg_remediation_audit_record import MapgRemediationAuditRecord
    from .mcas_alerts_audit_record import McasAlertsAuditRecord
    from .mdatp_audit_record import MdatpAuditRecord
    from .mda_audit_record import MdaAuditRecord
    from .mda_data_security_signal_record import MdaDataSecuritySignalRecord
    from .mdc_events_record import MdcEventsRecord
    from .mdi_audit_record import MdiAuditRecord
    from .mesh_worlds_audit_record import MeshWorldsAuditRecord
    from .microsoft365_backup_backup_item_audit_record import Microsoft365BackupBackupItemAuditRecord
    from .microsoft365_backup_backup_policy_audit_record import Microsoft365BackupBackupPolicyAuditRecord
    from .microsoft365_backup_granular_browse_task_audit_record import Microsoft365BackupGranularBrowseTaskAuditRecord
    from .microsoft365_backup_restore_item_audit_record import Microsoft365BackupRestoreItemAuditRecord
    from .microsoft365_backup_restore_task_audit_record import Microsoft365BackupRestoreTaskAuditRecord
    from .microsoft365_copilot_scheduled_prompt_audit_record import Microsoft365CopilotScheduledPromptAuditRecord
    from .microsoft_defender_experts_x_d_r_audit_record import MicrosoftDefenderExpertsXDRAuditRecord
    from .microsoft_flow_audit_record import MicrosoftFlowAuditRecord
    from .microsoft_forms_audit_record import MicrosoftFormsAuditRecord
    from .microsoft_graph_data_connect_consent import MicrosoftGraphDataConnectConsent
    from .microsoft_graph_data_connect_operation import MicrosoftGraphDataConnectOperation
    from .microsoft_purview_data_catalog_operation_record import MicrosoftPurviewDataCatalogOperationRecord
    from .microsoft_purview_data_map_operation_record import MicrosoftPurviewDataMapOperationRecord
    from .microsoft_purview_metadata_policy_operation_record import MicrosoftPurviewMetadataPolicyOperationRecord
    from .microsoft_purview_policy_operation_record import MicrosoftPurviewPolicyOperationRecord
    from .microsoft_purview_privacy_audit_event import MicrosoftPurviewPrivacyAuditEvent
    from .microsoft_purview_unified_catalog_operation_record import MicrosoftPurviewUnifiedCatalogOperationRecord
    from .microsoft_stream_audit_record import MicrosoftStreamAuditRecord
    from .microsoft_teams_admin_audit_record import MicrosoftTeamsAdminAuditRecord
    from .microsoft_teams_analytics_audit_record import MicrosoftTeamsAnalyticsAuditRecord
    from .microsoft_teams_audit_record import MicrosoftTeamsAuditRecord
    from .microsoft_teams_device_audit_record import MicrosoftTeamsDeviceAuditRecord
    from .microsoft_teams_retention_label_action_audit_record import MicrosoftTeamsRetentionLabelActionAuditRecord
    from .microsoft_teams_sensitivity_label_action_audit_record import MicrosoftTeamsSensitivityLabelActionAuditRecord
    from .microsoft_teams_shifts_audit_record import MicrosoftTeamsShiftsAuditRecord
    from .microsoft_teams_user_concern_audit_record import MicrosoftTeamsUserConcernAuditRecord
    from .mip_auto_label_exchange_item_audit_record import MipAutoLabelExchangeItemAuditRecord
    from .mip_auto_label_progress_feedback_audit_record import MipAutoLabelProgressFeedbackAuditRecord
    from .mip_auto_label_share_point_item_audit_record import MipAutoLabelSharePointItemAuditRecord
    from .mip_auto_label_share_point_policy_location_audit_record import MipAutoLabelSharePointPolicyLocationAuditRecord
    from .mip_auto_label_simulation_share_point_completion_record import MipAutoLabelSimulationSharePointCompletionRecord
    from .mip_auto_label_simulation_share_point_progress_record import MipAutoLabelSimulationSharePointProgressRecord
    from .mip_auto_label_simulation_statistics_record import MipAutoLabelSimulationStatisticsRecord
    from .mip_exact_data_match_audit_record import MipExactDataMatchAuditRecord
    from .mip_label_analytics_audit_record import MipLabelAnalyticsAuditRecord
    from .mip_label_audit_record import MipLabelAuditRecord
    from .mos_agent_info_record import MosAgentInfoRecord
    from .mos_agent_info_record_v2 import MosAgentInfoRecordV2
    from .ms365d_custom_detection_audit_record import Ms365dCustomDetectionAuditRecord
    from .ms365d_incident_audit_record import Ms365dIncidentAuditRecord
    from .ms365d_suppression_rule_audit_record import Ms365dSuppressionRuleAuditRecord
    from .msde_custom_collection_audit_record import MsdeCustomCollectionAuditRecord
    from .msde_general_settings_audit_record import MsdeGeneralSettingsAuditRecord
    from .msde_indicators_settings_audit_record import MsdeIndicatorsSettingsAuditRecord
    from .msde_response_actions_audit_record import MsdeResponseActionsAuditRecord
    from .msde_roles_settings_audit_record import MsdeRolesSettingsAuditRecord
    from .msp_vector_search_content_metadata_audit_record import MspVectorSearchContentMetadataAuditRecord
    from .mstic_nation_state_notification_record import MsticNationStateNotificationRecord
    from .multi_stage_disposition_audit_record import MultiStageDispositionAuditRecord
    from .my_analytics_settings_audit_record import MyAnalyticsSettingsAuditRecord
    from .m_d_a_s_h_audit_record import MDASHAuditRecord
    from .noisy_alert_policy_audit_record import NoisyAlertPolicyAuditRecord
    from .office_native_audit_record import OfficeNativeAuditRecord
    from .ome_portal_audit_record import OmePortalAuditRecord
    from .one_drive_audit_record import OneDriveAuditRecord
    from .on_demand_share_point_classification_audit_record import OnDemandSharePointClassificationAuditRecord
    from .on_premises_file_share_scanner_d_l_p_audit_record import OnPremisesFileShareScannerDLPAuditRecord
    from .on_premises_share_point_scanner_d_l_p_audit_record import OnPremisesSharePointScannerDLPAuditRecord
    from .organizational_data_in_m365_audit_record import OrganizationalDataInM365AuditRecord
    from .outlook_copilot_automation_audit_record import OutlookCopilotAutomationAuditRecord
    from .owa_get_access_token_for_resource_audit_record import OwaGetAccessTokenForResourceAuditRecord
    from .p4ai_assessment_category_record import P4aiAssessmentCategoryRecord
    from .p4ai_assessment_fabric_scanner_record import P4aiAssessmentFabricScannerRecord
    from .p4ai_assessment_location_result_record import P4aiAssessmentLocationResultRecord
    from .p4ai_assessment_record import P4aiAssessmentRecord
    from .p4_a_i_risk_score_record import P4AIRiskScoreRecord
    from .people_admin_settings_audit_record import PeopleAdminSettingsAuditRecord
    from .physical_badging_signal_audit_record import PhysicalBadgingSignalAuditRecord
    from .places_directory_audit_record import PlacesDirectoryAuditRecord
    from .planner_chat_message_audit_record import PlannerChatMessageAuditRecord
    from .planner_chat_message_list_audit_record import PlannerChatMessageListAuditRecord
    from .planner_copy_plan_audit_record import PlannerCopyPlanAuditRecord
    from .planner_goal_audit_record import PlannerGoalAuditRecord
    from .planner_goal_list_audit_record import PlannerGoalListAuditRecord
    from .planner_plan_audit_record import PlannerPlanAuditRecord
    from .planner_plan_list_audit_record import PlannerPlanListAuditRecord
    from .planner_plan_sensitivity_label_audit_record import PlannerPlanSensitivityLabelAuditRecord
    from .planner_roster_audit_record import PlannerRosterAuditRecord
    from .planner_roster_sensitivity_label_audit_record import PlannerRosterSensitivityLabelAuditRecord
    from .planner_task_audit_record import PlannerTaskAuditRecord
    from .planner_task_list_audit_record import PlannerTaskListAuditRecord
    from .planner_tenant_settings_audit_record import PlannerTenantSettingsAuditRecord
    from .policy_config_change_audit_record import PolicyConfigChangeAuditRecord
    from .power_apps_audit_app_record import PowerAppsAuditAppRecord
    from .power_apps_audit_plan_record import PowerAppsAuditPlanRecord
    from .power_apps_audit_resource_record import PowerAppsAuditResourceRecord
    from .power_b_i_audit_record import PowerBIAuditRecord
    from .power_b_i_dlp_audit_record import PowerBIDlpAuditRecord
    from .power_pages_site_audit_record import PowerPagesSiteAuditRecord
    from .power_platform_administrator_activity_record import PowerPlatformAdministratorActivityRecord
    from .power_platform_admin_dlp_audit_record import PowerPlatformAdminDlpAuditRecord
    from .power_platform_admin_environment_audit_record import PowerPlatformAdminEnvironmentAuditRecord
    from .power_platform_lockbox_resource_access_request_audit_record import PowerPlatformLockboxResourceAccessRequestAuditRecord
    from .power_platform_lockbox_resource_command_audit_record import PowerPlatformLockboxResourceCommandAuditRecord
    from .power_platform_service_activity_audit_record import PowerPlatformServiceActivityAuditRecord
    from .power_platform_tenant_isolation_record import PowerPlatformTenantIsolationRecord
    from .privacy_data_match_audit_record import PrivacyDataMatchAuditRecord
    from .privacy_data_minimization_record import PrivacyDataMinimizationRecord
    from .privacy_digest_email_record import PrivacyDigestEmailRecord
    from .privacy_open_access_audit_record import PrivacyOpenAccessAuditRecord
    from .privacy_portal_audit_record import PrivacyPortalAuditRecord
    from .privacy_remediation_action_record import PrivacyRemediationActionRecord
    from .privacy_remediation_record import PrivacyRemediationRecord
    from .priva_privacy_assessment_operation_record import PrivaPrivacyAssessmentOperationRecord
    from .priva_privacy_consent_operation_record import PrivaPrivacyConsentOperationRecord
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
    from .purview_m_c_recommendation_record import PurviewMCRecommendationRecord
    from .purview_posture_agent_audit_record import PurviewPostureAgentAuditRecord
    from .quarantine_audit_record import QuarantineAuditRecord
    from .records_management_audit_record import RecordsManagementAuditRecord
    from .report_submission import ReportSubmission
    from .report_submission_result_detail import ReportSubmissionResultDetail
    from .restricted_mode_audit_record import RestrictedModeAuditRecord
    from .retention_policy_audit_record import RetentionPolicyAuditRecord
    from .rti_operations_agent_audit_record import RtiOperationsAgentAuditRecord
    from .sbp_configuration_event_record import SbpConfigurationEventRecord
    from .sbp_usage_event_record import SbpUsageEventRecord
    from .score_evidence import ScoreEvidence
    from .score_platform_generic_audit_record import ScorePlatformGenericAuditRecord
    from .script_run_audit_record import ScriptRunAuditRecord
    from .search_audit_record import SearchAuditRecord
    from .security_compliance_alert_record import SecurityComplianceAlertRecord
    from .security_compliance_center_e_o_p_cmdlet_audit_record import SecurityComplianceCenterEOPCmdletAuditRecord
    from .security_compliance_insights_audit_record import SecurityComplianceInsightsAuditRecord
    from .security_compliance_r_b_a_c_audit_record import SecurityComplianceRBACAuditRecord
    from .security_compliance_user_change_audit_record import SecurityComplianceUserChangeAuditRecord
    from .security_copilot_identity_management_audit_record import SecurityCopilotIdentityManagementAuditRecord
    from .security_development_lifecycle_a_i_log_audit_record import SecurityDevelopmentLifecycleAILogAuditRecord
    from .sensitive_info_remediation_agent_data_record import SensitiveInfoRemediationAgentDataRecord
    from .sensitivity_labeled_file_action_audit_record import SensitivityLabeledFileActionAuditRecord
    from .sensitivity_label_action_audit_record import SensitivityLabelActionAuditRecord
    from .sensitivity_label_policy_match_audit_record import SensitivityLabelPolicyMatchAuditRecord
    from .sentinel_a_i_tool_audit_record import SentinelAIToolAuditRecord
    from .sentinel_graph_audit_record import SentinelGraphAuditRecord
    from .sentinel_job_audit_record import SentinelJobAuditRecord
    from .sentinel_k_q_l_on_lake_audit_record import SentinelKQLOnLakeAuditRecord
    from .sentinel_lake_data_onboarding_audit_record import SentinelLakeDataOnboardingAuditRecord
    from .sentinel_lake_encryption_audit_record import SentinelLakeEncryptionAuditRecord
    from .sentinel_lake_onboarding_audit_record import SentinelLakeOnboardingAuditRecord
    from .sentinel_notebook_on_lake_audit_record import SentinelNotebookOnLakeAuditRecord
    from .sentinel_package_audit_record import SentinelPackageAuditRecord
    from .share_point_app_permission_operation_audit_record import SharePointAppPermissionOperationAuditRecord
    from .share_point_audit_record import SharePointAuditRecord
    from .share_point_comment_operation_audit_record import SharePointCommentOperationAuditRecord
    from .share_point_content_security_policy_audit_record import SharePointContentSecurityPolicyAuditRecord
    from .share_point_content_type_operation_audit_record import SharePointContentTypeOperationAuditRecord
    from .share_point_e_signature_audit_record import SharePointESignatureAuditRecord
    from .share_point_field_operation_audit_record import SharePointFieldOperationAuditRecord
    from .share_point_file_operation_audit_record import SharePointFileOperationAuditRecord
    from .share_point_list_item_operation_audit_record import SharePointListItemOperationAuditRecord
    from .share_point_list_operation_audit_record import SharePointListOperationAuditRecord
    from .share_point_sharing_operation_audit_record import SharePointSharingOperationAuditRecord
    from .skype_for_business_cmdlets_audit_record import SkypeForBusinessCmdletsAuditRecord
    from .skype_for_business_p_s_t_n_usage_audit_record import SkypeForBusinessPSTNUsageAuditRecord
    from .skype_for_business_users_blocked_audit_record import SkypeForBusinessUsersBlockedAuditRecord
    from .sonar_detonation_content_metadata import SonarDetonationContentMetadata
    from .sonar_detonation_entity_audit_record import SonarDetonationEntityAuditRecord
    from .sonar_file_detonation_entity_audit_record import SonarFileDetonationEntityAuditRecord
    from .sonar_submission_entity_audit_record import SonarSubmissionEntityAuditRecord
    from .sonar_url_detonation_entity_audit_record import SonarUrlDetonationEntityAuditRecord
    from .spark_core_custom_live_pool_record import SparkCoreCustomLivePoolRecord
    from .submission_entity_audit_record import SubmissionEntityAuditRecord
    from .supervisory_review_day_x_insights_audit_record import SupervisoryReviewDayXInsightsAuditRecord
    from .synthetic_probe_audit_record import SyntheticProbeAuditRecord
    from .teams_easy_approvals_audit_record import TeamsEasyApprovalsAuditRecord
    from .teams_eval_data_hub_admin_operation_audit_record import TeamsEvalDataHubAdminOperationAuditRecord
    from .teams_eval_data_hub_data_access_audit_record import TeamsEvalDataHubDataAccessAuditRecord
    from .teams_eval_data_hub_permission_change_audit_record import TeamsEvalDataHubPermissionChangeAuditRecord
    from .teams_healthcare_audit_record import TeamsHealthcareAuditRecord
    from .teams_updates_audit_record import TeamsUpdatesAuditRecord
    from .team_copilot_interaction_audit_record import TeamCopilotInteractionAuditRecord
    from .tenant_allow_block_list_audit_record import TenantAllowBlockListAuditRecord
    from .threat_finder_audit_record import ThreatFinderAuditRecord
    from .threat_intelligence_atp_content_data import ThreatIntelligenceAtpContentData
    from .threat_intelligence_export_audit_record import ThreatIntelligenceExportAuditRecord
    from .threat_intelligence_mail_data import ThreatIntelligenceMailData
    from .threat_intelligence_object_audit_record import ThreatIntelligenceObjectAuditRecord
    from .threat_intelligence_url_click_data import ThreatIntelligenceUrlClickData
    from .todo_audit_record import TodoAuditRecord
    from .trainable_classifier_audit_record import TrainableClassifierAuditRecord
    from .uam_operation_audit_record import UamOperationAuditRecord
    from .unified_group_audit_record import UnifiedGroupAuditRecord
    from .unified_simulation_matched_item_audit_record import UnifiedSimulationMatchedItemAuditRecord
    from .unified_simulation_summary_audit_record import UnifiedSimulationSummaryAuditRecord
    from .universal_print_management_audit_record import UniversalPrintManagementAuditRecord
    from .universal_print_print_job_audit_record import UniversalPrintPrintJobAuditRecord
    from .urbac_assignment_audit_record import UrbacAssignmentAuditRecord
    from .urbac_enable_state_audit_record import UrbacEnableStateAuditRecord
    from .urbac_role_audit_record import UrbacRoleAuditRecord
    from .user_training_audit_record import UserTrainingAuditRecord
    from .usx_workspace_onboarding_audit_record import UsxWorkspaceOnboardingAuditRecord
    from .vfam_create_policy_audit_record import VfamCreatePolicyAuditRecord
    from .vfam_delete_policy_audit_record import VfamDeletePolicyAuditRecord
    from .vfam_update_policy_audit_record import VfamUpdatePolicyAuditRecord
    from .viva_amplify_audit_record import VivaAmplifyAuditRecord
    from .viva_engage_events_audit_record import VivaEngageEventsAuditRecord
    from .viva_engage_network_association_audit_record import VivaEngageNetworkAssociationAuditRecord
    from .viva_engage_segment_audit_record import VivaEngageSegmentAuditRecord
    from .viva_glint_advanced_configuration_audit_record import VivaGlintAdvancedConfigurationAuditRecord
    from .viva_glint_agentic_campaign_audit_record import VivaGlintAgenticCampaignAuditRecord
    from .viva_glint_feedback_program_audit_record import VivaGlintFeedbackProgramAuditRecord
    from .viva_glint_organizational_data_audit_record import VivaGlintOrganizationalDataAuditRecord
    from .viva_glint_pulse_program_audit_record import VivaGlintPulseProgramAuditRecord
    from .viva_glint_pulse_program_respondent_rate_audit_record import VivaGlintPulseProgramRespondentRateAuditRecord
    from .viva_glint_question_audit_record import VivaGlintQuestionAuditRecord
    from .viva_glint_role_audit_record import VivaGlintRoleAuditRecord
    from .viva_glint_rubicon_audit_record import VivaGlintRubiconAuditRecord
    from .viva_glint_support_access_audit_record import VivaGlintSupportAccessAuditRecord
    from .viva_glint_system_audit_record import VivaGlintSystemAuditRecord
    from .viva_glint_user_audit_record import VivaGlintUserAuditRecord
    from .viva_glint_user_group_audit_record import VivaGlintUserGroupAuditRecord
    from .viva_goals_audit_record import VivaGoalsAuditRecord
    from .viva_learning_admin_audit_record import VivaLearningAdminAuditRecord
    from .viva_learning_audit_record import VivaLearningAuditRecord
    from .viva_pulse_admin_audit_record import VivaPulseAdminAuditRecord
    from .viva_pulse_organizer_audit_record import VivaPulseOrganizerAuditRecord
    from .viva_pulse_report_audit_record import VivaPulseReportAuditRecord
    from .viva_pulse_response_audit_record import VivaPulseResponseAuditRecord
    from .wdatp_alerts_audit_record import WdatpAlertsAuditRecord
    from .web_content_filtering_audit_record import WebContentFilteringAuditRecord
    from .windows365_customer_lockbox_audit_record import Windows365CustomerLockboxAuditRecord
    from .workplace_analytics_audit_record import WorkplaceAnalyticsAuditRecord
    from .yammer_audit_record import YammerAuditRecord
    from .yammer_user_hiding_audit_record import YammerUserHidingAuditRecord

@dataclass
class AuditData(AdditionalDataHolder, BackedModel, Parsable):
    """
    Abstract base type for audit event data.
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The dynamicProperties property
    dynamic_properties: Optional[AuditRecordTypeDictionary] = None
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
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.a365AiExecuteTool".casefold():
            from .a365_ai_execute_tool import A365AiExecuteTool

            return A365AiExecuteTool()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.a365AiInferenceCall".casefold():
            from .a365_ai_inference_call import A365AiInferenceCall

            return A365AiInferenceCall()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.a365AiInvokeAgent".casefold():
            from .a365_ai_invoke_agent import A365AiInvokeAgent

            return A365AiInvokeAgent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.a365AiRunSummary".casefold():
            from .a365_ai_run_summary import A365AiRunSummary

            return A365AiRunSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.a365SpanOutputs".casefold():
            from .a365_span_outputs import A365SpanOutputs

            return A365SpanOutputs()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.aadRiskDetectionAuditRecord".casefold():
            from .aad_risk_detection_audit_record import AadRiskDetectionAuditRecord

            return AadRiskDetectionAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.aedAuditRecord".casefold():
            from .aed_audit_record import AedAuditRecord

            return AedAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.agentAdminActivityRecord".casefold():
            from .agent_admin_activity_record import AgentAdminActivityRecord

            return AgentAdminActivityRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.agentSettingAdminActivity".casefold():
            from .agent_setting_admin_activity import AgentSettingAdminActivity

            return AgentSettingAdminActivity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.aiAppInteractionAuditRecord".casefold():
            from .ai_app_interaction_audit_record import AiAppInteractionAuditRecord

            return AiAppInteractionAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.aiExecuteToolAuditRecord".casefold():
            from .ai_execute_tool_audit_record import AiExecuteToolAuditRecord

            return AiExecuteToolAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.aiInteractionsChangeNotificationAuditRecord".casefold():
            from .ai_interactions_change_notification_audit_record import AiInteractionsChangeNotificationAuditRecord

            return AiInteractionsChangeNotificationAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.aiInteractionsExportAuditRecord".casefold():
            from .ai_interactions_export_audit_record import AiInteractionsExportAuditRecord

            return AiInteractionsExportAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.aiInteractionsSubscriptionAuditRecord".casefold():
            from .ai_interactions_subscription_audit_record import AiInteractionsSubscriptionAuditRecord

            return AiInteractionsSubscriptionAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.aiInvokeAgentAuditRecord".casefold():
            from .ai_invoke_agent_audit_record import AiInvokeAgentAuditRecord

            return AiInvokeAgentAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.aipDiscover".casefold():
            from .aip_discover import AipDiscover

            return AipDiscover()
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
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.aISpanOutputsAuditRecord".casefold():
            from .a_i_span_outputs_audit_record import AISpanOutputsAuditRecord

            return AISpanOutputsAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.alertSubmissionAuditRecord".casefold():
            from .alert_submission_audit_record import AlertSubmissionAuditRecord

            return AlertSubmissionAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.alertSubmissionResultDetailAuditRecord".casefold():
            from .alert_submission_result_detail_audit_record import AlertSubmissionResultDetailAuditRecord

            return AlertSubmissionResultDetailAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.attackSimAdminAuditRecord".casefold():
            from .attack_sim_admin_audit_record import AttackSimAdminAuditRecord

            return AttackSimAdminAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.attackSimAuditRecord".casefold():
            from .attack_sim_audit_record import AttackSimAuditRecord

            return AttackSimAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.auditConfigAuditRecord".casefold():
            from .audit_config_audit_record import AuditConfigAuditRecord

            return AuditConfigAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.auditSearchAuditRecord".casefold():
            from .audit_search_audit_record import AuditSearchAuditRecord

            return AuditSearchAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.azfwApplicationRuleAggregationEventRecord".casefold():
            from .azfw_application_rule_aggregation_event_record import AzfwApplicationRuleAggregationEventRecord

            return AzfwApplicationRuleAggregationEventRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.azfwDnsQueryEventRecord".casefold():
            from .azfw_dns_query_event_record import AzfwDnsQueryEventRecord

            return AzfwDnsQueryEventRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.azfwNetworkRuleEventRecord".casefold():
            from .azfw_network_rule_event_record import AzfwNetworkRuleEventRecord

            return AzfwNetworkRuleEventRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.azureActiveDirectoryAccountLogonAuditRecord".casefold():
            from .azure_active_directory_account_logon_audit_record import AzureActiveDirectoryAccountLogonAuditRecord

            return AzureActiveDirectoryAccountLogonAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.azureActiveDirectoryAuditRecord".casefold():
            from .azure_active_directory_audit_record import AzureActiveDirectoryAuditRecord

            return AzureActiveDirectoryAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.azureActiveDirectoryStsLogonAuditRecord".casefold():
            from .azure_active_directory_sts_logon_audit_record import AzureActiveDirectoryStsLogonAuditRecord

            return AzureActiveDirectoryStsLogonAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.azureAISearchAuditRecord".casefold():
            from .azure_a_i_search_audit_record import AzureAISearchAuditRecord

            return AzureAISearchAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.campaignAuditRecord".casefold():
            from .campaign_audit_record import CampaignAuditRecord

            return CampaignAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ccraiPolicyViolationRecord".casefold():
            from .ccrai_policy_violation_record import CcraiPolicyViolationRecord

            return CcraiPolicyViolationRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.cdpClassifierHealthRecord".casefold():
            from .cdp_classifier_health_record import CdpClassifierHealthRecord

            return CdpClassifierHealthRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.cdpColdCrawlStatusRecord".casefold():
            from .cdp_cold_crawl_status_record import CdpColdCrawlStatusRecord

            return CdpColdCrawlStatusRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.cdpConsumptionResourceRecord".casefold():
            from .cdp_consumption_resource_record import CdpConsumptionResourceRecord

            return CdpConsumptionResourceRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.cdpContentExplorerAggregateRecord".casefold():
            from .cdp_content_explorer_aggregate_record import CdpContentExplorerAggregateRecord

            return CdpContentExplorerAggregateRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.cdpdlmaiInteractionInsightsRecord".casefold():
            from .cdpdlmai_interaction_insights_record import CdpdlmaiInteractionInsightsRecord

            return CdpdlmaiInteractionInsightsRecord()
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
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.cloudUpdateDeviceConfigAuditRecord".casefold():
            from .cloud_update_device_config_audit_record import CloudUpdateDeviceConfigAuditRecord

            return CloudUpdateDeviceConfigAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.cloudUpdateProfileConfigAuditRecord".casefold():
            from .cloud_update_profile_config_audit_record import CloudUpdateProfileConfigAuditRecord

            return CloudUpdateProfileConfigAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.cloudUpdateTenantConfigAuditRecord".casefold():
            from .cloud_update_tenant_config_audit_record import CloudUpdateTenantConfigAuditRecord

            return CloudUpdateTenantConfigAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.complianceConnectorAuditRecord".casefold():
            from .compliance_connector_audit_record import ComplianceConnectorAuditRecord

            return ComplianceConnectorAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.complianceDLMExchangeAuditRecord".casefold():
            from .compliance_d_l_m_exchange_audit_record import ComplianceDLMExchangeAuditRecord

            return ComplianceDLMExchangeAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.complianceDLMSharePointAuditRecord".casefold():
            from .compliance_d_l_m_share_point_audit_record import ComplianceDLMSharePointAuditRecord

            return ComplianceDLMSharePointAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.complianceDLPApplicationsAuditRecord".casefold():
            from .compliance_d_l_p_applications_audit_record import ComplianceDLPApplicationsAuditRecord

            return ComplianceDLPApplicationsAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.complianceDLPApplicationsClassificationAuditRecord".casefold():
            from .compliance_d_l_p_applications_classification_audit_record import ComplianceDLPApplicationsClassificationAuditRecord

            return ComplianceDLPApplicationsClassificationAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.complianceDLPEndpointAuditRecord".casefold():
            from .compliance_d_l_p_endpoint_audit_record import ComplianceDLPEndpointAuditRecord

            return ComplianceDLPEndpointAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.complianceDLPEndpointDiscoveryAuditRecord".casefold():
            from .compliance_d_l_p_endpoint_discovery_audit_record import ComplianceDLPEndpointDiscoveryAuditRecord

            return ComplianceDLPEndpointDiscoveryAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.complianceDLPEnforcementAuditRecord".casefold():
            from .compliance_d_l_p_enforcement_audit_record import ComplianceDLPEnforcementAuditRecord

            return ComplianceDLPEnforcementAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.complianceDLPExchangeAuditRecord".casefold():
            from .compliance_d_l_p_exchange_audit_record import ComplianceDLPExchangeAuditRecord

            return ComplianceDLPExchangeAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.complianceDLPExchangeClassificationAuditRecord".casefold():
            from .compliance_d_l_p_exchange_classification_audit_record import ComplianceDLPExchangeClassificationAuditRecord

            return ComplianceDLPExchangeClassificationAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.complianceDLPExchangeClassificationCdpRecord".casefold():
            from .compliance_d_l_p_exchange_classification_cdp_record import ComplianceDLPExchangeClassificationCdpRecord

            return ComplianceDLPExchangeClassificationCdpRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.complianceDLPExchangeDiscoveryAuditRecord".casefold():
            from .compliance_d_l_p_exchange_discovery_audit_record import ComplianceDLPExchangeDiscoveryAuditRecord

            return ComplianceDLPExchangeDiscoveryAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.complianceDLPSharePointAuditRecord".casefold():
            from .compliance_d_l_p_share_point_audit_record import ComplianceDLPSharePointAuditRecord

            return ComplianceDLPSharePointAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.complianceDLPSharePointClassificationAuditRecord".casefold():
            from .compliance_d_l_p_share_point_classification_audit_record import ComplianceDLPSharePointClassificationAuditRecord

            return ComplianceDLPSharePointClassificationAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.complianceDLPSharePointClassificationCdpRecord".casefold():
            from .compliance_d_l_p_share_point_classification_cdp_record import ComplianceDLPSharePointClassificationCdpRecord

            return ComplianceDLPSharePointClassificationCdpRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.complianceDLPSharePointClassificationExtendedAuditRecord".casefold():
            from .compliance_d_l_p_share_point_classification_extended_audit_record import ComplianceDLPSharePointClassificationExtendedAuditRecord

            return ComplianceDLPSharePointClassificationExtendedAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.complianceExchangeOcrAuditRecord".casefold():
            from .compliance_exchange_ocr_audit_record import ComplianceExchangeOcrAuditRecord

            return ComplianceExchangeOcrAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.complianceManagerActionRecord".casefold():
            from .compliance_manager_action_record import ComplianceManagerActionRecord

            return ComplianceManagerActionRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.compliancePolicyGradingSharePointAuditRecord".casefold():
            from .compliance_policy_grading_share_point_audit_record import CompliancePolicyGradingSharePointAuditRecord

            return CompliancePolicyGradingSharePointAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.complianceSettingsChangeAuditRecord".casefold():
            from .compliance_settings_change_audit_record import ComplianceSettingsChangeAuditRecord

            return ComplianceSettingsChangeAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.complianceSitGradingSharePointAuditRecord".casefold():
            from .compliance_sit_grading_share_point_audit_record import ComplianceSitGradingSharePointAuditRecord

            return ComplianceSitGradingSharePointAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.complianceSupervisionExchangeAuditRecord".casefold():
            from .compliance_supervision_exchange_audit_record import ComplianceSupervisionExchangeAuditRecord

            return ComplianceSupervisionExchangeAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.connectedAIAppInteractionAuditRecord".casefold():
            from .connected_a_i_app_interaction_audit_record import ConnectedAIAppInteractionAuditRecord

            return ConnectedAIAppInteractionAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.consumptionResourceAuditRecord".casefold():
            from .consumption_resource_audit_record import ConsumptionResourceAuditRecord

            return ConsumptionResourceAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.contentStoreMetadataRecord".casefold():
            from .content_store_metadata_record import ContentStoreMetadataRecord

            return ContentStoreMetadataRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.copilotAgentManagementAuditRecord".casefold():
            from .copilot_agent_management_audit_record import CopilotAgentManagementAuditRecord

            return CopilotAgentManagementAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.copilotForSecurityLoggingAuditRecord".casefold():
            from .copilot_for_security_logging_audit_record import CopilotForSecurityLoggingAuditRecord

            return CopilotForSecurityLoggingAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.copilotForSecurityTriggerAuditRecord".casefold():
            from .copilot_for_security_trigger_audit_record import CopilotForSecurityTriggerAuditRecord

            return CopilotForSecurityTriggerAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.copilotInteractionAuditRecord".casefold():
            from .copilot_interaction_audit_record import CopilotInteractionAuditRecord

            return CopilotInteractionAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.copilotPluginSettingAuditRecord".casefold():
            from .copilot_plugin_setting_audit_record import CopilotPluginSettingAuditRecord

            return CopilotPluginSettingAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.copilotPromptBookSettingAuditRecord".casefold():
            from .copilot_prompt_book_setting_audit_record import CopilotPromptBookSettingAuditRecord

            return CopilotPromptBookSettingAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.copilotSessionSharingAuditRecord".casefold():
            from .copilot_session_sharing_audit_record import CopilotSessionSharingAuditRecord

            return CopilotSessionSharingAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.copilotSettingAuditRecord".casefold():
            from .copilot_setting_audit_record import CopilotSettingAuditRecord

            return CopilotSettingAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.copilotWorkspaceSettingAuditRecord".casefold():
            from .copilot_workspace_setting_audit_record import CopilotWorkspaceSettingAuditRecord

            return CopilotWorkspaceSettingAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.coreReportingSettingsAuditRecord".casefold():
            from .core_reporting_settings_audit_record import CoreReportingSettingsAuditRecord

            return CoreReportingSettingsAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.cortanaBriefingAuditRecord".casefold():
            from .cortana_briefing_audit_record import CortanaBriefingAuditRecord

            return CortanaBriefingAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.criticalAssetManagementClassificationRecord".casefold():
            from .critical_asset_management_classification_record import CriticalAssetManagementClassificationRecord

            return CriticalAssetManagementClassificationRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.crmEntityOperationAuditRecord".casefold():
            from .crm_entity_operation_audit_record import CrmEntityOperationAuditRecord

            return CrmEntityOperationAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.crossTenantAccessPolicyAuditRecord".casefold():
            from .cross_tenant_access_policy_audit_record import CrossTenantAccessPolicyAuditRecord

            return CrossTenantAccessPolicyAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.customerKeyServiceEncryptionAuditRecord".casefold():
            from .customer_key_service_encryption_audit_record import CustomerKeyServiceEncryptionAuditRecord

            return CustomerKeyServiceEncryptionAuditRecord()
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
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.dataSecurityInvestigationAuditRecord".casefold():
            from .data_security_investigation_audit_record import DataSecurityInvestigationAuditRecord

            return DataSecurityInvestigationAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.dataShareOperationAuditRecord".casefold():
            from .data_share_operation_audit_record import DataShareOperationAuditRecord

            return DataShareOperationAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.defaultAuditData".casefold():
            from .default_audit_data import DefaultAuditData

            return DefaultAuditData()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.defenderCaseManagementAuditRecord".casefold():
            from .defender_case_management_audit_record import DefenderCaseManagementAuditRecord

            return DefenderCaseManagementAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.defenderPreviewFeaturesRecord".casefold():
            from .defender_preview_features_record import DefenderPreviewFeaturesRecord

            return DefenderPreviewFeaturesRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.defenderSecurityForAIConfigurationAuditRecord".casefold():
            from .defender_security_for_a_i_configuration_audit_record import DefenderSecurityForAIConfigurationAuditRecord

            return DefenderSecurityForAIConfigurationAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.deployFeatureActivityRecord".casefold():
            from .deploy_feature_activity_record import DeployFeatureActivityRecord

            return DeployFeatureActivityRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.deviceDiscoverySettingsAuthenticatedScansRecord".casefold():
            from .device_discovery_settings_authenticated_scans_record import DeviceDiscoverySettingsAuthenticatedScansRecord

            return DeviceDiscoverySettingsAuthenticatedScansRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.deviceDiscoverySettingsExclusionRecord".casefold():
            from .device_discovery_settings_exclusion_record import DeviceDiscoverySettingsExclusionRecord

            return DeviceDiscoverySettingsExclusionRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.deviceDiscoverySettingsRecord".casefold():
            from .device_discovery_settings_record import DeviceDiscoverySettingsRecord

            return DeviceDiscoverySettingsRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.discoveryAuditRecord".casefold():
            from .discovery_audit_record import DiscoveryAuditRecord

            return DiscoveryAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.dlpEndpointAuditRecord".casefold():
            from .dlp_endpoint_audit_record import DlpEndpointAuditRecord

            return DlpEndpointAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.dlpImportResultAuditRecord".casefold():
            from .dlp_import_result_audit_record import DlpImportResultAuditRecord

            return DlpImportResultAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.dlpSensitiveInformationTypeRulePackageCmdletRecord".casefold():
            from .dlp_sensitive_information_type_rule_package_cmdlet_record import DlpSensitiveInformationTypeRulePackageCmdletRecord

            return DlpSensitiveInformationTypeRulePackageCmdletRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.dragonCopilotAccessRecord".casefold():
            from .dragon_copilot_access_record import DragonCopilotAccessRecord

            return DragonCopilotAccessRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.dragonCopilotAdminRecord".casefold():
            from .dragon_copilot_admin_record import DragonCopilotAdminRecord

            return DragonCopilotAdminRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.dragonCopilotClinicalDataRecord".casefold():
            from .dragon_copilot_clinical_data_record import DragonCopilotClinicalDataRecord

            return DragonCopilotClinicalDataRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.dragonCopilotSessionRecord".casefold():
            from .dragon_copilot_session_record import DragonCopilotSessionRecord

            return DragonCopilotSessionRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.dynamics365BusinessCentralAuditRecord".casefold():
            from .dynamics365_business_central_audit_record import Dynamics365BusinessCentralAuditRecord

            return Dynamics365BusinessCentralAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ehrConnectorAuditBaseRecord".casefold():
            from .ehr_connector_audit_base_record import EhrConnectorAuditBaseRecord

            return EhrConnectorAuditBaseRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.eopSubmissionFeedEntityAuditRecord".casefold():
            from .eop_submission_feed_entity_audit_record import EopSubmissionFeedEntityAuditRecord

            return EopSubmissionFeedEntityAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.exchangeAdminAuditRecord".casefold():
            from .exchange_admin_audit_record import ExchangeAdminAuditRecord

            return ExchangeAdminAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.exchangeAggregatedMailboxAuditRecord".casefold():
            from .exchange_aggregated_mailbox_audit_record import ExchangeAggregatedMailboxAuditRecord

            return ExchangeAggregatedMailboxAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.exchangeAggregatedOperationRecord".casefold():
            from .exchange_aggregated_operation_record import ExchangeAggregatedOperationRecord

            return ExchangeAggregatedOperationRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.exchangeMailboxAuditGroupRecord".casefold():
            from .exchange_mailbox_audit_group_record import ExchangeMailboxAuditGroupRecord

            return ExchangeMailboxAuditGroupRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.exchangeMailboxAuditRecord".casefold():
            from .exchange_mailbox_audit_record import ExchangeMailboxAuditRecord

            return ExchangeMailboxAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.fabricAuditRecord".casefold():
            from .fabric_audit_record import FabricAuditRecord

            return FabricAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.fabricPolicyRecord".casefold():
            from .fabric_policy_record import FabricPolicyRecord

            return FabricPolicyRecord()
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
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.integratedAppsAppAdminActivityAuditRecord".casefold():
            from .integrated_apps_app_admin_activity_audit_record import IntegratedAppsAppAdminActivityAuditRecord

            return IntegratedAppsAppAdminActivityAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.integratedAppsAppSettingsAdminActivityAuditRecord".casefold():
            from .integrated_apps_app_settings_admin_activity_audit_record import IntegratedAppsAppSettingsAdminActivityAuditRecord

            return IntegratedAppsAppSettingsAdminActivityAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.irmActivityAuditTrailRecord".casefold():
            from .irm_activity_audit_trail_record import IrmActivityAuditTrailRecord

            return IrmActivityAuditTrailRecord()
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
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.m365daadAuditRecord".casefold():
            from .m365daad_audit_record import M365daadAuditRecord

            return M365daadAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.m365odspAssetMetadataRecord".casefold():
            from .m365odsp_asset_metadata_record import M365odspAssetMetadataRecord

            return M365odspAssetMetadataRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.m365SearchSectionsRecord".casefold():
            from .m365_search_sections_record import M365SearchSectionsRecord

            return M365SearchSectionsRecord()
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
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.mapgRemediationAuditRecord".casefold():
            from .mapg_remediation_audit_record import MapgRemediationAuditRecord

            return MapgRemediationAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.mcasAlertsAuditRecord".casefold():
            from .mcas_alerts_audit_record import McasAlertsAuditRecord

            return McasAlertsAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.mdaAuditRecord".casefold():
            from .mda_audit_record import MdaAuditRecord

            return MdaAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.mdaDataSecuritySignalRecord".casefold():
            from .mda_data_security_signal_record import MdaDataSecuritySignalRecord

            return MdaDataSecuritySignalRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.mDASHAuditRecord".casefold():
            from .m_d_a_s_h_audit_record import MDASHAuditRecord

            return MDASHAuditRecord()
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
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.microsoft365BackupGranularBrowseTaskAuditRecord".casefold():
            from .microsoft365_backup_granular_browse_task_audit_record import Microsoft365BackupGranularBrowseTaskAuditRecord

            return Microsoft365BackupGranularBrowseTaskAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.microsoft365BackupRestoreItemAuditRecord".casefold():
            from .microsoft365_backup_restore_item_audit_record import Microsoft365BackupRestoreItemAuditRecord

            return Microsoft365BackupRestoreItemAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.microsoft365BackupRestoreTaskAuditRecord".casefold():
            from .microsoft365_backup_restore_task_audit_record import Microsoft365BackupRestoreTaskAuditRecord

            return Microsoft365BackupRestoreTaskAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.microsoft365CopilotScheduledPromptAuditRecord".casefold():
            from .microsoft365_copilot_scheduled_prompt_audit_record import Microsoft365CopilotScheduledPromptAuditRecord

            return Microsoft365CopilotScheduledPromptAuditRecord()
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
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.microsoftPurviewDataCatalogOperationRecord".casefold():
            from .microsoft_purview_data_catalog_operation_record import MicrosoftPurviewDataCatalogOperationRecord

            return MicrosoftPurviewDataCatalogOperationRecord()
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
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.microsoftPurviewUnifiedCatalogOperationRecord".casefold():
            from .microsoft_purview_unified_catalog_operation_record import MicrosoftPurviewUnifiedCatalogOperationRecord

            return MicrosoftPurviewUnifiedCatalogOperationRecord()
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
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.microsoftTeamsUserConcernAuditRecord".casefold():
            from .microsoft_teams_user_concern_audit_record import MicrosoftTeamsUserConcernAuditRecord

            return MicrosoftTeamsUserConcernAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.mipAutoLabelExchangeItemAuditRecord".casefold():
            from .mip_auto_label_exchange_item_audit_record import MipAutoLabelExchangeItemAuditRecord

            return MipAutoLabelExchangeItemAuditRecord()
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
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.mipExactDataMatchAuditRecord".casefold():
            from .mip_exact_data_match_audit_record import MipExactDataMatchAuditRecord

            return MipExactDataMatchAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.mipLabelAnalyticsAuditRecord".casefold():
            from .mip_label_analytics_audit_record import MipLabelAnalyticsAuditRecord

            return MipLabelAnalyticsAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.mipLabelAuditRecord".casefold():
            from .mip_label_audit_record import MipLabelAuditRecord

            return MipLabelAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.mosAgentInfoRecord".casefold():
            from .mos_agent_info_record import MosAgentInfoRecord

            return MosAgentInfoRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.mosAgentInfoRecordV2".casefold():
            from .mos_agent_info_record_v2 import MosAgentInfoRecordV2

            return MosAgentInfoRecordV2()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ms365dCustomDetectionAuditRecord".casefold():
            from .ms365d_custom_detection_audit_record import Ms365dCustomDetectionAuditRecord

            return Ms365dCustomDetectionAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ms365dIncidentAuditRecord".casefold():
            from .ms365d_incident_audit_record import Ms365dIncidentAuditRecord

            return Ms365dIncidentAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ms365dSuppressionRuleAuditRecord".casefold():
            from .ms365d_suppression_rule_audit_record import Ms365dSuppressionRuleAuditRecord

            return Ms365dSuppressionRuleAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.msdeCustomCollectionAuditRecord".casefold():
            from .msde_custom_collection_audit_record import MsdeCustomCollectionAuditRecord

            return MsdeCustomCollectionAuditRecord()
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
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.mspVectorSearchContentMetadataAuditRecord".casefold():
            from .msp_vector_search_content_metadata_audit_record import MspVectorSearchContentMetadataAuditRecord

            return MspVectorSearchContentMetadataAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.msticNationStateNotificationRecord".casefold():
            from .mstic_nation_state_notification_record import MsticNationStateNotificationRecord

            return MsticNationStateNotificationRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.multiStageDispositionAuditRecord".casefold():
            from .multi_stage_disposition_audit_record import MultiStageDispositionAuditRecord

            return MultiStageDispositionAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.myAnalyticsSettingsAuditRecord".casefold():
            from .my_analytics_settings_audit_record import MyAnalyticsSettingsAuditRecord

            return MyAnalyticsSettingsAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.noisyAlertPolicyAuditRecord".casefold():
            from .noisy_alert_policy_audit_record import NoisyAlertPolicyAuditRecord

            return NoisyAlertPolicyAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.officeNativeAuditRecord".casefold():
            from .office_native_audit_record import OfficeNativeAuditRecord

            return OfficeNativeAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.omePortalAuditRecord".casefold():
            from .ome_portal_audit_record import OmePortalAuditRecord

            return OmePortalAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.onDemandSharePointClassificationAuditRecord".casefold():
            from .on_demand_share_point_classification_audit_record import OnDemandSharePointClassificationAuditRecord

            return OnDemandSharePointClassificationAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.oneDriveAuditRecord".casefold():
            from .one_drive_audit_record import OneDriveAuditRecord

            return OneDriveAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.onPremisesFileShareScannerDLPAuditRecord".casefold():
            from .on_premises_file_share_scanner_d_l_p_audit_record import OnPremisesFileShareScannerDLPAuditRecord

            return OnPremisesFileShareScannerDLPAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.onPremisesSharePointScannerDLPAuditRecord".casefold():
            from .on_premises_share_point_scanner_d_l_p_audit_record import OnPremisesSharePointScannerDLPAuditRecord

            return OnPremisesSharePointScannerDLPAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.organizationalDataInM365AuditRecord".casefold():
            from .organizational_data_in_m365_audit_record import OrganizationalDataInM365AuditRecord

            return OrganizationalDataInM365AuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.outlookCopilotAutomationAuditRecord".casefold():
            from .outlook_copilot_automation_audit_record import OutlookCopilotAutomationAuditRecord

            return OutlookCopilotAutomationAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.owaGetAccessTokenForResourceAuditRecord".casefold():
            from .owa_get_access_token_for_resource_audit_record import OwaGetAccessTokenForResourceAuditRecord

            return OwaGetAccessTokenForResourceAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.p4aiAssessmentCategoryRecord".casefold():
            from .p4ai_assessment_category_record import P4aiAssessmentCategoryRecord

            return P4aiAssessmentCategoryRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.p4aiAssessmentFabricScannerRecord".casefold():
            from .p4ai_assessment_fabric_scanner_record import P4aiAssessmentFabricScannerRecord

            return P4aiAssessmentFabricScannerRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.p4aiAssessmentLocationResultRecord".casefold():
            from .p4ai_assessment_location_result_record import P4aiAssessmentLocationResultRecord

            return P4aiAssessmentLocationResultRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.p4aiAssessmentRecord".casefold():
            from .p4ai_assessment_record import P4aiAssessmentRecord

            return P4aiAssessmentRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.p4AIRiskScoreRecord".casefold():
            from .p4_a_i_risk_score_record import P4AIRiskScoreRecord

            return P4AIRiskScoreRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.peopleAdminSettingsAuditRecord".casefold():
            from .people_admin_settings_audit_record import PeopleAdminSettingsAuditRecord

            return PeopleAdminSettingsAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.physicalBadgingSignalAuditRecord".casefold():
            from .physical_badging_signal_audit_record import PhysicalBadgingSignalAuditRecord

            return PhysicalBadgingSignalAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.placesDirectoryAuditRecord".casefold():
            from .places_directory_audit_record import PlacesDirectoryAuditRecord

            return PlacesDirectoryAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.plannerChatMessageAuditRecord".casefold():
            from .planner_chat_message_audit_record import PlannerChatMessageAuditRecord

            return PlannerChatMessageAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.plannerChatMessageListAuditRecord".casefold():
            from .planner_chat_message_list_audit_record import PlannerChatMessageListAuditRecord

            return PlannerChatMessageListAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.plannerCopyPlanAuditRecord".casefold():
            from .planner_copy_plan_audit_record import PlannerCopyPlanAuditRecord

            return PlannerCopyPlanAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.plannerGoalAuditRecord".casefold():
            from .planner_goal_audit_record import PlannerGoalAuditRecord

            return PlannerGoalAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.plannerGoalListAuditRecord".casefold():
            from .planner_goal_list_audit_record import PlannerGoalListAuditRecord

            return PlannerGoalListAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.plannerPlanAuditRecord".casefold():
            from .planner_plan_audit_record import PlannerPlanAuditRecord

            return PlannerPlanAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.plannerPlanListAuditRecord".casefold():
            from .planner_plan_list_audit_record import PlannerPlanListAuditRecord

            return PlannerPlanListAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.plannerPlanSensitivityLabelAuditRecord".casefold():
            from .planner_plan_sensitivity_label_audit_record import PlannerPlanSensitivityLabelAuditRecord

            return PlannerPlanSensitivityLabelAuditRecord()
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
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.policyConfigChangeAuditRecord".casefold():
            from .policy_config_change_audit_record import PolicyConfigChangeAuditRecord

            return PolicyConfigChangeAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.powerAppsAuditAppRecord".casefold():
            from .power_apps_audit_app_record import PowerAppsAuditAppRecord

            return PowerAppsAuditAppRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.powerAppsAuditPlanRecord".casefold():
            from .power_apps_audit_plan_record import PowerAppsAuditPlanRecord

            return PowerAppsAuditPlanRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.powerAppsAuditResourceRecord".casefold():
            from .power_apps_audit_resource_record import PowerAppsAuditResourceRecord

            return PowerAppsAuditResourceRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.powerBIAuditRecord".casefold():
            from .power_b_i_audit_record import PowerBIAuditRecord

            return PowerBIAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.powerBIDlpAuditRecord".casefold():
            from .power_b_i_dlp_audit_record import PowerBIDlpAuditRecord

            return PowerBIDlpAuditRecord()
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
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.powerPlatformTenantIsolationRecord".casefold():
            from .power_platform_tenant_isolation_record import PowerPlatformTenantIsolationRecord

            return PowerPlatformTenantIsolationRecord()
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
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.privaPrivacyAssessmentOperationRecord".casefold():
            from .priva_privacy_assessment_operation_record import PrivaPrivacyAssessmentOperationRecord

            return PrivaPrivacyAssessmentOperationRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.privaPrivacyConsentOperationRecord".casefold():
            from .priva_privacy_consent_operation_record import PrivaPrivacyConsentOperationRecord

            return PrivaPrivacyConsentOperationRecord()
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
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.purviewMCRecommendationRecord".casefold():
            from .purview_m_c_recommendation_record import PurviewMCRecommendationRecord

            return PurviewMCRecommendationRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.purviewPostureAgentAuditRecord".casefold():
            from .purview_posture_agent_audit_record import PurviewPostureAgentAuditRecord

            return PurviewPostureAgentAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.quarantineAuditRecord".casefold():
            from .quarantine_audit_record import QuarantineAuditRecord

            return QuarantineAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.recordsManagementAuditRecord".casefold():
            from .records_management_audit_record import RecordsManagementAuditRecord

            return RecordsManagementAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.reportSubmission".casefold():
            from .report_submission import ReportSubmission

            return ReportSubmission()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.reportSubmissionResultDetail".casefold():
            from .report_submission_result_detail import ReportSubmissionResultDetail

            return ReportSubmissionResultDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.restrictedModeAuditRecord".casefold():
            from .restricted_mode_audit_record import RestrictedModeAuditRecord

            return RestrictedModeAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.retentionPolicyAuditRecord".casefold():
            from .retention_policy_audit_record import RetentionPolicyAuditRecord

            return RetentionPolicyAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.rtiOperationsAgentAuditRecord".casefold():
            from .rti_operations_agent_audit_record import RtiOperationsAgentAuditRecord

            return RtiOperationsAgentAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.sbpConfigurationEventRecord".casefold():
            from .sbp_configuration_event_record import SbpConfigurationEventRecord

            return SbpConfigurationEventRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.sbpUsageEventRecord".casefold():
            from .sbp_usage_event_record import SbpUsageEventRecord

            return SbpUsageEventRecord()
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
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.securityCopilotIdentityManagementAuditRecord".casefold():
            from .security_copilot_identity_management_audit_record import SecurityCopilotIdentityManagementAuditRecord

            return SecurityCopilotIdentityManagementAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.securityDevelopmentLifecycleAILogAuditRecord".casefold():
            from .security_development_lifecycle_a_i_log_audit_record import SecurityDevelopmentLifecycleAILogAuditRecord

            return SecurityDevelopmentLifecycleAILogAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.sensitiveInfoRemediationAgentDataRecord".casefold():
            from .sensitive_info_remediation_agent_data_record import SensitiveInfoRemediationAgentDataRecord

            return SensitiveInfoRemediationAgentDataRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.sensitivityLabelActionAuditRecord".casefold():
            from .sensitivity_label_action_audit_record import SensitivityLabelActionAuditRecord

            return SensitivityLabelActionAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.sensitivityLabeledFileActionAuditRecord".casefold():
            from .sensitivity_labeled_file_action_audit_record import SensitivityLabeledFileActionAuditRecord

            return SensitivityLabeledFileActionAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.sensitivityLabelPolicyMatchAuditRecord".casefold():
            from .sensitivity_label_policy_match_audit_record import SensitivityLabelPolicyMatchAuditRecord

            return SensitivityLabelPolicyMatchAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.sentinelAIToolAuditRecord".casefold():
            from .sentinel_a_i_tool_audit_record import SentinelAIToolAuditRecord

            return SentinelAIToolAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.sentinelGraphAuditRecord".casefold():
            from .sentinel_graph_audit_record import SentinelGraphAuditRecord

            return SentinelGraphAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.sentinelJobAuditRecord".casefold():
            from .sentinel_job_audit_record import SentinelJobAuditRecord

            return SentinelJobAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.sentinelKQLOnLakeAuditRecord".casefold():
            from .sentinel_k_q_l_on_lake_audit_record import SentinelKQLOnLakeAuditRecord

            return SentinelKQLOnLakeAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.sentinelLakeDataOnboardingAuditRecord".casefold():
            from .sentinel_lake_data_onboarding_audit_record import SentinelLakeDataOnboardingAuditRecord

            return SentinelLakeDataOnboardingAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.sentinelLakeEncryptionAuditRecord".casefold():
            from .sentinel_lake_encryption_audit_record import SentinelLakeEncryptionAuditRecord

            return SentinelLakeEncryptionAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.sentinelLakeOnboardingAuditRecord".casefold():
            from .sentinel_lake_onboarding_audit_record import SentinelLakeOnboardingAuditRecord

            return SentinelLakeOnboardingAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.sentinelNotebookOnLakeAuditRecord".casefold():
            from .sentinel_notebook_on_lake_audit_record import SentinelNotebookOnLakeAuditRecord

            return SentinelNotebookOnLakeAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.sentinelPackageAuditRecord".casefold():
            from .sentinel_package_audit_record import SentinelPackageAuditRecord

            return SentinelPackageAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.sharePointAppPermissionOperationAuditRecord".casefold():
            from .share_point_app_permission_operation_audit_record import SharePointAppPermissionOperationAuditRecord

            return SharePointAppPermissionOperationAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.sharePointAuditRecord".casefold():
            from .share_point_audit_record import SharePointAuditRecord

            return SharePointAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.sharePointCommentOperationAuditRecord".casefold():
            from .share_point_comment_operation_audit_record import SharePointCommentOperationAuditRecord

            return SharePointCommentOperationAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.sharePointContentSecurityPolicyAuditRecord".casefold():
            from .share_point_content_security_policy_audit_record import SharePointContentSecurityPolicyAuditRecord

            return SharePointContentSecurityPolicyAuditRecord()
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
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.sharePointListItemOperationAuditRecord".casefold():
            from .share_point_list_item_operation_audit_record import SharePointListItemOperationAuditRecord

            return SharePointListItemOperationAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.sharePointListOperationAuditRecord".casefold():
            from .share_point_list_operation_audit_record import SharePointListOperationAuditRecord

            return SharePointListOperationAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.sharePointSharingOperationAuditRecord".casefold():
            from .share_point_sharing_operation_audit_record import SharePointSharingOperationAuditRecord

            return SharePointSharingOperationAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.skypeForBusinessCmdletsAuditRecord".casefold():
            from .skype_for_business_cmdlets_audit_record import SkypeForBusinessCmdletsAuditRecord

            return SkypeForBusinessCmdletsAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.skypeForBusinessPSTNUsageAuditRecord".casefold():
            from .skype_for_business_p_s_t_n_usage_audit_record import SkypeForBusinessPSTNUsageAuditRecord

            return SkypeForBusinessPSTNUsageAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.skypeForBusinessUsersBlockedAuditRecord".casefold():
            from .skype_for_business_users_blocked_audit_record import SkypeForBusinessUsersBlockedAuditRecord

            return SkypeForBusinessUsersBlockedAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.sonarDetonationContentMetadata".casefold():
            from .sonar_detonation_content_metadata import SonarDetonationContentMetadata

            return SonarDetonationContentMetadata()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.sonarDetonationEntityAuditRecord".casefold():
            from .sonar_detonation_entity_audit_record import SonarDetonationEntityAuditRecord

            return SonarDetonationEntityAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.sonarFileDetonationEntityAuditRecord".casefold():
            from .sonar_file_detonation_entity_audit_record import SonarFileDetonationEntityAuditRecord

            return SonarFileDetonationEntityAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.sonarSubmissionEntityAuditRecord".casefold():
            from .sonar_submission_entity_audit_record import SonarSubmissionEntityAuditRecord

            return SonarSubmissionEntityAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.sonarUrlDetonationEntityAuditRecord".casefold():
            from .sonar_url_detonation_entity_audit_record import SonarUrlDetonationEntityAuditRecord

            return SonarUrlDetonationEntityAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.sparkCoreCustomLivePoolRecord".casefold():
            from .spark_core_custom_live_pool_record import SparkCoreCustomLivePoolRecord

            return SparkCoreCustomLivePoolRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.submissionEntityAuditRecord".casefold():
            from .submission_entity_audit_record import SubmissionEntityAuditRecord

            return SubmissionEntityAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.supervisoryReviewDayXInsightsAuditRecord".casefold():
            from .supervisory_review_day_x_insights_audit_record import SupervisoryReviewDayXInsightsAuditRecord

            return SupervisoryReviewDayXInsightsAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.syntheticProbeAuditRecord".casefold():
            from .synthetic_probe_audit_record import SyntheticProbeAuditRecord

            return SyntheticProbeAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.teamCopilotInteractionAuditRecord".casefold():
            from .team_copilot_interaction_audit_record import TeamCopilotInteractionAuditRecord

            return TeamCopilotInteractionAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.teamsEasyApprovalsAuditRecord".casefold():
            from .teams_easy_approvals_audit_record import TeamsEasyApprovalsAuditRecord

            return TeamsEasyApprovalsAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.teamsEvalDataHubAdminOperationAuditRecord".casefold():
            from .teams_eval_data_hub_admin_operation_audit_record import TeamsEvalDataHubAdminOperationAuditRecord

            return TeamsEvalDataHubAdminOperationAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.teamsEvalDataHubDataAccessAuditRecord".casefold():
            from .teams_eval_data_hub_data_access_audit_record import TeamsEvalDataHubDataAccessAuditRecord

            return TeamsEvalDataHubDataAccessAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.teamsEvalDataHubPermissionChangeAuditRecord".casefold():
            from .teams_eval_data_hub_permission_change_audit_record import TeamsEvalDataHubPermissionChangeAuditRecord

            return TeamsEvalDataHubPermissionChangeAuditRecord()
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
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.threatIntelligenceExportAuditRecord".casefold():
            from .threat_intelligence_export_audit_record import ThreatIntelligenceExportAuditRecord

            return ThreatIntelligenceExportAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.threatIntelligenceMailData".casefold():
            from .threat_intelligence_mail_data import ThreatIntelligenceMailData

            return ThreatIntelligenceMailData()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.threatIntelligenceObjectAuditRecord".casefold():
            from .threat_intelligence_object_audit_record import ThreatIntelligenceObjectAuditRecord

            return ThreatIntelligenceObjectAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.threatIntelligenceUrlClickData".casefold():
            from .threat_intelligence_url_click_data import ThreatIntelligenceUrlClickData

            return ThreatIntelligenceUrlClickData()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.todoAuditRecord".casefold():
            from .todo_audit_record import TodoAuditRecord

            return TodoAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.trainableClassifierAuditRecord".casefold():
            from .trainable_classifier_audit_record import TrainableClassifierAuditRecord

            return TrainableClassifierAuditRecord()
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
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.universalPrintManagementAuditRecord".casefold():
            from .universal_print_management_audit_record import UniversalPrintManagementAuditRecord

            return UniversalPrintManagementAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.universalPrintPrintJobAuditRecord".casefold():
            from .universal_print_print_job_audit_record import UniversalPrintPrintJobAuditRecord

            return UniversalPrintPrintJobAuditRecord()
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
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.usxWorkspaceOnboardingAuditRecord".casefold():
            from .usx_workspace_onboarding_audit_record import UsxWorkspaceOnboardingAuditRecord

            return UsxWorkspaceOnboardingAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.vfamCreatePolicyAuditRecord".casefold():
            from .vfam_create_policy_audit_record import VfamCreatePolicyAuditRecord

            return VfamCreatePolicyAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.vfamDeletePolicyAuditRecord".casefold():
            from .vfam_delete_policy_audit_record import VfamDeletePolicyAuditRecord

            return VfamDeletePolicyAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.vfamUpdatePolicyAuditRecord".casefold():
            from .vfam_update_policy_audit_record import VfamUpdatePolicyAuditRecord

            return VfamUpdatePolicyAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.vivaAmplifyAuditRecord".casefold():
            from .viva_amplify_audit_record import VivaAmplifyAuditRecord

            return VivaAmplifyAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.vivaEngageEventsAuditRecord".casefold():
            from .viva_engage_events_audit_record import VivaEngageEventsAuditRecord

            return VivaEngageEventsAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.vivaEngageNetworkAssociationAuditRecord".casefold():
            from .viva_engage_network_association_audit_record import VivaEngageNetworkAssociationAuditRecord

            return VivaEngageNetworkAssociationAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.vivaEngageSegmentAuditRecord".casefold():
            from .viva_engage_segment_audit_record import VivaEngageSegmentAuditRecord

            return VivaEngageSegmentAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.vivaGlintAdvancedConfigurationAuditRecord".casefold():
            from .viva_glint_advanced_configuration_audit_record import VivaGlintAdvancedConfigurationAuditRecord

            return VivaGlintAdvancedConfigurationAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.vivaGlintAgenticCampaignAuditRecord".casefold():
            from .viva_glint_agentic_campaign_audit_record import VivaGlintAgenticCampaignAuditRecord

            return VivaGlintAgenticCampaignAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.vivaGlintFeedbackProgramAuditRecord".casefold():
            from .viva_glint_feedback_program_audit_record import VivaGlintFeedbackProgramAuditRecord

            return VivaGlintFeedbackProgramAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.vivaGlintOrganizationalDataAuditRecord".casefold():
            from .viva_glint_organizational_data_audit_record import VivaGlintOrganizationalDataAuditRecord

            return VivaGlintOrganizationalDataAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.vivaGlintPulseProgramAuditRecord".casefold():
            from .viva_glint_pulse_program_audit_record import VivaGlintPulseProgramAuditRecord

            return VivaGlintPulseProgramAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.vivaGlintPulseProgramRespondentRateAuditRecord".casefold():
            from .viva_glint_pulse_program_respondent_rate_audit_record import VivaGlintPulseProgramRespondentRateAuditRecord

            return VivaGlintPulseProgramRespondentRateAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.vivaGlintQuestionAuditRecord".casefold():
            from .viva_glint_question_audit_record import VivaGlintQuestionAuditRecord

            return VivaGlintQuestionAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.vivaGlintRoleAuditRecord".casefold():
            from .viva_glint_role_audit_record import VivaGlintRoleAuditRecord

            return VivaGlintRoleAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.vivaGlintRubiconAuditRecord".casefold():
            from .viva_glint_rubicon_audit_record import VivaGlintRubiconAuditRecord

            return VivaGlintRubiconAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.vivaGlintSupportAccessAuditRecord".casefold():
            from .viva_glint_support_access_audit_record import VivaGlintSupportAccessAuditRecord

            return VivaGlintSupportAccessAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.vivaGlintSystemAuditRecord".casefold():
            from .viva_glint_system_audit_record import VivaGlintSystemAuditRecord

            return VivaGlintSystemAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.vivaGlintUserAuditRecord".casefold():
            from .viva_glint_user_audit_record import VivaGlintUserAuditRecord

            return VivaGlintUserAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.vivaGlintUserGroupAuditRecord".casefold():
            from .viva_glint_user_group_audit_record import VivaGlintUserGroupAuditRecord

            return VivaGlintUserGroupAuditRecord()
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
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.webContentFilteringAuditRecord".casefold():
            from .web_content_filtering_audit_record import WebContentFilteringAuditRecord

            return WebContentFilteringAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.windows365CustomerLockboxAuditRecord".casefold():
            from .windows365_customer_lockbox_audit_record import Windows365CustomerLockboxAuditRecord

            return Windows365CustomerLockboxAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.workplaceAnalyticsAuditRecord".casefold():
            from .workplace_analytics_audit_record import WorkplaceAnalyticsAuditRecord

            return WorkplaceAnalyticsAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.yammerAuditRecord".casefold():
            from .yammer_audit_record import YammerAuditRecord

            return YammerAuditRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.yammerUserHidingAuditRecord".casefold():
            from .yammer_user_hiding_audit_record import YammerUserHidingAuditRecord

            return YammerUserHidingAuditRecord()
        return AuditData()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .a365_ai_execute_tool import A365AiExecuteTool
        from .a365_ai_inference_call import A365AiInferenceCall
        from .a365_ai_invoke_agent import A365AiInvokeAgent
        from .a365_ai_run_summary import A365AiRunSummary
        from .a365_span_outputs import A365SpanOutputs
        from .aad_risk_detection_audit_record import AadRiskDetectionAuditRecord
        from .aed_audit_record import AedAuditRecord
        from .agent_admin_activity_record import AgentAdminActivityRecord
        from .agent_setting_admin_activity import AgentSettingAdminActivity
        from .aip_discover import AipDiscover
        from .aip_file_deleted import AipFileDeleted
        from .aip_heart_beat import AipHeartBeat
        from .aip_protection_action_log_request import AipProtectionActionLogRequest
        from .aip_scanner_discover_event import AipScannerDiscoverEvent
        from .aip_sensitivity_label_action_log_request import AipSensitivityLabelActionLogRequest
        from .air_admin_action_investigation_data import AirAdminActionInvestigationData
        from .air_investigation_data import AirInvestigationData
        from .air_manual_investigation_data import AirManualInvestigationData
        from .ai_app_interaction_audit_record import AiAppInteractionAuditRecord
        from .ai_execute_tool_audit_record import AiExecuteToolAuditRecord
        from .ai_interactions_change_notification_audit_record import AiInteractionsChangeNotificationAuditRecord
        from .ai_interactions_export_audit_record import AiInteractionsExportAuditRecord
        from .ai_interactions_subscription_audit_record import AiInteractionsSubscriptionAuditRecord
        from .ai_invoke_agent_audit_record import AiInvokeAgentAuditRecord
        from .alert_submission_audit_record import AlertSubmissionAuditRecord
        from .alert_submission_result_detail_audit_record import AlertSubmissionResultDetailAuditRecord
        from .attack_sim_admin_audit_record import AttackSimAdminAuditRecord
        from .attack_sim_audit_record import AttackSimAuditRecord
        from .audit_config_audit_record import AuditConfigAuditRecord
        from .audit_record_type_dictionary import AuditRecordTypeDictionary
        from .audit_search_audit_record import AuditSearchAuditRecord
        from .azfw_application_rule_aggregation_event_record import AzfwApplicationRuleAggregationEventRecord
        from .azfw_dns_query_event_record import AzfwDnsQueryEventRecord
        from .azfw_network_rule_event_record import AzfwNetworkRuleEventRecord
        from .azure_active_directory_account_logon_audit_record import AzureActiveDirectoryAccountLogonAuditRecord
        from .azure_active_directory_audit_record import AzureActiveDirectoryAuditRecord
        from .azure_active_directory_sts_logon_audit_record import AzureActiveDirectoryStsLogonAuditRecord
        from .azure_a_i_search_audit_record import AzureAISearchAuditRecord
        from .a_i_span_outputs_audit_record import AISpanOutputsAuditRecord
        from .campaign_audit_record import CampaignAuditRecord
        from .ccrai_policy_violation_record import CcraiPolicyViolationRecord
        from .cdpdlmai_interaction_insights_record import CdpdlmaiInteractionInsightsRecord
        from .cdp_classifier_health_record import CdpClassifierHealthRecord
        from .cdp_cold_crawl_status_record import CdpColdCrawlStatusRecord
        from .cdp_consumption_resource_record import CdpConsumptionResourceRecord
        from .cdp_content_explorer_aggregate_record import CdpContentExplorerAggregateRecord
        from .cdp_dlp_sensitive_endpoint_audit_record import CdpDlpSensitiveEndpointAuditRecord
        from .cdp_log_record import CdpLogRecord
        from .cdp_ocr_billing_record import CdpOcrBillingRecord
        from .cdp_resource_scope_change_event_record import CdpResourceScopeChangeEventRecord
        from .cloud_update_device_config_audit_record import CloudUpdateDeviceConfigAuditRecord
        from .cloud_update_profile_config_audit_record import CloudUpdateProfileConfigAuditRecord
        from .cloud_update_tenant_config_audit_record import CloudUpdateTenantConfigAuditRecord
        from .compliance_connector_audit_record import ComplianceConnectorAuditRecord
        from .compliance_d_l_m_exchange_audit_record import ComplianceDLMExchangeAuditRecord
        from .compliance_d_l_m_share_point_audit_record import ComplianceDLMSharePointAuditRecord
        from .compliance_d_l_p_applications_audit_record import ComplianceDLPApplicationsAuditRecord
        from .compliance_d_l_p_applications_classification_audit_record import ComplianceDLPApplicationsClassificationAuditRecord
        from .compliance_d_l_p_endpoint_audit_record import ComplianceDLPEndpointAuditRecord
        from .compliance_d_l_p_endpoint_discovery_audit_record import ComplianceDLPEndpointDiscoveryAuditRecord
        from .compliance_d_l_p_enforcement_audit_record import ComplianceDLPEnforcementAuditRecord
        from .compliance_d_l_p_exchange_audit_record import ComplianceDLPExchangeAuditRecord
        from .compliance_d_l_p_exchange_classification_audit_record import ComplianceDLPExchangeClassificationAuditRecord
        from .compliance_d_l_p_exchange_classification_cdp_record import ComplianceDLPExchangeClassificationCdpRecord
        from .compliance_d_l_p_exchange_discovery_audit_record import ComplianceDLPExchangeDiscoveryAuditRecord
        from .compliance_d_l_p_share_point_audit_record import ComplianceDLPSharePointAuditRecord
        from .compliance_d_l_p_share_point_classification_audit_record import ComplianceDLPSharePointClassificationAuditRecord
        from .compliance_d_l_p_share_point_classification_cdp_record import ComplianceDLPSharePointClassificationCdpRecord
        from .compliance_d_l_p_share_point_classification_extended_audit_record import ComplianceDLPSharePointClassificationExtendedAuditRecord
        from .compliance_exchange_ocr_audit_record import ComplianceExchangeOcrAuditRecord
        from .compliance_manager_action_record import ComplianceManagerActionRecord
        from .compliance_policy_grading_share_point_audit_record import CompliancePolicyGradingSharePointAuditRecord
        from .compliance_settings_change_audit_record import ComplianceSettingsChangeAuditRecord
        from .compliance_sit_grading_share_point_audit_record import ComplianceSitGradingSharePointAuditRecord
        from .compliance_supervision_exchange_audit_record import ComplianceSupervisionExchangeAuditRecord
        from .connected_a_i_app_interaction_audit_record import ConnectedAIAppInteractionAuditRecord
        from .consumption_resource_audit_record import ConsumptionResourceAuditRecord
        from .content_store_metadata_record import ContentStoreMetadataRecord
        from .copilot_agent_management_audit_record import CopilotAgentManagementAuditRecord
        from .copilot_for_security_logging_audit_record import CopilotForSecurityLoggingAuditRecord
        from .copilot_for_security_trigger_audit_record import CopilotForSecurityTriggerAuditRecord
        from .copilot_interaction_audit_record import CopilotInteractionAuditRecord
        from .copilot_plugin_setting_audit_record import CopilotPluginSettingAuditRecord
        from .copilot_prompt_book_setting_audit_record import CopilotPromptBookSettingAuditRecord
        from .copilot_session_sharing_audit_record import CopilotSessionSharingAuditRecord
        from .copilot_setting_audit_record import CopilotSettingAuditRecord
        from .copilot_workspace_setting_audit_record import CopilotWorkspaceSettingAuditRecord
        from .core_reporting_settings_audit_record import CoreReportingSettingsAuditRecord
        from .cortana_briefing_audit_record import CortanaBriefingAuditRecord
        from .critical_asset_management_classification_record import CriticalAssetManagementClassificationRecord
        from .crm_entity_operation_audit_record import CrmEntityOperationAuditRecord
        from .cross_tenant_access_policy_audit_record import CrossTenantAccessPolicyAuditRecord
        from .customer_key_service_encryption_audit_record import CustomerKeyServiceEncryptionAuditRecord
        from .data_center_security_cmdlet_audit_record import DataCenterSecurityCmdletAuditRecord
        from .data_governance_audit_record import DataGovernanceAuditRecord
        from .data_insights_rest_api_audit_record import DataInsightsRestApiAuditRecord
        from .data_lake_export_operation_audit_record import DataLakeExportOperationAuditRecord
        from .data_security_investigation_audit_record import DataSecurityInvestigationAuditRecord
        from .data_share_operation_audit_record import DataShareOperationAuditRecord
        from .default_audit_data import DefaultAuditData
        from .defender_case_management_audit_record import DefenderCaseManagementAuditRecord
        from .defender_preview_features_record import DefenderPreviewFeaturesRecord
        from .defender_security_for_a_i_configuration_audit_record import DefenderSecurityForAIConfigurationAuditRecord
        from .deploy_feature_activity_record import DeployFeatureActivityRecord
        from .device_discovery_settings_authenticated_scans_record import DeviceDiscoverySettingsAuthenticatedScansRecord
        from .device_discovery_settings_exclusion_record import DeviceDiscoverySettingsExclusionRecord
        from .device_discovery_settings_record import DeviceDiscoverySettingsRecord
        from .discovery_audit_record import DiscoveryAuditRecord
        from .dlp_endpoint_audit_record import DlpEndpointAuditRecord
        from .dlp_import_result_audit_record import DlpImportResultAuditRecord
        from .dlp_sensitive_information_type_rule_package_cmdlet_record import DlpSensitiveInformationTypeRulePackageCmdletRecord
        from .dragon_copilot_access_record import DragonCopilotAccessRecord
        from .dragon_copilot_admin_record import DragonCopilotAdminRecord
        from .dragon_copilot_clinical_data_record import DragonCopilotClinicalDataRecord
        from .dragon_copilot_session_record import DragonCopilotSessionRecord
        from .dynamics365_business_central_audit_record import Dynamics365BusinessCentralAuditRecord
        from .ehr_connector_audit_base_record import EhrConnectorAuditBaseRecord
        from .eop_submission_feed_entity_audit_record import EopSubmissionFeedEntityAuditRecord
        from .exchange_admin_audit_record import ExchangeAdminAuditRecord
        from .exchange_aggregated_mailbox_audit_record import ExchangeAggregatedMailboxAuditRecord
        from .exchange_aggregated_operation_record import ExchangeAggregatedOperationRecord
        from .exchange_mailbox_audit_group_record import ExchangeMailboxAuditGroupRecord
        from .exchange_mailbox_audit_record import ExchangeMailboxAuditRecord
        from .fabric_audit_record import FabricAuditRecord
        from .fabric_policy_record import FabricPolicyRecord
        from .healthcare_signal_record import HealthcareSignalRecord
        from .hosted_rpa_audit_record import HostedRpaAuditRecord
        from .hr_signal_audit_record import HrSignalAuditRecord
        from .hygiene_event_record import HygieneEventRecord
        from .information_barrier_policy_application_audit_record import InformationBarrierPolicyApplicationAuditRecord
        from .information_worker_protection_audit_record import InformationWorkerProtectionAuditRecord
        from .insider_risk_scoped_users_record import InsiderRiskScopedUsersRecord
        from .insider_risk_scoped_user_insights_record import InsiderRiskScopedUserInsightsRecord
        from .integrated_apps_app_admin_activity_audit_record import IntegratedAppsAppAdminActivityAuditRecord
        from .integrated_apps_app_settings_admin_activity_audit_record import IntegratedAppsAppSettingsAdminActivityAuditRecord
        from .irm_activity_audit_trail_record import IrmActivityAuditTrailRecord
        from .irm_user_defined_detection_record import IrmUserDefinedDetectionRecord
        from .kaizala_audit_record import KaizalaAuditRecord
        from .label_analytics_aggregate_audit_record import LabelAnalyticsAggregateAuditRecord
        from .label_content_explorer_audit_record import LabelContentExplorerAuditRecord
        from .large_content_metadata_audit_record import LargeContentMetadataAuditRecord
        from .m365daad_audit_record import M365daadAuditRecord
        from .m365odsp_asset_metadata_record import M365odspAssetMetadataRecord
        from .m365_compliance_connector_audit_record import M365ComplianceConnectorAuditRecord
        from .m365_search_sections_record import M365SearchSectionsRecord
        from .mail_submission_data import MailSubmissionData
        from .managed_services_audit_record import ManagedServicesAuditRecord
        from .managed_tenants_audit_record import ManagedTenantsAuditRecord
        from .mapg_alerts_audit_record import MapgAlertsAuditRecord
        from .mapg_onboard_audit_record import MapgOnboardAuditRecord
        from .mapg_policy_audit_record import MapgPolicyAuditRecord
        from .mapg_remediation_audit_record import MapgRemediationAuditRecord
        from .mcas_alerts_audit_record import McasAlertsAuditRecord
        from .mdatp_audit_record import MdatpAuditRecord
        from .mda_audit_record import MdaAuditRecord
        from .mda_data_security_signal_record import MdaDataSecuritySignalRecord
        from .mdc_events_record import MdcEventsRecord
        from .mdi_audit_record import MdiAuditRecord
        from .mesh_worlds_audit_record import MeshWorldsAuditRecord
        from .microsoft365_backup_backup_item_audit_record import Microsoft365BackupBackupItemAuditRecord
        from .microsoft365_backup_backup_policy_audit_record import Microsoft365BackupBackupPolicyAuditRecord
        from .microsoft365_backup_granular_browse_task_audit_record import Microsoft365BackupGranularBrowseTaskAuditRecord
        from .microsoft365_backup_restore_item_audit_record import Microsoft365BackupRestoreItemAuditRecord
        from .microsoft365_backup_restore_task_audit_record import Microsoft365BackupRestoreTaskAuditRecord
        from .microsoft365_copilot_scheduled_prompt_audit_record import Microsoft365CopilotScheduledPromptAuditRecord
        from .microsoft_defender_experts_x_d_r_audit_record import MicrosoftDefenderExpertsXDRAuditRecord
        from .microsoft_flow_audit_record import MicrosoftFlowAuditRecord
        from .microsoft_forms_audit_record import MicrosoftFormsAuditRecord
        from .microsoft_graph_data_connect_consent import MicrosoftGraphDataConnectConsent
        from .microsoft_graph_data_connect_operation import MicrosoftGraphDataConnectOperation
        from .microsoft_purview_data_catalog_operation_record import MicrosoftPurviewDataCatalogOperationRecord
        from .microsoft_purview_data_map_operation_record import MicrosoftPurviewDataMapOperationRecord
        from .microsoft_purview_metadata_policy_operation_record import MicrosoftPurviewMetadataPolicyOperationRecord
        from .microsoft_purview_policy_operation_record import MicrosoftPurviewPolicyOperationRecord
        from .microsoft_purview_privacy_audit_event import MicrosoftPurviewPrivacyAuditEvent
        from .microsoft_purview_unified_catalog_operation_record import MicrosoftPurviewUnifiedCatalogOperationRecord
        from .microsoft_stream_audit_record import MicrosoftStreamAuditRecord
        from .microsoft_teams_admin_audit_record import MicrosoftTeamsAdminAuditRecord
        from .microsoft_teams_analytics_audit_record import MicrosoftTeamsAnalyticsAuditRecord
        from .microsoft_teams_audit_record import MicrosoftTeamsAuditRecord
        from .microsoft_teams_device_audit_record import MicrosoftTeamsDeviceAuditRecord
        from .microsoft_teams_retention_label_action_audit_record import MicrosoftTeamsRetentionLabelActionAuditRecord
        from .microsoft_teams_sensitivity_label_action_audit_record import MicrosoftTeamsSensitivityLabelActionAuditRecord
        from .microsoft_teams_shifts_audit_record import MicrosoftTeamsShiftsAuditRecord
        from .microsoft_teams_user_concern_audit_record import MicrosoftTeamsUserConcernAuditRecord
        from .mip_auto_label_exchange_item_audit_record import MipAutoLabelExchangeItemAuditRecord
        from .mip_auto_label_progress_feedback_audit_record import MipAutoLabelProgressFeedbackAuditRecord
        from .mip_auto_label_share_point_item_audit_record import MipAutoLabelSharePointItemAuditRecord
        from .mip_auto_label_share_point_policy_location_audit_record import MipAutoLabelSharePointPolicyLocationAuditRecord
        from .mip_auto_label_simulation_share_point_completion_record import MipAutoLabelSimulationSharePointCompletionRecord
        from .mip_auto_label_simulation_share_point_progress_record import MipAutoLabelSimulationSharePointProgressRecord
        from .mip_auto_label_simulation_statistics_record import MipAutoLabelSimulationStatisticsRecord
        from .mip_exact_data_match_audit_record import MipExactDataMatchAuditRecord
        from .mip_label_analytics_audit_record import MipLabelAnalyticsAuditRecord
        from .mip_label_audit_record import MipLabelAuditRecord
        from .mos_agent_info_record import MosAgentInfoRecord
        from .mos_agent_info_record_v2 import MosAgentInfoRecordV2
        from .ms365d_custom_detection_audit_record import Ms365dCustomDetectionAuditRecord
        from .ms365d_incident_audit_record import Ms365dIncidentAuditRecord
        from .ms365d_suppression_rule_audit_record import Ms365dSuppressionRuleAuditRecord
        from .msde_custom_collection_audit_record import MsdeCustomCollectionAuditRecord
        from .msde_general_settings_audit_record import MsdeGeneralSettingsAuditRecord
        from .msde_indicators_settings_audit_record import MsdeIndicatorsSettingsAuditRecord
        from .msde_response_actions_audit_record import MsdeResponseActionsAuditRecord
        from .msde_roles_settings_audit_record import MsdeRolesSettingsAuditRecord
        from .msp_vector_search_content_metadata_audit_record import MspVectorSearchContentMetadataAuditRecord
        from .mstic_nation_state_notification_record import MsticNationStateNotificationRecord
        from .multi_stage_disposition_audit_record import MultiStageDispositionAuditRecord
        from .my_analytics_settings_audit_record import MyAnalyticsSettingsAuditRecord
        from .m_d_a_s_h_audit_record import MDASHAuditRecord
        from .noisy_alert_policy_audit_record import NoisyAlertPolicyAuditRecord
        from .office_native_audit_record import OfficeNativeAuditRecord
        from .ome_portal_audit_record import OmePortalAuditRecord
        from .one_drive_audit_record import OneDriveAuditRecord
        from .on_demand_share_point_classification_audit_record import OnDemandSharePointClassificationAuditRecord
        from .on_premises_file_share_scanner_d_l_p_audit_record import OnPremisesFileShareScannerDLPAuditRecord
        from .on_premises_share_point_scanner_d_l_p_audit_record import OnPremisesSharePointScannerDLPAuditRecord
        from .organizational_data_in_m365_audit_record import OrganizationalDataInM365AuditRecord
        from .outlook_copilot_automation_audit_record import OutlookCopilotAutomationAuditRecord
        from .owa_get_access_token_for_resource_audit_record import OwaGetAccessTokenForResourceAuditRecord
        from .p4ai_assessment_category_record import P4aiAssessmentCategoryRecord
        from .p4ai_assessment_fabric_scanner_record import P4aiAssessmentFabricScannerRecord
        from .p4ai_assessment_location_result_record import P4aiAssessmentLocationResultRecord
        from .p4ai_assessment_record import P4aiAssessmentRecord
        from .p4_a_i_risk_score_record import P4AIRiskScoreRecord
        from .people_admin_settings_audit_record import PeopleAdminSettingsAuditRecord
        from .physical_badging_signal_audit_record import PhysicalBadgingSignalAuditRecord
        from .places_directory_audit_record import PlacesDirectoryAuditRecord
        from .planner_chat_message_audit_record import PlannerChatMessageAuditRecord
        from .planner_chat_message_list_audit_record import PlannerChatMessageListAuditRecord
        from .planner_copy_plan_audit_record import PlannerCopyPlanAuditRecord
        from .planner_goal_audit_record import PlannerGoalAuditRecord
        from .planner_goal_list_audit_record import PlannerGoalListAuditRecord
        from .planner_plan_audit_record import PlannerPlanAuditRecord
        from .planner_plan_list_audit_record import PlannerPlanListAuditRecord
        from .planner_plan_sensitivity_label_audit_record import PlannerPlanSensitivityLabelAuditRecord
        from .planner_roster_audit_record import PlannerRosterAuditRecord
        from .planner_roster_sensitivity_label_audit_record import PlannerRosterSensitivityLabelAuditRecord
        from .planner_task_audit_record import PlannerTaskAuditRecord
        from .planner_task_list_audit_record import PlannerTaskListAuditRecord
        from .planner_tenant_settings_audit_record import PlannerTenantSettingsAuditRecord
        from .policy_config_change_audit_record import PolicyConfigChangeAuditRecord
        from .power_apps_audit_app_record import PowerAppsAuditAppRecord
        from .power_apps_audit_plan_record import PowerAppsAuditPlanRecord
        from .power_apps_audit_resource_record import PowerAppsAuditResourceRecord
        from .power_b_i_audit_record import PowerBIAuditRecord
        from .power_b_i_dlp_audit_record import PowerBIDlpAuditRecord
        from .power_pages_site_audit_record import PowerPagesSiteAuditRecord
        from .power_platform_administrator_activity_record import PowerPlatformAdministratorActivityRecord
        from .power_platform_admin_dlp_audit_record import PowerPlatformAdminDlpAuditRecord
        from .power_platform_admin_environment_audit_record import PowerPlatformAdminEnvironmentAuditRecord
        from .power_platform_lockbox_resource_access_request_audit_record import PowerPlatformLockboxResourceAccessRequestAuditRecord
        from .power_platform_lockbox_resource_command_audit_record import PowerPlatformLockboxResourceCommandAuditRecord
        from .power_platform_service_activity_audit_record import PowerPlatformServiceActivityAuditRecord
        from .power_platform_tenant_isolation_record import PowerPlatformTenantIsolationRecord
        from .privacy_data_match_audit_record import PrivacyDataMatchAuditRecord
        from .privacy_data_minimization_record import PrivacyDataMinimizationRecord
        from .privacy_digest_email_record import PrivacyDigestEmailRecord
        from .privacy_open_access_audit_record import PrivacyOpenAccessAuditRecord
        from .privacy_portal_audit_record import PrivacyPortalAuditRecord
        from .privacy_remediation_action_record import PrivacyRemediationActionRecord
        from .privacy_remediation_record import PrivacyRemediationRecord
        from .priva_privacy_assessment_operation_record import PrivaPrivacyAssessmentOperationRecord
        from .priva_privacy_consent_operation_record import PrivaPrivacyConsentOperationRecord
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
        from .purview_m_c_recommendation_record import PurviewMCRecommendationRecord
        from .purview_posture_agent_audit_record import PurviewPostureAgentAuditRecord
        from .quarantine_audit_record import QuarantineAuditRecord
        from .records_management_audit_record import RecordsManagementAuditRecord
        from .report_submission import ReportSubmission
        from .report_submission_result_detail import ReportSubmissionResultDetail
        from .restricted_mode_audit_record import RestrictedModeAuditRecord
        from .retention_policy_audit_record import RetentionPolicyAuditRecord
        from .rti_operations_agent_audit_record import RtiOperationsAgentAuditRecord
        from .sbp_configuration_event_record import SbpConfigurationEventRecord
        from .sbp_usage_event_record import SbpUsageEventRecord
        from .score_evidence import ScoreEvidence
        from .score_platform_generic_audit_record import ScorePlatformGenericAuditRecord
        from .script_run_audit_record import ScriptRunAuditRecord
        from .search_audit_record import SearchAuditRecord
        from .security_compliance_alert_record import SecurityComplianceAlertRecord
        from .security_compliance_center_e_o_p_cmdlet_audit_record import SecurityComplianceCenterEOPCmdletAuditRecord
        from .security_compliance_insights_audit_record import SecurityComplianceInsightsAuditRecord
        from .security_compliance_r_b_a_c_audit_record import SecurityComplianceRBACAuditRecord
        from .security_compliance_user_change_audit_record import SecurityComplianceUserChangeAuditRecord
        from .security_copilot_identity_management_audit_record import SecurityCopilotIdentityManagementAuditRecord
        from .security_development_lifecycle_a_i_log_audit_record import SecurityDevelopmentLifecycleAILogAuditRecord
        from .sensitive_info_remediation_agent_data_record import SensitiveInfoRemediationAgentDataRecord
        from .sensitivity_labeled_file_action_audit_record import SensitivityLabeledFileActionAuditRecord
        from .sensitivity_label_action_audit_record import SensitivityLabelActionAuditRecord
        from .sensitivity_label_policy_match_audit_record import SensitivityLabelPolicyMatchAuditRecord
        from .sentinel_a_i_tool_audit_record import SentinelAIToolAuditRecord
        from .sentinel_graph_audit_record import SentinelGraphAuditRecord
        from .sentinel_job_audit_record import SentinelJobAuditRecord
        from .sentinel_k_q_l_on_lake_audit_record import SentinelKQLOnLakeAuditRecord
        from .sentinel_lake_data_onboarding_audit_record import SentinelLakeDataOnboardingAuditRecord
        from .sentinel_lake_encryption_audit_record import SentinelLakeEncryptionAuditRecord
        from .sentinel_lake_onboarding_audit_record import SentinelLakeOnboardingAuditRecord
        from .sentinel_notebook_on_lake_audit_record import SentinelNotebookOnLakeAuditRecord
        from .sentinel_package_audit_record import SentinelPackageAuditRecord
        from .share_point_app_permission_operation_audit_record import SharePointAppPermissionOperationAuditRecord
        from .share_point_audit_record import SharePointAuditRecord
        from .share_point_comment_operation_audit_record import SharePointCommentOperationAuditRecord
        from .share_point_content_security_policy_audit_record import SharePointContentSecurityPolicyAuditRecord
        from .share_point_content_type_operation_audit_record import SharePointContentTypeOperationAuditRecord
        from .share_point_e_signature_audit_record import SharePointESignatureAuditRecord
        from .share_point_field_operation_audit_record import SharePointFieldOperationAuditRecord
        from .share_point_file_operation_audit_record import SharePointFileOperationAuditRecord
        from .share_point_list_item_operation_audit_record import SharePointListItemOperationAuditRecord
        from .share_point_list_operation_audit_record import SharePointListOperationAuditRecord
        from .share_point_sharing_operation_audit_record import SharePointSharingOperationAuditRecord
        from .skype_for_business_cmdlets_audit_record import SkypeForBusinessCmdletsAuditRecord
        from .skype_for_business_p_s_t_n_usage_audit_record import SkypeForBusinessPSTNUsageAuditRecord
        from .skype_for_business_users_blocked_audit_record import SkypeForBusinessUsersBlockedAuditRecord
        from .sonar_detonation_content_metadata import SonarDetonationContentMetadata
        from .sonar_detonation_entity_audit_record import SonarDetonationEntityAuditRecord
        from .sonar_file_detonation_entity_audit_record import SonarFileDetonationEntityAuditRecord
        from .sonar_submission_entity_audit_record import SonarSubmissionEntityAuditRecord
        from .sonar_url_detonation_entity_audit_record import SonarUrlDetonationEntityAuditRecord
        from .spark_core_custom_live_pool_record import SparkCoreCustomLivePoolRecord
        from .submission_entity_audit_record import SubmissionEntityAuditRecord
        from .supervisory_review_day_x_insights_audit_record import SupervisoryReviewDayXInsightsAuditRecord
        from .synthetic_probe_audit_record import SyntheticProbeAuditRecord
        from .teams_easy_approvals_audit_record import TeamsEasyApprovalsAuditRecord
        from .teams_eval_data_hub_admin_operation_audit_record import TeamsEvalDataHubAdminOperationAuditRecord
        from .teams_eval_data_hub_data_access_audit_record import TeamsEvalDataHubDataAccessAuditRecord
        from .teams_eval_data_hub_permission_change_audit_record import TeamsEvalDataHubPermissionChangeAuditRecord
        from .teams_healthcare_audit_record import TeamsHealthcareAuditRecord
        from .teams_updates_audit_record import TeamsUpdatesAuditRecord
        from .team_copilot_interaction_audit_record import TeamCopilotInteractionAuditRecord
        from .tenant_allow_block_list_audit_record import TenantAllowBlockListAuditRecord
        from .threat_finder_audit_record import ThreatFinderAuditRecord
        from .threat_intelligence_atp_content_data import ThreatIntelligenceAtpContentData
        from .threat_intelligence_export_audit_record import ThreatIntelligenceExportAuditRecord
        from .threat_intelligence_mail_data import ThreatIntelligenceMailData
        from .threat_intelligence_object_audit_record import ThreatIntelligenceObjectAuditRecord
        from .threat_intelligence_url_click_data import ThreatIntelligenceUrlClickData
        from .todo_audit_record import TodoAuditRecord
        from .trainable_classifier_audit_record import TrainableClassifierAuditRecord
        from .uam_operation_audit_record import UamOperationAuditRecord
        from .unified_group_audit_record import UnifiedGroupAuditRecord
        from .unified_simulation_matched_item_audit_record import UnifiedSimulationMatchedItemAuditRecord
        from .unified_simulation_summary_audit_record import UnifiedSimulationSummaryAuditRecord
        from .universal_print_management_audit_record import UniversalPrintManagementAuditRecord
        from .universal_print_print_job_audit_record import UniversalPrintPrintJobAuditRecord
        from .urbac_assignment_audit_record import UrbacAssignmentAuditRecord
        from .urbac_enable_state_audit_record import UrbacEnableStateAuditRecord
        from .urbac_role_audit_record import UrbacRoleAuditRecord
        from .user_training_audit_record import UserTrainingAuditRecord
        from .usx_workspace_onboarding_audit_record import UsxWorkspaceOnboardingAuditRecord
        from .vfam_create_policy_audit_record import VfamCreatePolicyAuditRecord
        from .vfam_delete_policy_audit_record import VfamDeletePolicyAuditRecord
        from .vfam_update_policy_audit_record import VfamUpdatePolicyAuditRecord
        from .viva_amplify_audit_record import VivaAmplifyAuditRecord
        from .viva_engage_events_audit_record import VivaEngageEventsAuditRecord
        from .viva_engage_network_association_audit_record import VivaEngageNetworkAssociationAuditRecord
        from .viva_engage_segment_audit_record import VivaEngageSegmentAuditRecord
        from .viva_glint_advanced_configuration_audit_record import VivaGlintAdvancedConfigurationAuditRecord
        from .viva_glint_agentic_campaign_audit_record import VivaGlintAgenticCampaignAuditRecord
        from .viva_glint_feedback_program_audit_record import VivaGlintFeedbackProgramAuditRecord
        from .viva_glint_organizational_data_audit_record import VivaGlintOrganizationalDataAuditRecord
        from .viva_glint_pulse_program_audit_record import VivaGlintPulseProgramAuditRecord
        from .viva_glint_pulse_program_respondent_rate_audit_record import VivaGlintPulseProgramRespondentRateAuditRecord
        from .viva_glint_question_audit_record import VivaGlintQuestionAuditRecord
        from .viva_glint_role_audit_record import VivaGlintRoleAuditRecord
        from .viva_glint_rubicon_audit_record import VivaGlintRubiconAuditRecord
        from .viva_glint_support_access_audit_record import VivaGlintSupportAccessAuditRecord
        from .viva_glint_system_audit_record import VivaGlintSystemAuditRecord
        from .viva_glint_user_audit_record import VivaGlintUserAuditRecord
        from .viva_glint_user_group_audit_record import VivaGlintUserGroupAuditRecord
        from .viva_goals_audit_record import VivaGoalsAuditRecord
        from .viva_learning_admin_audit_record import VivaLearningAdminAuditRecord
        from .viva_learning_audit_record import VivaLearningAuditRecord
        from .viva_pulse_admin_audit_record import VivaPulseAdminAuditRecord
        from .viva_pulse_organizer_audit_record import VivaPulseOrganizerAuditRecord
        from .viva_pulse_report_audit_record import VivaPulseReportAuditRecord
        from .viva_pulse_response_audit_record import VivaPulseResponseAuditRecord
        from .wdatp_alerts_audit_record import WdatpAlertsAuditRecord
        from .web_content_filtering_audit_record import WebContentFilteringAuditRecord
        from .windows365_customer_lockbox_audit_record import Windows365CustomerLockboxAuditRecord
        from .workplace_analytics_audit_record import WorkplaceAnalyticsAuditRecord
        from .yammer_audit_record import YammerAuditRecord
        from .yammer_user_hiding_audit_record import YammerUserHidingAuditRecord

        from .a365_ai_execute_tool import A365AiExecuteTool
        from .a365_ai_inference_call import A365AiInferenceCall
        from .a365_ai_invoke_agent import A365AiInvokeAgent
        from .a365_ai_run_summary import A365AiRunSummary
        from .a365_span_outputs import A365SpanOutputs
        from .aad_risk_detection_audit_record import AadRiskDetectionAuditRecord
        from .aed_audit_record import AedAuditRecord
        from .agent_admin_activity_record import AgentAdminActivityRecord
        from .agent_setting_admin_activity import AgentSettingAdminActivity
        from .aip_discover import AipDiscover
        from .aip_file_deleted import AipFileDeleted
        from .aip_heart_beat import AipHeartBeat
        from .aip_protection_action_log_request import AipProtectionActionLogRequest
        from .aip_scanner_discover_event import AipScannerDiscoverEvent
        from .aip_sensitivity_label_action_log_request import AipSensitivityLabelActionLogRequest
        from .air_admin_action_investigation_data import AirAdminActionInvestigationData
        from .air_investigation_data import AirInvestigationData
        from .air_manual_investigation_data import AirManualInvestigationData
        from .ai_app_interaction_audit_record import AiAppInteractionAuditRecord
        from .ai_execute_tool_audit_record import AiExecuteToolAuditRecord
        from .ai_interactions_change_notification_audit_record import AiInteractionsChangeNotificationAuditRecord
        from .ai_interactions_export_audit_record import AiInteractionsExportAuditRecord
        from .ai_interactions_subscription_audit_record import AiInteractionsSubscriptionAuditRecord
        from .ai_invoke_agent_audit_record import AiInvokeAgentAuditRecord
        from .alert_submission_audit_record import AlertSubmissionAuditRecord
        from .alert_submission_result_detail_audit_record import AlertSubmissionResultDetailAuditRecord
        from .attack_sim_admin_audit_record import AttackSimAdminAuditRecord
        from .attack_sim_audit_record import AttackSimAuditRecord
        from .audit_config_audit_record import AuditConfigAuditRecord
        from .audit_record_type_dictionary import AuditRecordTypeDictionary
        from .audit_search_audit_record import AuditSearchAuditRecord
        from .azfw_application_rule_aggregation_event_record import AzfwApplicationRuleAggregationEventRecord
        from .azfw_dns_query_event_record import AzfwDnsQueryEventRecord
        from .azfw_network_rule_event_record import AzfwNetworkRuleEventRecord
        from .azure_active_directory_account_logon_audit_record import AzureActiveDirectoryAccountLogonAuditRecord
        from .azure_active_directory_audit_record import AzureActiveDirectoryAuditRecord
        from .azure_active_directory_sts_logon_audit_record import AzureActiveDirectoryStsLogonAuditRecord
        from .azure_a_i_search_audit_record import AzureAISearchAuditRecord
        from .a_i_span_outputs_audit_record import AISpanOutputsAuditRecord
        from .campaign_audit_record import CampaignAuditRecord
        from .ccrai_policy_violation_record import CcraiPolicyViolationRecord
        from .cdpdlmai_interaction_insights_record import CdpdlmaiInteractionInsightsRecord
        from .cdp_classifier_health_record import CdpClassifierHealthRecord
        from .cdp_cold_crawl_status_record import CdpColdCrawlStatusRecord
        from .cdp_consumption_resource_record import CdpConsumptionResourceRecord
        from .cdp_content_explorer_aggregate_record import CdpContentExplorerAggregateRecord
        from .cdp_dlp_sensitive_endpoint_audit_record import CdpDlpSensitiveEndpointAuditRecord
        from .cdp_log_record import CdpLogRecord
        from .cdp_ocr_billing_record import CdpOcrBillingRecord
        from .cdp_resource_scope_change_event_record import CdpResourceScopeChangeEventRecord
        from .cloud_update_device_config_audit_record import CloudUpdateDeviceConfigAuditRecord
        from .cloud_update_profile_config_audit_record import CloudUpdateProfileConfigAuditRecord
        from .cloud_update_tenant_config_audit_record import CloudUpdateTenantConfigAuditRecord
        from .compliance_connector_audit_record import ComplianceConnectorAuditRecord
        from .compliance_d_l_m_exchange_audit_record import ComplianceDLMExchangeAuditRecord
        from .compliance_d_l_m_share_point_audit_record import ComplianceDLMSharePointAuditRecord
        from .compliance_d_l_p_applications_audit_record import ComplianceDLPApplicationsAuditRecord
        from .compliance_d_l_p_applications_classification_audit_record import ComplianceDLPApplicationsClassificationAuditRecord
        from .compliance_d_l_p_endpoint_audit_record import ComplianceDLPEndpointAuditRecord
        from .compliance_d_l_p_endpoint_discovery_audit_record import ComplianceDLPEndpointDiscoveryAuditRecord
        from .compliance_d_l_p_enforcement_audit_record import ComplianceDLPEnforcementAuditRecord
        from .compliance_d_l_p_exchange_audit_record import ComplianceDLPExchangeAuditRecord
        from .compliance_d_l_p_exchange_classification_audit_record import ComplianceDLPExchangeClassificationAuditRecord
        from .compliance_d_l_p_exchange_classification_cdp_record import ComplianceDLPExchangeClassificationCdpRecord
        from .compliance_d_l_p_exchange_discovery_audit_record import ComplianceDLPExchangeDiscoveryAuditRecord
        from .compliance_d_l_p_share_point_audit_record import ComplianceDLPSharePointAuditRecord
        from .compliance_d_l_p_share_point_classification_audit_record import ComplianceDLPSharePointClassificationAuditRecord
        from .compliance_d_l_p_share_point_classification_cdp_record import ComplianceDLPSharePointClassificationCdpRecord
        from .compliance_d_l_p_share_point_classification_extended_audit_record import ComplianceDLPSharePointClassificationExtendedAuditRecord
        from .compliance_exchange_ocr_audit_record import ComplianceExchangeOcrAuditRecord
        from .compliance_manager_action_record import ComplianceManagerActionRecord
        from .compliance_policy_grading_share_point_audit_record import CompliancePolicyGradingSharePointAuditRecord
        from .compliance_settings_change_audit_record import ComplianceSettingsChangeAuditRecord
        from .compliance_sit_grading_share_point_audit_record import ComplianceSitGradingSharePointAuditRecord
        from .compliance_supervision_exchange_audit_record import ComplianceSupervisionExchangeAuditRecord
        from .connected_a_i_app_interaction_audit_record import ConnectedAIAppInteractionAuditRecord
        from .consumption_resource_audit_record import ConsumptionResourceAuditRecord
        from .content_store_metadata_record import ContentStoreMetadataRecord
        from .copilot_agent_management_audit_record import CopilotAgentManagementAuditRecord
        from .copilot_for_security_logging_audit_record import CopilotForSecurityLoggingAuditRecord
        from .copilot_for_security_trigger_audit_record import CopilotForSecurityTriggerAuditRecord
        from .copilot_interaction_audit_record import CopilotInteractionAuditRecord
        from .copilot_plugin_setting_audit_record import CopilotPluginSettingAuditRecord
        from .copilot_prompt_book_setting_audit_record import CopilotPromptBookSettingAuditRecord
        from .copilot_session_sharing_audit_record import CopilotSessionSharingAuditRecord
        from .copilot_setting_audit_record import CopilotSettingAuditRecord
        from .copilot_workspace_setting_audit_record import CopilotWorkspaceSettingAuditRecord
        from .core_reporting_settings_audit_record import CoreReportingSettingsAuditRecord
        from .cortana_briefing_audit_record import CortanaBriefingAuditRecord
        from .critical_asset_management_classification_record import CriticalAssetManagementClassificationRecord
        from .crm_entity_operation_audit_record import CrmEntityOperationAuditRecord
        from .cross_tenant_access_policy_audit_record import CrossTenantAccessPolicyAuditRecord
        from .customer_key_service_encryption_audit_record import CustomerKeyServiceEncryptionAuditRecord
        from .data_center_security_cmdlet_audit_record import DataCenterSecurityCmdletAuditRecord
        from .data_governance_audit_record import DataGovernanceAuditRecord
        from .data_insights_rest_api_audit_record import DataInsightsRestApiAuditRecord
        from .data_lake_export_operation_audit_record import DataLakeExportOperationAuditRecord
        from .data_security_investigation_audit_record import DataSecurityInvestigationAuditRecord
        from .data_share_operation_audit_record import DataShareOperationAuditRecord
        from .default_audit_data import DefaultAuditData
        from .defender_case_management_audit_record import DefenderCaseManagementAuditRecord
        from .defender_preview_features_record import DefenderPreviewFeaturesRecord
        from .defender_security_for_a_i_configuration_audit_record import DefenderSecurityForAIConfigurationAuditRecord
        from .deploy_feature_activity_record import DeployFeatureActivityRecord
        from .device_discovery_settings_authenticated_scans_record import DeviceDiscoverySettingsAuthenticatedScansRecord
        from .device_discovery_settings_exclusion_record import DeviceDiscoverySettingsExclusionRecord
        from .device_discovery_settings_record import DeviceDiscoverySettingsRecord
        from .discovery_audit_record import DiscoveryAuditRecord
        from .dlp_endpoint_audit_record import DlpEndpointAuditRecord
        from .dlp_import_result_audit_record import DlpImportResultAuditRecord
        from .dlp_sensitive_information_type_rule_package_cmdlet_record import DlpSensitiveInformationTypeRulePackageCmdletRecord
        from .dragon_copilot_access_record import DragonCopilotAccessRecord
        from .dragon_copilot_admin_record import DragonCopilotAdminRecord
        from .dragon_copilot_clinical_data_record import DragonCopilotClinicalDataRecord
        from .dragon_copilot_session_record import DragonCopilotSessionRecord
        from .dynamics365_business_central_audit_record import Dynamics365BusinessCentralAuditRecord
        from .ehr_connector_audit_base_record import EhrConnectorAuditBaseRecord
        from .eop_submission_feed_entity_audit_record import EopSubmissionFeedEntityAuditRecord
        from .exchange_admin_audit_record import ExchangeAdminAuditRecord
        from .exchange_aggregated_mailbox_audit_record import ExchangeAggregatedMailboxAuditRecord
        from .exchange_aggregated_operation_record import ExchangeAggregatedOperationRecord
        from .exchange_mailbox_audit_group_record import ExchangeMailboxAuditGroupRecord
        from .exchange_mailbox_audit_record import ExchangeMailboxAuditRecord
        from .fabric_audit_record import FabricAuditRecord
        from .fabric_policy_record import FabricPolicyRecord
        from .healthcare_signal_record import HealthcareSignalRecord
        from .hosted_rpa_audit_record import HostedRpaAuditRecord
        from .hr_signal_audit_record import HrSignalAuditRecord
        from .hygiene_event_record import HygieneEventRecord
        from .information_barrier_policy_application_audit_record import InformationBarrierPolicyApplicationAuditRecord
        from .information_worker_protection_audit_record import InformationWorkerProtectionAuditRecord
        from .insider_risk_scoped_users_record import InsiderRiskScopedUsersRecord
        from .insider_risk_scoped_user_insights_record import InsiderRiskScopedUserInsightsRecord
        from .integrated_apps_app_admin_activity_audit_record import IntegratedAppsAppAdminActivityAuditRecord
        from .integrated_apps_app_settings_admin_activity_audit_record import IntegratedAppsAppSettingsAdminActivityAuditRecord
        from .irm_activity_audit_trail_record import IrmActivityAuditTrailRecord
        from .irm_user_defined_detection_record import IrmUserDefinedDetectionRecord
        from .kaizala_audit_record import KaizalaAuditRecord
        from .label_analytics_aggregate_audit_record import LabelAnalyticsAggregateAuditRecord
        from .label_content_explorer_audit_record import LabelContentExplorerAuditRecord
        from .large_content_metadata_audit_record import LargeContentMetadataAuditRecord
        from .m365daad_audit_record import M365daadAuditRecord
        from .m365odsp_asset_metadata_record import M365odspAssetMetadataRecord
        from .m365_compliance_connector_audit_record import M365ComplianceConnectorAuditRecord
        from .m365_search_sections_record import M365SearchSectionsRecord
        from .mail_submission_data import MailSubmissionData
        from .managed_services_audit_record import ManagedServicesAuditRecord
        from .managed_tenants_audit_record import ManagedTenantsAuditRecord
        from .mapg_alerts_audit_record import MapgAlertsAuditRecord
        from .mapg_onboard_audit_record import MapgOnboardAuditRecord
        from .mapg_policy_audit_record import MapgPolicyAuditRecord
        from .mapg_remediation_audit_record import MapgRemediationAuditRecord
        from .mcas_alerts_audit_record import McasAlertsAuditRecord
        from .mdatp_audit_record import MdatpAuditRecord
        from .mda_audit_record import MdaAuditRecord
        from .mda_data_security_signal_record import MdaDataSecuritySignalRecord
        from .mdc_events_record import MdcEventsRecord
        from .mdi_audit_record import MdiAuditRecord
        from .mesh_worlds_audit_record import MeshWorldsAuditRecord
        from .microsoft365_backup_backup_item_audit_record import Microsoft365BackupBackupItemAuditRecord
        from .microsoft365_backup_backup_policy_audit_record import Microsoft365BackupBackupPolicyAuditRecord
        from .microsoft365_backup_granular_browse_task_audit_record import Microsoft365BackupGranularBrowseTaskAuditRecord
        from .microsoft365_backup_restore_item_audit_record import Microsoft365BackupRestoreItemAuditRecord
        from .microsoft365_backup_restore_task_audit_record import Microsoft365BackupRestoreTaskAuditRecord
        from .microsoft365_copilot_scheduled_prompt_audit_record import Microsoft365CopilotScheduledPromptAuditRecord
        from .microsoft_defender_experts_x_d_r_audit_record import MicrosoftDefenderExpertsXDRAuditRecord
        from .microsoft_flow_audit_record import MicrosoftFlowAuditRecord
        from .microsoft_forms_audit_record import MicrosoftFormsAuditRecord
        from .microsoft_graph_data_connect_consent import MicrosoftGraphDataConnectConsent
        from .microsoft_graph_data_connect_operation import MicrosoftGraphDataConnectOperation
        from .microsoft_purview_data_catalog_operation_record import MicrosoftPurviewDataCatalogOperationRecord
        from .microsoft_purview_data_map_operation_record import MicrosoftPurviewDataMapOperationRecord
        from .microsoft_purview_metadata_policy_operation_record import MicrosoftPurviewMetadataPolicyOperationRecord
        from .microsoft_purview_policy_operation_record import MicrosoftPurviewPolicyOperationRecord
        from .microsoft_purview_privacy_audit_event import MicrosoftPurviewPrivacyAuditEvent
        from .microsoft_purview_unified_catalog_operation_record import MicrosoftPurviewUnifiedCatalogOperationRecord
        from .microsoft_stream_audit_record import MicrosoftStreamAuditRecord
        from .microsoft_teams_admin_audit_record import MicrosoftTeamsAdminAuditRecord
        from .microsoft_teams_analytics_audit_record import MicrosoftTeamsAnalyticsAuditRecord
        from .microsoft_teams_audit_record import MicrosoftTeamsAuditRecord
        from .microsoft_teams_device_audit_record import MicrosoftTeamsDeviceAuditRecord
        from .microsoft_teams_retention_label_action_audit_record import MicrosoftTeamsRetentionLabelActionAuditRecord
        from .microsoft_teams_sensitivity_label_action_audit_record import MicrosoftTeamsSensitivityLabelActionAuditRecord
        from .microsoft_teams_shifts_audit_record import MicrosoftTeamsShiftsAuditRecord
        from .microsoft_teams_user_concern_audit_record import MicrosoftTeamsUserConcernAuditRecord
        from .mip_auto_label_exchange_item_audit_record import MipAutoLabelExchangeItemAuditRecord
        from .mip_auto_label_progress_feedback_audit_record import MipAutoLabelProgressFeedbackAuditRecord
        from .mip_auto_label_share_point_item_audit_record import MipAutoLabelSharePointItemAuditRecord
        from .mip_auto_label_share_point_policy_location_audit_record import MipAutoLabelSharePointPolicyLocationAuditRecord
        from .mip_auto_label_simulation_share_point_completion_record import MipAutoLabelSimulationSharePointCompletionRecord
        from .mip_auto_label_simulation_share_point_progress_record import MipAutoLabelSimulationSharePointProgressRecord
        from .mip_auto_label_simulation_statistics_record import MipAutoLabelSimulationStatisticsRecord
        from .mip_exact_data_match_audit_record import MipExactDataMatchAuditRecord
        from .mip_label_analytics_audit_record import MipLabelAnalyticsAuditRecord
        from .mip_label_audit_record import MipLabelAuditRecord
        from .mos_agent_info_record import MosAgentInfoRecord
        from .mos_agent_info_record_v2 import MosAgentInfoRecordV2
        from .ms365d_custom_detection_audit_record import Ms365dCustomDetectionAuditRecord
        from .ms365d_incident_audit_record import Ms365dIncidentAuditRecord
        from .ms365d_suppression_rule_audit_record import Ms365dSuppressionRuleAuditRecord
        from .msde_custom_collection_audit_record import MsdeCustomCollectionAuditRecord
        from .msde_general_settings_audit_record import MsdeGeneralSettingsAuditRecord
        from .msde_indicators_settings_audit_record import MsdeIndicatorsSettingsAuditRecord
        from .msde_response_actions_audit_record import MsdeResponseActionsAuditRecord
        from .msde_roles_settings_audit_record import MsdeRolesSettingsAuditRecord
        from .msp_vector_search_content_metadata_audit_record import MspVectorSearchContentMetadataAuditRecord
        from .mstic_nation_state_notification_record import MsticNationStateNotificationRecord
        from .multi_stage_disposition_audit_record import MultiStageDispositionAuditRecord
        from .my_analytics_settings_audit_record import MyAnalyticsSettingsAuditRecord
        from .m_d_a_s_h_audit_record import MDASHAuditRecord
        from .noisy_alert_policy_audit_record import NoisyAlertPolicyAuditRecord
        from .office_native_audit_record import OfficeNativeAuditRecord
        from .ome_portal_audit_record import OmePortalAuditRecord
        from .one_drive_audit_record import OneDriveAuditRecord
        from .on_demand_share_point_classification_audit_record import OnDemandSharePointClassificationAuditRecord
        from .on_premises_file_share_scanner_d_l_p_audit_record import OnPremisesFileShareScannerDLPAuditRecord
        from .on_premises_share_point_scanner_d_l_p_audit_record import OnPremisesSharePointScannerDLPAuditRecord
        from .organizational_data_in_m365_audit_record import OrganizationalDataInM365AuditRecord
        from .outlook_copilot_automation_audit_record import OutlookCopilotAutomationAuditRecord
        from .owa_get_access_token_for_resource_audit_record import OwaGetAccessTokenForResourceAuditRecord
        from .p4ai_assessment_category_record import P4aiAssessmentCategoryRecord
        from .p4ai_assessment_fabric_scanner_record import P4aiAssessmentFabricScannerRecord
        from .p4ai_assessment_location_result_record import P4aiAssessmentLocationResultRecord
        from .p4ai_assessment_record import P4aiAssessmentRecord
        from .p4_a_i_risk_score_record import P4AIRiskScoreRecord
        from .people_admin_settings_audit_record import PeopleAdminSettingsAuditRecord
        from .physical_badging_signal_audit_record import PhysicalBadgingSignalAuditRecord
        from .places_directory_audit_record import PlacesDirectoryAuditRecord
        from .planner_chat_message_audit_record import PlannerChatMessageAuditRecord
        from .planner_chat_message_list_audit_record import PlannerChatMessageListAuditRecord
        from .planner_copy_plan_audit_record import PlannerCopyPlanAuditRecord
        from .planner_goal_audit_record import PlannerGoalAuditRecord
        from .planner_goal_list_audit_record import PlannerGoalListAuditRecord
        from .planner_plan_audit_record import PlannerPlanAuditRecord
        from .planner_plan_list_audit_record import PlannerPlanListAuditRecord
        from .planner_plan_sensitivity_label_audit_record import PlannerPlanSensitivityLabelAuditRecord
        from .planner_roster_audit_record import PlannerRosterAuditRecord
        from .planner_roster_sensitivity_label_audit_record import PlannerRosterSensitivityLabelAuditRecord
        from .planner_task_audit_record import PlannerTaskAuditRecord
        from .planner_task_list_audit_record import PlannerTaskListAuditRecord
        from .planner_tenant_settings_audit_record import PlannerTenantSettingsAuditRecord
        from .policy_config_change_audit_record import PolicyConfigChangeAuditRecord
        from .power_apps_audit_app_record import PowerAppsAuditAppRecord
        from .power_apps_audit_plan_record import PowerAppsAuditPlanRecord
        from .power_apps_audit_resource_record import PowerAppsAuditResourceRecord
        from .power_b_i_audit_record import PowerBIAuditRecord
        from .power_b_i_dlp_audit_record import PowerBIDlpAuditRecord
        from .power_pages_site_audit_record import PowerPagesSiteAuditRecord
        from .power_platform_administrator_activity_record import PowerPlatformAdministratorActivityRecord
        from .power_platform_admin_dlp_audit_record import PowerPlatformAdminDlpAuditRecord
        from .power_platform_admin_environment_audit_record import PowerPlatformAdminEnvironmentAuditRecord
        from .power_platform_lockbox_resource_access_request_audit_record import PowerPlatformLockboxResourceAccessRequestAuditRecord
        from .power_platform_lockbox_resource_command_audit_record import PowerPlatformLockboxResourceCommandAuditRecord
        from .power_platform_service_activity_audit_record import PowerPlatformServiceActivityAuditRecord
        from .power_platform_tenant_isolation_record import PowerPlatformTenantIsolationRecord
        from .privacy_data_match_audit_record import PrivacyDataMatchAuditRecord
        from .privacy_data_minimization_record import PrivacyDataMinimizationRecord
        from .privacy_digest_email_record import PrivacyDigestEmailRecord
        from .privacy_open_access_audit_record import PrivacyOpenAccessAuditRecord
        from .privacy_portal_audit_record import PrivacyPortalAuditRecord
        from .privacy_remediation_action_record import PrivacyRemediationActionRecord
        from .privacy_remediation_record import PrivacyRemediationRecord
        from .priva_privacy_assessment_operation_record import PrivaPrivacyAssessmentOperationRecord
        from .priva_privacy_consent_operation_record import PrivaPrivacyConsentOperationRecord
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
        from .purview_m_c_recommendation_record import PurviewMCRecommendationRecord
        from .purview_posture_agent_audit_record import PurviewPostureAgentAuditRecord
        from .quarantine_audit_record import QuarantineAuditRecord
        from .records_management_audit_record import RecordsManagementAuditRecord
        from .report_submission import ReportSubmission
        from .report_submission_result_detail import ReportSubmissionResultDetail
        from .restricted_mode_audit_record import RestrictedModeAuditRecord
        from .retention_policy_audit_record import RetentionPolicyAuditRecord
        from .rti_operations_agent_audit_record import RtiOperationsAgentAuditRecord
        from .sbp_configuration_event_record import SbpConfigurationEventRecord
        from .sbp_usage_event_record import SbpUsageEventRecord
        from .score_evidence import ScoreEvidence
        from .score_platform_generic_audit_record import ScorePlatformGenericAuditRecord
        from .script_run_audit_record import ScriptRunAuditRecord
        from .search_audit_record import SearchAuditRecord
        from .security_compliance_alert_record import SecurityComplianceAlertRecord
        from .security_compliance_center_e_o_p_cmdlet_audit_record import SecurityComplianceCenterEOPCmdletAuditRecord
        from .security_compliance_insights_audit_record import SecurityComplianceInsightsAuditRecord
        from .security_compliance_r_b_a_c_audit_record import SecurityComplianceRBACAuditRecord
        from .security_compliance_user_change_audit_record import SecurityComplianceUserChangeAuditRecord
        from .security_copilot_identity_management_audit_record import SecurityCopilotIdentityManagementAuditRecord
        from .security_development_lifecycle_a_i_log_audit_record import SecurityDevelopmentLifecycleAILogAuditRecord
        from .sensitive_info_remediation_agent_data_record import SensitiveInfoRemediationAgentDataRecord
        from .sensitivity_labeled_file_action_audit_record import SensitivityLabeledFileActionAuditRecord
        from .sensitivity_label_action_audit_record import SensitivityLabelActionAuditRecord
        from .sensitivity_label_policy_match_audit_record import SensitivityLabelPolicyMatchAuditRecord
        from .sentinel_a_i_tool_audit_record import SentinelAIToolAuditRecord
        from .sentinel_graph_audit_record import SentinelGraphAuditRecord
        from .sentinel_job_audit_record import SentinelJobAuditRecord
        from .sentinel_k_q_l_on_lake_audit_record import SentinelKQLOnLakeAuditRecord
        from .sentinel_lake_data_onboarding_audit_record import SentinelLakeDataOnboardingAuditRecord
        from .sentinel_lake_encryption_audit_record import SentinelLakeEncryptionAuditRecord
        from .sentinel_lake_onboarding_audit_record import SentinelLakeOnboardingAuditRecord
        from .sentinel_notebook_on_lake_audit_record import SentinelNotebookOnLakeAuditRecord
        from .sentinel_package_audit_record import SentinelPackageAuditRecord
        from .share_point_app_permission_operation_audit_record import SharePointAppPermissionOperationAuditRecord
        from .share_point_audit_record import SharePointAuditRecord
        from .share_point_comment_operation_audit_record import SharePointCommentOperationAuditRecord
        from .share_point_content_security_policy_audit_record import SharePointContentSecurityPolicyAuditRecord
        from .share_point_content_type_operation_audit_record import SharePointContentTypeOperationAuditRecord
        from .share_point_e_signature_audit_record import SharePointESignatureAuditRecord
        from .share_point_field_operation_audit_record import SharePointFieldOperationAuditRecord
        from .share_point_file_operation_audit_record import SharePointFileOperationAuditRecord
        from .share_point_list_item_operation_audit_record import SharePointListItemOperationAuditRecord
        from .share_point_list_operation_audit_record import SharePointListOperationAuditRecord
        from .share_point_sharing_operation_audit_record import SharePointSharingOperationAuditRecord
        from .skype_for_business_cmdlets_audit_record import SkypeForBusinessCmdletsAuditRecord
        from .skype_for_business_p_s_t_n_usage_audit_record import SkypeForBusinessPSTNUsageAuditRecord
        from .skype_for_business_users_blocked_audit_record import SkypeForBusinessUsersBlockedAuditRecord
        from .sonar_detonation_content_metadata import SonarDetonationContentMetadata
        from .sonar_detonation_entity_audit_record import SonarDetonationEntityAuditRecord
        from .sonar_file_detonation_entity_audit_record import SonarFileDetonationEntityAuditRecord
        from .sonar_submission_entity_audit_record import SonarSubmissionEntityAuditRecord
        from .sonar_url_detonation_entity_audit_record import SonarUrlDetonationEntityAuditRecord
        from .spark_core_custom_live_pool_record import SparkCoreCustomLivePoolRecord
        from .submission_entity_audit_record import SubmissionEntityAuditRecord
        from .supervisory_review_day_x_insights_audit_record import SupervisoryReviewDayXInsightsAuditRecord
        from .synthetic_probe_audit_record import SyntheticProbeAuditRecord
        from .teams_easy_approvals_audit_record import TeamsEasyApprovalsAuditRecord
        from .teams_eval_data_hub_admin_operation_audit_record import TeamsEvalDataHubAdminOperationAuditRecord
        from .teams_eval_data_hub_data_access_audit_record import TeamsEvalDataHubDataAccessAuditRecord
        from .teams_eval_data_hub_permission_change_audit_record import TeamsEvalDataHubPermissionChangeAuditRecord
        from .teams_healthcare_audit_record import TeamsHealthcareAuditRecord
        from .teams_updates_audit_record import TeamsUpdatesAuditRecord
        from .team_copilot_interaction_audit_record import TeamCopilotInteractionAuditRecord
        from .tenant_allow_block_list_audit_record import TenantAllowBlockListAuditRecord
        from .threat_finder_audit_record import ThreatFinderAuditRecord
        from .threat_intelligence_atp_content_data import ThreatIntelligenceAtpContentData
        from .threat_intelligence_export_audit_record import ThreatIntelligenceExportAuditRecord
        from .threat_intelligence_mail_data import ThreatIntelligenceMailData
        from .threat_intelligence_object_audit_record import ThreatIntelligenceObjectAuditRecord
        from .threat_intelligence_url_click_data import ThreatIntelligenceUrlClickData
        from .todo_audit_record import TodoAuditRecord
        from .trainable_classifier_audit_record import TrainableClassifierAuditRecord
        from .uam_operation_audit_record import UamOperationAuditRecord
        from .unified_group_audit_record import UnifiedGroupAuditRecord
        from .unified_simulation_matched_item_audit_record import UnifiedSimulationMatchedItemAuditRecord
        from .unified_simulation_summary_audit_record import UnifiedSimulationSummaryAuditRecord
        from .universal_print_management_audit_record import UniversalPrintManagementAuditRecord
        from .universal_print_print_job_audit_record import UniversalPrintPrintJobAuditRecord
        from .urbac_assignment_audit_record import UrbacAssignmentAuditRecord
        from .urbac_enable_state_audit_record import UrbacEnableStateAuditRecord
        from .urbac_role_audit_record import UrbacRoleAuditRecord
        from .user_training_audit_record import UserTrainingAuditRecord
        from .usx_workspace_onboarding_audit_record import UsxWorkspaceOnboardingAuditRecord
        from .vfam_create_policy_audit_record import VfamCreatePolicyAuditRecord
        from .vfam_delete_policy_audit_record import VfamDeletePolicyAuditRecord
        from .vfam_update_policy_audit_record import VfamUpdatePolicyAuditRecord
        from .viva_amplify_audit_record import VivaAmplifyAuditRecord
        from .viva_engage_events_audit_record import VivaEngageEventsAuditRecord
        from .viva_engage_network_association_audit_record import VivaEngageNetworkAssociationAuditRecord
        from .viva_engage_segment_audit_record import VivaEngageSegmentAuditRecord
        from .viva_glint_advanced_configuration_audit_record import VivaGlintAdvancedConfigurationAuditRecord
        from .viva_glint_agentic_campaign_audit_record import VivaGlintAgenticCampaignAuditRecord
        from .viva_glint_feedback_program_audit_record import VivaGlintFeedbackProgramAuditRecord
        from .viva_glint_organizational_data_audit_record import VivaGlintOrganizationalDataAuditRecord
        from .viva_glint_pulse_program_audit_record import VivaGlintPulseProgramAuditRecord
        from .viva_glint_pulse_program_respondent_rate_audit_record import VivaGlintPulseProgramRespondentRateAuditRecord
        from .viva_glint_question_audit_record import VivaGlintQuestionAuditRecord
        from .viva_glint_role_audit_record import VivaGlintRoleAuditRecord
        from .viva_glint_rubicon_audit_record import VivaGlintRubiconAuditRecord
        from .viva_glint_support_access_audit_record import VivaGlintSupportAccessAuditRecord
        from .viva_glint_system_audit_record import VivaGlintSystemAuditRecord
        from .viva_glint_user_audit_record import VivaGlintUserAuditRecord
        from .viva_glint_user_group_audit_record import VivaGlintUserGroupAuditRecord
        from .viva_goals_audit_record import VivaGoalsAuditRecord
        from .viva_learning_admin_audit_record import VivaLearningAdminAuditRecord
        from .viva_learning_audit_record import VivaLearningAuditRecord
        from .viva_pulse_admin_audit_record import VivaPulseAdminAuditRecord
        from .viva_pulse_organizer_audit_record import VivaPulseOrganizerAuditRecord
        from .viva_pulse_report_audit_record import VivaPulseReportAuditRecord
        from .viva_pulse_response_audit_record import VivaPulseResponseAuditRecord
        from .wdatp_alerts_audit_record import WdatpAlertsAuditRecord
        from .web_content_filtering_audit_record import WebContentFilteringAuditRecord
        from .windows365_customer_lockbox_audit_record import Windows365CustomerLockboxAuditRecord
        from .workplace_analytics_audit_record import WorkplaceAnalyticsAuditRecord
        from .yammer_audit_record import YammerAuditRecord
        from .yammer_user_hiding_audit_record import YammerUserHidingAuditRecord

        fields: dict[str, Callable[[Any], None]] = {
            "dynamicProperties": lambda n : setattr(self, 'dynamic_properties', n.get_object_value(AuditRecordTypeDictionary)),
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
        writer.write_object_value("dynamicProperties", self.dynamic_properties)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

