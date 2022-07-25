from os import P_NOWAIT
from tracemalloc import start
from flask import Flask, render_template, request, redirect, url_for, flash,session
from flaskext.mysql import MySQL
import pymysql
import os
from werkzeug.utils import secure_filename
import re

 
app = Flask(__name__)
app.secret_key = "Cairocoders-Ednalan"
  
mysql = MySQL()

UPLOAD_FOLDER = 'static/images/'
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'chikun'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
mysql.init_app(app)


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS




@app.route('/add_employee')
def add_employee():
    return render_template('Add_Employee.html')
@app.route('/organization')
def organization():
    return render_template('Organization.html')


# @app.route('/company')
# def company():
#     return render_template('Company.html')
# @app.route('/department')
# def department():
#     return render_template('Department.html')
# @app.route('/location')
# def location():
#     return render_template('Location.html')
# @app.route('/designation')
# def designation():
#     return render_template('Designation.html')
@app.route('/add_company')
def add_company():
    return render_template('Add_Company_details.html')

@app.route('/add_department')
def add_department():
    return render_template('Add_department.html')
@app.route('/add_designation')
def add_designation():
    return render_template('Add_designation.html')
@app.route('/add_attendance')
def add_attendance():
    return render_template('Add_attendance.html')
@app.route('/add_location')
def add_location():
    return render_template('Add_location.html')

@app.route('/add_project')
def add_project():
    return render_template('Add_project.html')

@app.route('/add_payroll')
def add_payroll():
    return render_template('Add_payroll.html')

@app.route('/edit_employee')
def employee_info():
    return render_template('Edit_Employee.html')

#..LOGIN......................................login................................................................#
@app.route('/', methods =['GET', 'POST'])
def login():
    msg = ''
    conn=mysql.connect()
    cursor= conn.cursor(pymysql.cursors.DictCursor)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor.execute('SELECT * FROM admin_login WHERE username = % s AND password = % s', (username, password, ))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            msg = 'Logged in successfully !'
            return  redirect(url_for('dashboard')) 
        else:
            msg = 'Incorrect username / password !'
    return render_template('login.html', msg = msg)

#..LOGOUT.............................LOGOUT...........................................#
# @app.route('/logout')
# def logout():
#     session.pop('loggedin', None)
#     session.pop('id', None)
#     session.pop('username', None) 
#     session.clear()
#     return redirect(url_for('login'))




@app.route('/logout')
def logout():
    try:
        session.clear()
        return redirect(url_for('.login'))
    except Exception as e:
        print(e)    

#...DASHBOARD...........................................................Dashboard.........#
@app.route('/dasboard')
def dashboard():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT COUNT(id) as id FROM employee")
    emp = cursor.fetchone()
    cursor.execute("SELECT COUNT(id) as id FROM project")
    pr = cursor.fetchone()
    cursor.execute("SELECT SUM(final_salary) as final_salary FROM payroll")
    payroll = cursor.fetchone()
    cursor.execute("SELECT*FROM project")
    project = cursor.fetchall()
    cursor.execute("SELECT COUNT(id) as id FROM department")
    dp = cursor.fetchone()
    cursor.execute("SELECT COUNT(id) as id FROM location")
    loc = cursor.fetchone()
    return render_template('Dashboard.html', emp=emp,payroll=payroll,pr=pr,project=project,dp=dp,loc=loc)





#.................................EMPLOYEE...........................................#

#Employee list

@app.route('/employee')
def employee():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    cursor.execute("SELECT *FROM employee")
    employee = cursor.fetchall()
    return render_template('Employee.html', employee=employee)


#Employee add

