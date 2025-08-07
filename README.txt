My Solution Description (with problem description stated below):

The Python code gets the HTML content from the URL and extracts the data from the first table found in the published Google Doc using requests and BeautifulSoup. 
The largest x and y-coordinates are found to create an appropriately-sized 2D list of space strings (" "). 
The 2D list is then populated with the appropriate characters in their respective locations as specified in the table. 
The completed 2D list is finally condensed into printable rows and printed in reverse as the 0 y-coordinate is the last row to print.

------------------------------------------------------------------------------------------------------------------------------------------------------------
Coding Exercise: Decoding a Secret Message

In this exercise, you will write code to solve a problem. Your code must be in Python (preferred), JavaScript, TypeScript, Java, Kotlin, C#, C++, Go, Rust, Swift or Ruby—solutions in other languages will not be accepted! You can write your code using any IDE you want.

Problem

You are given a published Google Doc like this(https://docs.google.com/document/d/e/2PACX-1vTMOmshQe8YvaRXi6gEPKKlsC6UpFJSMAk4mQjLm_u1gmHdVVTaeh7nBNFBRlui0sTZ-snGwZM4DBCT/pub) one that contains a list of Unicode characters and their positions in a 2D grid. Your task is to write a function that takes in the URL for such a Google Doc as an argument, retrieves and parses the data in the document, and prints the grid of characters. When printed in a fixed-width font, the characters in the grid will form a graphic showing a sequence of uppercase letters, which is the secret message.

    The document specifies the Unicode characters in the grid, along with the x- and y-coordinates of each character.

    The minimum possible value of these coordinates is 0. There is no maximum possible value, so the grid can be arbitrarily large.

    Any positions in the grid that do not have a specified character should be filled with a space character.

    You can assume the document will always have the same format as the example document linked above.

For example, the simplified example document linked above draws out the letter 'F':

█▀▀▀
█▀▀ 
█   

Note that the coordinates (0, 0) will always correspond to the same corner of the grid as in this example, so make sure to understand in which directions the x- and y-coordinates increase.

Specifications

    Your code must be written in Python (preferred), JavaScript, TypeScript, Java, Kotlin, C#, C++, Go, Rust, Swift or Ruby.

    You may use external libraries.

    You may write helper functions, but there should be one function that:

    1. Takes in one argument, which is a string containing the URL for the Google Doc with the input data, AND

    2. When called, prints the grid of characters specified by the input data, displaying a graphic of correctly oriented uppercase letters.

To verify that your code works, please run your function with this URL (updated 8/1/25) as its argument:

https://docs.google.com/document/d/e/2PACX-1vRPzbNQcx5UriHSbZ-9vmsTow_R6RRe7eyAU60xIF9Dlz-vaHiHNO2TKgDi7jy4ZpTpNqM7EvEcfr_p/pub

What is the secret message encoded by this document? Your answer should only contain uppercase letters.
KICWEDB
