import psycopg2
class Main():
    def __init__(self):
        print ("Please enter information of the database")
        self.database_name = str(input ("Name of the db "))
        self.username = str(input("Username "))
        self.password = str(input("Password "))
        
        try:
            print ("Connecting to the db")
            self.connent_to_db()
            print ("Connection successfully established")
        except:
            print ("Can't establish connection to the db")
        action = 10
        while action != 0:
            print ("What do you wand to do?","\n","1= show tables,","\n","2-show jointed tables","\n","3-insert a line to the table","\n","0-EXIT")
            action = int(input("Yor action? "))
            if action == 1:
                self.show_tables()
            elif action ==2:
                print ("Not ready yet")     
            elif action ==3:
                print ("To which table you want to add a line? (print name) ")
                self.show_tables()
                which_table = (input())
                if which_table == "employee":
                    first_name = input ("Input first_name of the employee ")
                    last_name = input("Input last name of the employee ")
                    gender = input ("Input gender of the employee ")
                    phone_number = input ("Input phone number of the employee ")
                    self.add_values_to_the_table_employee (first_name,last_name,gender,phone_number)
                elif which_table == "addresses":
                    country = input ("Input country ")
                    city = input ("Input city ")
                    street= input ("Input street ")
                    house_number= input ("Input house_number ")
                    flat_number= int(input ("Input flat_number "))
                    owner= int (input ("Input employee id "))
                    self.add_values_to_the_table_addresses (country,city,street,house_number,flat_number,owner)

            elif action ==0:
                break
            else:
                print ("Unknown command")

    def  connent_to_db(self):
        self.db = psycopg2.connect(
            database=self.database_name,
            user = self.username,
            password = self.password,
            host = 'localhost',
            port = "5432"
        )
        print ("Connected to db")
        self.cur = self.db.cursor()

    def add_values_to_the_table_employee (self,first_name,last_name,gender,phone_number):

        #cur.execute ("SELECT * from employee;")
        #print (cur.fetchone())
        #try:
        self.cur.execute ("INSERT INTO employee(first_name,last_name,gender,phone_number)VALUES (%s,%s,%s,%s)",
            (first_name,last_name,gender,phone_number))
        self.db.commit()
        self.cur.execute ("SELECT * from employee;")
        print (self.cur.fetchone())
        #except:
           
    def add_values_to_the_table_addresses (self,country,city,street,house_number,flat_number,owner):
        #cur.execute ("SELECT * from employee;")
        #print (cur.fetchone())
        #try:
        self.cur.execute ("INSERT INTO addresses (country,city,street,house_number,flat_number,owner) VALUES (%s,%s,%s,%s,%s,%s)",
            (country,city,street,house_number,flat_number,owner))
        self.db.commit()
        self.cur.execute ("SELECT * from addresses;")
        print (self.cur.fetchone())
        #except:
            
    
    
    def show_tables (self):
        self.cur.execute("""SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'""")
        self.table_list = []
        print (self.cur.fetchall())
        for table in self.cur.fetchall():
            table = table[2:][:-3]
            self.table_list.append (table)
            print (table)
        

    

        
Main()