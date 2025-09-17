import pyodbc

conn = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=localhost\\SQLEXPRESS;"
    "Database=tracker;"
    "UID=raj;"
    "PWD=#@Raj270598$;"
)
print("Connected successfully!")


# Flask routes to landing page


# @app.route("/")
# def home():
#      return render_template("index.html")


# @app.route("/greet", methods=["GET", "POST"])
# def greet():
#     if request.method == "POST":
#         name = request.form["name"]
#         return f"<h1>Hello, {name}!</h1> <a href='\\'>home</a>"
#     return ''' 
#         <form method="post">
#             <input type="text" name="name" placeholder="Enter your name">
#             <input type="submit">
#         </form>
#     '''