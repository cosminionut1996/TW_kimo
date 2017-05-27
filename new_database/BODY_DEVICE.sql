create or replace PACKAGE BODY DEVICE_FUNC IS

FUNCTION update_child_location(v_longitudine float, v_latitudine float, v_id_copil int)
RETURN int AS
result int;
v_id int;
BEGIN
    Select id_copil into v_id from device where id_copil=v_id_copil;
    UPDATE DEVICE set longitudine=v_longitudine, latitudine=v_latitudine where id_copil = v_id_copil;
    return 1;
    EXCEPTION
      when no_data_found then
        return 0;
END;

FUNCTION add_device(v_id_copil int)
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

END DEVICE_FUNC;