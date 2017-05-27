--------------------------------------------------------
--  File created - luni-martie-13-2017   
--------------------------------------------------------
--------------------------------------------------------
--  DDL for Trigger COPIL_ON_INSERT
--------------------------------------------------------

  CREATE OR REPLACE TRIGGER "HR"."COPIL_ON_INSERT" 
  BEFORE INSERT ON COPIL
  FOR EACH ROW
BEGIN
  SELECT COPIL_sequence.nextval
  INTO :new.id
  FROM dual;
END;
/
ALTER TRIGGER "HR"."COPIL_ON_INSERT" ENABLE;
--------------------------------------------------------
--  DDL for Trigger DEVICE_ON_INSERT
--------------------------------------------------------

  CREATE OR REPLACE TRIGGER "HR"."DEVICE_ON_INSERT" 
  BEFORE INSERT ON DEVICE
  FOR EACH ROW
BEGIN
  SELECT DEVICE_sequence.nextval
  INTO :new.id
  FROM dual;
END;
/
ALTER TRIGGER "HR"."DEVICE_ON_INSERT" ENABLE;
--------------------------------------------------------
--  DDL for Trigger UTILIZATOR_ON_INSERT
--------------------------------------------------------

  CREATE OR REPLACE TRIGGER "HR"."UTILIZATOR_ON_INSERT" 
  BEFORE INSERT ON UTILIZATOR
  FOR EACH ROW
BEGIN
  SELECT UTILIZATOR_sequence.nextval
  INTO :new.id
  FROM dual;
END;
/
ALTER TRIGGER "HR"."UTILIZATOR_ON_INSERT" ENABLE;
--------------------------------------------------------
--  DDL for Trigger ZONA_ON_INSERT
--------------------------------------------------------

  CREATE OR REPLACE TRIGGER "HR"."ZONA_ON_INSERT" 
  BEFORE INSERT ON ZONA
  FOR EACH ROW
BEGIN
  SELECT ZONA_sequence.nextval
  INTO :new.id
  FROM dual;
END;
/
ALTER TRIGGER "HR"."ZONA_ON_INSERT" ENABLE;
