# Why Plugins are better
# 1. No need to modify main.py every time
# 2. Flexible Order and Easy Enable/Disable
# 3. External Developer Contributions
import os
import importlib.util # importlib.util -> import modules dynamically (while the program is running)
PLUGIN_FOLDER = "plugins"
plugins = []

for file in os.listdir(PLUGIN_FOLDER):
    if file.endswith(".py"):
        plugin_path = os.path.join(PLUGIN_FOLDER, file)
        module_name = file[:-3]   
        spec = importlib.util.spec_from_file_location(module_name, plugin_path) # where to find the module on your computer.
        module = importlib.util.module_from_spec(spec) # Creates a new module object in memory, based on that spec
        spec.loader.exec_module(module) # it actually runs the plugin file and loads its content into memory
        if hasattr(module, "run"):
            plugins.append(module.run)

data = input("Enter some text: ")

for plugin_func in plugins:
    data = plugin_func(data)

print("Final transformed data:", data)
