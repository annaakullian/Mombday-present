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
	# returns "<html><Body>..</body<</html>"

# @app.route("/memory-ajax")
# def get_memory_for_ajax():
# 	# get memory in same way as abovw
# 	# get year from args
# 	# render template -- memory-ajax.html
# 	return 
	# returns  "<div>Mom: 30, Me: 10, Memory: fggf</div>""


# @app.route("/memory?year=1991")
# html = render_template("1991.html")
# return html


if __name__ == "__main__":
	app.run(debug=True)