from flask import Flask, render_template, request, redirect

app = Flask(__name__)   

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    student_id = request.form['student_id']
    apple = request.form['apple']
    raspberry = request.form['raspberry']
    strawberry = request.form['strawberry']
    total = int(strawberry) + int(raspberry) + int(apple)
    print(f"charging customer: {first_name} {last_name} for {total} fruits you fat bastard ")
    return render_template("checkout.html", first_name= first_name, last_name = last_name , student_id = student_id, apple = apple, raspberry = raspberry, strawberry =strawberry )

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    