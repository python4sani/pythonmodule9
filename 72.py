# def heading_two(text):
#     """
#     This is heading to html text
#     :param text: heading do
#     :return: text tag
#     """
#     result = f'<h2>{text}</h2>'
#     return result
#
# print(heading_two.__doc__)

def html_tax(text, html_tag):
    result = f'<{html_tag}>{text}</{html_tag}>'
    return result

html_tag = input('Enter html Tag: ')
text = input('Enter text: ')


print(html_tax(text,html_tag))