@app.route('/employee_add', methods= ['GET','POST',])
def employee_add():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    if request.method == 'POST':
        name= request.form['name']
        emp_code= request.form['emp_code']
        department= request.form['department']
        designation=request.form['designation']
        role= request.form['role']
        gender= request.form['gender']
        dob=request.form['dob']
        bg=request.form['bg']
        email=request.form['email']
        phone=request.form['phone']
        date_of_joining=request.form['date_of_joining']
        files = request.files.getlist('files[]')
        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))

        cursor.execute('INSERT INTO employee(name,emp_code,department,designation, role,gender,dob,email,bg,phone,date_of_joining,files) '
                       'VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                       ( name,emp_code, department,designation, role,gender,dob,email,bg,phone,date_of_joining,files))
        conn.commit()
        return redirect (url_for('employee'))
    return render_template("Add_Employee.html")

#Employee Delete

@app.route('/delete/<string:id>', methods=['POST', 'GET'])
def delete_patient(id):
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute('DELETE FROM employee WHERE id = {0}'.format(id))
    conn.commit()
    flash('Employee Removed Successfully')
    return redirect(url_for('employee'))


# @app.route('/display/<filename>')
# def display_image(filename):
#     #print('display_image filename: ' + filename)
#     return redirect(url_for('static', filename='uploads/' + filename), code=301)

#EMPLOYEE DETAILS
@app.route('/edit/<id>', methods = ['POST', 'GET'])
def get_employee(id):
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
  
    cur.execute('SELECT * FROM employee WHERE id = %s', (id))
    data = cur.fetchall()
    cur.execute('SELECT * FROM employee WHERE id = %s', (id))
    rl= cur.fetchone()
    cur.execute('SELECT * FROM employee WHERE id = %s', (id))
    nm= cur.fetchone()
    cur.execute('SELECT * FROM employee WHERE id = %s', (id))
    em= cur.fetchone()
    cur.execute('SELECT * FROM employee WHERE id = %s', (id))
    pn= cur.fetchone()
    cur.execute('SELECT * FROM employee WHERE id = %s', (id))
    pro= cur.fetchone()
    cur.close()
    print(data[0])
    return render_template('Edit_Employee.html', employee = data[0],nm=nm,rl=rl,em=em,pn=pn,pro=pro)

#update employee details

@app.route('/update/<id>', methods=['POST'])
def update_employee(id):
    if request.method == 'POST':
        name= request.form['name']
        emp_code= request.form['emp_code']
        department= request.form['department']
        designation=request.form['designation']
        
        gender= request.form['gender']
        dob=request.form['dob']
        bg=request.form['bg']
        email=request.form['email']
        files=request.form['files']
        phone=request.form['phone']
        role=request.form['role']
        date_of_joining=request.form['date_of_joining']
        
        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute("""
            UPDATE employee
            SET name = %s,
                emp_code = %s,
               department= %s,
                designation = %s,
               
               gender= %s,
               dob = %s,
                email = %s,
                bg= %s,
               files= %s,
                phone= %s,
                role = %s,
               date_of_joining= %s
               
            WHERE id = %s
        """, (name,emp_code, department,designation,gender,dob,email,bg,files,phone,role,date_of_joining,id))
        conn.commit()
        return redirect(url_for('employee')) 

# employee search

@app.route('/search4', methods=['POST'])
def search_employee():
    _search = (request.form['search'])
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM employee WHERE name LIKE %s OR emp_code LIKE %s  OR email LIKE %s",
                       ("%" + _search + "%", "%" + _search + "%", "%" + _search + "%"))
        rows = cursor.fetchall()
        if not rows:
            return redirect(url_for('employee'))
        else:
            return render_template('Employee.html', employee=rows)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()



#..PAYROLL.....................................Payroll list..............................................#



#Payroll list
@app.route('/payroll')
def payroll():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT*FROM payroll")
    payroll = cursor.fetchall()
    return render_template('Payroll.html',payroll=payroll)

#payroll add

