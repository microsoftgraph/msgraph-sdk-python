import ast
import importlib
import inspect
import os
from typing import Set

import astunparse
import black
import isort
from more_itertools import flatten


def import_modules_from_directory(directory):
    def import_module(root, file):
        if file.endswith('.py') and not file.startswith('__'):
            module_path = os.path.join(root, file)
            parent_module = root.split(directory)[-1].replace("\\", ".")
            module_path = module_path.replace(root, ".".join(filter(None, [directory, parent_module])))
            full_module_name = module_path.replace(os.path.sep, '.')[:-3]
            full_module_name = full_module_name.replace("..", ".")
            return importlib.import_module(full_module_name)
        return None

    def import_modules(value):
        root, dirs, files = value
        return filter(None, map(lambda file: import_module(root, file), files))

    project_directory = __file__.replace(f"tests\\integration\\{os.path.basename(__file__)}", "")
    return flatten(map(import_modules, os.walk(f"{project_directory}{directory}")))


class RefactorVisitor(ast.NodeTransformer):

    def remove_imports(self, node, exclude: Set):
        names = []

        for alias in node.names:
            if not alias.name in exclude:
                names.append(alias)

        if len(names) == 0:
            return None

        node.names = names

        return node

    def visit_Import(self, node):
        return node

    def visit_ImportFrom(self, node):
        if node.module == "kiota_abstractions.serialization":
            return None

        # from dataclasses import dataclass, field
        if node.module == "dataclasses":
            return self.remove_imports(node, exclude={"field"})

        # from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
        if node.module == "typing":
            return self.remove_imports(node, exclude={"TYPE_CHECKING", "Any", "Callable", "Dict", "Union"})

        return node

    def visit_If(self, node):
        if node.test.id != "TYPE_CHECKING":
            return node
        return node.body

    def visit_ClassDef(self, node):
        entity = None

        for element in node.body:
            if isinstance(element, ast.AnnAssign) and \
               isinstance(element.target, ast.Name) and \
               element.target.id == "value":
                    entity = element.annotation.slice.slice.id
                    break

        if entity:
            # Find and update the base class
            for base in node.bases:
                if isinstance(base, ast.Name) and base.id.startswith('BaseCollectionPagination'):
                    base.id = f'{base.id}[{entity}]'

            # Add a constructor if it doesn't exist
            has_constructor = any(
                isinstance(item, ast.FunctionDef) and item.name == '__init__' for item in node.body)
            if not has_constructor:
                constructor = ast.parse(f"""def __init__(self):
                    super().__init__(entity={entity})""").body[0]
                node.body.append(constructor)

        # Remove unnecessary methods
        elements = []

        for element in node.body:
            if not isinstance(element, ast.FunctionDef) or element.name not in {'create_from_discriminator_value', 'get_field_deserializers', 'serialize'}:
                elements.append(element)

        node.body = elements

        return node

def get_subclasses(module):
    subclasses = []
    for name, obj in inspect.getmembers(module, inspect.isclass):
        orig_bases = dict(inspect.getmembers(obj)).get("__orig_bases__", [])
        for orig_base in orig_bases:
            if orig_base.__name__.startswith("BaseCollectionPagination"):
                subclasses.append((module, name, obj))
    return subclasses

def refactor_code(source_code):
    tree = ast.parse(source_code)
    RefactorVisitor().visit(tree)
    return black.format_str(astunparse.unparse(tree), mode=black.Mode())

# Example usage:

def do_refactor(module):
    for module, name, subclass in get_subclasses(module):
        source_code = inspect.getsource(module)
        refactored_code = refactor_code(source_code)

        print("----------------------------")
        print(f"module: {module}")
        print(f"name: {name}")
        print(f"subclass: {subclass}")
        print("----------------------------")

        with open(module.__file__, "w") as file:
            file.write(refactored_code)

        isort.file(module.__file__)


if __name__ == "__main__":
    for module in import_modules_from_directory("msgraph"):
        do_refactor(module)
