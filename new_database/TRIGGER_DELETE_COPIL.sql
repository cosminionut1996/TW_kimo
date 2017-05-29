CREATE OR REPLACE TRIGGER t
    BEFORE
        DELETE
          ON COPIL

FOR EACH ROW
BEGIN
  CASE
    WHEN DELETING THEN
      DELETE from DEVICE WHERE device.id_copil =  :old.id;
      DELETE from legatura WHERE legatura.id_copil =  :old.id;
  END CASE;
END;