import sqlite3

# connect to new db and create a cursor
con = sqlite3.connect('medicaldemo.db')
cur = con.cursor()

#cur.execute("drop table surgery")
#cur.execute("drop table doctor")
#cur.execute("drop table patient")

# Create tables
cur.execute('''create table surgery (
        surgeryID   varchar(4) primary key,
        surgeryDate varchar(10),
        surgeryDesc varchar(10),
        surgeryCost integer,
        patientID   varchar(4),
        doctorID    varchar(4) )''')

cur.execute('''create table doctor (
        doctorID    varchar(4) primary key,
        doctorFN    varchar(10),
        doctorLN    varchar(10),
        doctorPhone varchar(8),
        doctorEmail varchar(20) )''')

cur.execute('''create table patient (
        patientID    varchar(4) primary key,
        patientFN    varchar(10),
        patientLN    varchar(10),
        patientRoom  varchar(5),
        patientPhone varchar(8),
        doctorID     varchar(4) )''')

#Insert rows of data into the 3 tables
cur.execute('''insert into surgery values
("S001","12/09/2011","Heart",96000,"P100","D040"),
("S999","04/07/2012","Hand",5000,"P100","D040"),
("S303","10/10/2010","Back",14000,"P099","D300"),
("S201","11/11/2011","Heart",87000,"P200","D300"),
("S200","01/01/2001","Back",22000,"P300","D100"),
("S105","02/02/2002","Hand",3000,"P205","D200"),
("S210","03/03/2011","Shoulder",8000,"P205","D200"),
("S111","10/12/2011","Back",22000,"P400","D100")''')

cur.execute('''insert into doctor values
("D200","Sue","Pluto","555-1234","sue@pluto.com"),
("D100","Aaron","Saturn","555-1111","aaron@saturn.com"),
("D300","Jim","Mercury","555-2222","jim@mercury.com"),
("D040","Alice","Earth","555-5555","alice@earth.com")''')

cur.execute('''insert into patient values
("P100","Mary","Walnut","Ward1","555-8888","D040"),
("P099","Joe","Pecan","Ward3","555-7777","D300"),
("P200","Ali","Cashew","Ward4","555-3333","D300"),
("P300","Frank","Hazel","Ward5","555-5050","D100"),
("P205","Debra","Almond","Ward1","555-8888","D200"),
("P400","George","Peanut","Ward4","555-3333","D100")''')

# Save (commit) the changes
con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()
