from flask import Flask,render_template,request
import uuid  # for generating unique key (for unique image name)
import os
import schedule

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/design")
def design():
    return render_template("design.html")

@app.route("/form1")
def form1():
    template = request.args.get('template', 'design1')
    return render_template("form1.html", selected_template=template)


@app.route("/upload", methods = ["GET","POST"])
def upload():
    if request.method == 'POST':
        name = request.form.get("firstname")
        lastname = request.form.get("lastname")
        school = request.form.get("school")
        college = request.form.get("college")
        phone = request.form.get("phone")
        email = request.form.get("email")
        git = request.form.get("git")
        linkedin =  request.form.get("linkedin")
        skill1 = request.form.get("skill1")
        skill2 = request.form.get("skill2")
        skill3 = request.form.get("skill3")
        skill4 = request.form.get("skill4")
        about = request.form.get("about")
        
        key = uuid.uuid1()
        
        # Image uploading method (single image only)
        img = request.files["dp"]
        img.save(f"static/images/{img.filename}")
        
        img_new_name = f"{key}{img.filename}"  #unique name
        os.rename(f"static/images/{img.filename}",f"static/images/{img_new_name}")
        
    return render_template("portfolio1.html",img = img_new_name,dname = name,dlname = lastname,dsch = school, dcol = college,dph = phone,demail = email,ds1 = skill1,ds2 = skill2,ds3 =skill3,ds4 = skill4,dabout = about,
                           git=git,link=linkedin)

def delete():
    files = os.listdir("static/images")
    for f in files:
        os.remove(f"static/images/{f}")
 
if __name__=="__main__":
    schedule.every().day.at("23:59").do(delete)
    app.run(debug=True)