@app.route('/payroll_add', methods=['GET','POST'])
def payroll_add():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    if request.method == 'POST':
        name= request.form['name']
        emp_code= request.form['emp_code']
        salary= request.form['salary']
        loan= request.form['loan']
        hour= request.form['hour']
        deduction= request.form['deduction']
       
        pay_date=request.form['pay_date']
        
        cursor.execute('INSERT INTO payroll(name,emp_code,salary,loan,hour,deduction, pay_date) '
                       'VALUES (%s,%s,%s,%s,%s,%s,%s)',
                       (name,emp_code,salary,loan,hour,deduction, pay_date))

        if request.method == 'POST':
                cursor.execute('UPDATE payroll SET  final_salary=( salary - deduction)')
                conn.commit()
                return redirect(url_for('payroll'))
    return render_template('Add_payroll.html')

#Payroll Delete
@app.route('/delete1/<string:id>', methods=['POST', 'GET'])
def delete_payroll(id):
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute('DELETE FROM payroll WHERE id = {0}'.format(id))
    conn.commit()
    return redirect(url_for('payroll'))

#Payroll DETAILS
@app.route('/edit6/<id>', methods = ['POST', 'GET'])
def get_Payroll(id):
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
  
    cur.execute('SELECT * FROM payroll WHERE id = %s', (id))
    data = cur.fetchall()
    
    cur.close()
    print(data[0])
    return render_template('Edit_payroll.html', Payroll = data[0])

#update Payroll details

@app.route('/update6/<id>', methods=['POST'])
def update_Payroll(id):
    if request.method == 'POST':
        name= request.form['name']
        emp_code= request.form['emp_code']
        salary= request.form['salary']
        loan=request.form['loan']        
        hour= request.form['hour']
        deduction=request.form['deduction']
        pay_date=request.form['pay_date']
        
        
        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute("""
            UPDATE payroll
            SET name = %s,
                emp_code = %s,
               salary= %s,
               loan= %s,
                hour = %s,               
               deduction= %s,
               pay_date = %s
               
                
            WHERE id = %s
        """, (name,emp_code, salary,loan,hour,deduction,pay_date,id))
        if request.method == 'POST':
                cur.execute('UPDATE payroll SET  final_salary=( salary - deduction)')
                conn.commit()
        conn.commit()
        return redirect(url_for('payroll')) 

# payroll search

@app.route('/search7', methods=['POST'])
def search_payroll():
    _search = (request.form['search'])
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM payroll WHERE name LIKE %s OR name LIKE %s  OR emp_code LIKE %s",
                       ("%" + _search + "%", "%" + _search + "%", "%" + _search + "%"))
        rows = cursor.fetchall()
        if not rows:
            return redirect(url_for('payroll'))
        else:
            return render_template('Payroll.html', payroll=rows)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()






#..PROJECT.............................PROJECT.....................................#
#Project list

@app.route('/project')
def project():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT*FROM project")
    project = cursor.fetchall()
    return render_template('Project.html',project=project)

#Project add

@app.route('/project_add', methods=['GET','POST'])
def project_add():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    if request.method == 'POST':
        project_name= request.form['project_name']
        start_date= request.form['start_date']
        end_date= request.form['end_date']
        status= request.form['status']
        details= request.form['details']
        cursor.execute('INSERT INTO project(project_name,start_date,end_date,status,details) '
                       'VALUES (%s,%s,%s,%s,%s)',
                       (project_name,start_date,end_date,status,details))
        conn.commit()
        return redirect(url_for('project'))
    return render_template('Add_project.html')

@app.route('/edit1/<id>', methods = ['POST', 'GET'])
def get_project(id):
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
  
    cur.execute('SELECT * FROM project WHERE id = %s', (id))
    data = cur.fetchall()    
    cur.close()
    print(data[0])
    return render_template('Edit_project.html', project = data[0])

#update project details

