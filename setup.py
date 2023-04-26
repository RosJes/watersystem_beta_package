from setuptools import setup

with open("README.md","r",encoding="utf-8") as readme_file:
	long_description= readme_file.read()

setup(
	name= "watersystem_beta",
	version= "1.0.0",
	description="Network steering of Arduino based watering system",
	long_description=long_description,
	long_description_content_type="text/markdown",
	author= "RosJes",
	author_email="RosJes@example.com",
	license="MIT",
	packages=['watersystem_beta'],
	package_dir={'watersystem_beta':'watersystem_beta/'},
	classifiers =[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Environmment :: Console",
		"Operating System :: POSIX :: Linux"
	],
	entry_points = {
		'console_scripts':['watersystem_beta= watersystem_beta.watersystem_beta:main']
	},
	data_files= [
		('share/applications',['watersystem_beta.desktop'])
	],
	keywords= "watersystem steering UDP",
	python_requires =">=3.10"
)
