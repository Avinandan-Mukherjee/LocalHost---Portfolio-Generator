import google.generativeai as genai
from dotenv import load_dotenv
import os
from flask import Flask, session ,render_template, url_for, request, redirect, send_file
from werkzeug.utils import secure_filename
import base64
import zipfile
import io

from input_form import InputArea


load_dotenv()

app = Flask(__name__)
api_key = os.getenv("GEMINI_API")
if not api_key:
    print("WARNING: GEMINI_API environment variable not found!")
else:
    print(f"API key found")
genai.configure(api_key=api_key)
app.config['SECRET_KEY'] = os.getenv("FLASK_KEY")
app.config['UPLOAD_FOLDER'] = 'static/codes/images'






@app.route("/", methods=['GET','POST'])

def data_input():
    inp = InputArea()
    print(f"Form submitted: {request.method}")
    if request.method == 'POST':
        print(f"Form validation: {inp.validate_on_submit()}")
        if inp.errors:
            print(f"Form errors: {inp.errors}")
    
    if inp.validate_on_submit():



        image_file = inp.image.data
        filename = secure_filename(image_file.filename)
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        try:
            if os.path.exists(app.config['UPLOAD_FOLDER']):
                for old_file in os.listdir(app.config['UPLOAD_FOLDER']):
                    old_file_path = os.path.join(app.config['UPLOAD_FOLDER'], old_file)
                    if os.path.isfile(old_file_path):
                        os.remove(old_file_path)
                        print(f"Deleted old image: {old_file}")
        except Exception as e:
            print(f"Error cleaning up old images: {e}")
        
        # Save new image
        image_file.save(image_path)
        print(f"Saved new image: {filename}")
    
        html_image = image_path[13:]
        


        # Gemini
        behave = f"""
        You are a portfolio generator ai. You will generate a html css js portfolio website code for a user with his given data **with proper responsiveness**, that will be provided below. Design it in a professional way, with smooth minimal animations. if preferred color is given then with the colors, keep a constant theme, dont go and make a whole RGB Light website with every colors shining out there. If not given, make ur own call. And dont make every portfolio same.

        After writing the code, u will return it normally as a string, without any wrapper like ```html``` or ```css```. plain simple html css js in multi line string formal. and after html , css, code ends add a word that is 'endofthecode' so i can distinguish between the languages. Also, my task is to get the whole code and seperate them. Ill keep them in seperate file. so no need to explicitely add <style></style> or <script></script> tags. Just type it normally. The css and js file names are style.css and script.js respectively. So just write the connecting line in the html file. 

        At the Beginning of the HTML file, write a comment line 'Made with LocalHost. Lots of Love from Avinandan.' something like this. 


        Now the users data:
        Full Name: {inp.fullname.data}
        Profile Photo (Path): {html_image}
        Class / Year / Job: {inp.education.data}
        Institution/Company: {inp.company.data}
        Email: {inp.email.data}
        Skills: {inp.skills.data}
        Preferred Theme: {inp.theme.data}
        Preferred Colors: {inp.color.data}

        Social Links:
        Github: {inp.github.data}
        LinkedIn: {inp.linkedin.data}
        Instagram: {inp.instagram.data}
        YouTube: {inp.youtube.data}

        Also, user can give some extra request for his website. User Request: {inp.prompt.data}. Ignore if empty.

        """

        reply = ""
        try:
            print("Making API call to Gemini...")
            model = genai.GenerativeModel("gemini-2.5-pro")
            response = model.generate_content(behave)
            reply = response.text
            print("API call successful")
            
        except Exception as e:
            print(f"API Error: {str(e)}")
            reply = f"Error generating the code: {str(e)}"




        
        
        li = reply.split('endofthecode')
        

        html = li[0]
        css=li[1]
        js = li[2]
        print(f"HTML length: {len(html)}")
        print(f"CSS length: {len(css)}")
        print(f"JS length: {len(js)}")

        save_path = "codes" 

        try:
            with open(r'static/codes/index.html', "w", encoding="utf-8") as f:
                f.write(html)
            print("HTML file written successfully")
        except Exception as e:
            print(f"Error writing HTML: {e}")

        try:
            with open(r'static/codes/style.css', "w", encoding="utf-8") as f:
                f.write(css)
            print("CSS file written successfully")
        except Exception as e:
            print(f"Error writing CSS: {e}")

        try:
            with open(r'static/codes/script.js', "w", encoding="utf-8") as f:
                f.write(js)
            print("JS file written successfully")
        except Exception as e:
            print(f"Error writing JS: {e}")



        return redirect(url_for('generated_page'))

    return render_template('data.html', form = inp)









@app.route("/generated")
def generated_page():


    with open("static/codes/index.html", "r", encoding="utf-8") as f:
        html = f.read()

    with open("static/codes/style.css", "r", encoding="utf-8") as f:
        css = f.read()

    with open("static/codes/script.js", "r", encoding="utf-8") as f:
        js = f.read()

    print("Hi")

    return render_template('generated.html', html=html, css=css, js=js)




@app.route("/download")
def download_files():
    try:
        zip_buffer = io.BytesIO()
        
        with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            if os.path.exists("static/codes/index.html"):
                zip_file.write("static/codes/index.html", "index.html")
            

            if os.path.exists("static/codes/style.css"):
                zip_file.write("static/codes/style.css", "style.css")
            
  
            if os.path.exists("static/codes/script.js"):
                zip_file.write("static/codes/script.js", "script.js")
            

            if os.path.exists("static/codes/images"):
                for filename in os.listdir("static/codes/images"):
                    file_path = os.path.join("static/codes/images", filename)
                    if os.path.isfile(file_path):
                        zip_file.write(file_path, f"images/{filename}")
        
 
        zip_buffer.seek(0)
        
        return send_file(
            zip_buffer,
            mimetype='application/zip',
            as_attachment=True,
            download_name='portfolio_files.zip'
        )
        
    except Exception as e:
        print(f"Error creating zip file: {e}")
        return "Error creating download file", 500

if __name__ == "__main__":
    app.run()






