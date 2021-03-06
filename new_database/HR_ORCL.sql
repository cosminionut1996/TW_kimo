CREATE TABLE UTILIZATOR (
ID Integer,
TIP_SUBSCRIPTIE varchar(10),
NUME varchar(30),
PRENUME varchar(30),
ADRESA varchar(40),
NUMAR_TELEFON char(10),
USERNAME varchar(30) unique,
PAROLA varchar(30),
DATA_EXPIRARE Date,
PRIMARY KEY(ID),
CONSTRAINT CHK_UTILIZATOR CHECK (LENGTH(PAROLA) >5 AND (PAROLA LIKE '%0%' OR PAROLA LIKE '%1%' OR PAROLA LIKE '%2%' OR PAROLA LIKE '%3%' OR PAROLA LIKE '%4%' OR PAROLA LIKE '%5%' OR
PAROLA LIKE '%6%' OR PAROLA LIKE '%7%' OR PAROLA LIKE '%8%' OR PAROLA LIKE '%9%' ) )
);



CREATE TABLE COPIL (
ID Integer,
NUME varchar(30) ,
PRENUME varchar(30),
PRIMARY KEY (ID)
);

CREATE TABLE LEGATURA (
ID_PARINTE Integer,
ID_COPIL Integer,
FOREIGN KEY (ID_PARINTE) REFERENCES UTILIZATOR(ID),
FOREIGN KEY (ID_COPIL) REFERENCES COPIL(ID)
);

CREATE TABLE DEVICE (
ID Integer,
ID_COPIL Integer,
LONGITUDINE Float,
LATITUDINE Float,
PRIMARY KEY (ID),
FOREIGN KEY (ID_COPIL) REFERENCES COPIL(ID)
);

CREATE TABLE ZONA_APROBATA (
ID Integer,
ID_PARINTE Integer,
ID_COPIL Integer,
LONGITUDINE_1 Float,
LONGITUDINE_2 Float,
LATITUDINE_1 Float,
LATITUDINE_2 Float,
DENUMIRE varchar(30),
DESCRIERE varchar(30),
PRIMARY KEY(ID),
FOREIGN KEY(ID_PARINTE) REFERENCES UTILIZATOR (ID),
FOREIGN KEY(ID_COPIL) REFERENCES COPIL(ID)
);

CREATE TABLE ZONA_RISC (
ID Integer,
GRAD_PERICOL Integer,
TIP_PERICOL varchar (30),
LONGITUDINE_1 Float,
LONGITUDINE_2 Float,
LATITUDINE_1 Float,
LATITUDINE_2 Float,
PRIMARY KEY(ID),
CONSTRAINT CHK_ZONA CHECK ( GRAD_PERICOL < 11)
);
