from flask import Flask, render_template, abort

app = Flask(__name__)
projects = [
    {
        "name": "Autism Tracker",
        "sub": "with Flask and MongoDB",
        "thumb": "img/flask.png",
        "hero": "img/autism_hero.jpg",
        "categories": ["python", "web"],
        "slug": "python_portfolio",
        "prod": "#",
    },
    {
        "name": "work in progress",
        "sub": "",
        "thumb": "img/react.png",
        "hero": "img/personal-finance.png",
        "categories": ["react", "Typescript", "javascript"],
        "slug": "",
    },
    {
        "name": "REST API",
        "sub":  "Documentation with Postman",
        "thumb": "img/API.png",
        "hero": "img/rest-api-docs.png",
        "categories": ["writing", "Database"],
        "slug": "",
    },
]

slug_to_project = {project["slug"]: project for project in projects}


@app.route("/")
def home():
    return render_template("home.html", projects=projects)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/project/<string:slug>")
def project(slug):
    if slug not in slug_to_project:
        abort(404)
    return render_template(f"project_{slug}.html", project=slug_to_project[slug])


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404
