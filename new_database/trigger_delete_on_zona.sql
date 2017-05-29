CREATE OR REPLACE TRIGGER delete_on_zona
    BEFORE
        DELETE
          ON ZONA

FOR EACH ROW
BEGIN
  CASE
    WHEN DELETING THEN
      DELETE from ZONA_APROBATA WHERE zona_aprobata.id =  :old.id;
      DELETE from LEGATURA_ZONA WHERE LEGATURA_ZONA.id_zona =  :old.id;
    
      
  END CASE;
END;