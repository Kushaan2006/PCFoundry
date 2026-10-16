# PCFoundry

**PCFoundry** is a full-stack PC configuration web application developed as a three-person academic group project at Seneca Polytechnic. It helps users browse hardware components, assemble custom PCs, and identify hardware compatibility issues before saving a build or adding parts to a shopping cart.

The application uses **Python and Flask** for server-side functionality, **MongoDB** for persistent data storage, and a **rule-based compatibility engine** for evaluating component combinations.

My contribution was working on the compatability feature for this project, In addition, I contributed to all other areas equally.
Other contributors: Mahd Bin Faisal, Xi Tin Yan.

## Features

- **Custom PC builder:** Select parts across seven hardware categories: cases, motherboards, CPUs, CPU coolers, GPUs, power supplies, and RAM.
- **Hardware compatibility checks:** Evaluate selected components against specifications such as socket compatibility, supported memory, component dimensions, and power-related constraints, with reasons for incompatibilities.
- **Component catalog:** Browse products and filter by name, type, brand, and price range.
- **Saved configurations:** Save and reload custom PC builds while signed in.
- **Preset builds:** View predefined configurations and load them into the builder or add their components to the cart.
- **Shopping cart:** Add individual components or entire builds; supports carts for guests and signed-in users.
- **User accounts:** Register, sign in, and sign out using Flask sessions. **Note:** The current authentication implementation is intended for coursework, not production deployment (see [Limitations](#limitations-and-security)).

## Tech Stack

| Area | Technology |
| --- | --- |
| Backend | Python, Flask |
| Database | MongoDB, PyMongo |
| Frontend | HTML, CSS, Jinja templates |
| Configuration | python-dotenv |
| Testing | Python `unittest` |

## Project Structure

```text
.
├── app.py                       # Flask routes and application logic
├── compatibility.py             # Rule-based hardware compatibility checks
├── compatibility_selftests.py   # Unit tests for compatibility logic
├── db.py                        # MongoDB connection, validators, and indexes
├── seed.py                      # Sample hardware catalog
├── requirements.txt             # Python dependencies
├── static/
│   └── style.css
└── templates/                   # Jinja pages for the app
```

## Getting Started

### Prerequisites

- Python 3
- A running MongoDB database (local MongoDB or MongoDB Atlas)
- Git

### 1. Clone the repository

```bash
git clone <repository-url>
cd <repository-folder>
```

Replace the placeholders with the URL and directory name for your own copy of the project. The original course repository may be private.

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
```

**macOS / Linux:**

```bash
source .venv/bin/activate
```

**Windows (PowerShell):**

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure MongoDB

Create a `.env` file in the project root:

```dotenv
MONGODB_URI=mongodb://localhost:27017/
```

Replace this with your MongoDB Atlas connection string if using a hosted instance. **Never commit real credentials or the `.env` file.** The code uses the `PCFoundry` database.

### 5. Seed sample products

```bash
python seed.py
```

This inserts sample hardware components that are not already present by product name. MongoDB collection validation and indexes are configured in `db.py`.

### 6. Start the application

```bash
python app.py
```

Open **http://127.0.0.1:5000** in your browser.

> **Local development only:** The current application starts Flask in debug mode. Do not expose this configuration to the public internet.

## How Compatibility Checking Works

The compatibility logic is implemented in `compatibility.py`. It examines the specifications of a selected component against the other components in a proposed build, returning whether the component is compatible and, when it is not, explanatory reasons.

The engine contains dedicated checks for all seven component categories, including compatibility considerations such as:

- CPU and motherboard socket matching
- RAM type and platform support
- Motherboard and case form factors
- Graphics card and CPU cooler clearance
- Power supply and case compatibility
- Other component-specific specification constraints

The Flask route `/check_compatability` calls the compatibility functions. The route name preserves the spelling used in the original course implementation.

## Testing

PCFoundry includes **68 automated compatibility unit tests**, implemented using Python's built-in `unittest` framework. They cover compatible configurations, incompatible hardware combinations, and edge cases.

Run the tests from the repository root:

```bash
python compatibility_selftests.py
```

**Verification:** All **68 of 68** compatibility tests passed when run against the supplied project snapshot. This is a **100% pass rate for this test suite**, not a claim of 100% code coverage or end-to-end application coverage.

## Academic Project and Contributions

PCFoundry was developed collaboratively by **three students** as a university-level academic project.

My individual contribution included implementing the **rule-based component compatibility validation** across seven hardware categories and helping validate its behavior through automated tests. Other application features were developed collaboratively by the group.

## Limitations and Security

PCFoundry is an academic prototype and is **not production-ready**. Important known limitations in the supplied version include:

- Passwords are stored and compared without secure password hashing.
- The Flask session secret key is hardcoded.
- Flask debug mode is enabled in the application entry point.
- Passing compatibility unit tests does not verify all database, authentication, UI, or deployment behavior.

Before any public deployment, these issues should be addressed, along with a broader security review and additional integration tests.

## Potential Improvements

- Hash passwords using a suitable password-hashing library and move secrets into environment variables.
- Separate application concerns into Flask blueprints or services to improve maintainability.
- Expand database, route, and end-to-end test coverage.
- Add CI checks and strengthen input validation and error handling.
- Improve compatibility-rule coverage and maintainability as the hardware catalog grows.

## Acknowledgment

Developed as a collaborative academic project at **Seneca Polytechnic**.