@app.route('/update1/<id>', methods=['POST'])
def update_project(id):
    if request.method == 'POST':
        project_name= request.form['project_name']
        start_date= request.form['start_date']
        end_date= request.form['end_date']
        status=request.form['status']        
        details= request.form['details']
       
        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute("""
            UPDATE project
            SET project_name = %s,
                start_date = %s,
               end_date= %s,
                status = %s,               
               details= %s               
            WHERE id = %s
        """,
        (project_name,start_date, end_date,status,details,id))
        conn.commit()
        return redirect(url_for('project'))


#Project Delete
@app.route('/delete2/<string:id>', methods=['POST', 'GET'])
def delete_project(id):
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute('DELETE FROM project WHERE id = {0}'.format(id))
    conn.commit()
    return redirect(url_for('project'))


# project search

@app.route('/search5', methods=['POST'])
def search_project():
    _search = (request.form['search'])
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM project WHERE project_name LIKE %s OR status LIKE %s  OR start_date LIKE %s",
                       ("%" + _search + "%", "%" + _search + "%", "%" + _search + "%"))
        rows = cursor.fetchall()
        if not rows:
            return redirect(url_for('project'))
        else:
            return render_template('Project.html', project=rows)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route("/xyz")
def xyz():
    return render_template('Edit_project.html')  
@app.route("/xyzl")
def xyzl():
    return render_template('Edit_location.html')

@app.route("/xyzdes")
def xyzdes():
    return render_template('Edit_designation.html')

@app.route("/xyza")
def xyza():
    return render_template('Edit_attendance.html')
@app.route("/xyzd")
def xyzd():
    return render_template('Edit_department.html')

#..ATTENDANCE.................................ATTENDANCE......................................#

#Attendance
@app.route('/attendance')
def attendance():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT*FROM attendance")
    attendance = cursor.fetchall()
    return render_template('Attendance.html',attendance=attendance)


# Attendance add
@app.route('/attendance_add', methods=['GET','POST'])
def attendance_add():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    if request.method == 'POST':
        name= request.form['name']
        date= request.form['date']
        in_time= request.form['in_time']
        
        
        cursor.execute('INSERT INTO attendance(name,date,in_time) '
                       'VALUES (%s,%s,%s)',
                       (name,date,in_time,))
        conn.commit()
        return redirect(url_for('attendance'))
    return render_template('Add_attendance.html')

#edit attendance
@app.route('/edit5/<id>', methods = ['POST', 'GET'])
def get_attendance(id):
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
  
    cur.execute('SELECT * FROM attendance WHERE id = %s', (id))
    data = cur.fetchall()    
    cur.close()
    print(data[0])
    return render_template('Edit_attendance.html', attendance = data[0])

#update attendance details

@app.route('/update5/<id>', methods=['POST'])
def update_attendance(id):
    if request.method == 'POST':
        name= request.form['name']
        date= request.form['date']
        out_time= request.form['out_time']
        
       
        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute("""
            UPDATE attendance
            SET name = %s,
                date = %s,
               out_time= %s               
            WHERE id = %s
        """,
        (name,date, out_time,id))
        conn.commit()
        return redirect(url_for('attendance'))




# attendance search

@app.route('/search6', methods=['POST'])
def search_atteendance():
    _search = (request.form['search'])
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM attendance WHERE name LIKE %s OR date LIKE %s",
                       ("%" + _search + "%", "%" + _search + "%", ))
        rows = cursor.fetchall()
        if not rows:
            return redirect(url_for('attendance'))
        else:
            return render_template('Attendance.html', attendance=rows)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()



#..COMPANY...............................COMPANY.................................#

#company add

@app.route('/company_add', methods=['GET','POST'])
def company_add():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    if request.method == 'POST':
        cname= request.form['cname']
        cmail= request.form['cmail']
        cwsite= request.form['cwsite']
        city= request.form['city']
        country= request.form['country']
        
        cursor.execute('INSERT INTO company(cname,cmail,cwsite,city,country) '
                       'VALUES (%s,%s,%s,%s,%s)',
                       (cname,cmail,cwsite,city,country))
        conn.commit()
        return redirect(url_for('company'))
    return render_template('Add_Company_details.html')



