CREATE OR REPLACE TRIGGER delete_on_user
    BEFORE
        DELETE
          ON utilizator

FOR EACH ROW
BEGIN
  CASE
    WHEN DELETING THEN
      DELETE from COPIL where id = ( SELECT ID_COPIL FROM LEGATURA WHERE ID_PARINTE= :old.id); 
      DELETE from ZONA where id = (SELECT ID_ZONA FROM LEGATURA_ZONA where ID_PARINTE= :old.id);
      
  END CASE;
END;