from flask import Flask, request, session, redirect, jsonify, render_template
from db import db

#imported to see if selected component is compatible
from compatibility import (
    calculate_case_compatibility,
    calculate_motherboard_compatibility,
    calculate_cpu_compatibility,
    calculate_cooler_compatibility,
    calculate_gpu_compatibility,
    calculate_psu_compatibility,
    calculate_ram_compatibility
)

app = Flask(__name__)
app.secret_key = "secret123"

products_col = db["products"]
users_col = db["users"]


#load all products by type for dropdowns and listing
cases = list(products_col.find(
    {"type": "case"},
    {"_id": 0, "name": 1, "specs": 1, "price": 1}
))

coolers = list(products_col.find(
    {"type": "cooler"},
    {"_id": 0, "name": 1, "specs": 1, "price": 1}
))

motherboards = list(products_col.find(
    {"type": "motherboard"},
    {"_id": 0, "name": 1, "specs": 1, "price": 1}
))

cpus = list(products_col.find(
    {"type": "cpu"},
    {"_id": 0, "name": 1, "specs": 1, "price": 1}
))

gpus = list(products_col.find(
    {"type": "gpu"},
    {"_id": 0, "name": 1, "specs": 1, "price": 1}
))

psus = list(products_col.find(
    {"type": "psu"},
    {"_id": 0, "name": 1, "specs": 1, "price": 1}
))

rams = list(products_col.find(
    {"type": "ram"},
    {"_id": 0, "name": 1, "specs": 1, "price": 1}
))


#Helper functions

def get_current_user():
    """
    Returns the currently logged in user from MongoDB
    
    checks if user_email exists in flask session, 
    if logged in fetch user data from users collection,
    if not, return None
    """
    user_email = session.get("user_email")
    if not user_email:
        return None
    return users_col.find_one({"email": user_email})


def get_cart():
    """
    Returns the current cart.
    
    If user is logged in, returns cart stored in MongoDB
    If not logged in, uses cart stored in current session
    """
    user = get_current_user()
    if user:
        return user.get("cart", [])
    return session.get("cart", [])


def save_cart(cart):
    """
    Saves the cart.
    
    If the user is logged in, stores the cart in MongoDB
    if not logged in, the cart is stored in the session instead
    """
    user = get_current_user()
    if user:
        users_col.update_one(
            {"email": user["email"]},
            {"$set": {"cart": cart}}
        )
    else:
        session["cart"] = cart
        
def get_saved_builds():
    
    """
    Gets saved builds of the user.
    
    If user is logged in, fetches the builds saved from MongoDB
    """
    
    
    user = get_current_user()
    if user:
        return user.get("saved_builds", [])
    return []