#company list

@app.route('/company')
def company():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    cursor.execute("SELECT *FROM company")
    company = cursor.fetchall()
    return render_template('company.html', company=company)

#company Delete

@app.route('/delete3/<string:id>', methods=['POST', 'GET'])
def delete_company(id):
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute('DELETE FROM company WHERE id = {0}'.format(id))
    conn.commit()
    flash('Company Removed Successfully')
    return redirect(url_for('company'))

# Company search

@app.route('/search', methods=['POST'])
def search():
    _search = (request.form['search'])
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM company WHERE cname LIKE %s OR cwsite LIKE %s  OR cmail LIKE %s  OR city LIKE %s  OR country LIKE %s",
                       ("%" + _search + "%", "%" + _search + "%", "%" + _search + "%","%" + _search + "%","%" + _search + "%"))
        rows = cursor.fetchall()
        if not rows:
            return redirect(url_for('company'))
        else:
            return render_template('company.html', company=rows)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
        
#..DEPARTMENT...........................DEPARTMENT.................................#


#department add
@app.route('/department_add', methods=['GET','POST'])
def department_add():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    if request.method == 'POST':
        dname= request.form['dname']
        dhead= request.form['dhead']
        location= request.form['location']
       
        
        cursor.execute('INSERT INTO department(dname,dhead,location) '
                       'VALUES (%s,%s,%s)',
                       (dname,dhead,location))
        conn.commit()
        return redirect(url_for('department'))
    return render_template('Add_department.html')

#department list

@app.route('/department')
def department():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    cursor.execute("SELECT *FROM department")
    department = cursor.fetchall()
    return render_template('Department.html', department=department)    

#department Delete

@app.route('/delete4/<string:id>', methods=['POST', 'GET'])
def delete_department(id):
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute('DELETE FROM department WHERE id = {0}'.format(id))
    conn.commit()
    flash('Company Removed Successfully')
    return redirect(url_for('department'))


#edit department
@app.route('/edit2/<id>', methods = ['POST', 'GET'])
def get_department(id):
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
  
    cur.execute('SELECT * FROM department WHERE id = %s', (id))
    data = cur.fetchall()    
    cur.close()
    print(data[0])
    return render_template('Edit_department.html', department = data[0])

#update department details

@app.route('/update2/<id>', methods=['POST'])
def update_department(id):
    if request.method == 'POST':
        dname= request.form['dname']
        dhead= request.form['dhead']
        location= request.form['location']
       
       
        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute("""
            UPDATE department
            SET dname = %s,
                dhead = %s,
               location= %s              
            WHERE id = %s
        """,
        (dname,dhead, location,id))
        conn.commit()
        return redirect(url_for('department'))

# department search

@app.route('/search1', methods=['POST'])
def search_department():
    _search = (request.form['search'])
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM department WHERE dname LIKE %s OR dhead LIKE %s OR location LIKE %s",
                       ("%" + _search + "%", "%" + _search + "%", "%" + _search + "%"))
        rows = cursor.fetchall()
        if not rows:
            return redirect(url_for('department'))
        else:
            return render_template('Department.html', department=rows)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

#..LOCATION...............................LOCTION................................#
#Location add
@app.route('/location_add', methods=['GET','POST'])
def location_add():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    if request.method == 'POST':
        lname= request.form['lname']
        lhead= request.form['lhead']
        cname= request.form['cname']
        city= request.form['city']
        country= request.form['country']
       
        
        cursor.execute('INSERT INTO location(lname,lhead,cname,city,country) '
                       'VALUES (%s,%s,%s,%s,%s)',
                       (lname,lhead,cname,city,country))
        conn.commit()
        return redirect(url_for('location'))
    return render_template('Add_location.html')

#location list

