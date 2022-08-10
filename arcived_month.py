import datetime

with open('README.md', 'r') as readme_file:
    readme_content = readme_file.read()

start_marker = "## All language"
start_index = readme_content.find(start_marker)

if start_index != -1:
    extracted_content = readme_content[start_index:]
    with open(f'archived/{datetime.datetime.now().strftime("%Y-%m")}.md', 'w') as archive_file:
        archive_file.write(extracted_content)
    with open('README.md', 'w') as readme_file:
        readme_file.write(readme_content[:start_index])
    print("archive suceess")
else:
    print("archive fail")