def get_preset_builds():
    
    """
    Returns a list of presets (rn hardcoded, needs to be added to DB soon)
    
    """
    
    
    #hard coded presets
    preset_definitions = [
        {
            "key": "budget_gaming",
            "title": "Budget Gaming Build",
            "description": "A lower-cost gaming system for 1080p play and everyday use.",
            "builder_parts": {
                "case": "Montech AIR 903 Max",
                "motherboard": "MSI B550-A PRO",
                "cpu": "AMD Ryzen 5 5600X",
                "cooler": "ID-COOLING SE-214-XT",
                "gpu": "PowerColor Fighter Radeon RX 6600",
                "ram": "G.Skill Ripjaws V 16GB DDR4",
                "psu": "Cooler Master MWE 650 Bronze"
            },
            "extra_parts": [
                "TEAMGROUP MP33 1TB NVMe SSD"
            ]
        },
        {
            "key": "budget_editing",
            "title": "Budget Video Editing Build",
            "description": "A lower-cost editing-focused system with more memory and practical storage.",
            "builder_parts": {
                "case": "Corsair 4000D Airflow",
                "motherboard": "MSI PRO B760M-A",
                "cpu": "Intel Core i5-12400F",
                "cooler": "Cooler Master Hyper 212 Black",
                "gpu": "MSI GeForce RTX 4060 Ventus 2X",
                "ram": "Corsair Vengeance RGB 32GB DDR5",
                "psu": "Corsair RM750e 750W Gold"
            },
            "extra_parts": [
                "Samsung 980 Pro 1TB NVMe SSD"
            ]
        },
        {
            "key": "mid_gaming",
            "title": "Mid-Range Gaming Build",
            "description": "Balanced gaming performance without going into premium pricing.",
            "builder_parts": {
                "case": "Corsair 4000D Airflow",
                "motherboard": "Gigabyte B650 AORUS Elite AX",
                "cpu": "AMD Ryzen 7 7700X",
                "cooler": "Deepcool AK620",
                "gpu": "XFX Speedster QICK 319 Radeon RX 7800 XT",
                "ram": "Kingston Fury Beast 32GB DDR5",
                "psu": "be quiet! Pure Power 12 M 750W"
            },
            "extra_parts": [
                "Samsung 980 Pro 1TB NVMe SSD"
            ]
        },
        {
            "key": "mid_editing",
            "title": "Mid-Range Video Editing Build",
            "description": "A stronger editing system with more memory and faster workspace storage.",
            "builder_parts": {
                "case": "NZXT H5 Flow",
                "motherboard": "ASUS Prime B760M-A",
                "cpu": "Intel Core i7-13700K",
                "cooler": "Arctic Liquid Freezer III 360",
                "gpu": "MSI GeForce RTX 4070 Super Ventus 3X",
                "ram": "G.Skill Trident Z5 RGB 32GB DDR5",
                "psu": "Corsair RM850x 850W Gold"
            },
            "extra_parts": [
                "WD Black SN850X 2TB NVMe SSD"
            ]
        },
        {
            "key": "high_gaming",
            "title": "High-End Gaming Build",
            "description": "Top-tier gaming hardware for enthusiast-level performance.",
            "builder_parts": {
                "case": "Lian Li O11 Dynamic EVO",
                "motherboard": "ASUS ROG Strix Z790-H",
                "cpu": "Intel Core i9-13900K",
                "cooler": "NZXT Kraken 360 RGB",
                "gpu": "Gigabyte GeForce RTX 4090 Gaming OC",
                "ram": "Corsair Vengeance RGB 64GB DDR5",
                "psu": "MSI MPG A1000G 1000W Gold"
            },
            "extra_parts": [
                "Seagate FireCuda 530 1TB NVMe SSD"
            ]
        },
        {
            "key": "high_editing",
            "title": "High-End Video Editing Build",
            "description": "A professional-grade editing system with premium compute, memory, and storage.",
            "builder_parts": {
                "case": "Lian Li O11 Dynamic EVO",
                "motherboard": "Gigabyte B650 AORUS Elite AX",
                "cpu": "AMD Ryzen 9 7950X",
                "cooler": "Arctic Liquid Freezer III 360",
                "gpu": "ASUS TUF Gaming RTX 4070 Ti",
                "ram": "Corsair Vengeance RGB 64GB DDR5",
                "psu": "Corsair RM1000e 1000W Gold"
            },
            "extra_parts": [
                "WD Black SN850X 2TB NVMe SSD",
                "Western Digital Red 4TB HDD"
            ]
        }
    ]

    preset_builds = []

    for preset in preset_definitions:
        selected_parts = []
        total_price = 0

        #builder-supported parts
        for part_type, part_name in preset["builder_parts"].items():
            product = products_col.find_one({"type": part_type, "name": part_name}, {"_id": 0})
            if product:
                selected_parts.append(product)
                total_price += product["price"]

        #extra preset-only parts like storage
        for extra_name in preset["extra_parts"]:
            product = products_col.find_one({"name": extra_name}, {"_id": 0})
            if product:
                selected_parts.append(product)
                total_price += product["price"]

        preset_builds.append({
            "key": preset["key"],
            "title": preset["title"],
            "description": preset["description"],
            "builder_parts": preset["builder_parts"],
            "parts": selected_parts,
            "price": round(total_price, 2)
        })

    return preset_builds


