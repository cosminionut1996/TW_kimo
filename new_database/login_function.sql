CREATE OR REPLACE FUNCTION login(username1 varchar2, password1 varchar2)
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