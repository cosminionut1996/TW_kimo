--------------------------------------------------------
--  File created - duminic�-martie-12-2017   
--------------------------------------------------------
--------------------------------------------------------
--  DDL for View EMP_DETAILS_VIEW
--------------------------------------------------------

  CREATE OR REPLACE FORCE VIEW "HR"."EMP_DETAILS_VIEW" ("EMPLOYEE_ID", "JOB_ID", "MANAGER_ID", "DEPARTMENT_ID", "LOCATION_ID", "COUNTRY_ID", "FIRST_NAME", "LAST_NAME", "SALARY", "COMMISSION_PCT", "DEPARTMENT_NAME", "JOB_TITLE", "CITY", "STATE_PROVINCE", "COUNTRY_NAME", "REGION_NAME") AS 
  SELECT
  e.employee_id,
  e.job_id,
  e.manager_id,
  e.department_id,
  d.location_id,
  l.country_id,
  e.first_name,
  e.last_name,
  e.salary,
  e.commission_pct,
  d.department_name,
  j.job_title,
  l.city,
  l.state_province,
  c.country_name,
  r.region_name
FROM
  employees e,
  departments d,
  jobs j,
  locations l,
  countries c,
  regions r
WHERE e.department_id = d.department_id
  AND d.location_id = l.location_id
  AND l.country_id = c.country_id
  AND c.region_id = r.region_id
  AND j.job_id = e.job_id
WITH READ ONLY;
--------------------------------------------------------
--  DDL for Table UTILIZATOR
--------------------------------------------------------

  CREATE TABLE "HR"."UTILIZATOR" 
   (	"ID" NUMBER(*,0), 
	"TIP_SUBSCRIPTIE" VARCHAR2(10 BYTE), 
	"NUME" VARCHAR2(30 BYTE), 
	"PRENUME" VARCHAR2(30 BYTE), 
	"ADRESA" VARCHAR2(40 BYTE), 
	"NUMAR_TELEFON" CHAR(10 BYTE), 
	"USERNAME" VARCHAR2(30 BYTE), 
	"PAROLA" VARCHAR2(30 BYTE), 
	"DATA_EXPIRARE" DATE
   ) SEGMENT CREATION IMMEDIATE 
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1 BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;
--------------------------------------------------------
--  DDL for Table LEGATURA
--------------------------------------------------------

  CREATE TABLE "HR"."LEGATURA" 
   (	"ID_PARINTE" NUMBER(*,0), 
	"ID_COPIL" NUMBER(*,0)
   ) SEGMENT CREATION IMMEDIATE 
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1 BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;
--------------------------------------------------------
--  DDL for Table ZONA_RISC
--------------------------------------------------------

  CREATE TABLE "HR"."ZONA_RISC" 
   (	"ID" NUMBER(*,0), 
	"GRAD_PERICOL" NUMBER(*,0), 
	"TIP_PERICOL" VARCHAR2(30 BYTE), 
	"LONGITUDINE_1" FLOAT(126), 
	"LONGITUDINE_2" FLOAT(126), 
	"LATITUDINE_1" FLOAT(126), 
	"LATITUDINE_2" FLOAT(126)
   ) SEGMENT CREATION IMMEDIATE 
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1 BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;
--------------------------------------------------------
--  DDL for Table COPIL
--------------------------------------------------------

  CREATE TABLE "HR"."COPIL" 
   (	"ID" NUMBER(*,0), 
	"NUME" VARCHAR2(30 BYTE), 
	"PRENUME" VARCHAR2(30 BYTE)
   ) SEGMENT CREATION IMMEDIATE 
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1 BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;
--------------------------------------------------------
--  DDL for Table DEVICE
--------------------------------------------------------

  CREATE TABLE "HR"."DEVICE" 
   (	"ID" NUMBER(*,0), 
	"ID_COPIL" NUMBER(*,0), 
	"LONGITUDINE" FLOAT(126), 
	"LATITUDINE" FLOAT(126)
   ) SEGMENT CREATION IMMEDIATE 
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1 BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;
--------------------------------------------------------
--  DDL for Table ZONA_APROBATA
--------------------------------------------------------

  CREATE TABLE "HR"."ZONA_APROBATA" 
   (	"ID" NUMBER(*,0), 
	"ID_PARINTE" NUMBER(*,0), 
	"ID_COPIL" NUMBER(*,0), 
	"LONGITUDINE_1" FLOAT(126), 
	"LONGITUDINE_2" FLOAT(126), 
	"LATITUDINE_1" FLOAT(126), 
	"LATITUDINE_2" FLOAT(126), 
	"DENUMIRE" VARCHAR2(30 BYTE), 
	"DESCRIERE" VARCHAR2(30 BYTE)
   ) SEGMENT CREATION IMMEDIATE 
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1 BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;
--------------------------------------------------------
--  DDL for Sequence DEPARTMENTS_SEQ
--------------------------------------------------------

   CREATE SEQUENCE  "HR"."DEPARTMENTS_SEQ"  MINVALUE 1 MAXVALUE 9990 INCREMENT BY 10 START WITH 280 NOCACHE  NOORDER  NOCYCLE ;
