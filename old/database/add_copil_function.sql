CREATE OR REPLACE FUNCTION add_copil(v_nume varchar2, v_prenume varchar2, v_id_parinte int)
RETURN int AS
v_id_copil int;

BEGIN
  insert into copil(nume, prenume)
    values (v_nume, v_prenume);
  SELECT id into v_id_copil FROM (
    SELECT * FROM copil where nume like v_nume and prenume like v_prenume ORDER BY id DESC
) WHERE ROWNUM = 1;

  insert into legatura(id_parinte, id_copil)
    values(v_id_parinte, v_id_copil);
  insert into device ( id_copil, longitudine, latitudine)
    values(v_id_copil, 0, 0);
    return 1;
END;