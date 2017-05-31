create or replace PACKAGE body exportare_tabela IS

     PROCEDURE export_table
     is
  out_File  UTL_FILE.FILE_TYPE;
  result varchar2(10000);
  CURSOR get_objects is
  SELECT * FROM ALL_OBJECTS join dual on owner=sys_context( 'userenv', 'current_schema' )
    WHERE OBJECT_TYPE IN ('FUNCTION','PROCEDURE','PACKAGE','TRIGGER','VIEW','TABLE');
  
  
BEGIN
  out_File := utl_file.fopen ('MY_DIR', 'export.sql', 'w');
  
  FOR v_std_linie2 IN get_objects LOOP
    
    SELECT dbms_metadata.get_ddl( to_char(v_std_linie2.OBJECT_TYPE)||'', ''||to_char(v_std_linie2.OBJECT_NAME)||'' ) into result FROM DUAL;
    UTL_FILE.PUT_LINE(out_file,result);
    end loop;
  
END;
END exportare_tabela;
/