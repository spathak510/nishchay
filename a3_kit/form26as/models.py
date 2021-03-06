from django.db import models
from django.contrib.auth.models import User


class AsseseeDetails(models.Model):
    pan = models.CharField(max_length=255, blank=True, null=True)
    financial_year = models.CharField(max_length=255, blank=True, null=True)
    assessment_year = models.CharField(max_length=255, blank=True, null=True)
    current_pan_status = models.CharField(max_length=255, blank=True, null=True)
    name_of_assessee = models.CharField(max_length=255, blank=True, null=True)
    address_of_assessee = models.CharField(max_length=255, blank=True, null=True)
    deal_id = models.CharField(max_length=255, blank=True)
    customer_id = models.CharField(max_length=255, blank=True)
    created_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, related_name="f2_ad_created_by")
    creation_time = models.DateTimeField(auto_now_add=True)
    last_modified_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, related_name="f2_ad_last_modified_by")
    last_modification_time = models.DateTimeField(auto_now=True)
    image_name = models.CharField(max_length=255, blank=True)



class PartA(models.Model):
    sr_no = models.CharField(max_length=255, blank=True, null=True)
    section_1 = models.CharField(max_length=255, blank=True, null=True)
    tan_of_deductor = models.CharField(max_length=255, blank=True, null=True)
    amount_paid_credited = models.CharField(max_length=255, blank=True, null=True)
    tax_deducted = models.CharField(max_length=255, blank=True, null=True)
    tds_deposited = models.CharField(max_length=255, blank=True, null=True)
    remarks	= models.CharField(max_length=255, blank=True, null=True)
    transaction_date = models.CharField(max_length=255, blank=True, null=True)	
    status_of_booking = models.CharField(max_length=255, blank=True, null=True)
    date_of_booking	 = models.CharField(max_length=255, blank=True, null=True)
    name_of_deductor = models.CharField(max_length=255, blank=True, null=True)
    total_amount_paid_credited	= models.CharField(max_length=255, blank=True, null=True)
    total_tax_deducted = models.CharField(max_length=255, blank=True, null=True)	
    total_tds_deposited = models.CharField(max_length=255, blank=True, null=True)	
    pan	= models.CharField(max_length=255, blank=True, null=True)
    name_of_assessee = models.CharField(max_length=255, blank=True, null=True)
    assessment_year = models.CharField(max_length=255, blank=True, null=True)
    deal_id = models.CharField(max_length=255, blank=True)
    customer_id = models.CharField(max_length=255, blank=True)
    created_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, related_name="f2_pa_created_by")
    creation_time = models.DateTimeField(auto_now_add=True)
    last_modified_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, related_name="f2_pa_last_modified_by")
    last_modification_time = models.DateTimeField(auto_now=True)


class PartB(models.Model):
    sr_no = models.CharField(max_length=255, blank=True, null=True)
    section_1 = models.CharField(max_length=255, blank=True, null=True)
    tan_of_collector = models.CharField(max_length=255, blank=True, null=True)
    amount_paid_debited = models.CharField(max_length=255, blank=True, null=True)
    tax_collected = models.CharField(max_length=255, blank=True, null=True)
    tcs_deposited = models.CharField(max_length=255, blank=True, null=True)
    remarks	= models.CharField(max_length=255, blank=True, null=True)
    transaction_date = models.CharField(max_length=255, blank=True, null=True)	
    status_of_booking = models.CharField(max_length=255, blank=True, null=True)
    date_of_booking	 = models.CharField(max_length=255, blank=True, null=True)
    name_of_collector = models.CharField(max_length=255, blank=True, null=True)
    total_amount_paid_debited	= models.CharField(max_length=255, blank=True, null=True)
    total_tax_collected = models.CharField(max_length=255, blank=True, null=True)	
    total_tcs_deposited = models.CharField(max_length=255, blank=True, null=True)	
    pan	= models.CharField(max_length=255, blank=True, null=True)
    name_of_assessee = models.CharField(max_length=255, blank=True, null=True)
    assessment_year = models.CharField(max_length=255, blank=True, null=True)
    deal_id = models.CharField(max_length=255, blank=True)
    customer_id = models.CharField(max_length=255, blank=True)
    created_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, related_name="f2_pb_created_by")
    creation_time = models.DateTimeField(auto_now_add=True)
    last_modified_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, related_name="f2_pb_last_modified_by")
    last_modification_time = models.DateTimeField(auto_now=True)


