create or replace PACKAGE BODY UTILIZATOR_FUNC IS

FUNCTION add_copil(v_nume varchar2, v_prenume varchar2, v_id_parinte int)
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

FUNCTION login(username1 varchar2, password1 varchar2)
RETURN int AS
username2 varchar(50);
password2 varchar(50);
CURSOR get_linie is
      Select * from UTILIZATOR where username like username1;
v_std get_linie%ROWTYPE;
BEGIN
    for v_std in get_linie LOOP
      if v_std.parola like password1 then
        return 1;
      end if;
    END LOOP;
    return 0;
END;

FUNCTION register(v_tip_subscriptie varchar2, v_nume varchar2, v_prenume varchar2, v_adresa varchar2, v_numar_telefon char, v_username varchar2, v_parola varchar2,v_data_expirare date)
RETURN int AS
username2 varchar(40);
BEGIN
select username into username2 from utilizator where username like v_username or numar_telefon like v_numar_telefon;
return 0;
exception
  when no_data_found then 
    insert into utilizator ( TIP_SUBSCRIPTIE, NUME, PRENUME, ADRESA, NUMAR_TELEFON, USERNAME, PAROLA, DATA_EXPIRARE)
    VALUES (v_tip_subscriptie, v_nume, v_prenume, v_adresa, v_numar_telefon,v_username, v_parola, v_data_expirare);
    return 1;
  
END;

FUNCTION delete_utilizator(v_username varchar2)
RETURN int AS

v_user varchar2(30);
BEGIN
  Select username into v_user from utilizator where username like v_username;
  delete from utilizator where username = v_username;
  return 1;
  EXCEPTION
    when no_data_found then
      return 0;

END;

END UTILIZATOR_FUNC;