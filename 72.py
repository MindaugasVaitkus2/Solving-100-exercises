#Create a script that let the user type in a search term and opens and search on the browser for that
import webbrowser
search_term = raw_input('Enter your google query: ')
url = "https://www.google.com/search?q={}".format(search_term)
webbrowser.open(url)

# his answer
# import webbrowser
#
# query = input("Enter your Google query: ")
# url = "https://www.google.com/?gws_rd=cr,ssl&ei=NCZFWIOJN8yMsgHCyLV4&fg=1#q=%s" % str(query)
# webbrowser.open_new(url)
# Explanation:
# We're using webbrowser  here which is a standard library that is used to open a web browser. First, we're getting the search term through input  and then we construct the URL. You need to first do a manual search on Google and observe how Google will construct the URL. You will see that the URL contains your search term at the end. Therefore, we concatenate the first part of the URL with the search term we get from input .
