# HTML Dependencies Extractor
Making it easy and efficient to restructure one particular HTML file and copy its dependent files.

## The problem
After downloading an HTML template, this comes usually with a lot of pre-defined page layouts and its corresponding stylesheets, scripts, images and fonts. Whenever one of these predefined layouts is used as a base for a project, the developer should manually copy all the files which that particular HTML file is dependent on and should change all the paths referring to them. This can be really time-consuming and prone to errors.

## The solution
This small script copies all the file dependencies to the root folder and adjust all paths in the HTML file relatively with just the path to the desired HTML file.