@app.route('/location')
def location():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    cursor.execute("SELECT *FROM location")
    location = cursor.fetchall()
    return render_template('Location.html', location=location)

# location search

@app.route('/search2', methods=['POST'])
def search_location():
    _search = (request.form['search'])
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM location WHERE lname LIKE %s OR lhead LIKE %s OR cname LIKE %s OR city LIKE %s OR country LIKE %s ",
                       ("%" + _search + "%", "%" + _search + "%","%" + _search + "%","%" + _search + "%","%" + _search + "%"))
        rows = cursor.fetchall()
        if not rows:
            return redirect(url_for('location'))
        else:
            return render_template('Location.html', location=rows)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

#edit location
@app.route('/edit3/<id>', methods = ['POST', 'GET'])
def get_location(id):
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
  
    cur.execute('SELECT * FROM location WHERE id = %s', (id))
    data = cur.fetchall()    
    cur.close()
    print(data[0])
    return render_template('Edit_location.html', location = data[0])

#update location details

@app.route('/update3/<id>', methods=['POST'])
def update_location(id):
    if request.method == 'POST':
        lname= request.form['lname']
        lhead= request.form['lhead']
        cname= request.form['cname']
        city= request.form['city']
        country= request.form['country']
       
       
        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute("""
            UPDATE location
            SET lname = %s,
                lhead = %s,
               cname= %s,
               city= %s,
               country= %s              
            WHERE id = %s
        """,
        (lname,lhead, cname,city,country,id))
        conn.commit()
        return redirect(url_for('location'))

#location Delete

@app.route('/delete5/<string:id>', methods=['POST', 'GET'])
def delete_location(id):
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute('DELETE FROM location WHERE id = {0}'.format(id))
    conn.commit()
    flash('location Removed Successfully')
    return redirect(url_for('location'))


#...DESIGNATION..................................DESIGNATION...................................................#
#Designation add
@app.route('/designtion_add', methods=['GET','POST'])
def designtion_add():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    if request.method == 'POST':
        desname= request.form['desname']
        depname= request.form['depname']
        
       
        
        cursor.execute('INSERT INTO designation(desname,depname) '
                       'VALUES (%s,%s)',
                       (desname,depname))
        conn.commit()
        return redirect(url_for('designation'))
    return render_template('Add_designation.html')

#designation list

@app.route('/designation')
def designation():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    cursor.execute("SELECT *FROM designation")
    designation = cursor.fetchall()
    return render_template('Designation.html', designation=designation)

# designation search

@app.route('/search3', methods=['POST'])
def search_designation():
    _search = (request.form['search'])
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM designation WHERE desname LIKE %s OR depname LIKE %s",
                       ("%" + _search + "%", "%" + _search + "%",))
        rows = cursor.fetchall()
        if not rows:
            return redirect(url_for('designation'))
        else:
            return render_template('Designation.html', designation=rows)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

#edit designation
@app.route('/edit4/<id>', methods = ['POST', 'GET'])
def get_designation(id):
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
  
    cur.execute('SELECT * FROM designation WHERE id = %s', (id))
    data = cur.fetchall()    
    cur.close()
    print(data[0])
    return render_template('Edit_designation.html', designation = data[0])

#update designation details

@app.route('/update4/<id>', methods=['POST'])
def update_designation(id):
    if request.method == 'POST':
        desname= request.form['desname']
        depname= request.form['depname']
        
       
       
        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute("""
            UPDATE designation
            SET desname = %s,
                depname = %s
                             
            WHERE id = %s
        """,
        (desname,depname,id))
        conn.commit()
        return redirect(url_for('designation'))

#designation Delete

@app.route('/delete6/<string:id>', methods=['POST', 'GET'])
def delete_designation(id):
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute('DELETE FROM designation WHERE id = {0}'.format(id))
    conn.commit()
    flash('designation Removed Successfully')
    return redirect(url_for('designation'))



app.run(debug=True)


