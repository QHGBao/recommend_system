import json
import random
import os

# =========================
# RESOURCE TYPES (không cần nữa nhưng giữ lại nếu bạn muốn dùng sau)
# =========================
RESOURCE_TYPES = ["MOOC", "Book", "Article", "Video"]

# =========================
# SKILL → REAL LINKS
# =========================
RESOURCE_LINKS = {
    "python_basic": [
        ("Python Official Tutorial", "https://docs.python.org/3/tutorial/", "Article"),
        ("Python for Everybody", "https://www.coursera.org/specializations/python", "MOOC"),
        ("Automate the Boring Stuff", "https://automatetheboringstuff.com/", "Book"),
        ("freeCodeCamp Python Course", "https://www.freecodecamp.org/learn/scientific-computing-with-python/", "Video")
    ],
    "python_advanced": [
        ("Real Python", "https://realpython.com/", "Article"),
        ("Effective Python", "https://effectivepython.com/", "Book"),
        ("Advanced Python (DataCamp)", "https://www.datacamp.com/courses/intermediate-python", "MOOC"),
        ("Corey Schafer Python", "https://www.youtube.com/@coreyms", "Video")
    ],
    "sql": [
        ("W3Schools SQL", "https://www.w3schools.com/sql/", "Article"),
        ("SQL for Data Science", "https://www.coursera.org/learn/sql-for-data-science", "MOOC"),
        ("SQL Cookbook", "https://www.oreilly.com/library/view/sql-cookbook/0596009763/", "Book"),
        ("freeCodeCamp SQL", "https://www.youtube.com/watch?v=HXV3zeQKqGY", "Video")
    ],
    "machine_learning": [
        ("Google ML Crash Course", "https://developers.google.com/machine-learning/crash-course", "Article"),
        ("Andrew Ng ML", "https://www.coursera.org/learn/machine-learning", "MOOC"),
        ("Hands-On ML", "https://github.com/ageron/handson-ml2", "Book"),
        ("StatQuest ML", "https://www.youtube.com/@statquest", "Video")
    ],
    "etl": [
        ("Data Engineering Intro", "https://www.datacamp.com/courses/introduction-to-data-engineering", "MOOC"),
        ("ETL Concepts", "https://www.ibm.com/topics/etl", "Article"),
        ("Designing Data-Intensive Apps", "https://dataintensive.net/", "Book"),
        ("Data Engineering YouTube", "https://www.youtube.com/@DataEngineering", "Video")
    ],
    "big_data": [
        ("Apache Spark Docs", "https://spark.apache.org/docs/latest/", "Article"),
        ("Big Data Coursera", "https://www.coursera.org/specializations/big-data", "MOOC"),
        ("Spark: The Definitive Guide", "https://www.oreilly.com/library/view/spark-the-definitive/9781491912201/", "Book"),
        ("Spark Tutorial", "https://www.youtube.com/watch?v=_C8kWso4ne4", "Video")
    ],
    "html": [
        ("MDN HTML", "https://developer.mozilla.org/en-US/docs/Web/HTML", "Article"),
        ("freeCodeCamp HTML", "https://www.freecodecamp.org/learn/responsive-web-design/", "MOOC"),
        ("HTML & CSS Book", "https://www.htmlandcssbook.com/", "Book"),
        ("HTML Crash Course", "https://www.youtube.com/watch?v=UB1O30fR-EE", "Video")
    ],
    "css": [
        ("MDN CSS", "https://developer.mozilla.org/en-US/docs/Web/CSS", "Article"),
        ("freeCodeCamp CSS", "https://www.freecodecamp.org/learn/responsive-web-design/", "MOOC"),
        ("CSS Secrets", "https://csssecrets.io/", "Book"),
        ("CSS Crash Course", "https://www.youtube.com/watch?v=yfoY53QXEnI", "Video")
    ],
    "javascript": [
        ("JavaScript Info", "https://javascript.info/", "Article"),
        ("freeCodeCamp JS", "https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/", "MOOC"),
        ("You Don’t Know JS", "https://github.com/getify/You-Dont-Know-JS", "Book"),
        ("JS Crash Course", "https://www.youtube.com/watch?v=hdI2bqOjy3c", "Video")
    ],
    "react": [
        ("React Docs", "https://react.dev/learn", "Article"),
        ("Scrimba React", "https://scrimba.com/learn/learnreact", "MOOC"),
        ("Fullstack React Book", "https://www.fullstackreact.com/", "Book"),
        ("React Course", "https://www.youtube.com/watch?v=bMknfKXIFA8", "Video")
    ],
    "backend": [
        ("NodeJS Docs", "https://nodejs.dev/en/learn/", "Article"),
        ("Backend Coursera", "https://www.coursera.org/", "MOOC"),
        ("Designing Web APIs", "https://www.oreilly.com/library/view/designing-web-apis/9781492026914/", "Book"),
        ("NodeJS Crash Course", "https://www.youtube.com/watch?v=fBNz5xF-Kx4", "Video")
    ],
    "api": [
        ("REST API Guide", "https://restfulapi.net/", "Article"),
        ("Postman Course", "https://learning.postman.com/", "MOOC"),
        ("API Design Patterns", "https://www.manning.com/books/api-design-patterns", "Book"),
        ("REST API Tutorial Video", "https://www.youtube.com/watch?v=Q-BpqyOT3a8", "Video")
    ]
}

# =========================
# LOAD COURSES
# =========================
def load_courses():
    with open("data/courses.json", "r", encoding="utf-8") as f:
        return json.load(f)

# =========================
# GENERATE RESOURCES
# =========================
def generate_resources(courses, n=120):

    resources = []
    resource_id = 1

    while len(resources) < n:

        course = random.choice(courses)
        skill = course["skills"][0]

        if skill not in RESOURCE_LINKS:
            continue

        # FIX LỖI Ở ĐÂY
        title, url, r_type = random.choice(RESOURCE_LINKS[skill])

        resource = {
            "id": f"r{resource_id}",
            "title": title,
            "type": r_type,  # dùng type đúng từ data
            "url": url,
            "course_id": course["id"]
        }

        resources.append(resource)
        resource_id += 1

    return resources

# =========================
# SAVE JSON
# =========================
def save_json(data, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

# =========================
# MAIN
# =========================
def main():

    os.makedirs("data", exist_ok=True)

    courses = load_courses()

    resources = generate_resources(courses, 120)

    save_json(resources, "data/resources.json")

    print("120 REAL resources generated!")

if __name__ == "__main__":
    main()