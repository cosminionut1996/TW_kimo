CREATE OR REPLACE FUNCTION update_child_location(v_longitudine float, v_latitudine float, v_id_copil int)
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