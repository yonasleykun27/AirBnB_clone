#!/usr/bin/python3
"""Defines the HBNB command interpreter."""
import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command interpreter for AirBnB project.

    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "

    __classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def do_create(self, arg):
        """Creates a new instance of a class, saves it, and prints the id."""
        try:
            args = shlex.split(arg)
        except ValueError:
            args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        new_instance = HBNBCommand.__classes[args[0]]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance."""
        try:
            args = shlex.split(arg)
        except ValueError:
            args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        try:
            args = shlex.split(arg)
        except ValueError:
            args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances."""
        try:
            args = shlex.split(arg)
        except ValueError:
            args = arg.split()
        if len(args) > 0 and args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        obj_list = []
        for obj in storage.all().values():
            if len(args) == 0 or obj.__class__.__name__ == args[0]:
                obj_list.append(str(obj))
        print(obj_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id."""
        try:
            args = shlex.split(arg)
        except ValueError:
            args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attr_name = args[2]
        attr_val = args[3]
        if attr_name in ("id", "created_at", "updated_at"):
            return
        obj = storage.all()[key]
        if hasattr(obj, attr_name):
            attr_type = type(getattr(obj, attr_name))
            try:
                val = attr_type(attr_val)
            except (ValueError, TypeError):
                val = attr_val
        else:
            try:
                val = int(attr_val)
            except ValueError:
                try:
                    val = float(attr_val)
                except ValueError:
                    val = attr_val
        setattr(obj, attr_name, val)
        obj.save()

    def do_count(self, arg):
        """Retrieves the number of instances of a given class."""
        try:
            args = shlex.split(arg)
        except ValueError:
            args = arg.split()
        count = 0
        for obj in storage.all().values():
            if len(args) > 0 and args[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def default(self, line):
        """Default handling for <class_name>.<command>() syntax."""
        import ast

        parts = line.split(".", 1)
        if len(parts) == 2:
            cls_name, rest = parts
            if cls_name in HBNBCommand.__classes:
                if rest == "all()":
                    return self.do_all(cls_name)
                if rest == "count()":
                    return self.do_count(cls_name)
                if rest == "create()":
                    return self.do_create(cls_name)
                if rest.startswith("show(") and rest.endswith(")"):
                    id_arg = rest[5:-1].strip("\"'")
                    return self.do_show("{} {}".format(cls_name, id_arg))
                if rest.startswith("destroy(") and rest.endswith(")"):
                    id_arg = rest[8:-1].strip("\"'")
                    return self.do_destroy("{} {}".format(cls_name, id_arg))
                if rest.startswith("update(") and rest.endswith(")"):
                    inner = rest[7:-1].strip()
                    if "{" in inner and inner.endswith("}"):
                        d_parts = inner.split(",", 1)
                        if len(d_parts) == 2:
                            id_arg = d_parts[0].strip().strip("\"'")
                            dict_str = d_parts[1].strip()
                            try:
                                attr_dict = ast.literal_eval(dict_str)
                                if isinstance(attr_dict, dict):
                                    for k, v in attr_dict.items():
                                        self.do_update(
                                            "{} {} {} \"{}\"".format(
                                                cls_name, id_arg, k, v
                                            )
                                        )
                                    return
                            except Exception:
                                pass
                    update_args = inner.split(",")
                    if len(update_args) >= 3:
                        id_arg = update_args[0].strip().strip("\"'")
                        attr_name = update_args[1].strip().strip("\"'")
                        attr_val = update_args[2].strip()
                        cmd_str = "{} {} {} {}".format(
                            cls_name, id_arg, attr_name, attr_val
                        )
                        return self.do_update(cmd_str)
        return cmd.Cmd.default(self, line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
