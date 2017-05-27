create or replace PACKAGE DEVICE_FUNC IS

       FUNCTION add_device(v_id_copil int) RETURN int;
       FUNCTION update_child_location(v_longitudine float, v_latitudine float, v_id_copil int) RETURN int;
     
END DEVICE_FUNC;