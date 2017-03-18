# Python-google-scholar

add some functions of the API based on Christian Kreibich

## Step 1

using "main.py" 

```python main.py -c 100 -T 6675397154864859782 --citation "bt"```

and you get 100 Bibtex results of articles which cited the article with the cluster ID specified. The title of each article will be upload to a json file named "title.json"

## Step 2

using "create_keywords_presentation.py" "python create_keywords_presentation.py" and the program will open "title.json" and search keywords of each article on pubmed

## Step 3

using "create_journal_presentation.py" to get the presentation of journal the program will open "journal.json"
