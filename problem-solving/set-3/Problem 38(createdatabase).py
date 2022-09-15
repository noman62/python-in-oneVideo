
import sqlite3
sqlite3.connect('database_diabetes') #database create
conn = sqlite3.connect('database_diabetes')
c = conn.cursor()
c.execute("CREATE TABLE patient (age VARCHAR(255), weight VARCHAR(255), height VARCHAR(255),blood_pressure VARCHAR(255),working_status VARCHAR(255)" \
    ",martial_status VARCHAR(255),family_history VARCHAR(255),other_diseases VARCHAR(255))") #table create





c.execute('''INSERT INTO patient VALUES('18','55','5.3feet','130','teacher','married','Do not have any','No')
          ''')
c.execute('''INSERT INTO patient VALUES('28','50','5feet','90','student','unmarried','Do not have any','No')
          ''')
c.execute('''INSERT INTO patient VALUES('45','58','5.2feet','100','teacher','married','Do not have any','No')
          ''')
c.execute('''INSERT INTO patient VALUES('56','44','5.1feet','140','teacher','unmarried','Do not have any','No')
          ''')
c.execute('''INSERT INTO patient VALUES('23','50','4.9feet','130','student','married','Do not have any','No')
          ''')
c.execute('''INSERT INTO patient VALUES('22','70','5.0feet','120','student','unmarried','Do not have any','No')
          ''')
c.execute('''INSERT INTO patient VALUES('25','55','5.2feet','140','student','unmarried','Do not have any','No')
          ''')
c.execute('''INSERT INTO patient VALUES('33','77','5.1feet','140','teacher','married','Do not have any','No')
          ''')
c.execute('''INSERT INTO patient VALUES('31','59','5.6feet','100','teacher','unmarried','Do not have any','No')
          ''')
c.execute('''INSERT INTO patient VALUES('22','53','5.7feet','120','staff','unmarried','Do not have any','No')
          ''')
c.execute('''INSERT INTO patient VALUES('78','59','5.1feet','90','staff','married','Do not have any','No')
          ''')
c.execute('''INSERT INTO patient VALUES('68','52','5.2feet','140','teacher','married','Do not have any','No')
          ''')
c.execute('''INSERT INTO patient VALUES('78','50','4.6feet','100','staff','married','Do not have any','No')
          ''')
c.execute('''INSERT INTO patient VALUES('38','44','5feet','120','teacher','unmarried','Do not have any','No')
          ''')
c.execute('''INSERT INTO patient VALUES('28','47','5.3feet','120','student','married','Do not have any','No')
          ''')


conn.commit()

