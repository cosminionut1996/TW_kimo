CREATE OR REPLACE FUNCTION add_device(v_id_copil int)
RETURN int AS
v_id int;
BEGIN
select id_copil into v_id from device where id_copil like v_id_copil;
return 0;
  EXCEPTION
    when no_data_found then
      insert into device (id_copil, longitudine, latitudine)
        values (v_id_copil, 0.0,0.0);
        return 1;
END;