@app.route("/save_build", methods=["POST"])
def save_build():
    """
    Saves the custom build.
    
    If user is logged in, the custom build is allowed to be saved,
    Else the user cannot save the build
    
    """
    user = get_current_user()
    
    #checks user login status
    if not user:
        return redirect("/login")
    
    #accepts build name from page
    build_name = request.form.get("build_name", "").strip()

    selected_parts = {}
    total_price = 0

    part_types = ["case", "motherboard", "cpu", "cooler", "gpu", "ram", "psu"]
    
    
    for part_type in part_types:
        part_name = request.form.get(part_type, "").strip()
        selected_parts[part_type] = part_name

        if part_name:
            product = products_col.find_one(
                {"type": part_type, "name": part_name},
                {"_id": 0, "price": 1}
            )
            if product:
                total_price += product["price"]

    if not build_name:
        build_name = "My Build"

    saved_build = {
        "build_name": build_name,
        "parts": selected_parts,
        "total_price": total_price
    }

    saved_builds = user.get("saved_builds", [])
    saved_builds.append(saved_build)

    users_col.update_one(
        {"email": user["email"]},
        {"$set": {"saved_builds": saved_builds}}
    )

    return redirect("/saved_builds")


@app.route("/saved_builds")
def saved_builds():
    """
    Returns all saved builds for a logged in user.
    If no user is logged in then redirects to login page
    """
    user = get_current_user()

    if not user:
        return redirect("/login")

    builds = user.get("saved_builds", [])
    return render_template("saved_builds.html", builds=builds)


@app.route("/load_build/<int:build_index>")
def load_build(build_index):
    
    """
    Loads a saved build back into builder page.
    
    Parameters:
    build_index: index showing position of build inside saved_builds list
    
    User must be logged in, 
    if index is invalid redirect to saved builds page
    
    """
    
    user = get_current_user()

    if not user:
        return redirect("/login")
    
    
    builds = user.get("saved_builds", [])

    if build_index < 0 or build_index >= len(builds):
        return redirect("/saved_builds")

    selected_build = builds[build_index]["parts"]

    return render_template(
        "builder.html",
        cases=cases,
        motherboards=motherboards,
        cpus=cpus,
        coolers=coolers,
        gpus=gpus,
        rams=rams,
        psus=psus,
        selected_build=selected_build
    )


@app.route("/register", methods=["GET", "POST"])
def register():
    
    """
    Handles user registeration.
    Divided into GET and POST
    
    GET Req:
    Displays registeration form
    
    POST Req:
    Reads and validates fields, checks for duplicate user
    creates a new user in MongoDB and also 
    if there is a guest cart then it uploads it into the account cart MongoDB
    
    """
    message = ""

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "").strip()

        existing_user = users_col.find_one({"email": email})

        if not name or not email or not password:
            message = "Please fill all fields."
        elif existing_user:
            message = "Email already registered."
        else:
            users_col.insert_one({
            "name": name,
            "email": email,
            "password": password,
            "cart": session.get("cart", []),
            "saved_builds": []
        })

            session["user_email"] = email
            session["user_name"] = name
            session["cart"] = []

            return redirect("/")

    return render_template("register.html", message=message)


@app.route("/login", methods=["GET", "POST"])
def login():
    
    """
    Handles user login.
    Divided into GET and POST
    
    GET Req:
    Displays login form
    
    POST Req:
    Reads the values from form and validates them from MongoDB.
    if found then:  adds guest cart items into user cart in database,
    stores login info into session
    if not found:  shows error message    
    """
    message = ""

    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "").strip()

        user = users_col.find_one({
            "email": email,
            "password": password
        })
        
        
        if user:
            old_session_cart = session.get("cart", [])
            user_cart = user.get("cart", [])

            if old_session_cart:
                user_cart.extend(old_session_cart)
                users_col.update_one(
                    {"email": email},
                    {"$set": {"cart": user_cart}}
                )

            session["user_email"] = user["email"]
            session["user_name"] = user["name"]
            session["cart"] = []

            return redirect("/")
        else:
            message = "Invalid email or password."

    return render_template("login.html", message=message)


@app.route("/logout")
def logout():
    """
    Logs current user out.
    
    Removes user_email, user_name from session
    Empties the cart stored in session and redirects to homepage
    
    """
    session.pop("user_email", None)
    session.pop("user_name", None)
    session["cart"] = []
    return redirect("/")


