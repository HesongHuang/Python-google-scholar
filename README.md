# Python-google-scholar
add some functions of the API based on Christian Kreibich
step 1: using "main.py" "python main.py -c 100 -T 6675397154864859782 --citation "bt"
        and you get 100 Bibtex results of articles which cited "3D Slicer as an image computing platform for the Quantitative              Imaging Network". The title of each article will be upload to a json file named "title.json"
step 2: using "creat_keywords_presentation.py" "python creat_keywords_presentation.py" 
        and the program will open "title.json" and search keywords of each article on pubmed