--------------------------------------------------------
--  DDL for Sequence EMPLOYEES_SEQ
--------------------------------------------------------

   CREATE SEQUENCE  "HR"."EMPLOYEES_SEQ"  MINVALUE 1 MAXVALUE 9999999999999999999999999999 INCREMENT BY 1 START WITH 207 NOCACHE  NOORDER  NOCYCLE ;
--------------------------------------------------------
--  DDL for Sequence LOCATIONS_SEQ
--------------------------------------------------------

   CREATE SEQUENCE  "HR"."LOCATIONS_SEQ"  MINVALUE 1 MAXVALUE 9900 INCREMENT BY 100 START WITH 3300 NOCACHE  NOORDER  NOCYCLE ;
REM INSERTING into HR.UTILIZATOR
SET DEFINE OFF;
REM INSERTING into HR.LEGATURA
SET DEFINE OFF;
REM INSERTING into HR.ZONA_RISC
SET DEFINE OFF;
REM INSERTING into HR.COPIL
SET DEFINE OFF;
REM INSERTING into HR.DEVICE
SET DEFINE OFF;
REM INSERTING into HR.ZONA_APROBATA
SET DEFINE OFF;
--------------------------------------------------------
--  DDL for Index SYS_C007132
--------------------------------------------------------

  CREATE UNIQUE INDEX "HR"."SYS_C007132" ON "HR"."UTILIZATOR" ("ID") 
  PCTFREE 10 INITRANS 2 MAXTRANS 255 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1 BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;
--------------------------------------------------------
--  DDL for Index SYS_C007133
--------------------------------------------------------

  CREATE UNIQUE INDEX "HR"."SYS_C007133" ON "HR"."UTILIZATOR" ("USERNAME") 
  PCTFREE 10 INITRANS 2 MAXTRANS 255 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1 BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;
--------------------------------------------------------
--  DDL for Index SYS_C007143
--------------------------------------------------------

  CREATE UNIQUE INDEX "HR"."SYS_C007143" ON "HR"."ZONA_RISC" ("ID") 
  PCTFREE 10 INITRANS 2 MAXTRANS 255 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1 BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;
--------------------------------------------------------
--  DDL for Index SYS_C007134
--------------------------------------------------------

  CREATE UNIQUE INDEX "HR"."SYS_C007134" ON "HR"."COPIL" ("ID") 
  PCTFREE 10 INITRANS 2 MAXTRANS 255 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1 BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;
--------------------------------------------------------
--  DDL for Index SYS_C007137
--------------------------------------------------------

  CREATE UNIQUE INDEX "HR"."SYS_C007137" ON "HR"."DEVICE" ("ID") 
  PCTFREE 10 INITRANS 2 MAXTRANS 255 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1 BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;
--------------------------------------------------------
--  DDL for Index SYS_C007139
--------------------------------------------------------

  CREATE UNIQUE INDEX "HR"."SYS_C007139" ON "HR"."ZONA_APROBATA" ("ID") 
  PCTFREE 10 INITRANS 2 MAXTRANS 255 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1 BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;
--------------------------------------------------------
--  DDL for Procedure ADD_JOB_HISTORY
--------------------------------------------------------
set define off;

  CREATE OR REPLACE PROCEDURE "HR"."ADD_JOB_HISTORY" 
  (  p_emp_id          job_history.employee_id%type
   , p_start_date      job_history.start_date%type
   , p_end_date        job_history.end_date%type
   , p_job_id          job_history.job_id%type
   , p_department_id   job_history.department_id%type
   )
IS
BEGIN
  INSERT INTO job_history (employee_id, start_date, end_date,
                           job_id, department_id)
    VALUES(p_emp_id, p_start_date, p_end_date, p_job_id, p_department_id);
END add_job_history;

