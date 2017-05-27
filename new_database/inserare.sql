Declare
    rows_inserted number := 0;
Begin
    Loop
        Begin
            -- INSERARE IN TABELA UTILIZATOR
            INSERT INTO UTILIZATOR(TIP_SUBSCRIPTIE,NUME,PRENUME,ADRESA,NUMAR_TELEFON,USERNAME,PAROLA,DATA_EXPIRARE)
            VALUES(dbms_random.string('L', 9),
            dbms_random.string('L', 10),
            dbms_random.string('L', 10),
            dbms_random.string('L', 10),
            '0'||'7'||to_char(trunc(dbms_random.value(11111111,99999999))),
            dbms_random.string('L', 10),
            dbms_random.string('L', 10)||'6',
            to_date('2010-01-01', 'yyyy-mm-dd')+trunc(dbms_random.value(1,1000)));
            
            --INSERARE IN TABELA COPIL
            INSERT INTO COPIL(NUME,PRENUME)
            VALUES(dbms_random.string('L', 10), dbms_random.string('L', 10));
            
            rows_inserted := rows_inserted + 1;
        Exception When DUP_VAL_ON_INDEX Then Null;
        End;
        exit when rows_inserted = 10000;
    End loop;
    commit;
End;