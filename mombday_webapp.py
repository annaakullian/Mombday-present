from flask import Flask, render_template, request

import mombirthday

app = Flask(__name__)

@app.route("/")
def get_year():
	return render_template("get_year.html")

@app.route("/memory")
def get_memory():

	mombirthday.connect_to_db()
	year = request.args.get("year")
	row = mombirthday.get_memory_by_year(year)

	html = render_template("memory.html", mom_age = row[0], anna_age = row[1], memory = row[2]) 
	return html

if __name__ == "__main__":
	app.run(debug=True)