/
--------------------------------------------------------
--  DDL for Procedure SECURE_DML
--------------------------------------------------------
set define off;

  CREATE OR REPLACE PROCEDURE "HR"."SECURE_DML" 
IS
BEGIN
  IF TO_CHAR (SYSDATE, 'HH24:MI') NOT BETWEEN '08:00' AND '18:00'
        OR TO_CHAR (SYSDATE, 'DY') IN ('SAT', 'SUN') THEN
	RAISE_APPLICATION_ERROR (-20205,
		'You may only make changes during normal office hours');
  END IF;
END secure_dml;

/
--------------------------------------------------------
--  Constraints for Table UTILIZATOR
--------------------------------------------------------

  ALTER TABLE "HR"."UTILIZATOR" ADD UNIQUE ("USERNAME")
  USING INDEX PCTFREE 10 INITRANS 2 MAXTRANS 255 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1 BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS"  ENABLE;
  ALTER TABLE "HR"."UTILIZATOR" ADD PRIMARY KEY ("ID")
  USING INDEX PCTFREE 10 INITRANS 2 MAXTRANS 255 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1 BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS"  ENABLE;
  ALTER TABLE "HR"."UTILIZATOR" ADD CONSTRAINT "CHK_UTILIZATOR" CHECK (LENGTH(PAROLA) >5 AND (PAROLA LIKE '%0%' OR PAROLA LIKE '%1%' OR PAROLA LIKE '%2%' OR PAROLA LIKE '%3%' OR PAROLA LIKE '%4%' OR PAROLA LIKE '%5%' OR
PAROLA LIKE '%6%' OR PAROLA LIKE '%7%' OR PAROLA LIKE '%8%' OR PAROLA LIKE '%9%' ) ) ENABLE;
--------------------------------------------------------
--  Constraints for Table ZONA_RISC
--------------------------------------------------------

  ALTER TABLE "HR"."ZONA_RISC" ADD PRIMARY KEY ("ID")
  USING INDEX PCTFREE 10 INITRANS 2 MAXTRANS 255 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1 BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS"  ENABLE;
  ALTER TABLE "HR"."ZONA_RISC" ADD CONSTRAINT "CHK_ZONA" CHECK ( GRAD_PERICOL < 11 AND GRAD_PERICOL > -1) ENABLE;
--------------------------------------------------------
--  Constraints for Table COPIL
--------------------------------------------------------

  ALTER TABLE "HR"."COPIL" ADD PRIMARY KEY ("ID")
  USING INDEX PCTFREE 10 INITRANS 2 MAXTRANS 255 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1 BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS"  ENABLE;
--------------------------------------------------------
--  Constraints for Table DEVICE
--------------------------------------------------------

  ALTER TABLE "HR"."DEVICE" ADD PRIMARY KEY ("ID")
  USING INDEX PCTFREE 10 INITRANS 2 MAXTRANS 255 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1 BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS"  ENABLE;
--------------------------------------------------------
--  Constraints for Table ZONA_APROBATA
--------------------------------------------------------

  ALTER TABLE "HR"."ZONA_APROBATA" ADD PRIMARY KEY ("ID")
  USING INDEX PCTFREE 10 INITRANS 2 MAXTRANS 255 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1 BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS"  ENABLE;
--------------------------------------------------------
--  Ref Constraints for Table LEGATURA
--------------------------------------------------------

  ALTER TABLE "HR"."LEGATURA" ADD FOREIGN KEY ("ID_PARINTE")
	  REFERENCES "HR"."UTILIZATOR" ("ID") ENABLE;
  ALTER TABLE "HR"."LEGATURA" ADD FOREIGN KEY ("ID_COPIL")
	  REFERENCES "HR"."COPIL" ("ID") ENABLE;
--------------------------------------------------------
--  Ref Constraints for Table DEVICE
--------------------------------------------------------

  ALTER TABLE "HR"."DEVICE" ADD FOREIGN KEY ("ID_COPIL")
	  REFERENCES "HR"."COPIL" ("ID") ENABLE;
--------------------------------------------------------
--  Ref Constraints for Table ZONA_APROBATA
--------------------------------------------------------

  ALTER TABLE "HR"."ZONA_APROBATA" ADD FOREIGN KEY ("ID_PARINTE")
	  REFERENCES "HR"."UTILIZATOR" ("ID") ENABLE;
  ALTER TABLE "HR"."ZONA_APROBATA" ADD FOREIGN KEY ("ID_COPIL")
	  REFERENCES "HR"."COPIL" ("ID") ENABLE;
