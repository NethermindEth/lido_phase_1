import re
import csvtotable
import pandas as pd

# Auxiliary functions:

def construct_html_hyperlink(_address:str, _text:str,NewTab=False):
    """Turns an address-text pair into hyperlink format. Allows to specify whether it opens in a NewTab or not
    
    Default behavior is to open in the same tab.
    """
        
    if NewTab:
        boilerplate = '<a href="{address}" target = "_blank"> {text} </a>'
    else:
        boilerplate = '<a href="{address}"> {text} </a>'
    
    return boilerplate.format(address=_address, text=_text)

def pull_file_hyperlinks(path_to_html_file):
    """!Takes the path to an HTML file corresponding to the exported Notion database, and returns a dataframe with two columns:
    
    [Title, Path to file] 
    
    This dataframe can then be merged with the one from the CSV file to reconstruct the relevant hyperlinks.
    """
    
    # Read HTML
    html_string = open(path_to_html_file, "r").read()
    
    # Extract all hyperlinks from HTML, that do not correspond to links to papers (i.e. do not start with http).
    # Note that some hyperlinks are being divided by -new lines for some reason.
    regex = r'<a href="([^http].*?)">(.*?)<\/a>'
    hyperlink_pairs = re.findall(regex, html_string, flags=re.DOTALL)
    
    # Create dataframe
    file_link_df = pd.DataFrame(hyperlink_pairs, columns = ["Path to file", "Title"],
                                ).set_index("Title")
    return file_link_df

##########

def main():
    """!Takes the csv file exported from Notion as input and adds hyperlinks to the relevant columns

    Requires the csv file to be called "database.csv" and be located in the main folder.
    """

    # Fetch the database into pandas, and sort the columns as intended
    columns = ["Title", "Date of publication", "BS factor", "Score Phase 1", "Classification", "Link to the paper", "Abstract"]
    df = pd.read_csv('scripts/database.csv', usecols=columns)[columns].set_index("Title")

    # Add the hyperlinks to the "Link to Page" column.
    df["Link to the paper"] = df["Link to the paper"].apply(lambda link:construct_html_hyperlink(link,"Link", NewTab=True))

    # Add the hyperlinks to the "Title" column by merging with the dataframe from pull_paper_hyperlinks
    file_link_df = pull_file_hyperlinks("scripts/html.html")
    df = df.join(file_link_df, how = 'inner')
    
    # Undo using the Title as index
    df = df.reset_index()
    
    # Take "Path to file" column and turn it into a proper hyperlink (to the markdown files) on the article title.
    # df["Path to file"] = df["Path to file"].apply(lambda string : string[:-4] + "md") # This line not needed?
    df["Title"] = df["Path to file"].combine(df["Title"], construct_html_hyperlink)
    df = df.drop(columns = "Path to file")
     
    # Save changes:
    df.to_csv('scripts/database_out.csv', index=False)    

main()