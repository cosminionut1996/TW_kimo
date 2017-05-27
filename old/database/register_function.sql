CREATE OR REPLACE FUNCTION register(v_tip_subscriptie varchar2, v_nume varchar2, v_prenume varchar2, v_adresa varchar2, v_numar_telefon char, v_username varchar2, v_parola varchar2,v_data_expirare date)
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