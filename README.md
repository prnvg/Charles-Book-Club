# Charles-Book-Club

This data set represents information associated with individuals who are members of a book club. This is a model for predicting whether a person will purchase a book about the city of Florence based on past purchases or not.

Description of Variables:

Seq#: Sequence number in the partition

ID#: Identification number in the full (unpartitioned) market test data set

Gender: O=Male 1=Female

M: Monetary- Total money spent on books

R: Recency- Months since last purchase

F: Frequency - Total number of purchases

FirstPurch: Months since first purchase

ChildBks: Number of purchases from the category: Child books

YouthBks: Number of purchases from the category: Youth books

CookBks: Number of purchases from the category: Cookbooks

DoItYBks: Number of purchases from the category: Do It Yourself books I

RefBks: Number of purchases from the category: Reference books (Atlases, Encyclopedias, Dictionaries)

ArtBks: Number of purchases from the category: Art books

GeoBks: Number of purchases from the category: Geography books

ItalCook: Number of purchases of book title: "Secrets of Italian Cooking"

ItalAtlas: Number of purchases of book title: "Historical Atlas of Italy"

ItalArt: Number of purchases of book title: "Italian Art"

Florence: =1 if 'The Art History of Florence" was bought, = 0 if not

Related purchase: Number of related books purchased 


Algorithm used: Logistic Regression

Accuracy ~ 92%
