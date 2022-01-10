# Generated by Django 3.0.9 on 2020-10-01 07:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Quarters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quater', models.CharField(blank=True, max_length=255)),
                ('reciept_number', models.CharField(blank=True, max_length=255)),
                ('amount_credited', models.CharField(blank=True, max_length=255)),
                ('tax_deducted', models.CharField(blank=True, max_length=255)),
                ('tax_remitted', models.CharField(blank=True, max_length=255)),
                ('deal_id', models.CharField(blank=True, max_length=255)),
                ('customer_id', models.CharField(blank=True, max_length=255)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('last_modification_time', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='f1_qtr_created_by', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='f1_qtr_last_modified_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Partb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gross_salary_salary_as_per_provisions_contained_in_section_17_1', models.CharField(blank=True, max_length=255)),
                ('gross_salary_value_of_perquisites_under_section_17_2', models.CharField(blank=True, max_length=255)),
                ('gross_salary_profits_in_lieu_of_salary_under_section_17_3', models.CharField(blank=True, max_length=255)),
                ('gross_salary_total', models.CharField(blank=True, max_length=255)),
                ('gross_salary_reported_total_amount_of_salary_received_from_other_employers', models.CharField(blank=True, db_column='gr_sal_rprtd_total_amount_of_sal_received_from_other_employers', max_length=255)),
                ('less_allowance_to_the_extent_exempt_under_section_10', models.CharField(blank=True, max_length=255)),
                ('travel_concession_or_assistance_under_section_10_5', models.CharField(blank=True, max_length=255)),
                ('death_cum_retirement_gratuity_under_section_10_10', models.CharField(blank=True, max_length=255)),
                ('commuted_value_of_pension_under_section_10_10a', models.CharField(blank=True, max_length=255)),
                ('cash_equivalent_of_leave_salary_encashment_under_section_10_10aa', models.CharField(blank=True, max_length=255)),
                ('house_rent_allowance_under_section_10_13a', models.CharField(blank=True, max_length=255)),
                ('amount_of_any_other_exemption_under_section_10', models.CharField(blank=True, max_length=255)),
                ('total_amount_of_any_other_exemption_under_section_10', models.CharField(blank=True, max_length=255)),
                ('total_amount_of_exemption_claimed_under_section_10', models.CharField(blank=True, max_length=255)),
                ('total_amount_of_salary_received_from_current_employer_1d_minus_2h', models.CharField(blank=True, db_column='total_amount_of_sal_received_from_current_employer_1d_minus_2h', max_length=255)),
                ('standard_deduction_under_section_16_ia', models.CharField(blank=True, max_length=255)),
                ('entertainment_allowance_under_section_16_ii', models.CharField(blank=True, max_length=255)),
                ('tax_on_employment_under_section_16_iii', models.CharField(blank=True, max_length=255)),
                ('total_amount_of_deductions_under_section_16_4a_plus_4b_plus_4c', models.CharField(blank=True, max_length=255)),
                ('income_chargeable_under_the_head_salaries_3_plus_1e_minus_5', models.CharField(blank=True, max_length=255)),
                ('income_or_admissible_loss_from_house_property_reported_by_employee_offered_for_tds', models.CharField(blank=True, db_column='incm_or_admsble_los_frm_house_prprty_rprtd_by_empyee_ofr_for_tds', max_length=255)),
                ('income_under_the_head_other_sources_offered_for_tds', models.CharField(blank=True, max_length=255)),
                ('total_amount_of_other_income_reported_by_the_employee_7a_plus_7b', models.CharField(blank=True, max_length=255)),
                ('gross_total_income_6_plus_8', models.CharField(blank=True, max_length=255)),
                ('deduction_in_respect_of_life_insurance_premia_contributions_to_provident_fund_etc_under_section_80c_gross_amount', models.CharField(blank=True, db_column='ductn_in_rspct_of_lfe_inc_prmia_cntrbn_2_pf_undr_sec_80c_gr_amnt', max_length=255)),
                ('deduction_in_respect_of_contribution_to_certain_pension_funds_under_section_80ccc_gross_amount', models.CharField(blank=True, db_column='ductn_in_rspct_of_ctrbtn_2_crtn_pnsn_fnds_undr_sec_80ccc_gr_amnt', max_length=255)),
                ('deduction_in_respect_of_contribution_by_taxpayer_to_pension_scheme_under_section_80ccd_1_gross_amount', models.CharField(blank=True, db_column='dctn_in_rsp_of_cntbn_by_txpr_2_pnsn_scm_undr_sec_80ccd_1_gr_amnt', max_length=255)),
                ('total_deduction_under_section_80c_80ccc_and_80ccd_1_gross_amount', models.CharField(blank=True, max_length=255)),
                ('deductions_in_respect_of_amount_paid_deposited_to_notified_pension_scheme_under_section_80ccd_1b_gross_amount', models.CharField(blank=True, db_column='dtn_in_rsp_of_amnt_pd_dpt_2_ntfd_pnsn_scm_ndr_sc_80ccd_1b_gr_amt', max_length=255)),
                ('deduction_in_respect_of_contribution_by_employer_to_pension_scheme_under_section_80ccd_2_gross_amount', models.CharField(blank=True, db_column='dtn_in_rsp_of_cntrbtn_by_empyr_2_pnsn_scm_ndr_sc_80ccd_2_gr_amt', max_length=255)),
                ('deduction_in_respect_of_health_insurance_premia_under_section_80d_gross_amount', models.CharField(blank=True, db_column='dtn_in_rsp_of_hlt_insrnc_premia_ndr_sc_80d_gr_amt', max_length=255)),
                ('deduction_in_respect_of_interest_on_loan_taken_for_higher_education_under_section_80e_gross_amount', models.CharField(blank=True, db_column='dtn_in_rsp_of_intst_on_ln_tkn_for_hghr_edu_ndr_sec_80e_gr_amt', max_length=255)),
                ('total_deduction_in_respect_of_donations_to_certain_funds_charitable_institutions_etc_under_section_80g_gross_amount', models.CharField(blank=True, db_column='ttl_dtn_in_rsp_of_dntn_2_crtn_fnds_crtbl_ins_ndr_sc_80g_gr_amt', max_length=255)),
                ('deduction_in_respect_of_interest_on_deposits_in_savings_account_under_section_80tta_gross_amount', models.CharField(blank=True, db_column='dctn_in_rsp_of_inrst_on_dpst_in_svng_acnt_ndr_sec_80tta_gr_amt', max_length=255)),
                ('amount_deductible_under_any_other_provisions_of_chapter_vi_a_gross_amount', models.CharField(blank=True, db_column='amt_deductible_under_any_other_provisions_of_cptr_vi_a_gr_amt', max_length=255)),
                ('total_of_amount_deductible_under_any_other_provisions_of_chapter_vi_a', models.CharField(blank=True, db_column='ttl_of_amt_deductible_under_any_other_provisions_of_chapter_vi_a', max_length=255)),
                ('aggregate_of_deductible_amount_under_chapter_vi_a', models.CharField(blank=True, max_length=255)),
                ('total_taxable_income_9_minus_11', models.CharField(blank=True, max_length=255)),
                ('tax_on_total_income', models.CharField(blank=True, max_length=255)),
                ('rebate_under_section_87a_if_applicable', models.CharField(blank=True, max_length=255)),
                ('surcharge_wherever_applicable', models.CharField(blank=True, max_length=255)),
                ('health_and_education_cess', models.CharField(blank=True, max_length=255)),
                ('tax_payable_13_plus_15_plus_16_minus_14', models.CharField(blank=True, max_length=255)),
                ('relief_under_section_89', models.CharField(blank=True, max_length=255)),
                ('net_tax_payable_17_minus_18', models.CharField(blank=True, max_length=255)),
                ('deal_id', models.CharField(blank=True, max_length=255)),
                ('customer_id', models.CharField(blank=True, max_length=255)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('last_modification_time', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='f1_pb_created_by', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='f1_pb_last_modified_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certification_no', models.CharField(blank=True, max_length=255, null=True)),
                ('last_updated_on', models.DateField()),
                ('pan_of_the_deductor', models.CharField(blank=True, max_length=255)),
                ('tan_of_the_deductor', models.CharField(blank=True, max_length=255)),
                ('pan_of_the_employee', models.CharField(blank=True, max_length=255)),
                ('assessment_year', models.CharField(blank=True, max_length=255)),
                ('period_with_the_employer_from', models.DateField()),
                ('period_with_the_employer_to', models.DateField()),
                ('employer_name', models.CharField(blank=True, max_length=255)),
                ('employer_address', models.CharField(blank=True, max_length=255)),
                ('employee_name', models.CharField(blank=True, max_length=255)),
                ('employee_address', models.CharField(blank=True, max_length=255)),
                ('deal_id', models.CharField(blank=True, max_length=255)),
                ('customer_id', models.CharField(blank=True, max_length=255)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('last_modification_time', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='f1_info_created_by', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='f1_info_last_modified_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Challans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tax_deposited', models.CharField(blank=True, max_length=255)),
                ('bsr_code', models.CharField(blank=True, max_length=255)),
                ('tax_deposited_date', models.DateField()),
                ('challan_serial_no', models.CharField(blank=True, max_length=255)),
                ('status_match_oltas', models.CharField(blank=True, max_length=255)),
                ('deal_id', models.CharField(blank=True, max_length=255)),
                ('customer_id', models.CharField(blank=True, max_length=255)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('last_modification_time', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='f1_cln_created_by', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='f1_cln_last_modified_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
