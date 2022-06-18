#task 1
import os

my_values = ['settings','mainapp','adminapp','authapp']
my_keys = 'my_project'
my_dict = {my_keys : my_values}

dir_path = [os.makedirs(os.path.join(my_keys,i)) for i in my_values if not os.path.exists(os.path.join(my_keys,i))]

print(os.path.join(os.path.abspath(os.getcwd()), my_keys))
my_path=os.path.join(os.path.abspath(os.getcwd()), my_keys)
for i in my_values:
    print(os.path.join(my_path,i))

#task 3

if __name__ == "__main__":

    import os
    import sys
    import shutil

    glb_path = sys.argv[1]
    files = [os.path.relpath(os.path.join(root, file), glb_path) for root, _, files in os.walk(
        glb_path) for file in files if file.endswith(".html")]
    for rel_path in files:
        path, file = os.path.split(rel_path)
        test_path = os.path.join(glb_path, "template", path)
        if not os.path.exists(test_path):
            os.makedirs(test_path)
        shutil.copyfile(os.path.join(glb_path,rel_path), os.path.join(test_path, file))

# task 3
import os
import sys

size = {}


def scan_mem(pth):

    if not os.path.exists(pth):
        return
    with os.scandir(pth) as files:

        for node in files:

            if os.path.isfile(node):

                mem = 10 ** len(str(os.stat(node).st_size))
                size[mem] = size.get(mem, 0) + 1
            elif os.path.isdir(node):
                scan_mem(os.path.join(pth, node))


if __name__ == "__main__":

    if len(sys.argv) == 2:
        pth = sys.argv[1]
    else:
        pth = os.getcwd()

    scan_mem(pth)
    print(size)

