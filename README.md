# 0x00. AirBnB Clone - The Console

## Project Description
The **AirBnB Clone** is a foundational full-stack software development project designed to replicate the core backend functionalities of the AirBnB web application.

This repository marks the first phase (**The Console**), where an object-oriented hierarchy is established alongside a custom command-line interface (CLI) to manage data persistence using JSON serialization and deserialization.

### Core Objectives
- Create an Object-Oriented Data Model hierarchy with common attributes and behavior (`BaseModel`).
- Manage serialization and deserialization flows (`BaseModel` -> dictionary -> JSON string -> file -> JSON string -> dictionary -> `BaseModel`).
- Implement an extensible storage engine (`FileStorage`).
- Build unit test suites for all classes, methods, and functions.
- Ensure strict adherence to PEP8 / `pycodestyle`.

---

## Storage Architecture & Serialization Flow

The data lifecycle follows a structured pipeline:
```
[BaseModel Instance]
        |
        v  (to_dict)
[Python Dictionary Representation]
        |
        v  (json.dump / json.dumps)
[JSON String / file.json]
        |
        v  (json.load / json.loads)
[Python Dictionary Representation]
        |
        v  (**kwargs reconstruction)
[BaseModel Instance]
```

- **`models/base_model.py`**: Defines the base class from which all future entities inherit. It manages unique identifier generation via `uuid.uuid4()`, tracking creation and modification timestamps (`datetime`), string representation, and dictionary formatting.
- **`models/engine/file_storage.py`**: Handles persistent storage by reading from and writing to `file.json`.
- **`models/__init__.py`**: Instantiates a shared `FileStorage` object (`storage`) and reloads persisted state upon initialization.

---

## The Command Interpreter

The command interpreter is a shell-like command-line interface built using Python's `cmd` module to manage backend objects without a graphical user interface.

### How to Start It

#### Interactive Mode
To run the console interactively, invoke `console.py` directly:
```bash
$ ./console.py
(hbnb) 
```

#### Non-Interactive Mode
The interpreter can also execute commands piped via standard input:
```bash
$ echo "help" | ./console.py
(hbnb) 
Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
```

### Available Commands & Usage
- **`help`**: Displays available commands or documentation for a specific command.
- **`quit`** or **`EOF`**: Exits the command interpreter cleanly.
- **`create <class_name>`**: Creates a new instance of `<class_name>`, saves it to the JSON file, and prints its unique `id`.
- **`show <class_name> <id>`**: Prints the string representation of an instance based on the class name and id.
- **`destroy <class_name> <id>`**: Deletes an instance based on the class name and id, and persists changes.
- **`all`** or **`all <class_name>`**: Prints string representations of all instances or all instances of a specified class.
- **`update <class_name> <id> <attribute_name> "<attribute_value>"`**: Updates an instance attribute and saves the change.

### Example Console Session
```bash
$ ./console.py
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2026, 9, 11, 23, 10, 20, 123456), 'updated_at': datetime.datetime(2026, 9, 11, 23, 10, 20, 123456)}
(hbnb) quit
$
```

---

## File Structure

```
AirBnB_clone/
├── AUTHORS
├── README.md
├── models/
│   ├── __init__.py
│   ├── base_model.py
│   └── engine/
│       ├── __init__.py
│       └── file_storage.py
└── tests/
    ├── __init__.py
    └── test_models/
        ├── __init__.py
        ├── test_base_model.py
        └── test_engine/
            ├── __init__.py
            └── test_file_storage.py
```

---

## Testing & Quality Assurance

All code strictly conforms to the `pycodestyle` (PEP8) standard and includes exhaustive unit tests.

### Running Pycodestyle Checks
```bash
python3 -m pycodestyle models/ tests/
```

### Running Unit Tests
Unit tests can be executed interactively or non-interactively using Python's `unittest` framework:

**Interactive mode:**
```bash
python3 -m unittest discover tests
```

**Non-interactive mode:**
```bash
echo "python3 -m unittest discover tests" | bash
```

---

## Authors
- **Yonas Leykun** - [yonasleykun27](https://github.com/yonasleykun27) - <yonasleykun27@gmail.com>
