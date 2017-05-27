CREATE OR REPLACE FUNCTION delete_utilizator(v_username varchar2)
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