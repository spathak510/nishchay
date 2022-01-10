INSERT INTO mysite_country_master (country_id,country_name) VALUES ('1','India');


INSERT INTO mysite_state_master (state_id,state_desc,country_id) VALUES ('1','ANDAMAN & NICOBAR','1'),('2','ANDHRA PRADESH','1'),('3','ARUNACHAL PRADESH','1'),('4','ASSAM','1'),('5','BIHAR','1'),('6','CHANDIGARH','1'),('7','CHHATTISGARH','1'),('8','DADRA AND NAGAR HAVELI','1'),('9','DAMAN AND DIU','1'),('10','DELHI','1'),('11','GOA','1'),('12','GUJARAT','1'),('13','HARYANA','1'),('14','HIMACHAL PRADESH','1'),('15','JAMMU & KASHMIR','1'),('28','PUNJAB','1'),('34','UTTARAKHAND','1');


INSERT INTO mysite_district_master (district_id,district_desc,state_id) VALUES ('126','NORTH EAST DELHI','10'),('127','NORTH WEST DELHI','10'),('128','SOUTH DELHI','10'),('588','DEHRADUN','34'),('589','HARIDWAR','34'),('590','NAINITAL','34'),('1022','RUPNAGAR','28'),('1023','SAHIBZA AJIT SINGH NAGAR','28'),('1025','PATIALA','28');


INSERT INTO bank_bank_master (bank_id,bank_code,bank_name) VALUES ('1','1','ALLAHABAD BANK'), ('2','2','ANDHRA BANK'),('3','3','AXIS BANK LTD'),('4','4','BANK OF AMERICA'),('5','5','BANK OF BARODA'),('6','6','PUNJAB NATIONAL BANK'),('7','7','STATE BANK OF INDIA'),('8','8','ICICI');


INSERT INTO mysite_customer_details (customer_id,customer_name,customer_fname,customer_mname,customer_lname,customer_type,customer_dob,customer_constitution,customer_voter_id,customer_uid,customer_pan,customer_gender,customer_marital_status) VALUES ("476","PRADEEP","PRADEEP","","","I","1971-11-10","SALARIED","","460063179602","AGBPP4336P","M","M"), ("380","GUNJAN VERMA","GUNJAN","","VERMA","I","1973-11-08","INDIVIDUAL","","273509665060","ABUPV9550H","F","M"), ("120","SANGEETA","SANGEETA","","","I","1975-10-10","SELFEMP","","339678174965","JKOPS1827J","F","U"), ("223","ASHA KAKKAR","ASHA","","KAKKAR","I","1959-01-01","INDIVIDUAL","","707997484735","AKSPA6245M","F","M"), ("524","AAKANKSHA MEHRA","AAKANKSHA","","MEHRA","I","1992-09-15","SALARIED","","728360952448","CIMPM9698E","F","U");


INSERT INTO mysite_customer_address (customer_id,address_type,bptype,address_line1,address_line2,address_line3,country_id,state_id,district_id,pin_code,primary_phone,communication_address) VALUES ("476","RESIDENCE","CS","FLAT NO-505, MAGNOLIA TOWER","MAYFAIR SOCIETY, SECTOR-70","SECTOR 70 S.A.S. NAGAR","1","28","1023","160071","9779033929","Y"), ("380","RESIDENCE","CS","FLAT NO-505, MAGNOLIA TOWER","MAYFAIR SOCIETY, SECTOR-70","SECTOR 70 S.A.S. NAGAR","1","28","1023","160071","9779133929","Y"), ("120","OFFICE","CS","TRANSIT CAMP, SHIMLA BAHADUR","FULSUNGA, UDHAM SINGH NAGAR","T.C. RUDARPUR","1","34","127","263153","9988998800","Y"), ("223","OFFICE","CS","J-5/157, GROUND FLOOR","RAJOURI GARDEN","TAGORE GARDEN, WEST DELHI","1","34","588","248001","8877887700","N"), ("524","RESIDENCE","CS","A-1/204","PRINTERS APARTMENT","SECTOR-13, ROHINI","1","10","127","110085","7766776600","Y");


INSERT INTO mysite_los_details (deal_id,customer_id,loan_id,deal_customer_role_type,deal_customer_type,existing_customer,bank_name_id,bank_branch,account_no,account_type,guarantee_amount) VALUES ("250501","476","12","PRAPPL","I","N","6","12","123456","3","₹ 0"), ("250501","380","12","GUARANTOR","I","N","6","12","112233","3","₹ 1,00,000"), ("250502","120","15","PRAPPL","I","N","7","30","98765","3","₹ 0"), ("250502","223","15","COAPPL","I","N","7","30","78789","3","₹ 0"), ("250502","524","15","GUARANTOR","I","N","8","42","102938","3","₹ 2,50,000");


INSERT INTO mysite_document_type_master (document_id,document_name) VALUES ("1","PAN"), ("2","AADHAR"), ("3","ITR-V"), ("4","FORM16"), ("5","FORM26AS"), ("6","BANK STATEMENT");


INSERT INTO mysite_processed_document_details (deal_id,customer_id,loan_id,document_id,upload_status) VALUES ("250501","476","12","1","N"), ("250501","380","12","1","N"), ("250502","120","15","1","N"), ("250502","223","15","1","N"), ("250502","524","15","1","N");


INSERT INTO mysite_unprocessed_document_details (deal_id,customer_id,loan_id,document_id,upload_status) VALUES ("250501","476","12","1","N"), ("250501","380","12","1","N"), ("250502","120","15","1","N"), ("250502","223","15","1","N"), ("250502","524","15","1","N");
