from flask import Flask, render_template, request, redirect, session
import mysql.connector


application = Flask(__name__)
application.secret_key = "my Project"


updated_slots = ['9:00 AM - 9:30 AM', '9:30 AM - 10:00 AM', '10:00 AM - 10:30 AM', '10:30 AM - 11:00 AM', '11:00 AM - 11:30 AM', '11:30 AM - 12:00 PM']


bdate = ''
@application.route("/", methods=["GET", "POST"])
def Checkslot():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Shubham@IT551",
        port='3306',
        database='texcarp_vr'
    )
    if request.method == "GET":
        return render_template("Checkslot.html")
    
    elif request.method == "POST":
        Bdate = request.form["date"]
        sql = "SELECT * FROM client"        
        cursor = mydb.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()

        global updated_slots
        global bdate
        bdate = Bdate
        for m in data:
            if str(m[3]) == Bdate and m[4] in updated_slots:
                updated_slots.remove(m[4])
                
    return redirect("form")

@application.route("/form", methods=["GET", "POST"])
def Form():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Shubham@IT551",
        port='3306',
        database='texcarp_vr'
    )
    if request.method == "GET":
        print(updated_slots)
        return render_template("Form.html", slots=updated_slots,bdate=bdate)
    
    elif request.method == "POST":
        Name = request.form["name"]
        Email = request.form["email"]
        mobile = request.form['mobile']
        Booking_date = request.form["date"]
        Time_slot = request.form["timeSlot"]
        
        sql = "INSERT INTO client (Name, Email, Mobile, Booking_date, Time_slot) VALUES (%s, %s, %s, %s, %s)"
        val = (Name, Email, mobile, Booking_date, Time_slot)
        cursor = mydb.cursor()
        cursor.execute(sql, val)
        mydb.commit()    
        Msg = f"\nDear {Name},\n\nYour appointment has been scheduled for \n Date : {Booking_date} at Time : {Time_slot}."
        return render_template("thank_you.html",Msg=Msg)
 
if __name__ == "__main__":
    application.run(debug=True)

'''
 Msg = f"Appointment Confirmation !!! \nDear {Name},\n\nYour appointment has been scheduled for {Booking_date} at {Time_slot}.\n\nThank you!"
        phone_number = "+91"+mobile

      
        kit.sendwhatmsg_instantly(phone_number, Msg)
      Slots = ['9:00 AM - 9:30 AM', '9:30 AM - 10:00 AM', '10:00 AM - 10:30 AM', '10:30 AM - 11:00 AM', '11:00 AM - 11:30 AM', '11:30 AM - 12:00 PM']  

      
@application.route("/admin", methods=["GET", "POST"]) 
def Admin():
    return render_template("home.html")


'''