# COMPATIBILITY ROUTE

@app.route("/check_compatability", methods=["GET"])
def check_compatability():
    
    """
    Returns compatability information as JSON so that builder.html can access it
    
    Logic:
    Reads selected component name from the query string and fetches it from MongODB
    Builds a selected_build dictionary, run compatability check using the specs of document,
    Returns all result as JSON
    """
    
    selected_build = {
        "case": None,
        "motherboard": None,
        "cpu": None,
        "cooler": None,
        "gpu": None,
        "psu": None,
        "ram": None
    }

    case_name = request.args.get("case")
    if case_name:
        selected_build["case"] = products_col.find_one(
            {"type": "case", "name": case_name},
            {"_id": 0, "name": 1, "specs": 1}
        )

    cooler_name = request.args.get("cooler")
    if cooler_name:
        selected_build["cooler"] = products_col.find_one(
            {"type": "cooler", "name": cooler_name},
            {"_id": 0, "name": 1, "specs": 1}
        )

    motherboard_name = request.args.get("motherboard")
    if motherboard_name:
        selected_build["motherboard"] = products_col.find_one(
            {"type": "motherboard", "name": motherboard_name},
            {"_id": 0, "name": 1, "specs": 1}
        )

    cpu_name = request.args.get("cpu")
    if cpu_name:
        selected_build["cpu"] = products_col.find_one(
            {"type": "cpu", "name": cpu_name},
            {"_id": 0, "name": 1, "specs": 1}
        )

    gpu_name = request.args.get("gpu")
    if gpu_name:
        selected_build["gpu"] = products_col.find_one(
            {"type": "gpu", "name": gpu_name},
            {"_id": 0, "name": 1, "specs": 1}
        )

    psu_name = request.args.get("psu")
    if psu_name:
        selected_build["psu"] = products_col.find_one(
            {"type": "psu", "name": psu_name},
            {"_id": 0, "name": 1, "specs": 1}
        )

    ram_name = request.args.get("ram")
    if ram_name:
        selected_build["ram"] = products_col.find_one(
            {"type": "ram", "name": ram_name},
            {"_id": 0, "name": 1, "specs": 1}
        )

    case_compatability_list = [calculate_case_compatibility(prod, selected_build) for prod in cases]
    cooler_compatability_list = [calculate_cooler_compatibility(prod, selected_build) for prod in coolers]
    motherboard_compatability_list = [calculate_motherboard_compatibility(prod, selected_build) for prod in motherboards]
    cpu_compatability_list = [calculate_cpu_compatibility(prod, selected_build) for prod in cpus]
    gpu_compatability_list = [calculate_gpu_compatibility(prod, selected_build) for prod in gpus]
    psu_compatability_list = [calculate_psu_compatibility(prod, selected_build) for prod in psus]
    ram_compatability_list = [calculate_ram_compatibility(prod, selected_build) for prod in rams]

    return jsonify({
        "cases": case_compatability_list,
        "coolers": cooler_compatability_list,
        "motherboards": motherboard_compatability_list,
        "cpus": cpu_compatability_list,
        "gpus": gpu_compatability_list,
        "psus": psu_compatability_list,
        "rams": ram_compatability_list
    })


# CART ROUTES

@app.route("/add_to_cart", methods=["POST"])
def add_to_cart():
    """
    Adds product to cart.
    
    Logic:
    Reads product name from submitted form, and find its document in MongoDB
    Append it to current cart and save updated cart, then redirect to homepage
    """
    
    product_name = request.form.get("name")

    product = products_col.find_one(
        {"name": product_name},
        {"_id": 0}
    )

    if product:
        cart = get_cart()
        cart.append(product)
        save_cart(cart)

    return redirect("/")