class PartC(models.Model):
    sr = models.CharField(max_length=255, blank=True, null=True)
    major_head = models.CharField(max_length=255, blank=True, null=True)
    minor_head = models.CharField(max_length=255, blank=True, null=True)
    tax = models.CharField(max_length=255, blank=True, null=True)
    surcharge = models.CharField(max_length=255, blank=True, null=True)
    education_cess = models.CharField(max_length=255, blank=True, null=True)
    others = models.CharField(max_length=255, blank=True, null=True)
    total_tax = models.CharField(max_length=255, blank=True, null=True)
    bsr_code = models.CharField(max_length=255, blank=True, null=True)	
    date_of_deposit = models.CharField(max_length=255, blank=True, null=True)
    challan_serial_number = models.CharField(max_length=255, blank=True, null=True)
    remarks = models.CharField(max_length=255, blank=True, null=True)
    pan	= models.CharField(max_length=255, blank=True, null=True)
    name_of_assessee = models.CharField(max_length=255, blank=True, null=True)
    assessment_year = models.CharField(max_length=255, blank=True, null=True)
    deal_id = models.CharField(max_length=255, blank=True)
    customer_id = models.CharField(max_length=255, blank=True)
    created_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, related_name="f2_pc_created_by")
    creation_time = models.DateTimeField(auto_now_add=True)
    last_modified_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, related_name="f2_pc_last_modified_by")
    last_modification_time = models.DateTimeField(auto_now=True)


class PartD(models.Model):
    sr = models.CharField(max_length=255, blank=True, null=True)
    assessment_year_refund = models.CharField(max_length=255, blank=True, null=True)
    mode = models.CharField(max_length=255, blank=True, null=True)
    refund_issued = models.CharField(max_length=255, blank=True, null=True)
    nature_of_refund = models.CharField(max_length=255, blank=True, null=True)
    amount_of_refund = models.CharField(max_length=255, blank=True, null=True)
    interest = models.CharField(max_length=255, blank=True, null=True)
    date_of_payment = models.CharField(max_length=255, blank=True, null=True)
    remarks = models.CharField(max_length=255, blank=True, null=True)
    pan	= models.CharField(max_length=255, blank=True, null=True)
    name_of_assessee = models.CharField(max_length=255, blank=True, null=True)
    assessment_year = models.CharField(max_length=255, blank=True, null=True)
    deal_id = models.CharField(max_length=255, blank=True)
    customer_id = models.CharField(max_length=255, blank=True)
    created_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, related_name="f2_pd_created_by")
    creation_time = models.DateTimeField(auto_now_add=True)
    last_modified_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, related_name="f2_pd_last_modified_by")
    last_modification_time = models.DateTimeField(auto_now=True)



class PartG(models.Model):
    sr = models.CharField(max_length=255, blank=True, null=True)
    financial_year = models.CharField(max_length=255, blank=True, null=True)
    short_payment = models.CharField(max_length=255, blank=True, null=True)
    short_deduction = models.CharField(max_length=255, blank=True, null=True)
    interest_on_tds = models.CharField(max_length=255, blank=True, null=True)
    interest_on_tds_1 = models.CharField(max_length=255, blank=True, null=True)
    late_filing_fee_us = models.CharField(max_length=255, blank=True, null=True)
    interest_us = models.CharField(max_length=255, blank=True, null=True)
    total_default = models.CharField(max_length=255, blank=True, null=True)
    pan	= models.CharField(max_length=255, blank=True, null=True)
    name_of_assessee = models.CharField(max_length=255, blank=True, null=True)
    assessment_year = models.CharField(max_length=255, blank=True, null=True)
    deal_id = models.CharField(max_length=255, blank=True)
    customer_id = models.CharField(max_length=255, blank=True)
    created_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, related_name="f2_pg_created_by")
    creation_time = models.DateTimeField(auto_now_add=True)
    last_modified_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, related_name="f2_pg_last_modified_by")
    last_modification_time = models.DateTimeField(auto_now=True)