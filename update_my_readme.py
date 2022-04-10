import os

def get_problem_link(path):
    with open(path, "r") as leetcode_file:
        content = leetcode_file.readlines()
    return content[1].strip()

def get_problem_name(pblm_link):
    name = pblm_link.split("/")[-2]
    name = map(lambda n: n.title(), name.split("-"))
    return " ".join(name)


with open("README.md", "w+") as file:
    files = os.listdir("leetcode")
    files.sort()
    content = ""
    for index, _file in enumerate(files):
        problem_link = get_problem_link(f"leetcode/{_file}")
        problem_name = get_problem_name(problem_link)

        content += f"\n{index+1}.  [{problem_name}]({problem_link}) - [code](https://github.com/vyshuks/DSAlgo/blob/main/leetcode/{_file})\n"
    file.write(
        "# DSAlgo \n"+ "## Leetcode \n" + content)


