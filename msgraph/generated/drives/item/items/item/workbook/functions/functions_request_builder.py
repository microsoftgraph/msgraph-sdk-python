from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

abs_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.abs.abs_request_builder')
accr_int_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.accr_int.accr_int_request_builder')
accr_int_m_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.accr_int_m.accr_int_m_request_builder')
acos_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.acos.acos_request_builder')
acosh_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.acosh.acosh_request_builder')
acot_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.acot.acot_request_builder')
acoth_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.acoth.acoth_request_builder')
amor_degrc_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.amor_degrc.amor_degrc_request_builder')
amor_linc_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.amor_linc.amor_linc_request_builder')
and_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.and_.and_request_builder')
arabic_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.arabic.arabic_request_builder')
areas_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.areas.areas_request_builder')
asc_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.asc.asc_request_builder')
asin_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.asin.asin_request_builder')
asinh_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.asinh.asinh_request_builder')
atan_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.atan.atan_request_builder')
atan2_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.atan2.atan2_request_builder')
atanh_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.atanh.atanh_request_builder')
ave_dev_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.ave_dev.ave_dev_request_builder')
average_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.average.average_request_builder')
average_a_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.average_a.average_a_request_builder')
average_if_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.average_if.average_if_request_builder')
average_ifs_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.average_ifs.average_ifs_request_builder')
baht_text_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.baht_text.baht_text_request_builder')
base_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.base.base_request_builder')
bessel_i_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.bessel_i.bessel_i_request_builder')
bessel_j_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.bessel_j.bessel_j_request_builder')
bessel_k_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.bessel_k.bessel_k_request_builder')
bessel_y_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.bessel_y.bessel_y_request_builder')
beta_dist_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.beta_dist.beta_dist_request_builder')
beta_inv_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.beta_inv.beta_inv_request_builder')
bin2_dec_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.bin2_dec.bin2_dec_request_builder')
bin2_hex_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.bin2_hex.bin2_hex_request_builder')
bin2_oct_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.bin2_oct.bin2_oct_request_builder')
binom_dist_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.binom_dist.binom_dist_request_builder')
binom_dist_range_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.binom_dist_range.binom_dist_range_request_builder')
binom_inv_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.binom_inv.binom_inv_request_builder')
bitand_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.bitand.bitand_request_builder')
bitlshift_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.bitlshift.bitlshift_request_builder')
bitor_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.bitor.bitor_request_builder')
bitrshift_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.bitrshift.bitrshift_request_builder')
bitxor_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.bitxor.bitxor_request_builder')
ceiling_math_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.ceiling_math.ceiling_math_request_builder')
ceiling_precise_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.ceiling_precise.ceiling_precise_request_builder')
char_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.char.char_request_builder')
chi_sq_dist_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.chi_sq_dist.chi_sq_dist_request_builder')
chi_sq_dist_r_t_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.chi_sq_dist_r_t.chi_sq_dist_r_t_request_builder')
chi_sq_inv_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.chi_sq_inv.chi_sq_inv_request_builder')
chi_sq_inv_r_t_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.chi_sq_inv_r_t.chi_sq_inv_r_t_request_builder')
choose_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.choose.choose_request_builder')
clean_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.clean.clean_request_builder')
code_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.code.code_request_builder')
columns_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.columns.columns_request_builder')
combin_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.combin.combin_request_builder')
combina_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.combina.combina_request_builder')
complex_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.complex.complex_request_builder')
concatenate_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.concatenate.concatenate_request_builder')
confidence_norm_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.confidence_norm.confidence_norm_request_builder')
confidence_t_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.confidence_t.confidence_t_request_builder')
convert_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.convert.convert_request_builder')
cos_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.cos.cos_request_builder')
cosh_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.cosh.cosh_request_builder')
cot_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.cot.cot_request_builder')
coth_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.coth.coth_request_builder')
count_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.count.count_request_builder')
count_a_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.count_a.count_a_request_builder')
count_blank_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.count_blank.count_blank_request_builder')
count_if_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.count_if.count_if_request_builder')
count_ifs_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.count_ifs.count_ifs_request_builder')
coup_day_bs_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.coup_day_bs.coup_day_bs_request_builder')
coup_days_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.coup_days.coup_days_request_builder')
coup_days_nc_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.coup_days_nc.coup_days_nc_request_builder')
coup_ncd_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.coup_ncd.coup_ncd_request_builder')
coup_num_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.coup_num.coup_num_request_builder')
coup_pcd_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.coup_pcd.coup_pcd_request_builder')
csc_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.csc.csc_request_builder')
csch_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.csch.csch_request_builder')
cum_i_pmt_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.cum_i_pmt.cum_i_pmt_request_builder')
cum_princ_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.cum_princ.cum_princ_request_builder')
date_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.date.date_request_builder')
datevalue_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.datevalue.datevalue_request_builder')
daverage_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.daverage.daverage_request_builder')
day_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.day.day_request_builder')
days_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.days.days_request_builder')
days360_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.days360.days360_request_builder')
db_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.db.db_request_builder')
dbcs_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.dbcs.dbcs_request_builder')
dcount_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.dcount.dcount_request_builder')
dcount_a_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.dcount_a.dcount_a_request_builder')
ddb_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.ddb.ddb_request_builder')
dec2_bin_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.dec2_bin.dec2_bin_request_builder')
dec2_hex_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.dec2_hex.dec2_hex_request_builder')
dec2_oct_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.dec2_oct.dec2_oct_request_builder')
decimal_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.decimal.decimal_request_builder')
degrees_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.degrees.degrees_request_builder')
delta_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.delta.delta_request_builder')
dev_sq_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.dev_sq.dev_sq_request_builder')
dget_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.dget.dget_request_builder')
disc_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.disc.disc_request_builder')
dmax_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.dmax.dmax_request_builder')
dmin_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.dmin.dmin_request_builder')
dollar_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.dollar.dollar_request_builder')
dollar_de_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.dollar_de.dollar_de_request_builder')
dollar_fr_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.dollar_fr.dollar_fr_request_builder')
dproduct_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.dproduct.dproduct_request_builder')
dst_dev_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.dst_dev.dst_dev_request_builder')
dst_dev_p_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.dst_dev_p.dst_dev_p_request_builder')
dsum_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.dsum.dsum_request_builder')
duration_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.duration.duration_request_builder')
dvar_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.dvar.dvar_request_builder')
dvar_p_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.dvar_p.dvar_p_request_builder')
ecma_ceiling_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.ecma_ceiling.ecma_ceiling_request_builder')
edate_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.edate.edate_request_builder')
effect_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.effect.effect_request_builder')
eo_month_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.eo_month.eo_month_request_builder')
erf_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.erf.erf_request_builder')
erf_precise_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.erf_precise.erf_precise_request_builder')
erf_c_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.erf_c.erf_c_request_builder')
erf_c_precise_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.erf_c_precise.erf_c_precise_request_builder')
error_type_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.error_type.error_type_request_builder')
even_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.even.even_request_builder')
exact_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.exact.exact_request_builder')
exp_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.exp.exp_request_builder')
expon_dist_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.expon_dist.expon_dist_request_builder')
f_dist_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.f_dist.f_dist_request_builder')
f_dist_r_t_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.f_dist_r_t.f_dist_r_t_request_builder')
f_inv_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.f_inv.f_inv_request_builder')
f_inv_r_t_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.f_inv_r_t.f_inv_r_t_request_builder')
fact_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.fact.fact_request_builder')
fact_double_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.fact_double.fact_double_request_builder')
false_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.false_.false_request_builder')
find_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.find.find_request_builder')
find_b_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.find_b.find_b_request_builder')
fisher_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.fisher.fisher_request_builder')
fisher_inv_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.fisher_inv.fisher_inv_request_builder')
fixed_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.fixed.fixed_request_builder')
floor_math_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.floor_math.floor_math_request_builder')
floor_precise_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.floor_precise.floor_precise_request_builder')
fv_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.fv.fv_request_builder')
fvschedule_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.fvschedule.fvschedule_request_builder')
gamma_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.gamma.gamma_request_builder')
gamma_dist_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.gamma_dist.gamma_dist_request_builder')
gamma_inv_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.gamma_inv.gamma_inv_request_builder')
gamma_ln_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.gamma_ln.gamma_ln_request_builder')
gamma_ln_precise_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.gamma_ln_precise.gamma_ln_precise_request_builder')
gauss_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.gauss.gauss_request_builder')
gcd_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.gcd.gcd_request_builder')
geo_mean_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.geo_mean.geo_mean_request_builder')
ge_step_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.ge_step.ge_step_request_builder')
har_mean_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.har_mean.har_mean_request_builder')
hex2_bin_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.hex2_bin.hex2_bin_request_builder')
hex2_dec_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.hex2_dec.hex2_dec_request_builder')
hex2_oct_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.hex2_oct.hex2_oct_request_builder')
hlookup_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.hlookup.hlookup_request_builder')
hour_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.hour.hour_request_builder')
hyperlink_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.hyperlink.hyperlink_request_builder')
hyp_geom_dist_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.hyp_geom_dist.hyp_geom_dist_request_builder')
if_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.if_.if_request_builder')
im_abs_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.im_abs.im_abs_request_builder')
imaginary_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.imaginary.imaginary_request_builder')
im_argument_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.im_argument.im_argument_request_builder')
im_conjugate_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.im_conjugate.im_conjugate_request_builder')
im_cos_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.im_cos.im_cos_request_builder')
im_cosh_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.im_cosh.im_cosh_request_builder')
im_cot_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.im_cot.im_cot_request_builder')
im_csc_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.im_csc.im_csc_request_builder')
im_csch_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.im_csch.im_csch_request_builder')
im_div_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.im_div.im_div_request_builder')
im_exp_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.im_exp.im_exp_request_builder')
im_ln_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.im_ln.im_ln_request_builder')
im_log10_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.im_log10.im_log10_request_builder')
im_log2_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.im_log2.im_log2_request_builder')
im_power_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.im_power.im_power_request_builder')
im_product_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.im_product.im_product_request_builder')
im_real_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.im_real.im_real_request_builder')
im_sec_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.im_sec.im_sec_request_builder')
im_sech_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.im_sech.im_sech_request_builder')
im_sin_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.im_sin.im_sin_request_builder')
im_sinh_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.im_sinh.im_sinh_request_builder')
im_sqrt_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.im_sqrt.im_sqrt_request_builder')
im_sub_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.im_sub.im_sub_request_builder')
im_sum_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.im_sum.im_sum_request_builder')
im_tan_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.im_tan.im_tan_request_builder')
int_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.int.int_request_builder')
int_rate_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.int_rate.int_rate_request_builder')
ipmt_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.ipmt.ipmt_request_builder')
irr_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.irr.irr_request_builder')
is_err_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.is_err.is_err_request_builder')
is_error_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.is_error.is_error_request_builder')
is_even_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.is_even.is_even_request_builder')
is_formula_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.is_formula.is_formula_request_builder')
is_logical_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.is_logical.is_logical_request_builder')
is_n_a_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.is_n_a.is_n_a_request_builder')
is_non_text_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.is_non_text.is_non_text_request_builder')
is_number_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.is_number.is_number_request_builder')
iso_ceiling_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.iso_ceiling.iso_ceiling_request_builder')
is_odd_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.is_odd.is_odd_request_builder')
iso_week_num_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.iso_week_num.iso_week_num_request_builder')
ispmt_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.ispmt.ispmt_request_builder')
isref_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.isref.isref_request_builder')
is_text_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.is_text.is_text_request_builder')
kurt_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.kurt.kurt_request_builder')
large_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.large.large_request_builder')
lcm_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.lcm.lcm_request_builder')
left_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.left.left_request_builder')
leftb_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.leftb.leftb_request_builder')
len_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.len.len_request_builder')
lenb_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.lenb.lenb_request_builder')
ln_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.ln.ln_request_builder')
log_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.log.log_request_builder')
log10_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.log10.log10_request_builder')
log_norm_dist_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.log_norm_dist.log_norm_dist_request_builder')
log_norm_inv_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.log_norm_inv.log_norm_inv_request_builder')
lookup_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.lookup.lookup_request_builder')
lower_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.lower.lower_request_builder')
match_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.match.match_request_builder')
max_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.max.max_request_builder')
max_a_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.max_a.max_a_request_builder')
mduration_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.mduration.mduration_request_builder')
median_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.median.median_request_builder')
mid_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.mid.mid_request_builder')
midb_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.midb.midb_request_builder')
min_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.min.min_request_builder')
min_a_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.min_a.min_a_request_builder')
minute_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.minute.minute_request_builder')
mirr_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.mirr.mirr_request_builder')
mod_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.mod.mod_request_builder')
month_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.month.month_request_builder')
mround_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.mround.mround_request_builder')
multi_nomial_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.multi_nomial.multi_nomial_request_builder')
n_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.n.n_request_builder')
na_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.na.na_request_builder')
neg_binom_dist_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.neg_binom_dist.neg_binom_dist_request_builder')
network_days_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.network_days.network_days_request_builder')
network_days_intl_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.network_days_intl.network_days_intl_request_builder')
nominal_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.nominal.nominal_request_builder')
norm_dist_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.norm_dist.norm_dist_request_builder')
norm_inv_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.norm_inv.norm_inv_request_builder')
norm_s_dist_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.norm_s_dist.norm_s_dist_request_builder')
norm_s_inv_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.norm_s_inv.norm_s_inv_request_builder')
not_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.not_.not_request_builder')
now_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.now.now_request_builder')
nper_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.nper.nper_request_builder')
npv_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.npv.npv_request_builder')
number_value_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.number_value.number_value_request_builder')
oct2_bin_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.oct2_bin.oct2_bin_request_builder')
oct2_dec_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.oct2_dec.oct2_dec_request_builder')
oct2_hex_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.oct2_hex.oct2_hex_request_builder')
odd_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.odd.odd_request_builder')
odd_f_price_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.odd_f_price.odd_f_price_request_builder')
odd_f_yield_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.odd_f_yield.odd_f_yield_request_builder')
odd_l_price_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.odd_l_price.odd_l_price_request_builder')
odd_l_yield_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.odd_l_yield.odd_l_yield_request_builder')
or_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.or_.or_request_builder')
pduration_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.pduration.pduration_request_builder')
percentile_exc_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.percentile_exc.percentile_exc_request_builder')
percentile_inc_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.percentile_inc.percentile_inc_request_builder')
percent_rank_exc_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.percent_rank_exc.percent_rank_exc_request_builder')
percent_rank_inc_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.percent_rank_inc.percent_rank_inc_request_builder')
permut_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.permut.permut_request_builder')
permutationa_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.permutationa.permutationa_request_builder')
phi_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.phi.phi_request_builder')
pi_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.pi.pi_request_builder')
pmt_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.pmt.pmt_request_builder')
poisson_dist_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.poisson_dist.poisson_dist_request_builder')
power_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.power.power_request_builder')
ppmt_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.ppmt.ppmt_request_builder')
price_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.price.price_request_builder')
price_disc_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.price_disc.price_disc_request_builder')
price_mat_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.price_mat.price_mat_request_builder')
product_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.product.product_request_builder')
proper_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.proper.proper_request_builder')
pv_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.pv.pv_request_builder')
quartile_exc_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.quartile_exc.quartile_exc_request_builder')
quartile_inc_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.quartile_inc.quartile_inc_request_builder')
quotient_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.quotient.quotient_request_builder')
radians_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.radians.radians_request_builder')
rand_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.rand.rand_request_builder')
rand_between_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.rand_between.rand_between_request_builder')
rank_avg_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.rank_avg.rank_avg_request_builder')
rank_eq_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.rank_eq.rank_eq_request_builder')
rate_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.rate.rate_request_builder')
received_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.received.received_request_builder')
replace_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.replace.replace_request_builder')
replace_b_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.replace_b.replace_b_request_builder')
rept_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.rept.rept_request_builder')
right_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.right.right_request_builder')
rightb_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.rightb.rightb_request_builder')
roman_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.roman.roman_request_builder')
round_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.round.round_request_builder')
round_down_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.round_down.round_down_request_builder')
round_up_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.round_up.round_up_request_builder')
rows_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.rows.rows_request_builder')
rri_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.rri.rri_request_builder')
sec_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.sec.sec_request_builder')
sech_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.sech.sech_request_builder')
second_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.second.second_request_builder')
series_sum_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.series_sum.series_sum_request_builder')
sheet_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.sheet.sheet_request_builder')
sheets_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.sheets.sheets_request_builder')
sign_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.sign.sign_request_builder')
sin_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.sin.sin_request_builder')
sinh_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.sinh.sinh_request_builder')
skew_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.skew.skew_request_builder')
skew_p_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.skew_p.skew_p_request_builder')
sln_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.sln.sln_request_builder')
small_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.small.small_request_builder')
sqrt_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.sqrt.sqrt_request_builder')
sqrt_pi_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.sqrt_pi.sqrt_pi_request_builder')
standardize_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.standardize.standardize_request_builder')
st_dev_p_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.st_dev_p.st_dev_p_request_builder')
st_dev_s_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.st_dev_s.st_dev_s_request_builder')
st_dev_a_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.st_dev_a.st_dev_a_request_builder')
st_dev_p_a_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.st_dev_p_a.st_dev_p_a_request_builder')
substitute_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.substitute.substitute_request_builder')
subtotal_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.subtotal.subtotal_request_builder')
sum_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.sum.sum_request_builder')
sum_if_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.sum_if.sum_if_request_builder')
sum_ifs_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.sum_ifs.sum_ifs_request_builder')
sum_sq_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.sum_sq.sum_sq_request_builder')
syd_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.syd.syd_request_builder')
t_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.t.t_request_builder')
t_dist_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.t_dist.t_dist_request_builder')
t_dist_2_t_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.t_dist_2_t.t_dist_2_t_request_builder')
t_dist_r_t_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.t_dist_r_t.t_dist_r_t_request_builder')
t_inv_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.t_inv.t_inv_request_builder')
t_inv_2_t_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.t_inv_2_t.t_inv_2_t_request_builder')
tan_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.tan.tan_request_builder')
tanh_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.tanh.tanh_request_builder')
tbill_eq_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.tbill_eq.tbill_eq_request_builder')
tbill_price_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.tbill_price.tbill_price_request_builder')
tbill_yield_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.tbill_yield.tbill_yield_request_builder')
text_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.text.text_request_builder')
time_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.time.time_request_builder')
timevalue_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.timevalue.timevalue_request_builder')
today_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.today.today_request_builder')
trim_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.trim.trim_request_builder')
trim_mean_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.trim_mean.trim_mean_request_builder')
true_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.true_.true_request_builder')
trunc_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.trunc.trunc_request_builder')
type_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.type.type_request_builder')
unichar_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.unichar.unichar_request_builder')
unicode_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.unicode.unicode_request_builder')
upper_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.upper.upper_request_builder')
usdollar_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.usdollar.usdollar_request_builder')
value_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.value.value_request_builder')
var_p_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.var_p.var_p_request_builder')
var_s_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.var_s.var_s_request_builder')
var_a_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.var_a.var_a_request_builder')
var_p_a_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.var_p_a.var_p_a_request_builder')
vdb_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.vdb.vdb_request_builder')
vlookup_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.vlookup.vlookup_request_builder')
weekday_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.weekday.weekday_request_builder')
week_num_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.week_num.week_num_request_builder')
weibull_dist_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.weibull_dist.weibull_dist_request_builder')
work_day_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.work_day.work_day_request_builder')
work_day_intl_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.work_day_intl.work_day_intl_request_builder')
xirr_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.xirr.xirr_request_builder')
xnpv_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.xnpv.xnpv_request_builder')
xor_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.xor.xor_request_builder')
year_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.year.year_request_builder')
year_frac_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.year_frac.year_frac_request_builder')
yield_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.yield_.yield_request_builder')
yield_disc_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.yield_disc.yield_disc_request_builder')
yield_mat_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.yield_mat.yield_mat_request_builder')
z_test_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.z_test.z_test_request_builder')
workbook_functions = lazy_import('msgraph.generated.models.workbook_functions')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class FunctionsRequestBuilder():
    """
    Provides operations to manage the functions property of the microsoft.graph.workbook entity.
    """
    @property
    def abs(self) -> abs_request_builder.AbsRequestBuilder:
        """
        Provides operations to call the abs method.
        """
        return abs_request_builder.AbsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def accr_int(self) -> accr_int_request_builder.AccrIntRequestBuilder:
        """
        Provides operations to call the accrInt method.
        """
        return accr_int_request_builder.AccrIntRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def accr_int_m(self) -> accr_int_m_request_builder.AccrIntMRequestBuilder:
        """
        Provides operations to call the accrIntM method.
        """
        return accr_int_m_request_builder.AccrIntMRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def acos(self) -> acos_request_builder.AcosRequestBuilder:
        """
        Provides operations to call the acos method.
        """
        return acos_request_builder.AcosRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def acosh(self) -> acosh_request_builder.AcoshRequestBuilder:
        """
        Provides operations to call the acosh method.
        """
        return acosh_request_builder.AcoshRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def acot(self) -> acot_request_builder.AcotRequestBuilder:
        """
        Provides operations to call the acot method.
        """
        return acot_request_builder.AcotRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def acoth(self) -> acoth_request_builder.AcothRequestBuilder:
        """
        Provides operations to call the acoth method.
        """
        return acoth_request_builder.AcothRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def amor_degrc(self) -> amor_degrc_request_builder.AmorDegrcRequestBuilder:
        """
        Provides operations to call the amorDegrc method.
        """
        return amor_degrc_request_builder.AmorDegrcRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def amor_linc(self) -> amor_linc_request_builder.AmorLincRequestBuilder:
        """
        Provides operations to call the amorLinc method.
        """
        return amor_linc_request_builder.AmorLincRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def and_(self) -> and_request_builder.AndRequestBuilder:
        """
        Provides operations to call the and method.
        """
        return and_request_builder.AndRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def arabic(self) -> arabic_request_builder.ArabicRequestBuilder:
        """
        Provides operations to call the arabic method.
        """
        return arabic_request_builder.ArabicRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def areas(self) -> areas_request_builder.AreasRequestBuilder:
        """
        Provides operations to call the areas method.
        """
        return areas_request_builder.AreasRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def asc(self) -> asc_request_builder.AscRequestBuilder:
        """
        Provides operations to call the asc method.
        """
        return asc_request_builder.AscRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def asin(self) -> asin_request_builder.AsinRequestBuilder:
        """
        Provides operations to call the asin method.
        """
        return asin_request_builder.AsinRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def asinh(self) -> asinh_request_builder.AsinhRequestBuilder:
        """
        Provides operations to call the asinh method.
        """
        return asinh_request_builder.AsinhRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def atan(self) -> atan_request_builder.AtanRequestBuilder:
        """
        Provides operations to call the atan method.
        """
        return atan_request_builder.AtanRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def atan2(self) -> atan2_request_builder.Atan2RequestBuilder:
        """
        Provides operations to call the atan2 method.
        """
        return atan2_request_builder.Atan2RequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def atanh(self) -> atanh_request_builder.AtanhRequestBuilder:
        """
        Provides operations to call the atanh method.
        """
        return atanh_request_builder.AtanhRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def ave_dev(self) -> ave_dev_request_builder.AveDevRequestBuilder:
        """
        Provides operations to call the aveDev method.
        """
        return ave_dev_request_builder.AveDevRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def average(self) -> average_request_builder.AverageRequestBuilder:
        """
        Provides operations to call the average method.
        """
        return average_request_builder.AverageRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def average_a(self) -> average_a_request_builder.AverageARequestBuilder:
        """
        Provides operations to call the averageA method.
        """
        return average_a_request_builder.AverageARequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def average_if(self) -> average_if_request_builder.AverageIfRequestBuilder:
        """
        Provides operations to call the averageIf method.
        """
        return average_if_request_builder.AverageIfRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def average_ifs(self) -> average_ifs_request_builder.AverageIfsRequestBuilder:
        """
        Provides operations to call the averageIfs method.
        """
        return average_ifs_request_builder.AverageIfsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def baht_text(self) -> baht_text_request_builder.BahtTextRequestBuilder:
        """
        Provides operations to call the bahtText method.
        """
        return baht_text_request_builder.BahtTextRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def base(self) -> base_request_builder.BaseRequestBuilder:
        """
        Provides operations to call the base method.
        """
        return base_request_builder.BaseRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def bessel_i(self) -> bessel_i_request_builder.BesselIRequestBuilder:
        """
        Provides operations to call the besselI method.
        """
        return bessel_i_request_builder.BesselIRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def bessel_j(self) -> bessel_j_request_builder.BesselJRequestBuilder:
        """
        Provides operations to call the besselJ method.
        """
        return bessel_j_request_builder.BesselJRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def bessel_k(self) -> bessel_k_request_builder.BesselKRequestBuilder:
        """
        Provides operations to call the besselK method.
        """
        return bessel_k_request_builder.BesselKRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def bessel_y(self) -> bessel_y_request_builder.BesselYRequestBuilder:
        """
        Provides operations to call the besselY method.
        """
        return bessel_y_request_builder.BesselYRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def beta_dist(self) -> beta_dist_request_builder.Beta_DistRequestBuilder:
        """
        Provides operations to call the beta_Dist method.
        """
        return beta_dist_request_builder.Beta_DistRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def beta_inv(self) -> beta_inv_request_builder.Beta_InvRequestBuilder:
        """
        Provides operations to call the beta_Inv method.
        """
        return beta_inv_request_builder.Beta_InvRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def bin2_dec(self) -> bin2_dec_request_builder.Bin2DecRequestBuilder:
        """
        Provides operations to call the bin2Dec method.
        """
        return bin2_dec_request_builder.Bin2DecRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def bin2_hex(self) -> bin2_hex_request_builder.Bin2HexRequestBuilder:
        """
        Provides operations to call the bin2Hex method.
        """
        return bin2_hex_request_builder.Bin2HexRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def bin2_oct(self) -> bin2_oct_request_builder.Bin2OctRequestBuilder:
        """
        Provides operations to call the bin2Oct method.
        """
        return bin2_oct_request_builder.Bin2OctRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def binom_dist(self) -> binom_dist_request_builder.Binom_DistRequestBuilder:
        """
        Provides operations to call the binom_Dist method.
        """
        return binom_dist_request_builder.Binom_DistRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def binom_dist_range(self) -> binom_dist_range_request_builder.Binom_Dist_RangeRequestBuilder:
        """
        Provides operations to call the binom_Dist_Range method.
        """
        return binom_dist_range_request_builder.Binom_Dist_RangeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def binom_inv(self) -> binom_inv_request_builder.Binom_InvRequestBuilder:
        """
        Provides operations to call the binom_Inv method.
        """
        return binom_inv_request_builder.Binom_InvRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def bitand(self) -> bitand_request_builder.BitandRequestBuilder:
        """
        Provides operations to call the bitand method.
        """
        return bitand_request_builder.BitandRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def bitlshift(self) -> bitlshift_request_builder.BitlshiftRequestBuilder:
        """
        Provides operations to call the bitlshift method.
        """
        return bitlshift_request_builder.BitlshiftRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def bitor(self) -> bitor_request_builder.BitorRequestBuilder:
        """
        Provides operations to call the bitor method.
        """
        return bitor_request_builder.BitorRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def bitrshift(self) -> bitrshift_request_builder.BitrshiftRequestBuilder:
        """
        Provides operations to call the bitrshift method.
        """
        return bitrshift_request_builder.BitrshiftRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def bitxor(self) -> bitxor_request_builder.BitxorRequestBuilder:
        """
        Provides operations to call the bitxor method.
        """
        return bitxor_request_builder.BitxorRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def ceiling_math(self) -> ceiling_math_request_builder.Ceiling_MathRequestBuilder:
        """
        Provides operations to call the ceiling_Math method.
        """
        return ceiling_math_request_builder.Ceiling_MathRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def ceiling_precise(self) -> ceiling_precise_request_builder.Ceiling_PreciseRequestBuilder:
        """
        Provides operations to call the ceiling_Precise method.
        """
        return ceiling_precise_request_builder.Ceiling_PreciseRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def char(self) -> char_request_builder.CharRequestBuilder:
        """
        Provides operations to call the char method.
        """
        return char_request_builder.CharRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def chi_sq_dist(self) -> chi_sq_dist_request_builder.ChiSq_DistRequestBuilder:
        """
        Provides operations to call the chiSq_Dist method.
        """
        return chi_sq_dist_request_builder.ChiSq_DistRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def chi_sq_dist_r_t(self) -> chi_sq_dist_r_t_request_builder.ChiSq_Dist_RTRequestBuilder:
        """
        Provides operations to call the chiSq_Dist_RT method.
        """
        return chi_sq_dist_r_t_request_builder.ChiSq_Dist_RTRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def chi_sq_inv(self) -> chi_sq_inv_request_builder.ChiSq_InvRequestBuilder:
        """
        Provides operations to call the chiSq_Inv method.
        """
        return chi_sq_inv_request_builder.ChiSq_InvRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def chi_sq_inv_r_t(self) -> chi_sq_inv_r_t_request_builder.ChiSq_Inv_RTRequestBuilder:
        """
        Provides operations to call the chiSq_Inv_RT method.
        """
        return chi_sq_inv_r_t_request_builder.ChiSq_Inv_RTRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def choose(self) -> choose_request_builder.ChooseRequestBuilder:
        """
        Provides operations to call the choose method.
        """
        return choose_request_builder.ChooseRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def clean(self) -> clean_request_builder.CleanRequestBuilder:
        """
        Provides operations to call the clean method.
        """
        return clean_request_builder.CleanRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def code(self) -> code_request_builder.CodeRequestBuilder:
        """
        Provides operations to call the code method.
        """
        return code_request_builder.CodeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def columns(self) -> columns_request_builder.ColumnsRequestBuilder:
        """
        Provides operations to call the columns method.
        """
        return columns_request_builder.ColumnsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def combin(self) -> combin_request_builder.CombinRequestBuilder:
        """
        Provides operations to call the combin method.
        """
        return combin_request_builder.CombinRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def combina(self) -> combina_request_builder.CombinaRequestBuilder:
        """
        Provides operations to call the combina method.
        """
        return combina_request_builder.CombinaRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def complex(self) -> complex_request_builder.ComplexRequestBuilder:
        """
        Provides operations to call the complex method.
        """
        return complex_request_builder.ComplexRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def concatenate(self) -> concatenate_request_builder.ConcatenateRequestBuilder:
        """
        Provides operations to call the concatenate method.
        """
        return concatenate_request_builder.ConcatenateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def confidence_norm(self) -> confidence_norm_request_builder.Confidence_NormRequestBuilder:
        """
        Provides operations to call the confidence_Norm method.
        """
        return confidence_norm_request_builder.Confidence_NormRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def confidence_t(self) -> confidence_t_request_builder.Confidence_TRequestBuilder:
        """
        Provides operations to call the confidence_T method.
        """
        return confidence_t_request_builder.Confidence_TRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def convert(self) -> convert_request_builder.ConvertRequestBuilder:
        """
        Provides operations to call the convert method.
        """
        return convert_request_builder.ConvertRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def cos(self) -> cos_request_builder.CosRequestBuilder:
        """
        Provides operations to call the cos method.
        """
        return cos_request_builder.CosRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def cosh(self) -> cosh_request_builder.CoshRequestBuilder:
        """
        Provides operations to call the cosh method.
        """
        return cosh_request_builder.CoshRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def cot(self) -> cot_request_builder.CotRequestBuilder:
        """
        Provides operations to call the cot method.
        """
        return cot_request_builder.CotRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def coth(self) -> coth_request_builder.CothRequestBuilder:
        """
        Provides operations to call the coth method.
        """
        return coth_request_builder.CothRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def count(self) -> count_request_builder.CountRequestBuilder:
        """
        Provides operations to call the count method.
        """
        return count_request_builder.CountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def count_a(self) -> count_a_request_builder.CountARequestBuilder:
        """
        Provides operations to call the countA method.
        """
        return count_a_request_builder.CountARequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def count_blank(self) -> count_blank_request_builder.CountBlankRequestBuilder:
        """
        Provides operations to call the countBlank method.
        """
        return count_blank_request_builder.CountBlankRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def count_if(self) -> count_if_request_builder.CountIfRequestBuilder:
        """
        Provides operations to call the countIf method.
        """
        return count_if_request_builder.CountIfRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def count_ifs(self) -> count_ifs_request_builder.CountIfsRequestBuilder:
        """
        Provides operations to call the countIfs method.
        """
        return count_ifs_request_builder.CountIfsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def coup_day_bs(self) -> coup_day_bs_request_builder.CoupDayBsRequestBuilder:
        """
        Provides operations to call the coupDayBs method.
        """
        return coup_day_bs_request_builder.CoupDayBsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def coup_days(self) -> coup_days_request_builder.CoupDaysRequestBuilder:
        """
        Provides operations to call the coupDays method.
        """
        return coup_days_request_builder.CoupDaysRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def coup_days_nc(self) -> coup_days_nc_request_builder.CoupDaysNcRequestBuilder:
        """
        Provides operations to call the coupDaysNc method.
        """
        return coup_days_nc_request_builder.CoupDaysNcRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def coup_ncd(self) -> coup_ncd_request_builder.CoupNcdRequestBuilder:
        """
        Provides operations to call the coupNcd method.
        """
        return coup_ncd_request_builder.CoupNcdRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def coup_num(self) -> coup_num_request_builder.CoupNumRequestBuilder:
        """
        Provides operations to call the coupNum method.
        """
        return coup_num_request_builder.CoupNumRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def coup_pcd(self) -> coup_pcd_request_builder.CoupPcdRequestBuilder:
        """
        Provides operations to call the coupPcd method.
        """
        return coup_pcd_request_builder.CoupPcdRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def csc(self) -> csc_request_builder.CscRequestBuilder:
        """
        Provides operations to call the csc method.
        """
        return csc_request_builder.CscRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def csch(self) -> csch_request_builder.CschRequestBuilder:
        """
        Provides operations to call the csch method.
        """
        return csch_request_builder.CschRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def cum_i_pmt(self) -> cum_i_pmt_request_builder.CumIPmtRequestBuilder:
        """
        Provides operations to call the cumIPmt method.
        """
        return cum_i_pmt_request_builder.CumIPmtRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def cum_princ(self) -> cum_princ_request_builder.CumPrincRequestBuilder:
        """
        Provides operations to call the cumPrinc method.
        """
        return cum_princ_request_builder.CumPrincRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def date(self) -> date_request_builder.DateRequestBuilder:
        """
        Provides operations to call the date method.
        """
        return date_request_builder.DateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def datevalue(self) -> datevalue_request_builder.DatevalueRequestBuilder:
        """
        Provides operations to call the datevalue method.
        """
        return datevalue_request_builder.DatevalueRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def daverage(self) -> daverage_request_builder.DaverageRequestBuilder:
        """
        Provides operations to call the daverage method.
        """
        return daverage_request_builder.DaverageRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def day(self) -> day_request_builder.DayRequestBuilder:
        """
        Provides operations to call the day method.
        """
        return day_request_builder.DayRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def days(self) -> days_request_builder.DaysRequestBuilder:
        """
        Provides operations to call the days method.
        """
        return days_request_builder.DaysRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def days360(self) -> days360_request_builder.Days360RequestBuilder:
        """
        Provides operations to call the days360 method.
        """
        return days360_request_builder.Days360RequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def db(self) -> db_request_builder.DbRequestBuilder:
        """
        Provides operations to call the db method.
        """
        return db_request_builder.DbRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dbcs(self) -> dbcs_request_builder.DbcsRequestBuilder:
        """
        Provides operations to call the dbcs method.
        """
        return dbcs_request_builder.DbcsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dcount(self) -> dcount_request_builder.DcountRequestBuilder:
        """
        Provides operations to call the dcount method.
        """
        return dcount_request_builder.DcountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dcount_a(self) -> dcount_a_request_builder.DcountARequestBuilder:
        """
        Provides operations to call the dcountA method.
        """
        return dcount_a_request_builder.DcountARequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def ddb(self) -> ddb_request_builder.DdbRequestBuilder:
        """
        Provides operations to call the ddb method.
        """
        return ddb_request_builder.DdbRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dec2_bin(self) -> dec2_bin_request_builder.Dec2BinRequestBuilder:
        """
        Provides operations to call the dec2Bin method.
        """
        return dec2_bin_request_builder.Dec2BinRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dec2_hex(self) -> dec2_hex_request_builder.Dec2HexRequestBuilder:
        """
        Provides operations to call the dec2Hex method.
        """
        return dec2_hex_request_builder.Dec2HexRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dec2_oct(self) -> dec2_oct_request_builder.Dec2OctRequestBuilder:
        """
        Provides operations to call the dec2Oct method.
        """
        return dec2_oct_request_builder.Dec2OctRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def decimal(self) -> decimal_request_builder.DecimalRequestBuilder:
        """
        Provides operations to call the decimal method.
        """
        return decimal_request_builder.DecimalRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def degrees(self) -> degrees_request_builder.DegreesRequestBuilder:
        """
        Provides operations to call the degrees method.
        """
        return degrees_request_builder.DegreesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def delta(self) -> delta_request_builder.DeltaRequestBuilder:
        """
        Provides operations to call the delta method.
        """
        return delta_request_builder.DeltaRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dev_sq(self) -> dev_sq_request_builder.DevSqRequestBuilder:
        """
        Provides operations to call the devSq method.
        """
        return dev_sq_request_builder.DevSqRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dget(self) -> dget_request_builder.DgetRequestBuilder:
        """
        Provides operations to call the dget method.
        """
        return dget_request_builder.DgetRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def disc(self) -> disc_request_builder.DiscRequestBuilder:
        """
        Provides operations to call the disc method.
        """
        return disc_request_builder.DiscRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dmax(self) -> dmax_request_builder.DmaxRequestBuilder:
        """
        Provides operations to call the dmax method.
        """
        return dmax_request_builder.DmaxRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dmin(self) -> dmin_request_builder.DminRequestBuilder:
        """
        Provides operations to call the dmin method.
        """
        return dmin_request_builder.DminRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dollar(self) -> dollar_request_builder.DollarRequestBuilder:
        """
        Provides operations to call the dollar method.
        """
        return dollar_request_builder.DollarRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dollar_de(self) -> dollar_de_request_builder.DollarDeRequestBuilder:
        """
        Provides operations to call the dollarDe method.
        """
        return dollar_de_request_builder.DollarDeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dollar_fr(self) -> dollar_fr_request_builder.DollarFrRequestBuilder:
        """
        Provides operations to call the dollarFr method.
        """
        return dollar_fr_request_builder.DollarFrRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dproduct(self) -> dproduct_request_builder.DproductRequestBuilder:
        """
        Provides operations to call the dproduct method.
        """
        return dproduct_request_builder.DproductRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dst_dev(self) -> dst_dev_request_builder.DstDevRequestBuilder:
        """
        Provides operations to call the dstDev method.
        """
        return dst_dev_request_builder.DstDevRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dst_dev_p(self) -> dst_dev_p_request_builder.DstDevPRequestBuilder:
        """
        Provides operations to call the dstDevP method.
        """
        return dst_dev_p_request_builder.DstDevPRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dsum(self) -> dsum_request_builder.DsumRequestBuilder:
        """
        Provides operations to call the dsum method.
        """
        return dsum_request_builder.DsumRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def duration(self) -> duration_request_builder.DurationRequestBuilder:
        """
        Provides operations to call the duration method.
        """
        return duration_request_builder.DurationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dvar(self) -> dvar_request_builder.DvarRequestBuilder:
        """
        Provides operations to call the dvar method.
        """
        return dvar_request_builder.DvarRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dvar_p(self) -> dvar_p_request_builder.DvarPRequestBuilder:
        """
        Provides operations to call the dvarP method.
        """
        return dvar_p_request_builder.DvarPRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def ecma_ceiling(self) -> ecma_ceiling_request_builder.Ecma_CeilingRequestBuilder:
        """
        Provides operations to call the ecma_Ceiling method.
        """
        return ecma_ceiling_request_builder.Ecma_CeilingRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def edate(self) -> edate_request_builder.EdateRequestBuilder:
        """
        Provides operations to call the edate method.
        """
        return edate_request_builder.EdateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def effect(self) -> effect_request_builder.EffectRequestBuilder:
        """
        Provides operations to call the effect method.
        """
        return effect_request_builder.EffectRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def eo_month(self) -> eo_month_request_builder.EoMonthRequestBuilder:
        """
        Provides operations to call the eoMonth method.
        """
        return eo_month_request_builder.EoMonthRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def erf(self) -> erf_request_builder.ErfRequestBuilder:
        """
        Provides operations to call the erf method.
        """
        return erf_request_builder.ErfRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def erf_precise(self) -> erf_precise_request_builder.Erf_PreciseRequestBuilder:
        """
        Provides operations to call the erf_Precise method.
        """
        return erf_precise_request_builder.Erf_PreciseRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def erf_c(self) -> erf_c_request_builder.ErfCRequestBuilder:
        """
        Provides operations to call the erfC method.
        """
        return erf_c_request_builder.ErfCRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def erf_c_precise(self) -> erf_c_precise_request_builder.ErfC_PreciseRequestBuilder:
        """
        Provides operations to call the erfC_Precise method.
        """
        return erf_c_precise_request_builder.ErfC_PreciseRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def error_type(self) -> error_type_request_builder.Error_TypeRequestBuilder:
        """
        Provides operations to call the error_Type method.
        """
        return error_type_request_builder.Error_TypeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def even(self) -> even_request_builder.EvenRequestBuilder:
        """
        Provides operations to call the even method.
        """
        return even_request_builder.EvenRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def exact(self) -> exact_request_builder.ExactRequestBuilder:
        """
        Provides operations to call the exact method.
        """
        return exact_request_builder.ExactRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def exp(self) -> exp_request_builder.ExpRequestBuilder:
        """
        Provides operations to call the exp method.
        """
        return exp_request_builder.ExpRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def expon_dist(self) -> expon_dist_request_builder.Expon_DistRequestBuilder:
        """
        Provides operations to call the expon_Dist method.
        """
        return expon_dist_request_builder.Expon_DistRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def f_dist(self) -> f_dist_request_builder.F_DistRequestBuilder:
        """
        Provides operations to call the f_Dist method.
        """
        return f_dist_request_builder.F_DistRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def f_dist_r_t(self) -> f_dist_r_t_request_builder.F_Dist_RTRequestBuilder:
        """
        Provides operations to call the f_Dist_RT method.
        """
        return f_dist_r_t_request_builder.F_Dist_RTRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def f_inv(self) -> f_inv_request_builder.F_InvRequestBuilder:
        """
        Provides operations to call the f_Inv method.
        """
        return f_inv_request_builder.F_InvRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def f_inv_r_t(self) -> f_inv_r_t_request_builder.F_Inv_RTRequestBuilder:
        """
        Provides operations to call the f_Inv_RT method.
        """
        return f_inv_r_t_request_builder.F_Inv_RTRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def fact(self) -> fact_request_builder.FactRequestBuilder:
        """
        Provides operations to call the fact method.
        """
        return fact_request_builder.FactRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def fact_double(self) -> fact_double_request_builder.FactDoubleRequestBuilder:
        """
        Provides operations to call the factDouble method.
        """
        return fact_double_request_builder.FactDoubleRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def false_(self) -> false_request_builder.FalseRequestBuilder:
        """
        Provides operations to call the false method.
        """
        return false_request_builder.FalseRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def find(self) -> find_request_builder.FindRequestBuilder:
        """
        Provides operations to call the find method.
        """
        return find_request_builder.FindRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def find_b(self) -> find_b_request_builder.FindBRequestBuilder:
        """
        Provides operations to call the findB method.
        """
        return find_b_request_builder.FindBRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def fisher(self) -> fisher_request_builder.FisherRequestBuilder:
        """
        Provides operations to call the fisher method.
        """
        return fisher_request_builder.FisherRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def fisher_inv(self) -> fisher_inv_request_builder.FisherInvRequestBuilder:
        """
        Provides operations to call the fisherInv method.
        """
        return fisher_inv_request_builder.FisherInvRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def fixed(self) -> fixed_request_builder.FixedRequestBuilder:
        """
        Provides operations to call the fixed method.
        """
        return fixed_request_builder.FixedRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def floor_math(self) -> floor_math_request_builder.Floor_MathRequestBuilder:
        """
        Provides operations to call the floor_Math method.
        """
        return floor_math_request_builder.Floor_MathRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def floor_precise(self) -> floor_precise_request_builder.Floor_PreciseRequestBuilder:
        """
        Provides operations to call the floor_Precise method.
        """
        return floor_precise_request_builder.Floor_PreciseRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def fv(self) -> fv_request_builder.FvRequestBuilder:
        """
        Provides operations to call the fv method.
        """
        return fv_request_builder.FvRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def fvschedule(self) -> fvschedule_request_builder.FvscheduleRequestBuilder:
        """
        Provides operations to call the fvschedule method.
        """
        return fvschedule_request_builder.FvscheduleRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def gamma(self) -> gamma_request_builder.GammaRequestBuilder:
        """
        Provides operations to call the gamma method.
        """
        return gamma_request_builder.GammaRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def gamma_dist(self) -> gamma_dist_request_builder.Gamma_DistRequestBuilder:
        """
        Provides operations to call the gamma_Dist method.
        """
        return gamma_dist_request_builder.Gamma_DistRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def gamma_inv(self) -> gamma_inv_request_builder.Gamma_InvRequestBuilder:
        """
        Provides operations to call the gamma_Inv method.
        """
        return gamma_inv_request_builder.Gamma_InvRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def gamma_ln(self) -> gamma_ln_request_builder.GammaLnRequestBuilder:
        """
        Provides operations to call the gammaLn method.
        """
        return gamma_ln_request_builder.GammaLnRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def gamma_ln_precise(self) -> gamma_ln_precise_request_builder.GammaLn_PreciseRequestBuilder:
        """
        Provides operations to call the gammaLn_Precise method.
        """
        return gamma_ln_precise_request_builder.GammaLn_PreciseRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def gauss(self) -> gauss_request_builder.GaussRequestBuilder:
        """
        Provides operations to call the gauss method.
        """
        return gauss_request_builder.GaussRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def gcd(self) -> gcd_request_builder.GcdRequestBuilder:
        """
        Provides operations to call the gcd method.
        """
        return gcd_request_builder.GcdRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def geo_mean(self) -> geo_mean_request_builder.GeoMeanRequestBuilder:
        """
        Provides operations to call the geoMean method.
        """
        return geo_mean_request_builder.GeoMeanRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def ge_step(self) -> ge_step_request_builder.GeStepRequestBuilder:
        """
        Provides operations to call the geStep method.
        """
        return ge_step_request_builder.GeStepRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def har_mean(self) -> har_mean_request_builder.HarMeanRequestBuilder:
        """
        Provides operations to call the harMean method.
        """
        return har_mean_request_builder.HarMeanRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def hex2_bin(self) -> hex2_bin_request_builder.Hex2BinRequestBuilder:
        """
        Provides operations to call the hex2Bin method.
        """
        return hex2_bin_request_builder.Hex2BinRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def hex2_dec(self) -> hex2_dec_request_builder.Hex2DecRequestBuilder:
        """
        Provides operations to call the hex2Dec method.
        """
        return hex2_dec_request_builder.Hex2DecRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def hex2_oct(self) -> hex2_oct_request_builder.Hex2OctRequestBuilder:
        """
        Provides operations to call the hex2Oct method.
        """
        return hex2_oct_request_builder.Hex2OctRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def hlookup(self) -> hlookup_request_builder.HlookupRequestBuilder:
        """
        Provides operations to call the hlookup method.
        """
        return hlookup_request_builder.HlookupRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def hour(self) -> hour_request_builder.HourRequestBuilder:
        """
        Provides operations to call the hour method.
        """
        return hour_request_builder.HourRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def hyperlink(self) -> hyperlink_request_builder.HyperlinkRequestBuilder:
        """
        Provides operations to call the hyperlink method.
        """
        return hyperlink_request_builder.HyperlinkRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def hyp_geom_dist(self) -> hyp_geom_dist_request_builder.HypGeom_DistRequestBuilder:
        """
        Provides operations to call the hypGeom_Dist method.
        """
        return hyp_geom_dist_request_builder.HypGeom_DistRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def if_(self) -> if_request_builder.IfRequestBuilder:
        """
        Provides operations to call the if method.
        """
        return if_request_builder.IfRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def im_abs(self) -> im_abs_request_builder.ImAbsRequestBuilder:
        """
        Provides operations to call the imAbs method.
        """
        return im_abs_request_builder.ImAbsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def imaginary(self) -> imaginary_request_builder.ImaginaryRequestBuilder:
        """
        Provides operations to call the imaginary method.
        """
        return imaginary_request_builder.ImaginaryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def im_argument(self) -> im_argument_request_builder.ImArgumentRequestBuilder:
        """
        Provides operations to call the imArgument method.
        """
        return im_argument_request_builder.ImArgumentRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def im_conjugate(self) -> im_conjugate_request_builder.ImConjugateRequestBuilder:
        """
        Provides operations to call the imConjugate method.
        """
        return im_conjugate_request_builder.ImConjugateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def im_cos(self) -> im_cos_request_builder.ImCosRequestBuilder:
        """
        Provides operations to call the imCos method.
        """
        return im_cos_request_builder.ImCosRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def im_cosh(self) -> im_cosh_request_builder.ImCoshRequestBuilder:
        """
        Provides operations to call the imCosh method.
        """
        return im_cosh_request_builder.ImCoshRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def im_cot(self) -> im_cot_request_builder.ImCotRequestBuilder:
        """
        Provides operations to call the imCot method.
        """
        return im_cot_request_builder.ImCotRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def im_csc(self) -> im_csc_request_builder.ImCscRequestBuilder:
        """
        Provides operations to call the imCsc method.
        """
        return im_csc_request_builder.ImCscRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def im_csch(self) -> im_csch_request_builder.ImCschRequestBuilder:
        """
        Provides operations to call the imCsch method.
        """
        return im_csch_request_builder.ImCschRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def im_div(self) -> im_div_request_builder.ImDivRequestBuilder:
        """
        Provides operations to call the imDiv method.
        """
        return im_div_request_builder.ImDivRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def im_exp(self) -> im_exp_request_builder.ImExpRequestBuilder:
        """
        Provides operations to call the imExp method.
        """
        return im_exp_request_builder.ImExpRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def im_ln(self) -> im_ln_request_builder.ImLnRequestBuilder:
        """
        Provides operations to call the imLn method.
        """
        return im_ln_request_builder.ImLnRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def im_log10(self) -> im_log10_request_builder.ImLog10RequestBuilder:
        """
        Provides operations to call the imLog10 method.
        """
        return im_log10_request_builder.ImLog10RequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def im_log2(self) -> im_log2_request_builder.ImLog2RequestBuilder:
        """
        Provides operations to call the imLog2 method.
        """
        return im_log2_request_builder.ImLog2RequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def im_power(self) -> im_power_request_builder.ImPowerRequestBuilder:
        """
        Provides operations to call the imPower method.
        """
        return im_power_request_builder.ImPowerRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def im_product(self) -> im_product_request_builder.ImProductRequestBuilder:
        """
        Provides operations to call the imProduct method.
        """
        return im_product_request_builder.ImProductRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def im_real(self) -> im_real_request_builder.ImRealRequestBuilder:
        """
        Provides operations to call the imReal method.
        """
        return im_real_request_builder.ImRealRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def im_sec(self) -> im_sec_request_builder.ImSecRequestBuilder:
        """
        Provides operations to call the imSec method.
        """
        return im_sec_request_builder.ImSecRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def im_sech(self) -> im_sech_request_builder.ImSechRequestBuilder:
        """
        Provides operations to call the imSech method.
        """
        return im_sech_request_builder.ImSechRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def im_sin(self) -> im_sin_request_builder.ImSinRequestBuilder:
        """
        Provides operations to call the imSin method.
        """
        return im_sin_request_builder.ImSinRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def im_sinh(self) -> im_sinh_request_builder.ImSinhRequestBuilder:
        """
        Provides operations to call the imSinh method.
        """
        return im_sinh_request_builder.ImSinhRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def im_sqrt(self) -> im_sqrt_request_builder.ImSqrtRequestBuilder:
        """
        Provides operations to call the imSqrt method.
        """
        return im_sqrt_request_builder.ImSqrtRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def im_sub(self) -> im_sub_request_builder.ImSubRequestBuilder:
        """
        Provides operations to call the imSub method.
        """
        return im_sub_request_builder.ImSubRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def im_sum(self) -> im_sum_request_builder.ImSumRequestBuilder:
        """
        Provides operations to call the imSum method.
        """
        return im_sum_request_builder.ImSumRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def im_tan(self) -> im_tan_request_builder.ImTanRequestBuilder:
        """
        Provides operations to call the imTan method.
        """
        return im_tan_request_builder.ImTanRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def int(self) -> int_request_builder.IntRequestBuilder:
        """
        Provides operations to call the int method.
        """
        return int_request_builder.IntRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def int_rate(self) -> int_rate_request_builder.IntRateRequestBuilder:
        """
        Provides operations to call the intRate method.
        """
        return int_rate_request_builder.IntRateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def ipmt(self) -> ipmt_request_builder.IpmtRequestBuilder:
        """
        Provides operations to call the ipmt method.
        """
        return ipmt_request_builder.IpmtRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def irr(self) -> irr_request_builder.IrrRequestBuilder:
        """
        Provides operations to call the irr method.
        """
        return irr_request_builder.IrrRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def is_err(self) -> is_err_request_builder.IsErrRequestBuilder:
        """
        Provides operations to call the isErr method.
        """
        return is_err_request_builder.IsErrRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def is_error(self) -> is_error_request_builder.IsErrorRequestBuilder:
        """
        Provides operations to call the isError method.
        """
        return is_error_request_builder.IsErrorRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def is_even(self) -> is_even_request_builder.IsEvenRequestBuilder:
        """
        Provides operations to call the isEven method.
        """
        return is_even_request_builder.IsEvenRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def is_formula(self) -> is_formula_request_builder.IsFormulaRequestBuilder:
        """
        Provides operations to call the isFormula method.
        """
        return is_formula_request_builder.IsFormulaRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def is_logical(self) -> is_logical_request_builder.IsLogicalRequestBuilder:
        """
        Provides operations to call the isLogical method.
        """
        return is_logical_request_builder.IsLogicalRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def is_n_a(self) -> is_n_a_request_builder.IsNARequestBuilder:
        """
        Provides operations to call the isNA method.
        """
        return is_n_a_request_builder.IsNARequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def is_non_text(self) -> is_non_text_request_builder.IsNonTextRequestBuilder:
        """
        Provides operations to call the isNonText method.
        """
        return is_non_text_request_builder.IsNonTextRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def is_number(self) -> is_number_request_builder.IsNumberRequestBuilder:
        """
        Provides operations to call the isNumber method.
        """
        return is_number_request_builder.IsNumberRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def iso_ceiling(self) -> iso_ceiling_request_builder.Iso_CeilingRequestBuilder:
        """
        Provides operations to call the iso_Ceiling method.
        """
        return iso_ceiling_request_builder.Iso_CeilingRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def is_odd(self) -> is_odd_request_builder.IsOddRequestBuilder:
        """
        Provides operations to call the isOdd method.
        """
        return is_odd_request_builder.IsOddRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def iso_week_num(self) -> iso_week_num_request_builder.IsoWeekNumRequestBuilder:
        """
        Provides operations to call the isoWeekNum method.
        """
        return iso_week_num_request_builder.IsoWeekNumRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def ispmt(self) -> ispmt_request_builder.IspmtRequestBuilder:
        """
        Provides operations to call the ispmt method.
        """
        return ispmt_request_builder.IspmtRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def isref(self) -> isref_request_builder.IsrefRequestBuilder:
        """
        Provides operations to call the isref method.
        """
        return isref_request_builder.IsrefRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def is_text(self) -> is_text_request_builder.IsTextRequestBuilder:
        """
        Provides operations to call the isText method.
        """
        return is_text_request_builder.IsTextRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def kurt(self) -> kurt_request_builder.KurtRequestBuilder:
        """
        Provides operations to call the kurt method.
        """
        return kurt_request_builder.KurtRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def large(self) -> large_request_builder.LargeRequestBuilder:
        """
        Provides operations to call the large method.
        """
        return large_request_builder.LargeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def lcm(self) -> lcm_request_builder.LcmRequestBuilder:
        """
        Provides operations to call the lcm method.
        """
        return lcm_request_builder.LcmRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def left(self) -> left_request_builder.LeftRequestBuilder:
        """
        Provides operations to call the left method.
        """
        return left_request_builder.LeftRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def leftb(self) -> leftb_request_builder.LeftbRequestBuilder:
        """
        Provides operations to call the leftb method.
        """
        return leftb_request_builder.LeftbRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def len(self) -> len_request_builder.LenRequestBuilder:
        """
        Provides operations to call the len method.
        """
        return len_request_builder.LenRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def lenb(self) -> lenb_request_builder.LenbRequestBuilder:
        """
        Provides operations to call the lenb method.
        """
        return lenb_request_builder.LenbRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def ln(self) -> ln_request_builder.LnRequestBuilder:
        """
        Provides operations to call the ln method.
        """
        return ln_request_builder.LnRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def log(self) -> log_request_builder.LogRequestBuilder:
        """
        Provides operations to call the log method.
        """
        return log_request_builder.LogRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def log10(self) -> log10_request_builder.Log10RequestBuilder:
        """
        Provides operations to call the log10 method.
        """
        return log10_request_builder.Log10RequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def log_norm_dist(self) -> log_norm_dist_request_builder.LogNorm_DistRequestBuilder:
        """
        Provides operations to call the logNorm_Dist method.
        """
        return log_norm_dist_request_builder.LogNorm_DistRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def log_norm_inv(self) -> log_norm_inv_request_builder.LogNorm_InvRequestBuilder:
        """
        Provides operations to call the logNorm_Inv method.
        """
        return log_norm_inv_request_builder.LogNorm_InvRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def lookup(self) -> lookup_request_builder.LookupRequestBuilder:
        """
        Provides operations to call the lookup method.
        """
        return lookup_request_builder.LookupRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def lower(self) -> lower_request_builder.LowerRequestBuilder:
        """
        Provides operations to call the lower method.
        """
        return lower_request_builder.LowerRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def match(self) -> match_request_builder.MatchRequestBuilder:
        """
        Provides operations to call the match method.
        """
        return match_request_builder.MatchRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def max(self) -> max_request_builder.MaxRequestBuilder:
        """
        Provides operations to call the max method.
        """
        return max_request_builder.MaxRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def max_a(self) -> max_a_request_builder.MaxARequestBuilder:
        """
        Provides operations to call the maxA method.
        """
        return max_a_request_builder.MaxARequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mduration(self) -> mduration_request_builder.MdurationRequestBuilder:
        """
        Provides operations to call the mduration method.
        """
        return mduration_request_builder.MdurationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def median(self) -> median_request_builder.MedianRequestBuilder:
        """
        Provides operations to call the median method.
        """
        return median_request_builder.MedianRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mid(self) -> mid_request_builder.MidRequestBuilder:
        """
        Provides operations to call the mid method.
        """
        return mid_request_builder.MidRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def midb(self) -> midb_request_builder.MidbRequestBuilder:
        """
        Provides operations to call the midb method.
        """
        return midb_request_builder.MidbRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def min(self) -> min_request_builder.MinRequestBuilder:
        """
        Provides operations to call the min method.
        """
        return min_request_builder.MinRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def min_a(self) -> min_a_request_builder.MinARequestBuilder:
        """
        Provides operations to call the minA method.
        """
        return min_a_request_builder.MinARequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def minute(self) -> minute_request_builder.MinuteRequestBuilder:
        """
        Provides operations to call the minute method.
        """
        return minute_request_builder.MinuteRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mirr(self) -> mirr_request_builder.MirrRequestBuilder:
        """
        Provides operations to call the mirr method.
        """
        return mirr_request_builder.MirrRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mod(self) -> mod_request_builder.ModRequestBuilder:
        """
        Provides operations to call the mod method.
        """
        return mod_request_builder.ModRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def month(self) -> month_request_builder.MonthRequestBuilder:
        """
        Provides operations to call the month method.
        """
        return month_request_builder.MonthRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mround(self) -> mround_request_builder.MroundRequestBuilder:
        """
        Provides operations to call the mround method.
        """
        return mround_request_builder.MroundRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def multi_nomial(self) -> multi_nomial_request_builder.MultiNomialRequestBuilder:
        """
        Provides operations to call the multiNomial method.
        """
        return multi_nomial_request_builder.MultiNomialRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def n(self) -> n_request_builder.NRequestBuilder:
        """
        Provides operations to call the n method.
        """
        return n_request_builder.NRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def na(self) -> na_request_builder.NaRequestBuilder:
        """
        Provides operations to call the na method.
        """
        return na_request_builder.NaRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def neg_binom_dist(self) -> neg_binom_dist_request_builder.NegBinom_DistRequestBuilder:
        """
        Provides operations to call the negBinom_Dist method.
        """
        return neg_binom_dist_request_builder.NegBinom_DistRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def network_days(self) -> network_days_request_builder.NetworkDaysRequestBuilder:
        """
        Provides operations to call the networkDays method.
        """
        return network_days_request_builder.NetworkDaysRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def network_days_intl(self) -> network_days_intl_request_builder.NetworkDays_IntlRequestBuilder:
        """
        Provides operations to call the networkDays_Intl method.
        """
        return network_days_intl_request_builder.NetworkDays_IntlRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def nominal(self) -> nominal_request_builder.NominalRequestBuilder:
        """
        Provides operations to call the nominal method.
        """
        return nominal_request_builder.NominalRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def norm_dist(self) -> norm_dist_request_builder.Norm_DistRequestBuilder:
        """
        Provides operations to call the norm_Dist method.
        """
        return norm_dist_request_builder.Norm_DistRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def norm_inv(self) -> norm_inv_request_builder.Norm_InvRequestBuilder:
        """
        Provides operations to call the norm_Inv method.
        """
        return norm_inv_request_builder.Norm_InvRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def norm_s_dist(self) -> norm_s_dist_request_builder.Norm_S_DistRequestBuilder:
        """
        Provides operations to call the norm_S_Dist method.
        """
        return norm_s_dist_request_builder.Norm_S_DistRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def norm_s_inv(self) -> norm_s_inv_request_builder.Norm_S_InvRequestBuilder:
        """
        Provides operations to call the norm_S_Inv method.
        """
        return norm_s_inv_request_builder.Norm_S_InvRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def not_(self) -> not_request_builder.NotRequestBuilder:
        """
        Provides operations to call the not method.
        """
        return not_request_builder.NotRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def now(self) -> now_request_builder.NowRequestBuilder:
        """
        Provides operations to call the now method.
        """
        return now_request_builder.NowRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def nper(self) -> nper_request_builder.NperRequestBuilder:
        """
        Provides operations to call the nper method.
        """
        return nper_request_builder.NperRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def npv(self) -> npv_request_builder.NpvRequestBuilder:
        """
        Provides operations to call the npv method.
        """
        return npv_request_builder.NpvRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def number_value(self) -> number_value_request_builder.NumberValueRequestBuilder:
        """
        Provides operations to call the numberValue method.
        """
        return number_value_request_builder.NumberValueRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def oct2_bin(self) -> oct2_bin_request_builder.Oct2BinRequestBuilder:
        """
        Provides operations to call the oct2Bin method.
        """
        return oct2_bin_request_builder.Oct2BinRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def oct2_dec(self) -> oct2_dec_request_builder.Oct2DecRequestBuilder:
        """
        Provides operations to call the oct2Dec method.
        """
        return oct2_dec_request_builder.Oct2DecRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def oct2_hex(self) -> oct2_hex_request_builder.Oct2HexRequestBuilder:
        """
        Provides operations to call the oct2Hex method.
        """
        return oct2_hex_request_builder.Oct2HexRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def odd(self) -> odd_request_builder.OddRequestBuilder:
        """
        Provides operations to call the odd method.
        """
        return odd_request_builder.OddRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def odd_f_price(self) -> odd_f_price_request_builder.OddFPriceRequestBuilder:
        """
        Provides operations to call the oddFPrice method.
        """
        return odd_f_price_request_builder.OddFPriceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def odd_f_yield(self) -> odd_f_yield_request_builder.OddFYieldRequestBuilder:
        """
        Provides operations to call the oddFYield method.
        """
        return odd_f_yield_request_builder.OddFYieldRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def odd_l_price(self) -> odd_l_price_request_builder.OddLPriceRequestBuilder:
        """
        Provides operations to call the oddLPrice method.
        """
        return odd_l_price_request_builder.OddLPriceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def odd_l_yield(self) -> odd_l_yield_request_builder.OddLYieldRequestBuilder:
        """
        Provides operations to call the oddLYield method.
        """
        return odd_l_yield_request_builder.OddLYieldRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def or_(self) -> or_request_builder.OrRequestBuilder:
        """
        Provides operations to call the or method.
        """
        return or_request_builder.OrRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def pduration(self) -> pduration_request_builder.PdurationRequestBuilder:
        """
        Provides operations to call the pduration method.
        """
        return pduration_request_builder.PdurationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def percentile_exc(self) -> percentile_exc_request_builder.Percentile_ExcRequestBuilder:
        """
        Provides operations to call the percentile_Exc method.
        """
        return percentile_exc_request_builder.Percentile_ExcRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def percentile_inc(self) -> percentile_inc_request_builder.Percentile_IncRequestBuilder:
        """
        Provides operations to call the percentile_Inc method.
        """
        return percentile_inc_request_builder.Percentile_IncRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def percent_rank_exc(self) -> percent_rank_exc_request_builder.PercentRank_ExcRequestBuilder:
        """
        Provides operations to call the percentRank_Exc method.
        """
        return percent_rank_exc_request_builder.PercentRank_ExcRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def percent_rank_inc(self) -> percent_rank_inc_request_builder.PercentRank_IncRequestBuilder:
        """
        Provides operations to call the percentRank_Inc method.
        """
        return percent_rank_inc_request_builder.PercentRank_IncRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def permut(self) -> permut_request_builder.PermutRequestBuilder:
        """
        Provides operations to call the permut method.
        """
        return permut_request_builder.PermutRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def permutationa(self) -> permutationa_request_builder.PermutationaRequestBuilder:
        """
        Provides operations to call the permutationa method.
        """
        return permutationa_request_builder.PermutationaRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def phi(self) -> phi_request_builder.PhiRequestBuilder:
        """
        Provides operations to call the phi method.
        """
        return phi_request_builder.PhiRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def pi(self) -> pi_request_builder.PiRequestBuilder:
        """
        Provides operations to call the pi method.
        """
        return pi_request_builder.PiRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def pmt(self) -> pmt_request_builder.PmtRequestBuilder:
        """
        Provides operations to call the pmt method.
        """
        return pmt_request_builder.PmtRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def poisson_dist(self) -> poisson_dist_request_builder.Poisson_DistRequestBuilder:
        """
        Provides operations to call the poisson_Dist method.
        """
        return poisson_dist_request_builder.Poisson_DistRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def power(self) -> power_request_builder.PowerRequestBuilder:
        """
        Provides operations to call the power method.
        """
        return power_request_builder.PowerRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def ppmt(self) -> ppmt_request_builder.PpmtRequestBuilder:
        """
        Provides operations to call the ppmt method.
        """
        return ppmt_request_builder.PpmtRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def price(self) -> price_request_builder.PriceRequestBuilder:
        """
        Provides operations to call the price method.
        """
        return price_request_builder.PriceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def price_disc(self) -> price_disc_request_builder.PriceDiscRequestBuilder:
        """
        Provides operations to call the priceDisc method.
        """
        return price_disc_request_builder.PriceDiscRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def price_mat(self) -> price_mat_request_builder.PriceMatRequestBuilder:
        """
        Provides operations to call the priceMat method.
        """
        return price_mat_request_builder.PriceMatRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def product(self) -> product_request_builder.ProductRequestBuilder:
        """
        Provides operations to call the product method.
        """
        return product_request_builder.ProductRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def proper(self) -> proper_request_builder.ProperRequestBuilder:
        """
        Provides operations to call the proper method.
        """
        return proper_request_builder.ProperRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def pv(self) -> pv_request_builder.PvRequestBuilder:
        """
        Provides operations to call the pv method.
        """
        return pv_request_builder.PvRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def quartile_exc(self) -> quartile_exc_request_builder.Quartile_ExcRequestBuilder:
        """
        Provides operations to call the quartile_Exc method.
        """
        return quartile_exc_request_builder.Quartile_ExcRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def quartile_inc(self) -> quartile_inc_request_builder.Quartile_IncRequestBuilder:
        """
        Provides operations to call the quartile_Inc method.
        """
        return quartile_inc_request_builder.Quartile_IncRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def quotient(self) -> quotient_request_builder.QuotientRequestBuilder:
        """
        Provides operations to call the quotient method.
        """
        return quotient_request_builder.QuotientRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def radians(self) -> radians_request_builder.RadiansRequestBuilder:
        """
        Provides operations to call the radians method.
        """
        return radians_request_builder.RadiansRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def rand(self) -> rand_request_builder.RandRequestBuilder:
        """
        Provides operations to call the rand method.
        """
        return rand_request_builder.RandRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def rand_between(self) -> rand_between_request_builder.RandBetweenRequestBuilder:
        """
        Provides operations to call the randBetween method.
        """
        return rand_between_request_builder.RandBetweenRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def rank_avg(self) -> rank_avg_request_builder.Rank_AvgRequestBuilder:
        """
        Provides operations to call the rank_Avg method.
        """
        return rank_avg_request_builder.Rank_AvgRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def rank_eq(self) -> rank_eq_request_builder.Rank_EqRequestBuilder:
        """
        Provides operations to call the rank_Eq method.
        """
        return rank_eq_request_builder.Rank_EqRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def rate(self) -> rate_request_builder.RateRequestBuilder:
        """
        Provides operations to call the rate method.
        """
        return rate_request_builder.RateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def received(self) -> received_request_builder.ReceivedRequestBuilder:
        """
        Provides operations to call the received method.
        """
        return received_request_builder.ReceivedRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def replace(self) -> replace_request_builder.ReplaceRequestBuilder:
        """
        Provides operations to call the replace method.
        """
        return replace_request_builder.ReplaceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def replace_b(self) -> replace_b_request_builder.ReplaceBRequestBuilder:
        """
        Provides operations to call the replaceB method.
        """
        return replace_b_request_builder.ReplaceBRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def rept(self) -> rept_request_builder.ReptRequestBuilder:
        """
        Provides operations to call the rept method.
        """
        return rept_request_builder.ReptRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def right(self) -> right_request_builder.RightRequestBuilder:
        """
        Provides operations to call the right method.
        """
        return right_request_builder.RightRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def rightb(self) -> rightb_request_builder.RightbRequestBuilder:
        """
        Provides operations to call the rightb method.
        """
        return rightb_request_builder.RightbRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def roman(self) -> roman_request_builder.RomanRequestBuilder:
        """
        Provides operations to call the roman method.
        """
        return roman_request_builder.RomanRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def round(self) -> round_request_builder.RoundRequestBuilder:
        """
        Provides operations to call the round method.
        """
        return round_request_builder.RoundRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def round_down(self) -> round_down_request_builder.RoundDownRequestBuilder:
        """
        Provides operations to call the roundDown method.
        """
        return round_down_request_builder.RoundDownRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def round_up(self) -> round_up_request_builder.RoundUpRequestBuilder:
        """
        Provides operations to call the roundUp method.
        """
        return round_up_request_builder.RoundUpRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def rows(self) -> rows_request_builder.RowsRequestBuilder:
        """
        Provides operations to call the rows method.
        """
        return rows_request_builder.RowsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def rri(self) -> rri_request_builder.RriRequestBuilder:
        """
        Provides operations to call the rri method.
        """
        return rri_request_builder.RriRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sec(self) -> sec_request_builder.SecRequestBuilder:
        """
        Provides operations to call the sec method.
        """
        return sec_request_builder.SecRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sech(self) -> sech_request_builder.SechRequestBuilder:
        """
        Provides operations to call the sech method.
        """
        return sech_request_builder.SechRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def second(self) -> second_request_builder.SecondRequestBuilder:
        """
        Provides operations to call the second method.
        """
        return second_request_builder.SecondRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def series_sum(self) -> series_sum_request_builder.SeriesSumRequestBuilder:
        """
        Provides operations to call the seriesSum method.
        """
        return series_sum_request_builder.SeriesSumRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sheet(self) -> sheet_request_builder.SheetRequestBuilder:
        """
        Provides operations to call the sheet method.
        """
        return sheet_request_builder.SheetRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sheets(self) -> sheets_request_builder.SheetsRequestBuilder:
        """
        Provides operations to call the sheets method.
        """
        return sheets_request_builder.SheetsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sign(self) -> sign_request_builder.SignRequestBuilder:
        """
        Provides operations to call the sign method.
        """
        return sign_request_builder.SignRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sin(self) -> sin_request_builder.SinRequestBuilder:
        """
        Provides operations to call the sin method.
        """
        return sin_request_builder.SinRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sinh(self) -> sinh_request_builder.SinhRequestBuilder:
        """
        Provides operations to call the sinh method.
        """
        return sinh_request_builder.SinhRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def skew(self) -> skew_request_builder.SkewRequestBuilder:
        """
        Provides operations to call the skew method.
        """
        return skew_request_builder.SkewRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def skew_p(self) -> skew_p_request_builder.Skew_pRequestBuilder:
        """
        Provides operations to call the skew_p method.
        """
        return skew_p_request_builder.Skew_pRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sln(self) -> sln_request_builder.SlnRequestBuilder:
        """
        Provides operations to call the sln method.
        """
        return sln_request_builder.SlnRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def small(self) -> small_request_builder.SmallRequestBuilder:
        """
        Provides operations to call the small method.
        """
        return small_request_builder.SmallRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sqrt(self) -> sqrt_request_builder.SqrtRequestBuilder:
        """
        Provides operations to call the sqrt method.
        """
        return sqrt_request_builder.SqrtRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sqrt_pi(self) -> sqrt_pi_request_builder.SqrtPiRequestBuilder:
        """
        Provides operations to call the sqrtPi method.
        """
        return sqrt_pi_request_builder.SqrtPiRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def standardize(self) -> standardize_request_builder.StandardizeRequestBuilder:
        """
        Provides operations to call the standardize method.
        """
        return standardize_request_builder.StandardizeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def st_dev_p(self) -> st_dev_p_request_builder.StDev_PRequestBuilder:
        """
        Provides operations to call the stDev_P method.
        """
        return st_dev_p_request_builder.StDev_PRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def st_dev_s(self) -> st_dev_s_request_builder.StDev_SRequestBuilder:
        """
        Provides operations to call the stDev_S method.
        """
        return st_dev_s_request_builder.StDev_SRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def st_dev_a(self) -> st_dev_a_request_builder.StDevARequestBuilder:
        """
        Provides operations to call the stDevA method.
        """
        return st_dev_a_request_builder.StDevARequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def st_dev_p_a(self) -> st_dev_p_a_request_builder.StDevPARequestBuilder:
        """
        Provides operations to call the stDevPA method.
        """
        return st_dev_p_a_request_builder.StDevPARequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def substitute(self) -> substitute_request_builder.SubstituteRequestBuilder:
        """
        Provides operations to call the substitute method.
        """
        return substitute_request_builder.SubstituteRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def subtotal(self) -> subtotal_request_builder.SubtotalRequestBuilder:
        """
        Provides operations to call the subtotal method.
        """
        return subtotal_request_builder.SubtotalRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sum(self) -> sum_request_builder.SumRequestBuilder:
        """
        Provides operations to call the sum method.
        """
        return sum_request_builder.SumRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sum_if(self) -> sum_if_request_builder.SumIfRequestBuilder:
        """
        Provides operations to call the sumIf method.
        """
        return sum_if_request_builder.SumIfRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sum_ifs(self) -> sum_ifs_request_builder.SumIfsRequestBuilder:
        """
        Provides operations to call the sumIfs method.
        """
        return sum_ifs_request_builder.SumIfsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sum_sq(self) -> sum_sq_request_builder.SumSqRequestBuilder:
        """
        Provides operations to call the sumSq method.
        """
        return sum_sq_request_builder.SumSqRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def syd(self) -> syd_request_builder.SydRequestBuilder:
        """
        Provides operations to call the syd method.
        """
        return syd_request_builder.SydRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def t(self) -> t_request_builder.TRequestBuilder:
        """
        Provides operations to call the t method.
        """
        return t_request_builder.TRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def t_dist(self) -> t_dist_request_builder.T_DistRequestBuilder:
        """
        Provides operations to call the t_Dist method.
        """
        return t_dist_request_builder.T_DistRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def t_dist_2_t(self) -> t_dist_2_t_request_builder.T_Dist_2TRequestBuilder:
        """
        Provides operations to call the t_Dist_2T method.
        """
        return t_dist_2_t_request_builder.T_Dist_2TRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def t_dist_r_t(self) -> t_dist_r_t_request_builder.T_Dist_RTRequestBuilder:
        """
        Provides operations to call the t_Dist_RT method.
        """
        return t_dist_r_t_request_builder.T_Dist_RTRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def t_inv(self) -> t_inv_request_builder.T_InvRequestBuilder:
        """
        Provides operations to call the t_Inv method.
        """
        return t_inv_request_builder.T_InvRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def t_inv_2_t(self) -> t_inv_2_t_request_builder.T_Inv_2TRequestBuilder:
        """
        Provides operations to call the t_Inv_2T method.
        """
        return t_inv_2_t_request_builder.T_Inv_2TRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tan(self) -> tan_request_builder.TanRequestBuilder:
        """
        Provides operations to call the tan method.
        """
        return tan_request_builder.TanRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tanh(self) -> tanh_request_builder.TanhRequestBuilder:
        """
        Provides operations to call the tanh method.
        """
        return tanh_request_builder.TanhRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tbill_eq(self) -> tbill_eq_request_builder.TbillEqRequestBuilder:
        """
        Provides operations to call the tbillEq method.
        """
        return tbill_eq_request_builder.TbillEqRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tbill_price(self) -> tbill_price_request_builder.TbillPriceRequestBuilder:
        """
        Provides operations to call the tbillPrice method.
        """
        return tbill_price_request_builder.TbillPriceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tbill_yield(self) -> tbill_yield_request_builder.TbillYieldRequestBuilder:
        """
        Provides operations to call the tbillYield method.
        """
        return tbill_yield_request_builder.TbillYieldRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def text(self) -> text_request_builder.TextRequestBuilder:
        """
        Provides operations to call the text method.
        """
        return text_request_builder.TextRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def time(self) -> time_request_builder.TimeRequestBuilder:
        """
        Provides operations to call the time method.
        """
        return time_request_builder.TimeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def timevalue(self) -> timevalue_request_builder.TimevalueRequestBuilder:
        """
        Provides operations to call the timevalue method.
        """
        return timevalue_request_builder.TimevalueRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def today(self) -> today_request_builder.TodayRequestBuilder:
        """
        Provides operations to call the today method.
        """
        return today_request_builder.TodayRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def trim(self) -> trim_request_builder.TrimRequestBuilder:
        """
        Provides operations to call the trim method.
        """
        return trim_request_builder.TrimRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def trim_mean(self) -> trim_mean_request_builder.TrimMeanRequestBuilder:
        """
        Provides operations to call the trimMean method.
        """
        return trim_mean_request_builder.TrimMeanRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def true_(self) -> true_request_builder.TrueRequestBuilder:
        """
        Provides operations to call the true method.
        """
        return true_request_builder.TrueRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def trunc(self) -> trunc_request_builder.TruncRequestBuilder:
        """
        Provides operations to call the trunc method.
        """
        return trunc_request_builder.TruncRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def type(self) -> type_request_builder.TypeRequestBuilder:
        """
        Provides operations to call the type method.
        """
        return type_request_builder.TypeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def unichar(self) -> unichar_request_builder.UnicharRequestBuilder:
        """
        Provides operations to call the unichar method.
        """
        return unichar_request_builder.UnicharRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def unicode(self) -> unicode_request_builder.UnicodeRequestBuilder:
        """
        Provides operations to call the unicode method.
        """
        return unicode_request_builder.UnicodeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def upper(self) -> upper_request_builder.UpperRequestBuilder:
        """
        Provides operations to call the upper method.
        """
        return upper_request_builder.UpperRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def usdollar(self) -> usdollar_request_builder.UsdollarRequestBuilder:
        """
        Provides operations to call the usdollar method.
        """
        return usdollar_request_builder.UsdollarRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def value(self) -> value_request_builder.ValueRequestBuilder:
        """
        Provides operations to call the value method.
        """
        return value_request_builder.ValueRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def var_p(self) -> var_p_request_builder.Var_PRequestBuilder:
        """
        Provides operations to call the var_P method.
        """
        return var_p_request_builder.Var_PRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def var_s(self) -> var_s_request_builder.Var_SRequestBuilder:
        """
        Provides operations to call the var_S method.
        """
        return var_s_request_builder.Var_SRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def var_a(self) -> var_a_request_builder.VarARequestBuilder:
        """
        Provides operations to call the varA method.
        """
        return var_a_request_builder.VarARequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def var_p_a(self) -> var_p_a_request_builder.VarPARequestBuilder:
        """
        Provides operations to call the varPA method.
        """
        return var_p_a_request_builder.VarPARequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def vdb(self) -> vdb_request_builder.VdbRequestBuilder:
        """
        Provides operations to call the vdb method.
        """
        return vdb_request_builder.VdbRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def vlookup(self) -> vlookup_request_builder.VlookupRequestBuilder:
        """
        Provides operations to call the vlookup method.
        """
        return vlookup_request_builder.VlookupRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def weekday(self) -> weekday_request_builder.WeekdayRequestBuilder:
        """
        Provides operations to call the weekday method.
        """
        return weekday_request_builder.WeekdayRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def week_num(self) -> week_num_request_builder.WeekNumRequestBuilder:
        """
        Provides operations to call the weekNum method.
        """
        return week_num_request_builder.WeekNumRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def weibull_dist(self) -> weibull_dist_request_builder.Weibull_DistRequestBuilder:
        """
        Provides operations to call the weibull_Dist method.
        """
        return weibull_dist_request_builder.Weibull_DistRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def work_day(self) -> work_day_request_builder.WorkDayRequestBuilder:
        """
        Provides operations to call the workDay method.
        """
        return work_day_request_builder.WorkDayRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def work_day_intl(self) -> work_day_intl_request_builder.WorkDay_IntlRequestBuilder:
        """
        Provides operations to call the workDay_Intl method.
        """
        return work_day_intl_request_builder.WorkDay_IntlRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def xirr(self) -> xirr_request_builder.XirrRequestBuilder:
        """
        Provides operations to call the xirr method.
        """
        return xirr_request_builder.XirrRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def xnpv(self) -> xnpv_request_builder.XnpvRequestBuilder:
        """
        Provides operations to call the xnpv method.
        """
        return xnpv_request_builder.XnpvRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def xor(self) -> xor_request_builder.XorRequestBuilder:
        """
        Provides operations to call the xor method.
        """
        return xor_request_builder.XorRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def year(self) -> year_request_builder.YearRequestBuilder:
        """
        Provides operations to call the year method.
        """
        return year_request_builder.YearRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def year_frac(self) -> year_frac_request_builder.YearFracRequestBuilder:
        """
        Provides operations to call the yearFrac method.
        """
        return year_frac_request_builder.YearFracRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def yield_(self) -> yield_request_builder.YieldRequestBuilder:
        """
        Provides operations to call the yield method.
        """
        return yield_request_builder.YieldRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def yield_disc(self) -> yield_disc_request_builder.YieldDiscRequestBuilder:
        """
        Provides operations to call the yieldDisc method.
        """
        return yield_disc_request_builder.YieldDiscRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def yield_mat(self) -> yield_mat_request_builder.YieldMatRequestBuilder:
        """
        Provides operations to call the yieldMat method.
        """
        return yield_mat_request_builder.YieldMatRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def z_test(self) -> z_test_request_builder.Z_TestRequestBuilder:
        """
        Provides operations to call the z_Test method.
        """
        return z_test_request_builder.Z_TestRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new FunctionsRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/drives/{drive%2Did}/items/{driveItem%2Did}/workbook/functions{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[FunctionsRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property functions for drives
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[FunctionsRequestBuilderGetRequestConfiguration] = None) -> Optional[workbook_functions.WorkbookFunctions]:
        """
        Get functions from drives
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[workbook_functions.WorkbookFunctions]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, workbook_functions.WorkbookFunctions, error_mapping)
    
    async def patch(self,body: Optional[workbook_functions.WorkbookFunctions] = None, request_configuration: Optional[FunctionsRequestBuilderPatchRequestConfiguration] = None) -> Optional[workbook_functions.WorkbookFunctions]:
        """
        Update the navigation property functions in drives
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[workbook_functions.WorkbookFunctions]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, workbook_functions.WorkbookFunctions, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[FunctionsRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property functions for drives
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.DELETE
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[FunctionsRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get functions from drives
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def to_patch_request_information(self,body: Optional[workbook_functions.WorkbookFunctions] = None, request_configuration: Optional[FunctionsRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property functions in drives
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PATCH
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    @dataclass
    class FunctionsRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class FunctionsRequestBuilderGetQueryParameters():
        """
        Get functions from drives
        """
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            Args:
                originalName: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise Exception("original_name cannot be undefined")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
    
    @dataclass
    class FunctionsRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[FunctionsRequestBuilder.FunctionsRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class FunctionsRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

