# Feedback Finder
Python tool for creating a .html file that allows you to browse text easily.

![alt text](https://github.com/Peter-Devine/text_finder/blob/main/Feedback_finder_interface.png?raw=true)

This tool gives two lists:
* A search list
* A similarity list

To use the tool effectively, you first search for feedback that you would like to investigate. 

For example, if you are looking for performance complaints, you could search for the term "lag" from the search bar. 

Then, the search list will show you all the feedback that contains the word "lag". 

Clicking on one of these complaints will then show the (by default) 30 similar complaints to the one clicked, which might not contain the word "lag", but contain other complaints about performance (perhaps mentioning words like "slow" or "freeze".

This allows you to see not just the feedback that contains your keyword, but all the feedback that relates to this.

# Prerequisites

* Python 3
* tensorflow-hub (+ dependencies - TensorFlow 2 etc. pip should do this automatically)
* sentence-transformers
* sklearn
* numpy
* bokeh
* scipy
* pandas
* argparse

# How to run

Have a .csv file that contains the text you would like to browse. By default, this tool searches for the column named "text" within the supplied .csv file for the text to analyse.

Then run:
```python run.py --text_csv_dir=[DIRECTORY TO YOUR CSV FILE]```
By default, this should create a .html file in your cwd that contains the above browser interface and your data.

Current options for this tool include changing the name of the column that you want to analyse:
```python run.py --text_csv_dir=[DIRECTORY TO YOUR CSV FILE] --csv_text_column_name=[DIFFERENT COLUMN NAME]```

and a custom directory where you want to send your .html file. Be warned that this directory will add ".html" to the end, and then make this a file, so take care to add your desired file name without the .html suffix to the cusom directory:
```python run.py --text_csv_dir=[DIRECTORY TO YOUR CSV FILE] --output_dir=[DIR TO OUTPUT WITH BARE FILE NAME]```