@app.route("/add_build_to_cart", methods=["POST"])
def add_build_to_cart():
    
    """
    Adds a custom build to the cart.

    Logic:
    Read selected part names from form
    Fetch each selected product from MongoDB
    Calculate total price
    Store the full build as one cart item
    """
    
    selected_parts = []
    total_price = 0

    part_types = ["case", "motherboard", "cpu", "cooler", "gpu", "ram", "psu"]

    for part_type in part_types:
        part_name = request.form.get(part_type)
        if part_name:
            product = products_col.find_one(
                {"type": part_type, "name": part_name},
                {"_id": 0}
            )
            if product:
                selected_parts.append(product)
                total_price += product["price"]

    if selected_parts:
        build = {
            "name": "Custom PC Build",
            "price": total_price,
            "parts": selected_parts,
            "type": "custom_build"
        }

        cart = get_cart()
        cart.append(build)
        save_cart(cart)

    return redirect("/cart")


@app.route("/cart")
def cart():
    
    """
    Displays current cart page with cart items
    """
    
    
    cart_items = get_cart()
    return render_template("cart.html", cart=cart_items)


@app.route("/builder")
def builder():
    """
    Displays the builder page with empty fields
    """
    
    return render_template(
        "builder.html",
        cases=cases,
        motherboards=motherboards,
        cpus=cpus,
        coolers=coolers,
        gpus=gpus,
        rams=rams,
        psus=psus,
        selected_build={}
    )

@app.route("/presets")
def presets():
    
    """
    Displays preset page with all presets
    """
    
    preset_builds = get_preset_builds()
    return render_template("presets.html", preset_builds=preset_builds)


@app.route("/add_preset_to_cart", methods=["POST"])
def add_preset_to_cart():
    """
    Adds a preset build to the cart.
    
    Logic:
    Reads the preset key from form, 
    finds the matching preset and 
    convert it into a cart item
    """
    
    preset_key = request.form.get("preset_key", "").strip()
    preset_builds = get_preset_builds()

    selected_preset = None
    for preset in preset_builds:
        if preset["key"] == preset_key:
            selected_preset = preset
            break

    if selected_preset:
        cart = get_cart()
        cart.append({
            "name": selected_preset["title"],
            "price": selected_preset["price"],
            "parts": selected_preset["parts"],
            "type": "custom_build"
        })
        save_cart(cart)

    return redirect("/cart")


@app.route("/load_preset/<preset_key>")
def load_preset(preset_key):
    """
    Loads a preset build into the builder page.

    Parameter:
    preset_key: unique key of the preset

    If preset is not found, redirect back to presets page.
    """
    
    preset_builds = get_preset_builds()

    selected_preset = None
    for preset in preset_builds:
        if preset["key"] == preset_key:
            selected_preset = preset
            break

    if not selected_preset:
        return redirect("/presets")

    return render_template(
        "builder.html",
        cases=cases,
        motherboards=motherboards,
        cpus=cpus,
        coolers=coolers,
        gpus=gpus,
        rams=rams,
        psus=psus,
        selected_build=selected_preset["builder_parts"]
    )


@app.route("/", methods=["GET"])
def home():
    """
    Home page route.

    Responsibilities:
    Ensure guest cart exists in session
    Read search filters from URL
    Dynamically build MongoDB query
    Fetch matching products
    Render the index page
    """
    
    #makes sure guest cart exists
    if "cart" not in session:
        session["cart"] = []
        
    #Read all searc/filter inputs
    name = request.args.get("name", "").strip()
    product_type = request.args.get("type", "").strip()
    brand = request.args.get("brand", "").strip()
    min_price = request.args.get("min_price", "").strip()
    max_price = request.args.get("max_price", "").strip()
    
    #MongoDB query object
    query = {}
    
    #Using query object for filtering purposes
    if name:
        query["name"] = {"$regex": name, "$options": "i"}

    if product_type:
        query["type"] = product_type

    if brand:
        query["brand"] = {"$regex": brand, "$options": "i"}

    price_filter = {}
    if min_price:
        price_filter["$gte"] = float(min_price)
    if max_price:
        price_filter["$lte"] = float(max_price)

    if price_filter:
        query["price"] = price_filter

    if query:
        products = list(products_col.find(query, {"_id": 0}))
        searched = True
    else:
        products = list(products_col.find({}, {"_id": 0}))
        searched = False

    return render_template(
        "index.html",
        products=products,
        searched=searched,
        name=name,
        product_type=product_type,
        brand=brand,
        min_price=min_price,
        max_price=max_price
    )


if __name__ == "__main__":
    app.run(debug=True)