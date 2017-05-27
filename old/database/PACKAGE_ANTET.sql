create or replace PACKAGE UTILIZATOR_FUNC IS
      
     
     FUNCTION add_copil(v_nume varchar2, v_prenume varchar2, v_id_parinte int) RETURN int;
     FUNCTION login(username1 varchar2, password1 varchar2) RETURN int;
     FUNCTION register(v_tip_subscriptie varchar2, v_nume varchar2, v_prenume varchar2, v_adresa varchar2, v_numar_telefon char, v_username varchar2, v_parola varchar2,v_data_expirare date) RETURN int;

END UTILIZATOR_FUNC;